import ctypes
import string

with open('input.txt', 'r') as fp:
  orig_p = fp.readline().replace('\n', '')

val_len = {}

for value in string.ascii_lowercase:
  p = ctypes.create_string_buffer(orig_p)
  p = ctypes.create_string_buffer(str(p.value).replace(value, ''))
  p = ctypes.create_string_buffer(str(p.value).replace(value.upper(), ''))
  op = True
  while(op):
    op=False
    for x in xrange(len(p)-1):
      if (p[x].islower() and p[x+1] == p[x].upper() 
          or p[x].isupper() and p[x+1] == p[x].lower()):
        op = True
        p[x] = '_'
        p[x+1] = '_'
    p = ctypes.create_string_buffer(str(p.value).replace('_', ''))
  # Print as we go along in case we get lucky.
  print 'min length for value %s: %d' % (value, len(p.value))
  val_len[value] = len(p.value)-1
    
min_letter = min(val_len, key=val_len.get)
print 'Minimum reacted removal: %s; %d reacted length' % (min_letter, val_len[min_letter])
