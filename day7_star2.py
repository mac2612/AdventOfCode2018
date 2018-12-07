import string

class Node(object):
  def __init__(self, letter):
    self.letter = letter
    self.deps = []
    self.nxt = []
    self.visited=False
    self.working=False

class Worker(object):
  def __init__(self, id):
    self.id = id
    self.step = None
    self.secs_remaining = 0

workers = []
for x in xrange(5):
  workers.append(Worker(x))

nodes = {}
cost_map = {}
cost = 1
for l in string.ascii_uppercase:
  nodes[l] = Node(l)
  cost_map[l] = cost + 60
  cost += 1


with open('input.txt', 'r') as fp:
  for line in fp:
    dep = line[line.find('Step ')+5: line.find(' must')]
    step = line[line.find('step ')+5:line.find(' can')]
    nodes[step].deps.append(dep)
    nodes[dep].nxt.append(step)

visit_count = 0
secs = 0
while(True):
  for w in workers:
    if w.step:
      w.secs_remaining -= 1
    if w.step and w.secs_remaining == 0:
      w.secs_remaining = 0
      nodes[w.step].visited = True
      nodes[w.step].working = False
      for node in nodes.itervalues():
        if w.step in node.deps:
          node.deps.remove(w.step)
      w.step = None
      visit_count += 1

  choices = sorted([x for x in nodes.iterkeys() if not nodes[x].deps and not nodes[x].visited and not nodes[x].working])
  for w in workers:
    if len(choices) > 0 and not w.step:
      choice = choices[0]
      print "worker %d visiting node %s" % (w.id, choice)
      w.step = choice
      w.secs_remaining = cost_map[choice]
      nodes[choice].working = True
      choices.remove(choice)
   
  print ("second %d worker 1 %s worker 2 %s worker 3 %s worker 4 %s worker 5 %s done %s" % 
	        (secs, 
		workers[0].step, 
		workers[1].step, 
		workers[2].step, 
		workers[3].step, 
		workers[4].step, 
		''.join([x for x in nodes.iterkeys() if nodes[x].visited])))
  if visit_count == len(nodes):
    break
  secs += 1

print 'total secs = %d' % secs
