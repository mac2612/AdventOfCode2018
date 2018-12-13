import ctypes
import pdb
PAD = 2000

state = ctypes.create_string_buffer('.' * PAD + '#.#.#..##.#....#.#.##..##.##..#..#...##....###..#......###.#..#.....#.###.#...#####.####...#####.#.#' + '.' * PAD)

rules_str = """..#.. => .
#...# => .
.#... => #
#.##. => .
..#.# => #
#.#.# => .
###.. => #
###.# => #
..... => .
....# => .
.##.. => #
##### => .
####. => .
..##. => .
##.#. => #
.#..# => #
##..# => .
.##.# => .
.#### => #
..### => .
...## => #
#..## => #
#.... => .
##.## => .
#.#.. => .
##... => .
.#.## => #
.###. => #
...#. => .
#.### => .
#..#. => #
.#.#. => .
"""


def count_all(val):
  count = 0
  for x in xrange(len(val)):
    if val[x] == '#':
      count += (x-PAD)
  return count


class Rule(object):
  def __init__(self, matrix, state):
    self.matrix = matrix
    self.state = state

rules = []

for rule in rules_str.split('\n'):
  matrix = rule[0:5]
  mystate = rule[-1:]
  rules.append(Rule(matrix,mystate))


def test_pot(array, array_new, idx, rules):
  for rule in rules:
    if len([i for i, j in zip(array[idx-2:idx+3], rule.matrix) if i == j]) == 5:
      array_new[idx] = rule.state
    
debug = False
generations = 200
old_count = count_all(state.value)
if debug:
  print "%d: %s" % (0, state.value)
new_state = state
for g in xrange(generations):
  if debug:
    print "%d: %s" % (g+1, state.value)
  state = new_state
  new_state = ctypes.create_string_buffer(len(state.value) * '.')
  for x in xrange(len(state)):
    test_pot(state, new_state, x, rules)
  count = count_all(new_state.value)
  print "gen = %s count = %s diff = %s" % (g+1, count, count-old_count)
  old_count = count

