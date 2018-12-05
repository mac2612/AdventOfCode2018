accum = 0
freqs = set()
found = False

while(not found):
  with open('input.txt', 'r') as fp:
    for line in fp:
      accum += int(line)
      if accum in freqs:
        print "Dupefreq: " + str(accum)
        found = True
        break
      freqs.add(accum)
