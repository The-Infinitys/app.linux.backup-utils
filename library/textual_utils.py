from textual.color import Color

def Color_HSV(h,s,v):
    h=h/360
    s=s/100
    v=v/100
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    p=int(p)
    q=int(q)
    v=int(v)
    t=int(t)
    if i == 0: return Color(v, t, p)
    if i == 1: return Color(q, v, p)
    if i == 2: return Color(p, v, t)
    if i == 3: return Color(p, q, v)
    if i == 4: return Color(t, p, v)
    if i == 5: return Color(v, p, q)