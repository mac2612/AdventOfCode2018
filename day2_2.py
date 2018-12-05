import difflib

lines = []

with open('input.txt', 'r') as fp:
  for line in fp:
    lines.append(line)

found = False
for line in lines:
  if not found:
    for lineb in lines:
      if line != lineb:
        test = difflib.SequenceMatcher(None, line, lineb)
        blocks = test.get_matching_blocks()
        match_size = sum([x.size for x in blocks])
        if match_size == (len(line)-1) and match_size == (len(lineb) - 1):
          print "Found! line = %s lineb = %s" % (line, lineb)
          found = True
          break 

