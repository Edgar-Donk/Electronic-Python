from tkinter import Tk,Canvas, PIESLICE, Frame
from math import pi,sin,cos
from DialUtils import colour_choice,tk_arc,tk_tick,tk_text,tk_delta

'''
converting to class, based loosely on Ardiotech
'''
class LCD(Canvas):
    def __init__(self,parent,select,enlargement=1,colour='red',unit='Temp C'):
        super().__init__(parent,bd=0,highlightthickness=0)
        self.select=select
        self.enlargement=enlargement
        self.colour=colour
        self.unit=unit

        # lcd gauge type; min,max scale extent; st,end start end degrees;
        # upt units per tick; w width pixels; tw tick width
        self.lcds=lcds={
            1:{'lcd':'lcd70','min':-30,'max':70,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'temperature'},
            2:{'lcd':'lcd100','min':0,'max':100,'st':120,'end':60,'upt':1,
                    'w':201,'tw':3,'mess':'general\npurpose'},
            3:{'lcd':'lcd255','min':0,'max':270,'st':135,'end':45,'upt':2,
                    'w':201,'tw':2,'mess':'analogue\n output'},
            4:{'lcd':'lcd1023','min':0,'max':1030,'st':117,'end':63,'upt':10,
                    'w':201,'tw':4,'mess':'analogue\n input'}
                    }

        #select=3
        self.e=e=enlargement
        we=lcds[select]['w']*e
        he=lcds[select]['w']*e
        self['width']=we
        self['height']=he
        self.ce=ce=we//2,he//2
        self.re=re=we//2
        lwe=re/25*e

        self.max_value=max_value=int(lcds[select]['lcd'].strip('lcd')) #70
        self.min_value=min_value=lcds[select]['min'] #-30
        val=(max_value+min_value)//2
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
        # end_scale=60 # physical end scale in degrees

        bdial,fdial,gdial,sdial=colour_choice(colour)
        self.fdial=fdial
        self.dfont=dfont = 'Digital-7 Mono'
        background=bdial # '#090B0E'

        # create bezel, add 20 degrees to scale extent
        phi=-(start_scale-10)
        ext=-(degree_extent+20)
        tk_arc(self,ce,re,style=PIESLICE,start=phi,extent=ext,
            outline='',fill=sdial)
        tk_arc(self,ce,re-lwe,style=PIESLICE,start=phi,extent=ext,
            outline='',fill=background)
        theta=(-phi-90)
        rangle=theta*pi/180

        # clean up central area
        st=ce[0]-(re+lwe/2)*sin(rangle),ce[1]+(re-lwe/2)*cos(rangle)
        end=ce[0]+(re+lwe/2)*sin(rangle),ce[1]+(re-lwe/2)*cos(rangle)
        self.create_polygon(ce,st,end,fill=background)

        # join the 2 ends
        self.create_line([st,end],fill=sdial,width=lwe)

        # create outer 2 rows ticks
        for j in range(0,scale_extent//unitspertick+1): # degree_extent//tick_extent
            angle=j*tick_extent*unitspertick +start_scale # measured angle
            tk_tick(self,ce,re-8*e,2*e,angle,fill=fdial,width=tick_width*e)
            tk_tick(self,ce,re-18*e,8*e,angle,fill=gdial,width=tick_width*e)

        # inner ticks need to be made before any deltas
        for j in range(0,degree_extent+1): # range 300 scale_extent degree_extent//tick_extent
            angle=j + start_scale
            tk_tick(self,ce,re-20*e,2*e,angle,fill=sdial,width=1*e)

        if max_value in (70,100):
            x=29
        elif max_value==255:
            x=31
        else:
            x=34

        for j in range(0,scale_extent//unitspertick+1):
            angle=j*tick_extent*unitspertick + start_scale
            if j % 10==0:
                tangle=str((j+min_value)*unitspertick)
                tk_delta(self,angle,ce,re-19*e,e,fill=fdial)
                tk_text(self,tangle,ce,re-x*e,angle,fill=fdial,font=dfont,size=10)

        if max_value != 1023:
            tk_text(self,'888',ce,0,0,fill=gdial,font=dfont,size=60)
        else:
            tk_text(self,'8888',ce,0,0,fill=gdial,font=dfont,size=45)

        y=(re*4//10 if max_value in (255,1023) else re//2)
        tk_text(self,mess,(ce[0],ce[1]-y),0,0,
            fill=fdial,font=dfont,size=10)

        y=(re*7//10 if max_value==255 else re*4//5)
        tk_text(self,unit,(ce[0],ce[1]+y),0,0,
            fill=fdial,font=dfont,size=10)

        self.lcd_pointer(val,self.min_value)

    def lcd_pointer(self,val,oldval):
        re=self.re
        ce=self.ce
        dfont=self.dfont
        e=self.e
        fdial=self.fdial
        dial=self.dial
        min_value=self.min_value
        unitspertick=self.unitspertick
        start_scale=self.start_scale

        if val==oldval:
            pass
        elif val<oldval:
            for x in range((val-min_value)//unitspertick+1,
                (oldval-min_value)//unitspertick+1):
                angle=x*self.tick_extent*unitspertick + start_scale
                self.delete(dial+'_'+str(int(angle-start_scale)))

        else:
            for j in range(((oldval-min_value)//unitspertick),
                        ((val-min_value)//unitspertick+1)):
                angle=j*self.tick_extent*unitspertick + start_scale
                tag=(dial+'_'+str(int(angle-start_scale)))
                tk_tick(self,ce,re-18*e,8*e,angle,fill=fdial,
                    width=self.tick_width*self.e,tags=tag)

        # display draw_text needs 3 or 4 letters or spaces
        sval=str(val)
        self.delete(dial)
        if self.max_value != 1023:
            pinput=(3-len(sval))*' '+sval
            tk_text(self,pinput,ce,0,0,fill=fdial,font=dfont,
                size=60,tags=dial)

        else:
            pinput=(4-len(sval))*' '+sval
            tk_text(self,pinput,ce,0,0,fill=fdial,font=dfont,
                size=45,tags=dial)

if __name__ == '__main__':
    root = Tk()
    winsys = root.tk.call("tk", "windowingsystem")
    BASELINE = 1.33398982438864281 if winsys != 'aqua' else 1.000492368291482
    scaling = root.tk.call("tk", "scaling")
    enlargement = int(scaling / BASELINE + 0.5)
    fr=Frame(root)
    fr.grid(row=0,column=0,sticky='nsew')
    l1=LCD(fr,select=4,enlargement=enlargement,colour='red',unit='Luminosity')
    l1.grid(row=0,column=0,sticky='nsew')
    l2=LCD(fr,select=4,enlargement=enlargement,colour='blue',unit='Luminosity')
    l2.grid(row=0,column=1,sticky='nsew')
    oldval=1023//2
    val=100
    l1.lcd_pointer(val,oldval)
    l2.lcd_pointer(val,oldval)

    root.mainloop()