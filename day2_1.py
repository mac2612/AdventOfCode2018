import difflib

count_withtwo = 0
count_withthree = 0

with open('input.txt', 'r') as fp:
  for line in fp:
    chars = {}
    for char in line:
      if char in chars:
        chars[char] += 1
      else:
        chars[char] = 1
    for count in chars.itervalues():
      if count == 2:
        count_withtwo += 1
        break
    for count in chars.itervalues():
      if count == 3:
        count_withthree += 1
        break

print "Checksum: %d" % (count_withtwo * count_withthree)
