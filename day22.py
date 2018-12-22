import numpy

depth = 3339
target = (10, 715)
# Example data:
#depth = 510
#target = (10, 10)

TOOL_TYPES = {'.': ['c', 't'],
              '=': ['c', 'n'],
              '|':  ['t', 'n']}


def reconstruct_path(cameFrom, current):
  total_path = [current]
  while current in cameFrom.keys():
    current = cameFrom[current]
    total_path.append(current)
  return total_path

def get_types(node, cave):
  return [(node[0], node[1], r) for r in TOOL_TYPES[cave[node[0]][node[1]][3]]]


def get_neighbors(node, cave):
  potential_neighbors = [(node[0]+1, node[1]),
          (node[0]-1, node[1]),
          (node[0],   node[1]+1),
          (node[0],   node[1]-1)]
  ret = []
  for n in potential_neighbors:
    if (n[0] >= 0 and n[1] >= 0 and n[0] < len(cave) and n[1] < len(cave[0])):
      ret.extend(get_types(n, cave))
  return ret

def a_star(start, goal, board, debug = False):
  closedSet = set()
  openSet = set([start])
  cameFrom = {}
  gScore = {}
  gScore[start] = 0
  fScore = {}
  fScore[start] = heuristic_cost_estimate(start, goal)
  while openSet:
    minscore = 99999999999
    minnode = None
    for node in openSet:
      if fScore[node] < minscore:
        minscore = fScore[node]
        minnode = node
    current = minnode
    if debug:
      print "current = %s goal = %s" % (str(current), str(goal))
    if current == goal:
      return reconstruct_path(cameFrom, current)
    openSet.remove(current)
    closedSet.add(current)
    for neighbor in get_neighbors(current, board):
      if neighbor in closedSet:
        continue
      tentative_gscore = gScore[current] + get_cost_estimate(current, neighbor)
      if neighbor not in openSet:
        openSet.add(neighbor)
      elif tentative_gscore >= gScore[neighbor]:
        continue
      cameFrom[neighbor] = current
      gScore[neighbor] = tentative_gscore
      fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

def get_cost_estimate(start, goal):
  # Can't change to a tool that we're not allowed to equip in the current space.
  if goal[2] not in TOOL_TYPES[cave[start[0]][start[1]][3]]:
    return 999999
  # Changing a tool is 7 minutes changing + 1 minute moving
  elif start[2] != goal[2]:
    return 8
  else:
    return 1

def heuristic_cost_estimate(start, goal):
  return (abs(start[0]-goal[0]) + abs(start[1]-goal[1]))


def build_cave(size, depth, target):
  cave = numpy.zeros(size, dtype=object)

  for x in xrange(len(cave)):
    for y in xrange(len(cave[0])):
      if (x, y) in [(0, 0), target]:
        geo = 0
      elif x == 0:
        geo = y * 48271
      elif y == 0:
        geo = x * 16807
      else:
        geo = cave[x-1][y][1] * cave[x][y-1][1]
      erosion = (geo + depth) % 20183
      types = ['.', '=', '|'] 
      cvscore = erosion % 3
      cvtyp = types[cvscore]
      cave[x][y] = (geo, erosion, cvscore, cvtyp)
  return cave


cave = build_cave((50, 1000), depth, target)

# Part 1: Risk level
mysum = 0
for x in xrange(target[0]+1):
  for y in xrange(target[1]+1):
    mysum += cave[x][y][2]
print "Part 1: Risk level = %s" % mysum


# Part 2: Shortest Path
route = a_star((0,0,'t'), (target[0], target[1], 't'), cave)

cost = 0
# a* gives us the route from finish to start, switch it around to the right order.
route.reverse()
for x in xrange(1, len(route)):
  cost += get_cost_estimate(route[x-1], route[x])
print "Part 2: Minimum cost = %s" % cost
    

