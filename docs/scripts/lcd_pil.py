from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, Label, PhotoImage
from DialUtils import colour_choice,create_circle,draw_text,create_pieslice

def pilpointer(select,val,unit='Temp C'):

    # lcd gauge type; min,max scale extent; st,end start end degrees;
    # upt units per tick; w width pixels; tw tick width; farbe colour
    # mess gauge type
    lcds={
            1:{'lcd':'lcd70','min':-30,'max':70,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'temperature','farbe': 'blue'},
            2:{'lcd':'lcd100','min':0,'max':100,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'general\npurpose','farbe': 'purple'},
            3:{'lcd':'lcd255','min':0,'max':270,'st':135,'end':45,'upt':2,
                    'w':201,'tw':2,'mess':'analogue\n output','farbe': 'red'},
            4:{'lcd':'lcd1023','min':0,'max':1030,'st':117,'end':63,'upt':10,
                    'w':201,'tw':4,'mess':'analogue\n input','farbe': 'green'}
                    }

    h=w=lcds[select]['w']
    c=w//2,h//2
    r=w//2
    max_value=lcds[select]['max']
    min_value=lcds[select]['min']
    max_scale=lcds[select]['max']
    unitspertick=lcds[select]['upt']
    # 300° scale extent, 100 divisions therefore 1 tick interval 3 degrees
    degree_extent=360-lcds[select]['st']+lcds[select]['end'] # 300
    scale_extent=max_scale-min_value # 100
    tick_extent=degree_extent/scale_extent
    # trig_start=240 # scale degrees corresponding to 0° trig
    start_scale=lcds[select]['st'] # physical start scale in degrees
    colour=lcds[select]['farbe']
    fdial=colour_choice(colour)[1]

    dfont = 'digital-7 (mono italic)'

    img = Image.new('RGBA', (w,h), '#00000000') # need transparency
    idraw = ImageDraw.Draw(img)

    for j in range(0,(val-min_value)//unitspertick+1): # pointer leds, add dial starting value
        angle=j*tick_extent*unitspertick + start_scale # measured angle
        create_pieslice(idraw,c,r-10,fill=fdial,outline=None,start=angle-0.5,
                end=angle+0.5)

    create_circle(idraw,c,r-18,fill='#00000000',outline=None)

    # display draw_text needs 3 or 4 letters or spaces
    sval=str(val)
    if max_value != 1023:
        pinput=(3-len(sval))*' '+sval
        draw_text(idraw,pinput,c,0,0,fill=fdial,font=dfont,
                size=60)

    else:
        pinput=(4-len(sval))*' '+sval
        draw_text(idraw,pinput,c,0,0,fill=fdial,font=dfont,
                size=45)

    y=(r*7//10 if max_value==255 else r*3//5)
    draw_text(idraw,unit,(c[0],c[1]+y),0,0,fill=fdial,font=dfont,size=10)

    gtype=lcds[select]['lcd']
    bimg=Image.open('../figures/'+gtype+'.png')
    cimg=Image.alpha_composite(bimg,img)

    # cimg.save('lcd_comp_point_test.png', quality=95)
    return cimg


if __name__ =='__main__':
    root=Tk()
    # select 1,2,3,4 -30:70,0:100,0:255,0:1023
    select=1
    # val value to be shown
    val=25
    image=pilpointer(select,val)
    tki=ImageTk.PhotoImage(image)
    l=Label(root,image=tki)
    l.image=tki
    l.grid()
    root.mainloop()


