from PIL import ImageFont # Image, ImageDraw,
from math import pi, sin, cos

#e=9

# basic colour choice for lcd dial
def colour_choice(colour):
    blued={'f':'#02fdf6','b':'#0031a7','g':'#0d4fdb','s':'#18a1ff'}
    oranged={'f':'#fee737','b':'#7b0106','g':'#5E0B0B','s':'#fa0e20'} # g410101 c6020b
    greend={'f':'#00F23C','b':'#002504','g':'#005914','s':'#84aea7'} # f00d435
    purpled={'f':'#F9F9FD','b':'#1D1739','g':'#3F1E4B','s':'#9493A1'}
# b 350002
    if colour=='purple':
        bdial=purpled['b']
        gdial=purpled['g']
        fdial=purpled['f']
        sdial=purpled['s']

    elif colour=='blue':
        bdial=blued['b']
        gdial=blued['g']
        fdial=blued['f']
        sdial=blued['s']

    elif colour=='green':
        bdial=greend['b']
        gdial=greend['g']
        fdial=greend['f']
        sdial=greend['s']

    else:
        bdial=oranged['b']
        gdial=oranged['g']
        fdial=oranged['f']
        sdial=oranged['s']
    return bdial,fdial,gdial,sdial

# create pieslice with centre and radius
def create_pieslice(idraw,c,r,outline='#888888',fill='#888888',start=0,end=90):
    return idraw.pieslice([c[0]-r,c[1]-r,c[0]+r,c[1]+r], # c[0]+r-1,c[1]+r-1],
                          outline=outline,fill=fill,start=start,end=end)

# extent starts at 0 along x axis, goes anticlockwise, style PIESLICE
def tk_arc(canvas,c,r,style,start,extent,outline='#888888',fill='#888888'):
    return canvas.create_arc([c[0]-r,c[1]-r,c[0]+r,c[1]+r],style=style,
        start=start,extent=extent,outline=outline,fill=fill)

def create_chord(idraw,c,r,outline='#888888',fill='#888888',start=0,end=90):
    return idraw.chord([c[0]-r,c[1]-r,c[0]+r,c[1]+r],
                          outline=outline,fill=fill,start=start,end=end)

# create circle with centre and radius
def create_circle(idraw,c,r,outline='#888888',fill='#888888'):
    return idraw.ellipse([c[0]-r,c[1]-r,c[0]+r,c[1]+r],
                          outline=outline,fill=fill)

# create circle with centre and radius
def tk_circle(canvas,c,r,outline='#888888',fill='#888888'):
    return canvas.create_oval([c[0]-r,c[1]-r,c[0]+r,c[1]+r],
                          outline=outline,fill=fill)

# create text according to polar co-ordinates
def draw_text(idraw,text,c,ro,angle,font='arial',size=12,fill='#888888'):
    rangle = angle * pi / 180.0
    x0 = c[0] + ro * cos(rangle)
    y0 = c[1] + ro * sin(rangle)
    ttffont = ImageFont.truetype(font+'.ttf', size=size) # LCD needed TTF
    (width, height), (offset_x, offset_y) = ttffont.font.getsize(text)
    return idraw.text((x0-width//2-offset_x,y0-height//2-offset_y),text,
        font=ttffont,fill=fill)

# create text according to polar co-ordinates
def tk_text(canvas,text,c,ro,angle,font='arial',size=12,fill='#888888',tags=''):
    rangle = angle * pi / 180.0
    x0 = c[0] + ro * cos(rangle)
    y0 = c[1] + ro * sin(rangle)
    return canvas.create_text((x0,y0),text=text,font=(font,size,'italic'),
        fill=fill,tags=tags)

# make triangles around dial
def draw_delta(idraw,angle,c,ro,e,fill='#888888'):
    rangle = angle * pi / 180.0
    x0 = c[0] + ro * cos(rangle)
    y0 = c[1] + ro * sin(rangle)
    x1 = x0 + 2*e * sin(rangle)
    y1 = y0 - 2*e * cos(rangle)
    x2 = x0 - 2*e * sin(rangle)
    y2 = y0 + 2*e * cos(rangle)
    x3 = c[0] + (ro -3*e) * cos(rangle)
    y3 = c[1] + (ro -3*e) * sin(rangle)
    #print(x1,x2,x3)
    return idraw.polygon([x1,y1,x2,y2,x3,y3],fill=fill)

def tk_delta(canvas,angle,c,ro,e,fill='#888888'):
    rangle = angle * pi / 180.0
    x0 = c[0] + ro * cos(rangle)
    y0 = c[1] + ro * sin(rangle)
    x1 = x0 + 2*e * sin(rangle)
    y1 = y0 - 2*e * cos(rangle)
    x2 = x0 - 2*e * sin(rangle)
    y2 = y0 + 2*e * cos(rangle)
    x3 = c[0] + (ro -3*e) * cos(rangle)
    y3 = c[1] + (ro -3*e) * sin(rangle)
    return canvas.create_polygon([x1,y1,x2,y2,x3,y3],fill=fill)


# create tick with centre, radius, length, angle (starting 3 o' clock
# increasing clockwise
def draw_tick(idraw,c,ri,l,angle,fill='#888888',width=1):
    rangle = angle * pi / 180.0
    x0 = c[0] + ri * cos(rangle)
    y0 = c[1] + ri * sin(rangle)
    x1 = c[0] + (ri + l) * cos(rangle)
    y1 = c[1] + (ri + l) * sin(rangle)
    return idraw.line([x0,y0,x1,y1],fill=fill,width=width)

# create tick with centre, radius, length, angle (starting 3 o' clock
# increasing clockwise
def tk_tick(canvas,c,ri,l,angle,fill='#888888',width=1,tags=None):
    rangle = angle * pi / 180.0
    x0 = c[0] + ri * cos(rangle)
    y0 = c[1] + ri * sin(rangle)
    x1 = c[0] + (ri + l) * cos(rangle)
    y1 = c[1] + (ri + l) * sin(rangle)
    return canvas.create_line([x0,y0,x1,y1],fill=fill,width=width,tags=tags)

# pointer angle for analogue dial, used when superimposing rotating pointer
def pangle(val, maxval, minval):
    val = val if val < maxval else maxval
    val = val if val > minval else minval
    return (val- minval) / (maxval - minval) * degree_extent

