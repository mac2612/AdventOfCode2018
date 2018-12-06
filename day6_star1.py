import numpy

allx = []
ally = []

with open('input.txt', 'r') as fp:
  for line in fp:
   points = line.split(', ')
   (x, y) = int(points[0]), int(points[1])
   allx.append(x)
   ally.append(y)

max_x = max(allx)
max_y = max(ally)

array = numpy.full((max_x+1, max_y+1), fill_value=-2)

for i in xrange(len(allx)):
  array[allx[i]][ally[i]] = i

for x in xrange(max_x+1):
  for y in xrange(max_y+1):
    if array[x][y] == -2:
      min_val = 9999999999999999
      min_idx = -1
      dupe = False
      for it in xrange(len(allx)):
        dist = abs(allx[it]-x) + abs(ally[it] - y)
        if dist == min_val:
          dupe = True
        if dist < min_val:
          dupe = False
          min_val = dist
          min_idx = it
      closest_anchor = min_idx if not dupe else -1
      array[x][y] = closest_anchor

areas = {}
(unique, counts) = numpy.unique(array.flatten(), return_counts=True)
for x in xrange(len(unique)):
  areas[unique[x]] = counts[x]

inf = set()
for x in xrange(max_x+1):
  inf.add(array[x][0])
  inf.add(array[x][max_y])

for y in xrange(max_y+1):
  inf.add(array[0][y])
  inf.add(array[max_x][y])

for x in set(inf):
  if x in areas:
    areas.pop(x)

print "non-infinite areas: %s " % areas
print "Max area: id: %s count %d" % (max(areas, key=areas.get), areas[max(areas, key=areas.get)])
