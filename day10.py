from PIL import Image, ImageDraw, ImageColor

class Point(object):
  def __init__(self, posx, posy, velx, vely):
    self.posx = posx
    self.posy = posy
    self.last_posx = posx
    self.last_posy = posy
    self.velx = velx
    self.vely = vely
  
points = []
with open('input.txt', 'r') as fp:
  for line in fp:
    coord = (line[line.find("sition<")+11:line.find("> veloc")]).split(',')
    vel = (line[line.find("locity<")-7:-2]).split(',')
    points.append(Point(int(coord[0]), int(coord[1]), int(vel[0]), int(vel[1])))

x_pos = [x.posx for x in points]
y_pos = [x.posy for x in points]
last_maxdiff_x = max(x_pos)-min(x_pos) 
num_iter = 100000
have_soln = False
for i in xrange(num_iter):
  for point in points:
    point.last_posx = point.posx
    point.last_posy = point.posy
    point.posx += point.velx
    point.posy += point.vely
  x_pos = [x.posx for x in points]
  y_pos = [x.posy for x in points]
  maxdiff_x = max(x_pos)-min(x_pos)
  if last_maxdiff_x < maxdiff_x:
    have_soln=True
    print "Found solution! i = %s" % i
    break
  #print "iter = %s maxdiff_x = %s maxdiff_y = %s" % (i, max(x_pos)-min(x_pos), max(y_pos)-min(y_pos))
  last_maxdiff_x = maxdiff_x


   
x_pos = [x.last_posx for x in points]
y_pos = [y.last_posy for y in points]
offset_zero_x = 0-min(x_pos)
img_max_x = max(x_pos)+offset_zero_x
offset_zero_y = 0-min(y_pos)
img_max_y = max(y_pos)+offset_zero_y
print "Image size %s %s" % (img_max_x, img_max_y)
im = Image.new('RGB', (img_max_x+1, img_max_y+1), color='white')
for p in points:
  im.putpixel((p.last_posx+offset_zero_x, p.last_posy+offset_zero_y), (0, 0, 0))

im.save('test.png')

