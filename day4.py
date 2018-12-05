from datetime import datetime
from datetime import timedelta

entries = []

class Entry:
  def __init__(self, date, event):
    self.date = date
    self.event = event
  def __str__(self):
    return "Date: %s Event: %s" % (self.date, self.event)

with open('input.txt', 'r') as fp:
  for line in fp:
    datestr = line[line.find('[')+1:line.find(']')]
    date = datetime.strptime(datestr, '%Y-%m-%d %H:%M')
    event = line[line.find(']')+2:-1]
    entries.append(Entry(date,event))
  entries.sort(key=lambda r: r.date)
  guard_id = 0
  asleep_time = None
  guards = {}
  guard_minute = {}
  for e in entries:
    if e.event.find('Guard') >= 0:
      guard_id = e.event[e.event.find('#')+1:e.event.find(' begins')]
    if e.event.find('asleep') >= 0:
      asleep_time = e.date
    if e.event.find('wakes up') >= 0:
      if guard_id not in guards:
        guards[guard_id] = 0
      minutes = (e.date - asleep_time).seconds/60
      guards[guard_id] += minutes
      for i in range(((e.date - asleep_time).seconds/60)):
        minute = (asleep_time + timedelta(0, i*60)).minute
        key = "%s_%s" % (guard_id, minute)
        if key not in guard_minute:
          guard_minute[key] = 0
        guard_minute[key] += 1

  maxguard = max(guards, key=guards.get)
  print 'Part 1: Sleepiest guard id %s slept for %d minutes' % (maxguard, guards[maxguard])
  tmp_minutes = {x[0].split('_')[1]:x[1]
                  for x in guard_minute.iteritems() 
                  if x[0].startswith(maxguard)}
  max_minute = int(max(tmp_minutes, key=tmp_minutes.get))
  print 'Max sleepy minute: %d, multiplied: %d' % (max_minute, max_minute * int(maxguard))
   
  
  maxkey = max(guard_minute, key=guard_minute.get)
  print 'Part 2: Max guard/minute slept: %s, value: %s' % (maxkey, guard_minute[maxkey])
  keys = maxkey.split('_')
  print 'Guard * minute = %d' % (int(keys[0]) * int(keys[1]))
