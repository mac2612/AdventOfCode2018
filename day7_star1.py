import string

class Node(object):
  def __init__(self, letter):
    self.letter = letter
    self.deps = []
    self.visited=False

nodes = {}
for l in string.ascii_uppercase:
  nodes[l] = Node(l)
    

with open('input.txt', 'r') as fp:
  for line in fp:
    dep = line[line.find('Step ')+5: line.find(' must')]
    step = line[line.find('step ')+5:line.find(' can')]
    nodes[step].deps.append(dep)

for n in nodes.itervalues():
  if not n.deps:
    print "potential start step %s" % n.letter


curNode = nodes['D']
path = []
while(True):
  path += curNode.letter
  nodes[curNode.letter].visited = True
  print "visiting node %s" % curNode.letter
  for node in nodes.itervalues():
    if curNode.letter in node.deps:
      node.deps.remove(curNode.letter)
  choices = sorted([x for x in nodes.iterkeys() if not nodes[x].deps and not nodes[x].visited])
  # print "choices = %s" % str(choices)
  if not choices:
    print 'no choices!'
    break
  curNode = nodes[choices[0]]

print 'path = %s' % ''.join(path)
