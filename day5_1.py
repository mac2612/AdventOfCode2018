import ctypes

with open('input.txt', 'r') as fp:
  p = fp.readline().replace('\n', '')

op = True
p = ctypes.create_string_buffer(p)
while(op):
  op=False
  for x in xrange(len(p)-1):
    if (p[x].islower() and p[x+1] == p[x].upper() 
        or p[x].isupper() and p[x+1] == p[x].lower()):
      op = True
      p[x] = '_'
      p[x+1] = '_'
  p = ctypes.create_string_buffer(str(p.value).replace('_', ''))

print 'reacted length %d' % len(p.value)
