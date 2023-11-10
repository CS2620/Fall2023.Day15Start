def rgb_to_hsv(r, g, b):
  h = 0
  s = 0
  v = 0
  return (h, s, v)

def rgb_to_cmyk(r, g, b):
  mx = max(r/255,g/255,b/255)
  k = 1 - mx
  if mx == 0:
    return (0,0,0,1)
  c = (1-r/255-k)/(1-k)
  m = (1-g/255-k)/(1-k)
  y = (1-b/255-k)/(1-k)
  return (int(c*255),int(m*255),int(y*255),int(k*255))