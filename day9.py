NUM_PLAYERS = 458
LAST_MARBLE = 71307

class Player(object):
  def __init__(self, player_num):
    self.player_num = player_num
    self.score = 0

class Marble(object):
  def __init__(self, num):
    self.num = num
    self.next = None
    self.prev = None

players = []

for n in xrange(NUM_PLAYERS):
  players.append(Player(n))

def insert_fwd(marble, newmarble):
  newmarble.next = marble.next
  newmarble.prev = marble
  marble.next = newmarble
  newmarble.next.prev = newmarble
  return newmarble

def remove_cur(marble):
  marble.prev.next = marble.next
  marble.next.prev = marble.prev
  new_cur = marble.next
  return new_cur

def back_7(marble):
  return marble.prev.prev.prev.prev.prev.prev.prev

def play(player, marble, turn):
  if turn % 23 == 0:
    player.score += turn
    marble = back_7(marble)
    player.score += marble.num
    marble = remove_cur(marble)
  else:
    marble = insert_fwd(marble.next, Marble(turn))
  return marble

cur_marble = Marble(0)
cur_marble.next = cur_marble
cur_marble.prev = cur_marble

turn = 1
playing = True
while playing:
  for player in players:
    cur_marble = play(player, cur_marble, turn)
    turn += 1
    if turn >= LAST_MARBLE:
      playing = False
      break

print "Winning score is %d" % max([x.score for x in players])

