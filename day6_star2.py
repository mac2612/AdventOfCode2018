import numpy

allx = []
ally = []

class Point:
  def __init__(self, id, is_anchor, closest_anchor, is_infinite, coordinate_dist_sum):
    self.id = id
    self.is_anchor = is_anchor
    self.closest_anchor = closest_anchor
    self.coordinate_dist_sum = coordinate_dist_sum
  def __str__(self):
    return "id: %s is_anchor: %s closest %s" % (self.id, self.is_anchor, closest_anchor)


with open('input.txt', 'r') as fp:
  for line in fp:
   points = line.split(', ')
   (x, y) = int(points[0]), int(points[1])
   allx.append(x)
   ally.append(y)

max_x = max(allx)
max_y = max(ally)

array = numpy.zeros((max_x+1, max_y+1), dtype=object)

for i in xrange(len(allx)):
  csum = 0
  for it in xrange(len(allx)):
    dist = abs(allx[i] - allx[it]) + abs(ally[i] - ally[it])
    csum += dist
  array[allx[i]][ally[i]] = Point(i, True, None, False, csum)


for x in xrange(max_x+1):
  for y in xrange(max_y+1):
    if array[x][y] == 0:
      min_val = 9999999999999999
      min_idx = -1
      dupe = False
      csum = 0
      for it in xrange(len(allx)):
        dist = abs(x - allx[it]) + abs(y - ally[it])
        csum += dist
        if dist == min_val:
          dupe = True
        if dist < min_val:
          dupe = False
          min_val = dist
          min_idx = it
      closest_anchor = min_idx if not dupe else -1
      array[x][y] = Point(-1, False, closest_anchor, False, csum)

areas = {}
for it in xrange(len(allx)):
  area = len([i for i in array.flatten() if i.closest_anchor == it or (i.is_anchor and i.id == it)])
  areas[it] = area

inf = set()
for x in xrange(max_x+1):
  if array[x][0].is_anchor:
    inf.add(array[x][0].id)
  else:
    inf.add(array[x][0].closest_anchor)
  if array[x][max_y].is_anchor:
    inf.add(array[x][0].id)
  else:
    inf.add(array[x][max_y].closest_anchor)
for y in xrange(max_y+1):
  if array[0][y].is_anchor:
    inf.add(array[0][y].id)
  else:
    inf.add(array[0][y].closest_anchor)
  if array[max_x][y].is_anchor:
    inf.add(array[max_x][y].id)
  else:
    inf.add(array[max_x][y].closest_anchor)

for x in set(inf):
  if x in areas:
    areas.pop(x)
    
print "Non-infinite areas: %s " % areas

print "Max area: id: %s count %d" % (max(areas, key=areas.get), areas[max(areas, key=areas.get)])

region_size = len([x for x in array.flatten() if x.coordinate_dist_sum < 10000])
print "Region size %d" % region_size
