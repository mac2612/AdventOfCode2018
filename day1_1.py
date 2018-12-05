accum = 0

with open('input.txt', 'r') as fp:
  for line in fp:
    accum += int(line)

print "Total: " + str(accum)

