
class Node(object):
  def __init__(self, num_children, num_metadata, node_num):
    self.num_children = num_children
    self.num_metadata = num_metadata
    self.children = []
    self.metadata = []
    self.node_num = node_num


def parseNode(num_iter, node_num):
  num_children = num_iter.next()
  num_metadata = num_iter.next()
  node = Node(num_children, num_metadata, node_num)
  for x in xrange(num_children):
    newnode = parseNode(node_iter, node_num+1)
    node.children.append(newnode)
  for x in xrange(num_metadata):
    node.metadata.append(num_iter.next())
  return node


def get_value(node):
  if node.num_children == 0:
    return sum(node.metadata)
  value = 0
  for m in node.metadata:
    if m != 0 and m-1 < len(node.children):
      value += get_value(node.children[m-1])
  return value

def get_metasum(node):
  return sum(node.metadata) + sum([get_metasum(x) for x in node.children]) 
    

with open('input.txt', 'r') as fp:
  for line in fp:
    nums = [int(x) for x in line[:-1].split(' ')]
    node_iter = iter(nums)
    root_node = parseNode(node_iter, 0)
    print "metadata sum = %s" % get_metasum(root_node)
    print "root value = %s" % get_value(root_node) 


