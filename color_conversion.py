def rgb_to_hsv(r, g, b):
  v = max(r,g,b)
  n = min(r,g,b)
  d = 0
  if (g > r > b) or (b > r > g):
    d = r
  elif (r > g > b) or (b > g > r):
    d = g
  else
    d = b

  s = (v - n)/v

  base_angle = 0
  offset_angle = 0

  if v == r:
    base_angle = 0
    offset_angle = (g - b)/(v-n)*60
  elif v == g:
    base_angle = 120
    offset_angle = (b-r)/(v-n)*60
  else if v == b:
    base_angle = 240
    offset_angle = (r-g)/(v-n)*60

  final_angle = base_angle + offset_angle

  if final_angle < 0:
    final_angle += 360

  h = final_angle
  
  return (h/360, s, v)

def rgb_to_cmyk(r, g, b):
  _r, _g, _b = r/255, g/255, b/255
  maximum = max(_r, _g, _b)

  k = 1-maximum
  if k == 1:
    return (0,0,0,1)
  c = (1-_r-k)/(1-k)
  m = (1-_g-k)/(1-k)
  y = (1-_b-k)/(1-k)
  return (int(c*255),int(m*255),int(y*255),int(k*255))