import numpy as np

SERNUM=9435

a = np.zeros((300,300))


def get_digit(number, n):
  return number // 10**n % 10

def get_power(x, y):
  rack_id = int(x)+1 + 10
  power = rack_id * (int(y)+1)
  power += SERNUM
  power = power * rack_id
  power = get_digit(power, 2)
  power -= 5
  return power

for x in xrange(300):
  for y in xrange(300):
    a[x][y] = get_power(x, y)

sums = {}
coords = {}

for msz in xrange(300):
  print 'msz = %s' % msz
  max_sum = 0
  for x in xrange(300-msz):
    for y in xrange(300-msz): 
      mysum = 0
      for sumx in xrange(msz):
        for sumy in xrange(msz):
          mysum += a[x+sumx][y+sumy]
        
      if mysum > max_sum:
        max_sum = mysum 
        sums[msz] = (max_sum, x+1, y+1)
  if msz in sums:
    print "Max for size msz %s: %s, (%s, %s)" % (msz, sums[msz][0], sums[msz][1], sums[msz][2]) 


maxv = 0
for key, val in sums.iteritems():
  if val[0] > maxv:
    print "new max sz %s:  %s %s %s" % (key,val[0], val[1], val[2])
    max = val[0]

