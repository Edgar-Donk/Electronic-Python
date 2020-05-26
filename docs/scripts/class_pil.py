from PIL import Image, ImageDraw, ImageFont
from math import pi, sin, cos
from DialUtils import colour_choice,create_pieslice,create_chord,create_circle,\
        draw_text,draw_delta,draw_tick

class LCDpil:
    def __init__(self,select,enlargement=9): # ,unit='Temp C'
        self.select=select
        self.enlargement=enlargement
        #self.unit=unit

        # lcd gauge type; min,max scale extent; st,end start end degrees;
        # upt units per tick; w width pixels; tw tick width; farbe colour
        # mess gauge type
        self.lcds=lcds={
            1:{'lcd':'lcd70','min':-30,'max':70,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'temperature','farbe': 'blue'},
            2:{'lcd':'lcd100','min':0,'max':100,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'general\npurpose','farbe': 'purple'},
            3:{'lcd':'lcd255','min':0,'max':270,'st':135,'end':45,'upt':2,
                    'w':201,'tw':2,'mess':'analogue\n output','farbe': 'red'},
            4:{'lcd':'lcd1023','min':0,'max':1030,'st':117,'end':63,'upt':10,
                    'w':201,'tw':4,'mess':'analogue\n input','farbe': 'green'}
                    }

        self.e=e=enlargement
        we=lcds[select]['w']*e
        he=lcds[select]['w']*e
        self.ce=ce=we//2,he//2
        self.re=re=we//2
        lwe=re/25*e
        background='#090B0E'
        self.max_value=max_value=int(lcds[select]['lcd'].strip('lcd')) #70
        self.min_value=min_value=lcds[select]['min'] #-30
        val=(max_value+min_value)//2
        #print(val)
        max_scale=lcds[select]['max']
        self.unitspertick=unitspertick=lcds[select]['upt']
        self.dial=lcds[select]['lcd']
        mess=lcds[select]['mess']
        # angular calculations
        # 300° scale extent, 100 divisions therefore 1 tick interval 3 degrees
        degree_extent=360-lcds[select]['st']+lcds[select]['end'] # 300
        scale_extent=max_scale-min_value # 100
        self.tick_extent=tick_extent=degree_extent/scale_extent
        self.tick_width=tick_width=lcds[select]['tw']
        # trig_start=240 # scale degrees corresponding to 0° trig
        self.start_scale=start_scale=lcds[select]['st'] # physical start scale in degrees
        self.end_scale=end_scale=lcds[select]['end'] # physical end scale in degrees
        colour=lcds[select]['farbe']
        bdial,fdial,gdial,sdial=colour_choice(colour)
        self.fdial=fdial
        self.dfont=dfont = 'digital-7 (mono italic)'

        img = Image.new('RGBA', (we,he), '#00000000') # need transparency
        idraw = ImageDraw.Draw(img)

        # create bezel, add 20 degrees to scale extent
        create_pieslice(idraw,ce,re,fill=sdial,outline=None,start=start_scale-10,
                    end=end_scale+10)
        create_pieslice(idraw,ce,re-4*e,fill=bdial,outline=None,
                start=start_scale-10,end=end_scale+10)
        create_chord(idraw,ce,re,fill=sdial,outline=None,start=start_scale-10,
                    end=end_scale+10)
        create_chord(idraw,ce,re-4*e,fill=bdial,outline=None,start=start_scale-10,
                    end=end_scale+10)

        for j in range(0,scale_extent//unitspertick+1):
            angle=j*tick_extent*unitspertick + start_scale # measured angle
            draw_tick(idraw,ce,re-8*e,2*e,angle,fill=fdial,width=2*e)
            create_pieslice(idraw,ce,re-10*e,fill=gdial,outline=None,
                start=angle-0.5,end=angle+0.5)

        create_chord(idraw,ce,re-18*e,fill=bdial,outline=None,start=start_scale,
                    end=end_scale)

        # inner ticks need to be before any deltas
        if max_value != 1023:
            for j in range(0,scale_extent//unitspertick+1):
                angle=j*tick_extent*unitspertick + start_scale
                draw_tick(idraw,ce,re-20*e,2*e,angle,fill=sdial,width=1*e)
        else:
            for j in range(0,scale_extent//unitspertick+1):
                angle=j*tick_extent*unitspertick + start_scale
                draw_tick(idraw,ce,re-20*e,2*e,angle,fill=sdial,width=1*e)

        # deltas and scale numbers
        for j in range(0,scale_extent//unitspertick+1):
            angle=j*tick_extent*unitspertick + start_scale
            if j % 10==0:
                tangle=str(int(j+min_value)*unitspertick)
                draw_delta(idraw,angle,ce,re-19*e,e,fill=fdial)
                draw_text(idraw,tangle,ce,re-29*e,angle,fill=fdial,
                    font=dfont,size=10*e)

        # ghost value
        if max_value != 1023:
            draw_text(idraw,'888',ce,0,0,fill=gdial,font=dfont,size=60*e)
        else:
            draw_text(idraw,'8888',ce,0,0,fill=gdial,font=dfont,size=45*e)

        # gauge type
        y=(re*4//10 if max_value in (70,255,1023) else re//2)
        ttffont = ImageFont.truetype(dfont+'.ttf', size=10*e)
        (width, height), (offset_x, offset_y) = ttffont.font.getsize(mess)
        dx=(-width//2 if max_value==70 else -width//4)
        idraw.text((ce[0]+dx-offset_x,ce[1]-y-height//2-offset_y),
            mess,fill=fdial,font=ttffont)

        w=lcds[select]['w']
        gtype=lcds[select]['lcd']
        # better looking than just drawing original size
        imgr=img.resize((w,w),resample=Image.LANCZOS)
        imgr.save('../figures/'+gtype+'.png')

if __name__ =='__main__':
    LCDpil(4)


