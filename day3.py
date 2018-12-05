import numpy

array = numpy.zeros((1000, 1000), dtype=object)

lines = []
with open('input.txt', 'r') as fp:
  for line in fp:
    startloc = line[line.find('@')+2:line.find(':')]
    (startx, starty) = [int(x) for x in startloc.rsplit(',')]
    sizeline = line[line.find(':')+2:]
    (sizex, sizey) = [int(x) for x in sizeline.rsplit('x')]
    lot = line[line.find('#')+1:line.find('@')-1]
    for x in xrange(sizex):
      for y in xrange(sizey):
        if array[startx+x][starty+y] == 0:
          array[startx+x][starty+y] = []
        array[startx+x][starty+y].append(lot)
  count = sum([1 for x in array.flat if x != 0 and len(x) >= 2])
  overlapping = [x for x in array.flat if x!= 0 and len(x) >= 2]
  overset = set([item for sublist in overlapping for item in sublist])
  singlelot = [x for x in array.flat if x != 0 and len(x) == 1]
  singleset = set([item for sublist in singlelot for item in sublist])
  
  print "sqin within 2 or more claims: %d" % count
  print "claims with no overlaps: %s" % str(singleset - overset)
