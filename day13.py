import ctypes
import numpy
import copy

collision = False
crashed_cars = []

line_map = {'<': '-', '>': '-', '^': '|', 'v': '|'}
class Car(object):
  def __init__(self, direction):
    self.direction = direction
    self.decision = ['left', 'straight', 'right']
    self.decision_state = 0
    self.moved = False

def turn_car_left(car):
  dirs = {'^': '<', 'v': '>', '<': 'v', '>': '^'}
  car.direction = dirs[car.direction]

def turn_car_right(car):
  dirs = {'^': '>', 'v': '<', '<': '^', '>': 'v'}
  car.direction = dirs[car.direction]

lines_parsed = []
with open('input.txt', 'r') as fp:
  for line in fp:
    lines_parsed.append(ctypes.create_string_buffer(line[:-1]))
cars = numpy.zeros((len(lines_parsed), len(lines_parsed[0])), dtype=list)
for x in xrange(len(lines_parsed)):
    for y in xrange(len(lines_parsed[x])):
      if lines_parsed[x][y] in ['<', '>', '^', 'v']:
        cars[x][y] = [Car(lines_parsed[x][y])]
        lines_parsed[x][y] = line_map[lines_parsed[x][y]]

def tick():
  uncrashed_cars = len([x for x in cars.flatten() if x != 0])
  print "%s uncrashed cars" % uncrashed_cars
  if uncrashed_cars == 1:
    print "Only 1 cart left!:"
    for x in xrange(len(cars)):
      for y in xrange(len(cars[0])):
        if cars[x][y] != 0:
          print "(%d, %d)" % (y, x)
    return False
  for c in cars.flatten():
    if c != 0:
      c[0].moved = False
  for x in xrange(len(cars)):
    for y in xrange(len(cars[0])):
      if cars[x][y] != 0:
        car = cars[x][y][0]
        if not car.moved:
          move_car(car, x, y)
        car.moved = True
  return True

def move_car(car, x, y):
  if lines_parsed[x][y] == '+':
    handle_intersection(car, x, y)
  if car.direction == '<':
    move_car_left(car, x, y)
  elif car.direction == '>':
    move_car_right(car, x, y)
  elif car.direction == '^':
    move_car_up(car, x, y)
  elif car.direction == 'v':
    move_car_down(car, x, y)


def move_car_left(car, x, y):
  if cars[x][y-1] != 0 and len(cars[x][y-1]) == 1:
    print "Collision! at (%d, %d) " % (y-1, x)
    collision = True
    crashed_cars.append(cars[x][y][0])
    crashed_cars.append(cars[x][y-1][0])
    cars[x][y] = 0
    cars[x][y-1] = 0
    return
  cars[x][y] = 0
  cars[x][y-1] = [car]
  char = lines_parsed[x][y-1]
  if char == '/':
    car.direction = 'v'
  elif char == '\\':
    car.direction = '^'
  elif char != '-' and char != '+':
    print "left: Nowhere to go!"


def move_car_right(car, x, y):
  if cars[x][y+1] != 0 and len(cars[x][y+1]) == 1:
    print "Collision! at (%d, %d) " % (y+1, x)
    crashed_cars.append(cars[x][y][0])
    crashed_cars.append(cars[x][y-1][0])
    cars[x][y] = 0
    cars[x][y-1] = 0
    return
  cars[x][y] = 0
  cars[x][y+1] = [car]
  char = lines_parsed[x][y+1]
  if char == '/':
    car.direction = '^'
  elif char == "\\":
    car.direction = 'v'
  elif char != '-' and char != '+':
    print "right:Nowhere to go!"


def move_car_up(car, x, y):
  if cars[x-1][y] != 0 and len(cars[x-1][y]) == 1:
    print "Collision! at (%d, %d) " % (y, x-1)
    crashed_cars.append(cars[x][y][0])
    crashed_cars.append(cars[x-1][y][0])
    cars[x][y] = 0
    cars[x-1][y] = 0
    return
  cars[x][y] = 0
  cars[x-1][y] = [car]
  char = lines_parsed[x-1][y]
  if char == '\\':
    car.direction = '<'
  elif char == "/":
    car.direction = '>'
  elif char != '|' and char != '+':
    print "up: Nowhere to go!"

def move_car_down(car, x, y):
  if cars[x+1][y] != 0 and len(cars[x+1][y]) == 1:
    print "Collision! at (%d, %d) " % (y, x+1)
    crashed_cars.append(cars[x][y][0])
    crashed_cars.append(cars[x+1][y][0])
    cars[x][y] = 0
    cars[x+1][y] = 0
    return
  cars[x][y] = 0
  cars[x+1][y] = [car]
  char = lines_parsed[x+1][y]
  if char == '\\':
    car.direction = '>'
  elif char == "/":
    car.direction = '<'
  elif char != '|' and char != '+':
    print "down: Nowhere to go!"

def handle_intersection(car, x, y):
  decision = car.decision[car.decision_state]
  if decision == 'left':
    turn_car_left(car)
  elif decision == 'straight':
    pass 
  elif decision == 'right':
    turn_car_right(car)
  car.decision_state += 1
  car.decision_state = car.decision_state % len(car.decision)

iter = 0
cont = True
dump = False
while(cont):
  print "iter = %s" % iter
  if dump:
    for x in xrange(len(lines_parsed)):
      value = copy.deepcopy(lines_parsed[x])
      for y in xrange(len(lines_parsed[x].value)):
        if cars[x][y] != 0:
          value[y] = cars[x][y][0].direction
      print value.value
  cont = tick()
  iter += 1
