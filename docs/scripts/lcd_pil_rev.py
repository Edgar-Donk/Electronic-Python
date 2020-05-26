from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, Label, PhotoImage
from DialUtils import colour_choice,draw_text,draw_tick

class lcd_pil:
    def __init__(self,select,unit='Temp C'):

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

        self.unit=unit
        h=w=lcds[select]['w']
        self.c=w//2,h//2
        self.r=w//2
        #max_value=lcds[select]['max']
        self.min_value=lcds[select]['min']
        self.max_scale=max_scale=lcds[select]['max']
        self.unitspertick=lcds[select]['upt']
        # 300° scale extent, 100 divisions therefore 1 tick interval 3 degrees
        degree_extent=360-lcds[select]['st']+lcds[select]['end'] # 300
        scale_extent=max_scale-self.min_value # 100
        self.tick_extent=degree_extent/scale_extent
        self.tick_width=lcds[select]['tw']
        # trig_start=240 # scale degrees corresponding to 0° trig
        self.start_scale=lcds[select]['st'] # physical start scale in degrees
        colour=lcds[select]['farbe']
        self.fdial=colour_choice(colour)[1]

        self.dfont = 'digital-7 (mono italic)'

        gtype=lcds[select]['lcd']
        self.bimg=Image.open('../figures/'+gtype+'.png')

    def pilpointer(self,val):
        img = self.bimg
        dfont=self.dfont
        c=self.c
        r=self.r
        fdial=self.fdial

        #img = Image.new('RGBA', (w,h), '#00000000') # need transparency
        idraw = ImageDraw.Draw(img)

        for j in range(0,(val-self.min_value)//self.unitspertick+1): # pointer leds, add dial starting value
            angle=j*self.tick_extent*self.unitspertick + self.start_scale # measured angle
            draw_tick(idraw,c,r-17,8,angle,fill=self.fdial,
                width=self.tick_width)

        #create_circle(idraw,c,r-18,fill='#00000000',outline=None)

        # display draw_text needs 3 or 4 letters or spaces
        sval=str(val)
        if self.max_scale != 1023:
            pinput=(3-len(sval))*' '+sval
            draw_text(idraw,pinput,c,0,0,fill=fdial,font=dfont,size=60)

        else:
            pinput=(4-len(sval))*' '+sval
            draw_text(idraw,pinput,c,0,0,fill=fdial,font=dfont,size=45)

        y=(r*7//10 if self.max_scale==255 else r*3//5)
        draw_text(idraw,self.unit,(c[0],c[1]+y),0,0,fill=fdial,font=dfont,size=10)

        #gtype=lcds[select]['lcd']
        #bimg=Image.open('../figures/'+gtype+'.png')
        #cimg=Image.alpha_composite(bimg,img)

        #img.save('lcd_comp_point_test.png', quality=95)
        return img


if __name__ =='__main__':
    root=Tk()
    # select 1,2,3,4 -30:70,0:100,0:255,0:1023
    select=1
    # val value to be shown
    val=35
    lp=lcd_pil(select)
    im=lp.pilpointer(val)
    tki=ImageTk.PhotoImage(im)
    l=Label(root,image=tki)
    l.image=tki
    l.grid()
    root.mainloop()


