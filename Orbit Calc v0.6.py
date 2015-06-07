

from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font
import tkinter.tix
import math
from math import log10, floor

 #MAKE THIS NOT EXIST


#FIXED

#FIXED BAD SCREEN ERROR. Was setting A after A was used.
#ADD SET PERIAPSIS/APOAPSIS, MAKING IT SOLVE FOR HOW MUCH dV CHANGE IS NEEDED_DONE!
#MAKE PLANET VALUE SELECTION ANIMATED_FIXED!
#HAVE TO DOUBLE CLICK PLANET INPUT_ FIXED!
#ALTITUDE IS A BIT BUGGER AND WONT LET YOU MAKE IT BIGGER, ESPECIALLY AT LOW SPEEDS _FIXED!
#MAKE INPUT NOT ALLOW 0 OR NEGATIVES (NEGATIVES GO TO POSITIVE) _ DONE!
#ORBIT GOES INTO COMPLEX NUMBERS FOR SOME REASON, SOMETHING TO DO WITH TOO BIG OF A JUMP IN xCHANGE _ FIXED!
#NOT GETTING RIGHT ORBITAL VELOCITY WITH SMALLER PLANETS FIXED
#V Was overshooting, check others dont do that same FIXED
#Divison by zero with too small of a change FIXED
#Make buttons clickable only once DONE
#Orbit setting needs boundries like vel setting DONE
#SOMETIMES A SLIGHT OVERSHOOT IN VALUES. DIVISION BY ZERO SOMETIMES FIXED
#MAKE USER SHIP SPEED A FUNCTION OF ORBITAL PERIOD DONE
#MAKE SHIP SPEED AND SLOW DOWN DEPENDING ON ORBIT POSITION DONE
#ADD CRAFT DATA IN RENDERING DONE
#MAKE PLANET DATA MOVE DONE
#ADD STATIC CRAFT SITTING AND DOING NOTHING DONE
#Visual errors withmini side on view with inclines FIXED
#turns out oval headwau doubles as a zoom function. Use that DONE
# OPTIONAL - ADD CENTRIPETAL FORCE WITH SHIP DRAW, ACCEL x MASS DONE
#make zooming work properly DONE
#Fc needs prety up and photoshopping DONE
#disable zoom while animation DONE
#Add all picture art in and pretty that shizz up DONE
#remake incline view with pics DONE
#ship goes in wrong direction in 90-180 and 180-270 i think FIXED
#Ship doesnt like 180-270 for some reasonssnsnnsn FIXED
#Obirtal data not deleting for some reason FIXED
#PRETTY IT UP A BIT done?
#make zooom go from 0 -100 DONE
#mission control needs touching up DONE
#ADD INFO ON HOW MUCH A PARTICULAR MANEUVOUR COST IN TERMS OF dV TO MAINBOARD DONE
#SHADOW TOO FAR FOWARD ON NEWTON BAR FIXED
#ADD ECCENTRICTY ORBITAL PERIOD AND DONE
#Make switch to apo/peri a thing DONE
#Make FAQ and such on bottom boad DONE
#move orbital Data into new window DONE
#MAKE croot open with bottom board button DONE
#iknclination goes from 0 - 180, not to 360. fix that DONE
#make button hide behind something so it appears when error DONE
#Make dv change update faster and show calculating DONE
#Layering off orbits FIXED
#Finish calculator thing DONE


#SCRAPPED

#SOI RADIUS



#WORK BOARD

#word ecentricity better


#SOMEHOPW MAKE ORBIT CHANGES JUMP GAP FROM 180 to -180

#DONT SHRINK


#Make ship crash into planet
#Balance ship speed

#Make inclination window work different, make orbit smaller when planet sets certain size



#BUG BOARD




groot = tkinter.tix.Tk()
groot.wm_title("Menu")


groot.configure(background = 'silver')
orbitcalcopen = 0




#neptuune/jool/duna have weird issue.





class App():
    def __init__(self, groot):

        

        

        def orbitcalc():
            self.root = Toplevel()

            orbitopen.grid_remove()
            tutopen.grid_remove()

            
            
        
            
            
                
            
            def loopchangecore():


                userchangeclean()

                self.PRshorta = self.PRdentry.get()
                self.PRshortb = self.PReentry.get()
                self.PRshort = abs(int(self.PRshorta * 10** self.PRshortb))
                                
                self.PRuserchange= (self.PRshort)/2 - self.planetradius
                self.oldPRuserchange = self.PRuserchange



                self.Pchange =  abs(self.PRuserchange/self.changeamount)

                


           
                self.loopvaluechange = self.PRuserchange/abs(self.Pchange)
                    
                
                self.totalPRchange = self.loopvaluechange * abs(self.Pchange)

                if self.PRuserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0
                


            def loopchangemass():




                userchangeclean()
                self.Mshorta = self.Mdentry.get()
                self.Mshortb = self.Meentry.get()
                self.Mshort =  abs(self.Mshorta * 10** self.Mshortb)

                self.Muserchange= self.Mshort - self.M
                self.oldMuserchange = self.Muserchange



                self.Mchange = abs(self.Muserchange/self.changeamount)

                


       
                self.loopvaluechange = self.Muserchange/abs(self.Mchange)
                    
                self.totalMchange = self.loopvaluechange * abs(self.Mchange)

                if self.Muserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0





            def loopchangeath():




                userchangeclean()
                self.Atshorta = self.Atdentry.get()
                self.Atshortb = self.Ateentry.get()
                self.Atshort =  abs(self.Atshorta * 10** self.Atshortb)
                
                self.Atuserchange= self.Atshort - self.atmospheresize
                self.oldAtuserchange = self.Atuserchange


     
                
                self.Atchange =  abs(self.Atuserchange/self.changeamount)

                    
                self.loopvaluechange = self.Atuserchange/abs(self.Atchange)
                   
                
                self.totalAtchange = self.loopvaluechange * abs(self.Atchange)
                if self.Atuserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0
                

                
            def loopchangealt():





                userchangeclean()
                self.Ashorta = self.Adentry.get()
                self.Ashortb = self.Aeentry.get()
                self.Ashort =  abs(self.Ashorta * 10** self.Ashortb)
                

                self.Auserchange= self.Ashort - self.UA
                self.oldAuserchange = self.Auserchange



                self.Achange = abs(self.Auserchange/self.changeamount)

                self.loopvaluechange = self.Auserchange/abs(self.Achange)

                
                self.totalAchange = self.loopvaluechange * abs(self.Achange)

                if self.Auserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0


            def loopchangeincline():



                userchangeclean()

                self.Ishort = -1* self.InclineSlide.get()
                

                self.Iuserchange= self.Ishort - self.incline
                self.oldIuserchange = self.Iuserchange



                self.Ichange = abs(self.Iuserchange/self.changeamount)

                self.loopvaluechange = self.Iuserchange/abs(self.Ichange)

                
                self.totalIchange = self.loopvaluechange * abs(self.Ichange)

                if self.Iuserchange != 0:
                    self.dvchange = ((2*self.V**2 )*(1- math.cos (self.Iuserchange*( math.pi/180))))**0.5
                    self.tdvchange = self.dvchange + self.tdvchange

                print (self.dvchange, "idv")
                    
                

                
                #self.incline = -1 * self.InclineSlide.get()
                #self.Vchange=0
                #self.Mchange=0
                #self.Pchange=0
                #self.Achange=0  #MAKE ALL THIS INSIDE A DEFINE
                #self.Atchange=0
                #self.update_frame()
            def loopchangeorbit():


                #add function for too much orbit

              #  print (self.Vuserchange)
               # print (self.Auserchange)
                userchangeclean()

                self.Oshorta = self.Odentry.get()
                self.Oshortb = self.Oeentry.get()
                self.Oshort =  abs(self.Oshorta * 10** self.Oshortb)

                self.R = self.planetradius + self.UA
                self.L = (self.R + self.planetradius + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                self.Vshort = (self.U * (2/self.R - 1/self.L))**0.5
                print (self.eV, "EV")
                print (self.Vshort, "VSHORT")
                if self.Vshort >= self.eV:
                    self.Vshort = math.trunc(self.eV)
                    self.notification = "Escape velocity exceeded, setting velocity to highest possible orbital velocity."
                    self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                    #works

                else:
                    self.Vshort = self.Vshort
                print (self.L)
                print (self.R)
                print (self.Vshort)

                
                self.Vuserchange= self.Vshort - self.V
                #if self.Ventry.get() > self.eV:
                #    self.Vuserchange =math.trunc(self.eV - self.V) #for safety
                #    self.notification = "Escape velocity exceeded, setting velocity to highest possible orbital velocity."
                  #  self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification) #Yes I know it doubles up
               # #else:
                   # if abs(self.Ventry.get()) == 0:
                   #     self.Vuserchange = 1 - self.V
                   #     self.notification = "Cannot have a velocity of 0 - bug of code"
                  # #     self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification) #Yes I know it doubles up
                   # else:
                   #     self.Vuserchange =abs(self.Ventry.get()) - self.V
                        
                        
               # print (self.Vuserchange)
                self.oldVuserchange = self.Vuserchange



                #if self.Vuserchange

                #self.Vchange = abs( math.ceil(self.Vuserchange/self.changeamount))
                self.Vchange = abs(self.Vuserchange/self.changeamount)

                self.loopvaluechange = self.Vuserchange/abs(self.Vchange)

                
                self.totalVchange = self.loopvaluechange * abs(self.Vchange)
               # print (self.totalVchange)
               # print(self.Vround)
                self.dvchange = self.Vuserchange
                self.tdvchange = self.dvchange + self.tdvchange
                print (self.Vuserchange, "=DV")

                


            def loopchangeposition():

                userchangeclean()
                self.Auserchange = self.B - self.A
                self.oldAuserchange = self.Auserchange
                self.R = self.B
                #self.L = (self.R + self.planetradius + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                self.Vshort = (self.U * (2/self.R - 1/self.L))**0.5
                # (self.Vshort)
                self.Vuserchange= self.Vshort - self.V
                self.oldVuserchange = self.Vuserchange

                self.Iuserchange= -2 * self.incline
                self.oldIuserchange = self.Iuserchange

                self.Ichange = (self.Iuserchange/self.changeamount)

                self.totalIchange = self.loopvaluechange * abs(self.Ichange)


                
                self.Vchange = (self.Vuserchange/self.changeamount)

                #print (self.Auserchange, "AU")

               
                self.Achange = (self.Auserchange/self.changeamount)

                #print (self.loopvalue)

               

                

                

                self.loopvalue = self.changeamount#  self.Auserchange/abs(self.Achange)

                #self.Achange = abs(self.Auserchange/self.changeamount)
                self.totalVchange = self.loopvalue * abs(self.Vchange)
                   
                
                self.totalAchange = self.loopvalue* abs(self.Achange)
                
                update_frame()
            
            def loopchangevel():




              #  print (self.Vuserchange)
               # print (self.Auserchange)
                userchangeclean()
                if self.Ventry.get() > self.eV:
                    self.Vuserchange =math.trunc(self.eV - self.V) #for safety
                    self.notification = "Escape velocity exceeded, setting velocity to highest possible orbital velocity."
                    self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                else:
                    if abs(self.Ventry.get()) == 0:
                        self.Vuserchange = 1 - self.V
                        self.notification = "Cannot have a velocity of 0 - bug of code"
                        self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                    else:
                        self.Vuserchange =abs(self.Ventry.get()) - self.V
                        
                        
               # print (self.Vuserchange)
                self.oldVuserchange = self.Vuserchange


                print (self.Vuserchange, "VU")
                print (self.V, "V")

                self.Vchange =  abs(self.Vuserchange/self.changeamount)
                print (self.Vchange, "VC")
                
                self.loopvaluechange = self.Vuserchange/abs(self.Vchange)

                
                self.totalVchange = self.loopvaluechange * abs(self.Vchange)
                print (self.V, "V")
                self.dvchange = self.Vuserchange
                self.tdvchange = self.dvchange + self.tdvchange
                print (self.Vuserchange, "=DV")

                
            def shipmassset():
                self.w.delete(self.smallban)
                self.w.delete(self.smalltext)
                self.shipmass =  abs(self.shipmassentry.get())

                self.Fc = (self.shipmass * self.shipg) *1000 # in N
                print (self.shipmass)
                print (self.g)
                print(self.shipg)
                print (self.Fc)

                if self.Fc != 0:
                    self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                    self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)
            def reset():
                self.UA= 300000
                self.planetradius = 6370000
                self.M = 5.972*10**24
                self.V = 800 #Must be above 0. Bad screen error at escape velocity.
                self.A= self.UA + self.planetradius #MAKE THIS VALUE CHANGE DEPEND ON STARTING MODEL PLANET
                self.incline = 0

                if self.prootopen == 1:

                    self.sua.grid_remove()
                    self.sa.grid_remove()
                    self.sm.grid_remove()
                    self.sv.grid_remove()
                    self.su.grid_remove()
                    self.sb.grid_remove()
                    self.sl.grid_remove()
                    self.se.grid_remove()
                    self.sh.grid_remove()
                    self.sp.grid_remove()
                    self.sd.grid_remove()
                    self.suat.grid_remove()
                    self.sat.grid_remove()
                    self.smt.grid_remove()
                    self.svt.grid_remove()
                    self.sut.grid_remove()
                    self.sbt.grid_remove()
                    self.slt.grid_remove()
                    self.set.grid_remove()
                    self.sht.grid_remove()
                    self.spt.grid_remove()
                    self.sdt.grid_remove()

                update_frame()

            
                
                

                
            def looprun():
                global loopvalue
                global loopcurrent

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()

                self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
                self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

                self.dvchangelab.grid(row = 9, column = 1, columnspan = 1, sticky = W)
                self.tdvchangelab.grid(row = 9, column = 2, columnspan = 2, sticky = W)

               

                self.resetbutton.configure(background = 'crimson',foreground = 'snow',borderwidth=2,state = NORMAL)


                
                self.loopvalue = self.loopvaluechange
                self.loopcurrent = 0
                self.intVchange = 0
                #self.Vchange = abs(self.Vchange)   #move these back
                self.enterbutton.configure (state = DISABLED)
                self.entercorebutton.configure (state = DISABLED)
                self.entermassbutton.configure (state = DISABLED)
                self.enteraltbutton.configure (state = DISABLED)
                self.enterorbbutton.configure (state = DISABLED)
                self.enterathbutton.configure (state = DISABLED)
                self.enterincbutton.configure (state =DISABLED)
                self.buttonrun.configure (state = DISABLED)
                self.shiprunbutton.configure (state = DISABLED)
                self.resetbutton.configure (state = NORMAL)
                self.bodybutton.configure (state = DISABLED)
                self.ZoomSlide.configure (state = DISABLED)
                self.InclineSlide.configure (state = DISABLED)
                self.entershipmass.configure (state = DISABLED)
                self.resetdv.configure(state = DISABLED)

                

                self.waitnes = Label(groot, text =("Calculating..."), background = 'silver')
                self.waitnes.grid(row = 9, column = 1, columnspan = 3)

                if self.prootopen == 1:

                    self.waitmes = Label(self.proot, text =("Calculating..."), background = 'silver')
                    self.waitmes.grid(row = 6, column = 1, columnspan = 3)

                    

                    self.sua.grid_remove()
                    self.sa.grid_remove()
                    self.sm.grid_remove()
                    self.sv.grid_remove()
                    self.su.grid_remove()
                    self.sb.grid_remove()
                    self.sl.grid_remove()
                    self.se.grid_remove()
                    self.sh.grid_remove()
                    self.sp.grid_remove()
                    self.sd.grid_remove()
                    self.suat.grid_remove()
                    self.sat.grid_remove()
                    self.smt.grid_remove()
                    self.svt.grid_remove()
                    self.sut.grid_remove()
                    self.sbt.grid_remove()
                    self.slt.grid_remove()
                    self.set.grid_remove()
                    self.sht.grid_remove()
                    self.spt.grid_remove()
                    self.sdt.grid_remove()

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()

                update_frame()
                

            
                
            def planetbox():
                planetdetails()
                #orbitmath()
                #print (self.planetcombobox.current())
                #SUN,Merc, VEnus, EARTH, MON, MAARS,JUPITER,SATURN, URANUS, NEPTUNE, .... , KERBOL, Moho, Eve, gilly, Kerbin, mun,minmud, duna, ike, dres, jool, laythe, vall, tylo, bop, pol , eeloo
    #GOES UP BOT NOT DOWN


        

                
                   
                #print ((self.SIGround(self.fM, 4)))
               # print ((elf.SIGround(self.fplanetradius, 3)))
               # print ("START")

                self.Muserchange = (self.fM) - self.M
                self.PRuserchange = self.fplanetradius - self.planetradius
                self.Vuserchange = ((self.G * self.fM )/(self.UA + self.fplanetradius))**0.5 - self.V
                #print (((self.G * self.fM )/(self.UA + self.fplanetradius))**0.5)

               # print (self.Muserchange)
               # print (self.PRuserchange)
                #print (self.Vuserchange)

                self.Mchange =  (self.Muserchange/self.changeamount)
                self.Pchange =  (self.PRuserchange/self.changeamount)
                #self.Pchange = 100
                self.Vchange =  (self.Vuserchange/self.changeamount)

                #print (self.Mchange, "M")
                #print (self.Pchange, "P")
                #print (self.Vchange, "V")

                self.oldMuserchange = self.Muserchange
                self.oldPRuserchange = self.PRuserchange
                self.oldVuserchange = self.Vuserchange
            
                    
                #self.Vchange = 0
                #self.Pchange = 0
                #self.Mchange = 0
                self.Achange = 0
                self.Atchange = 0
                
                self.loopvaluechange = self.changeamount
                
                self.totalVchange = self.loopvaluechange * self.Vchange
                self.totalMchange = self.loopvaluechange * self.Mchange
                self.totalPRchange = self.loopvaluechange * self.Pchange

               # print (self.totalVchange)

                
                
                looprun()

         

            
            global Ventry

            
            
            
            

            
            

            self.root.wm_title("Orbital Calculator v 0.6")
            groot.wm_title("Mission Control")
            
            
            self.root.configure(background='silver') # windoow background
            groot.configure(background='silver')
            
            self.screenx = self.root.winfo_screenwidth()
            self.screeny = self.root.winfo_screenheight()
            self.canvasshrink = 1.3
            #self.canvasx = 900
            #self.canvasy = 700

            self.canvasx = self.screenx/self.canvasshrink
            self.canvasy = self.screeny/self.canvasshrink
            self.ovalheadway = 200 #higher is more headway MUST NOT BE MORE THAN OR EQUAL TO CANVASY/2\

            self.crootopen = 0
            self.prootopen = 0
            self.frootopen = 0
            self.orootopen = 0
            

            def frootwindowclose():
                self.froot.destroy()
                self.frootopen = 0

            def orootwindowclose():
                self.oroot.destroy()
                self.orootopen = 0

            def grootwindowclose():
                global orbitcalcopen 
                if self.orootopen == 1:
                    self.oroot.destroy()
                elif self.frootopen == 1:
                    self.froot.destroy()
                elif self.prootopen == 1:
                    self.proot.destroy()
                elif self.crootopen == 1:
                    self.croot.destroy()
                
                self.root.destroy()
              



                self.planetcombobox.grid_remove()
             
                self.enterbutton.grid_remove()
                self.entercorebutton .grid_remove()
                self.entermassbutton.grid_remove()
                self.enteraltbutton.grid_remove()
                self.enterorbbutton.grid_remove()
                self.enterathbutton.grid_remove()
                self.enterincbutton.grid_remove()
                self.buttonrun.grid_remove()
                
                self.shiprunbutton.grid_remove()
                self.resetbutton.grid_remove()
                self.bodybutton.grid_remove()
                #self.zoominbutton = Button(self.groot text = "Zoom In", command=zoomin)
                #self.zoomoutbutton = Button(self.groot, text = "Zoom Out", command=zoomout)
                self.entershipmass.grid_remove()
                self.resetdv.grid_remove()
                self.changeposition.grid_remove()
                self.crootwindowopen.grid_remove()
                self.prootwindowopen.grid_remove()
                self.frootwindowopen.grid_remove()
                self.orootwindowopen.grid_remove()
                
                self.VelBox.grid_remove()
                self.PRBox.grid_remove()
                self.MBox.grid_remove()
                self.ABox.grid_remove()
                self.OBox.grid_remove()
                self.AtBox.grid_remove()
                self.PReBox.grid_remove()
                self.MeBox.grid_remove()
                self.AeBox.grid_remove()
                self.OeBox.grid_remove()
                self.AteBox.grid_remove()
                
                self.shipmassBox.grid_remove()

                self.PrLab.grid_remove()
                self.MLab.grid_remove()
                self.ALab.grid_remove()
                self.OLab.grid_remove()
                self.AtLab.grid_remove()

                self.ZoomSlide.grid_remove()

                self.InclineSlide.grid_remove()

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()
                self.zoomlab.grid_remove()

                self.fplanetradiuslab.grid_remove()
                self.fMlab.grid_remove()

                self.LINELAB1.grid_remove()
                self.LINELAB2.grid_remove()

                self.calccombust.grid_remove()

                orbitcalcopen = 0
                print ("ETS")

                


                
                orbitopen = Button(groot, text="Open Calculator", command=orbitcalccommand)
                orbitopen.grid(row = 1, column = 1)
                tutopen = Button(groot, text="Open Tutorial", command=orbitcalccommand)
                tutopen.grid(row = 2, column = 1)
                groot.wm_title("Menu")
            

            def orootwindow():
                if self.orootopen == 0:
                    self.oroot = Toplevel()
                    self.orootopen = 1 
                    self.oroot.wm_title("Glossary")
                    self.oroot.configure(background='silver')

                    Label(self.oroot,text = "|",background='silver').grid(row = 1 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 2 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 3 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 4 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 5 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 6 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 7 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 8 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 9 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 10 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 11 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 12 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 13 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 14 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 15 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 16 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 17 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 18 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 19 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 20 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 21 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 22 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 23 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 24 , column = 2)
                    Label(self.oroot,text = "|",background='silver').grid(row = 25 , column = 2)

                    Label(self.oroot, text = "Altitude",font = self.ArialBg,background='silver').grid(row = 1 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Distance from the current position to Bodies centre of mass.",background='silver').grid(row = 1 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Apoapsis",font = self.ArialBg,background='silver').grid(row = 2 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point of orbit that is furthest from body. Lowest possible orbital speed is here.",background='silver').grid(row = 2 , column = 3, columnspan = 1, sticky = W)
                    

                    Label(self.oroot, text = "Body",font = self.ArialBg,background='silver').grid(row = 3 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The planet/sun/moon a satellite is orbiting.",background='silver').grid(row = 3 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Centre of Mass",font = self.ArialBg,background='silver').grid(row = 4 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point where all mass is concentrated. Assumed Centre of Mass in centre of body for calculations.",background='silver').grid(row = 4 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Eccentricity",font = self.ArialBg,background='silver').grid(row = 5 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "A measure of how much a conic section deviates from being circular.",background='silver').grid(row = 5 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Delta V",font = self.ArialBg,background='silver').grid(row = 6 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Change in velocity.",background='silver').grid(row = 6 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Equatorial Plane",font = self.ArialBg,background='silver').grid(row = 7 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Plane parrellel with equaotiral line.",background='silver').grid(row = 7 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Burn Time",font = self.ArialBg,background='silver').grid(row = 8 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How long an engine can run for before burnout.",background='silver').grid(row = 8 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Burnout",font = self.ArialBg,background='silver').grid(row = 9 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Shutdown of engine due to lack of fuel.",background='silver').grid(row = 9 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Inclination",font = self.ArialBg,background='silver').grid(row = 10 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Angle of orbit measured from equatorial plane.",background='silver').grid(row = 10 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Orbit",font = self.ArialBg,background='silver').grid(row = 11 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Path of satellite around a body.",background='silver').grid(row = 11 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Periapsis",font = self.ArialBg,background='silver').grid(row = 12 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point of orbit that is closest to body. Highest possible orbital speed is here.",background='silver').grid(row = 12 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Period",font = self.ArialBg,background='silver').grid(row = 13 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Time required for one circuit of orbit.",background='silver').grid(row = 13 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Prograde",font = self.ArialBg,background='silver').grid(row = 14 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The direction in the orbit is travelling.",background='silver').grid(row = 14 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Retrograde",font = self.ArialBg,background='silver').grid(row = 15 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The direction opposite from the direction the orbit is travelling.",background='silver').grid(row = 15 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Semi-Major Axis",font = self.ArialBg,background='silver').grid(row = 16 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Half of the longest part of an orbit.",background='silver').grid(row = 16 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Semi-Minor Axis",font = self.ArialBg,background='silver').grid(row = 17 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Half of the shortest part of an orbit.",background='silver').grid(row = 17 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Focal Length",font = self.ArialBg,background='silver').grid(row = 18 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Distance from the centre of orbit to where the orbiting body is.",background='silver').grid(row = 18 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Parameter",font = self.ArialBg,background='silver').grid(row = 19 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Expressed as μ and and shown in unit m^3/s. Product of Gravational Constant and mass of body.",background='silver').grid(row = 19 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Constant",font = self.ArialBg,background='silver').grid(row = 20 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Use to calculate the attractive forces of two bodies as proportionate to their own mass. Approximately 6.674x 10 ^ -11 Nm^2/kg^2.",background='silver').grid(row = 20 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Velocity",font = self.ArialBg,background='silver').grid(row = 21 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How fast an object is travelling in a praticular direction.",background='silver').grid(row = 21 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Radar Altitude",font = self.ArialBg,background='silver').grid(row = 22 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How high something is from the surface beneath it. Eg. Atltiude of spacecraft from surface of body.",background='silver').grid(row = 22 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Mass",font = self.ArialBg,background='silver').grid(row = 23 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much matter is in an object. The more matter the 'heavier' when combined with gravational acceleration.",background='silver').grid(row = 23 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Acceleration",font = self.ArialBg,background='silver').grid(row = 24 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Measurement of how much acceleration an object will inherit when no other forces are active.",background='silver').grid(row = 24 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Centripetal Force",font = self.ArialBg,background='silver').grid(row = 25 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much force is acting on an object to keep it in the circle/ellipse that it is travelling in. Expressed as Fc.",background='silver').grid(row = 25 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Specific Impulse",font = self.ArialBg,background='silver').grid(row = 26 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Expressed as Isp, and measured in seconds. It is a measurement of how effeciency of converting fuel into thrust.",background='silver').grid(row = 26 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Wet Mass",font = self.ArialBg,background='silver').grid(row = 27 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Mass of a spacecraft when full of fuel.",background='silver').grid(row = 27 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Dry Mass",font = self.ArialBg,background='silver').grid(row = 28 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Mass of a spacecraft when fuel is empty.",background='silver').grid(row = 28 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Thrust",font = self.ArialBg,background='silver').grid(row = 29 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much force an engine can exhert.",background='silver').grid(row = 29 , column = 3, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Fuel Mass",font = self.ArialBg,background='silver').grid(row = 30 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much mass of a spacecraft is fuel.",background='silver').grid(row = 30 , column = 3, columnspan = 1, sticky = W)


                    self.glosscombust = Button(self.oroot, text = "Close", command = orootwindowclose)
                    self.glosscombust.grid(row = 31, column = 1, columnspan = 3)

                    b.bind_widget(self.glosscombust, balloonmsg='Close Window')

            def frootwindow():
                if self.frootopen == 0:
                    self.froot = Toplevel()
                    self.frootopen = 1 
                    self.froot.wm_title("Frequently Asked Questions")
                    self.froot.configure(background='silver')
                    
                    self.OBERTHOP = -1

                    

                    def OBERTHOPEN():
                        self.OBERTHOP = self.OBERTHOP * -1
                        if self.OBERTHOP == 1:
                            self.l11 = Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver')
                            self.l11.grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                            self.l12 = Label(self.froot, text = "to perform a 'burn' is at orbital periapsis, where orbital speed is the highest. When burning,",background='silver')
                            self.l12.grid(row = 3 , column = 1, columnspan = 10, sticky = W)
                            self.l13 = Label(self.froot, text = "kinetic energy is increased as speed increases. However, since the equation for kinteic energy",background='silver')
                            self.l13.grid(row = 4 , column = 1, columnspan = 10, sticky = W)
                            self.l14 = Label(self.froot, text = "is increased as speed increases. However, since the equation for kinteic energy is Ek = 0.5mv^2,",background='silver')
                            self.l14.grid(row = 5 , column = 1, columnspan = 10, sticky = W)
                            self.l15 = Label(self.froot, text = "velocity is squared. So going from 10m/s to 20m/s will produce significantly more energy than ")
                            self.l15.grid(row = 6 , column = 1, columnspan = 10, sticky = W)
                            self.l16 = Label(self.froot, text = "going from 0m/s to 10m/s. This is utilised when burning at periapsis. Since speed is the highest")
                            self.l16.grid(row = 7 , column = 1, columnspan = 10, sticky = W)
                            self.l17 = Label(self.froot, text = "possible at this point, kinetic energy is increased to the square of the added velocity.")
                            self.l17.grid(row = 8 , column = 1, columnspan = 10, sticky = W)
                        else:
                            self.l11.grid_remove()
                            self.l12.grid_remove()
                            self.l13.grid_remove()
                            self.l14.grid_remove()
                            self.l15.grid_remove()
                            self.l16.grid_remove()
                            self.l17.grid_remove()


                    self.OBERTH = Button(self.froot, text = "Why does the orbit get much larger when the ship is travelling faster?",  font = self.ArialBg,background='silver',command = OBERTHOPEN)
                    self.OBERTH.grid(row = 1 , column = 1, columnspan = 10, sticky = W)

                    self.SHIPSPEED = Button(self.froot, text = "Why does the ship speed up when getting closer to the planet?",  font = self.ArialBg,command = OBERTHOPEN)
                    self.SHIPSPEED.grid(row = 10 , column = 1, columnspan = 10, sticky = W)


                    #GLOSSARY
                    

                        

                    

                    
                        
                    
                    #Label(self.froot, text = "Heading",  font = self.ArialBg,background='silver').grid(row = 1 , column = 1, columnspan = 10)
                   # Label(self.froot, text = "Body",background='silver').grid(row = 2 , column = 2, columnspan = 10)

                    
                    
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)


                    

                    

                    self.faqcombust = Button(self.froot, text = "Close", command = frootwindowclose)
                    self.faqcombust.grid(row = 30, column = 1, columnspan = 3)

                    b.bind_widget(self.faqcombust, balloonmsg='Close Window')
                    

            def prootwindowclose():
                self.proot.destroy()
                self.prootopen = 0

            def prootwindow():
                if self.prootopen == 0:
                    self.proot = Toplevel()
                    self.prootopen = 1 
                    self.proot.wm_title("Orbital Characteristics")
                    self.proot.configure(background='silver')

                    Label(self.proot, text = "                                                        ",background='silver').grid(row=1, column = 2)
                    Label(self.proot, text = "",background='silver').grid(row=2, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=3, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=4, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=5, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=6, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=7, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=8, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=9, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=10, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=11, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=12, column = 5)
                    Label(self.proot, text = "",background='silver').grid(row=13, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=14, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=15, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=16, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=17, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=18, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=19, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=20, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=21, column = 5)

                    
                    self.sua =Label(self.proot, text=(round((self.UA),1),"m"))
                    self.sua.grid(row=2, column = 1, sticky=W, columnspan = 3)
                    self.sa =Label(self.proot, text=(round((self.A),1),"m"))
                    self.sa.grid(row=3, column = 1, sticky=W, columnspan = 3)
                    self.sm =Label(self.proot, text=(round((self.M),1),"kg"))
                    self.sm.grid(row=4, column = 1, sticky=W, columnspan = 3)
                    self.sv =Label(self.proot, text=(round((self.V),1),"m/s")) 
                    self.sv.grid(row=5, column = 1, sticky=W, columnspan = 3)
                    self.su =Label(self.proot, text=(round((self.U),1),"m^3/s"))
                    self.su.grid(row=6, column = 1, sticky=W, columnspan = 3)
                    self.sb =Label(self.proot, text=(round((self.B),1),"m"))
                    self.sb.grid(row=7, column = 1, sticky=W, columnspan = 3)
                    self.sl =Label(self.proot, text=(round((self.L),1),"m"))
                    self.sl.grid(row=8, column = 1, sticky=W, columnspan = 3)
                    self.se =Label(self.proot, text=(round((self.E),1),"m"))
                    self.se.grid(row=9, column = 1, sticky=W, columnspan = 3)
                    self.sh =Label(self.proot, text=(round((self.H),1),"m"))
                    self.sh.grid(row=10, column = 1, sticky=W, columnspan = 3)
                    self.sp =Label(self.proot, text= (round((self.T),1),"s"))
                    self.sp.grid(row=11, column = 1, sticky=W, columnspan = 3)
                    self.sd =Label(self.proot, text= (round((self.Ec),1)))
                    self.sd.grid(row=12, column = 1, sticky=W, columnspan = 3)
                   
                    
                    
                    self.suat =Label(self.proot, text=("Radar Altitude"))
                    self.suat.grid(row=2, column = 3, sticky=W, columnspan = 3)
                    self.sat =Label(self.proot, text=("Altitude"))
                    self.sat.grid(row=3, column = 3, sticky=W, columnspan = 3)
                    self.smt =Label(self.proot, text=("Body Mass"))
                    self.smt.grid(row=4, column = 3, sticky=W, columnspan = 3)
                    self.svt =Label(self.proot, text=("Spacecraft Velocity"))
                    self.svt.grid(row=5, column = 3, sticky=W, columnspan = 3)
                    self.sut =Label(self.proot, text=("Gravational Parameter"))
                    self.sut.grid(row=6, column = 3, sticky=W, columnspan = 3)

                    if self.A >= self.B:
                        self.sbt =Label(self.proot, text=("Value of Periapsis"))

                    else:
                        self.sbt =Label(self.proot, text=("Value of Apoapsis"))
                    self.sbt.grid(row=7, column = 3, sticky=W, columnspan = 3)
                    self.slt =Label(self.proot, text=("Semi-Major Axis"))
                    self.slt.grid(row=8, column = 3, sticky=W, columnspan = 3)
                    self.set =Label(self.proot, text=("Focal Length"))
                    self.set.grid(row=9, column = 3, sticky=W, columnspan = 3)
                    self.sht =Label(self.proot, text=("Semi-Minor Axis"))
                    self.sht.grid(row=10, column = 3, sticky=W, columnspan = 3)
                    self.spt =Label(self.proot, text=("Orbital Period"))
                    self.spt.grid(row=11, column = 3, sticky=W, columnspan = 3)
                    self.sdt =Label(self.proot, text=("Eccentricity"))
                    self.sdt.grid(row=12, column = 3, sticky=W, columnspan = 3)

                    

                    self.waitmes = Label(self.proot, text =("Calculating..."), background = 'silver')
                    self.waitmes.grid(row = 6, column = 1, columnspan = 3)
                    self.waitmes.grid_remove()

                    b.bind_widget(self.suat, balloonmsg='Altitude above Body Surface')
                    
                    b.bind_widget(self.smt, balloonmsg='Body Mass')
                    b.bind_widget(self.svt, balloonmsg='Velocity of Spacecraft')
                    b.bind_widget(self.sut, balloonmsg='Gravational Parameter')
                    if self.A >= self.B:
                        b.bind_widget(self.sbt, balloonmsg='Height of Periapsis')
                        b.bind_widget(self.sat, balloonmsg='Altitude from Body Centre. Also height of Apoapsis')

                    else:
                        b.bind_widget(self.sbt, balloonmsg='Height of Apoapsis')
                        b.bind_widget(self.sat, balloonmsg='Altitude from Body Centre. Also height of Periapsis')
                        
                    
                    b.bind_widget(self.slt, balloonmsg='Half the distance of the longest part of the Orbit')
                    b.bind_widget(self.set, balloonmsg='Distance from the middle of the Orbit from the centre of the Body')
                    b.bind_widget(self.sht, balloonmsg='Half the distance of the shortest part of the Orbit')
                    b.bind_widget(self.spt, balloonmsg='Time it takes to comeplete one Orbit (in seconds)')
                    b.bind_widget(self.sdt, balloonmsg='Eccentrictiy of the Orbit')


                    

                    

                    self.pcombust = Button(self.proot, text = "Close", command = prootwindowclose)
                    self.pcombust.grid(row = 15, column = 1, columnspan = 3)

                    b.bind_widget(self.pcombust, balloonmsg='Close Window')

            def crootwindowclose():
                self.croot.destroy()
                self.crootopen = 0

            def crootwindow():
                if self.crootopen == 0:
                    self.croot = Toplevel()
                    self.crootopen = 1 
                    self.croot.wm_title("Calculator")
                    self.croot.configure(background='silver')
                    self.dvbutton = Button(self.croot, text = "Calculate Delta V", command = dvCalculator)
                    self.burnbutton = Button(self.croot, text = "Calculate Burn Time", command = burntimeCalculator)
                    self.ispBox = Entry(self.croot, textvariable=self.ispentry)
                    self.ispBox.grid(row=1, column=1)
                    self.wetBox = Entry(self.croot, textvariable=self.wetmassentry)
                    self.wetBox.grid(row=2, column=1)
                    self.dryBox = Entry(self.croot, textvariable=self.drymassentry)
                    self.dryBox.grid(row=3, column=1)

                    self.dvbutton.grid(row = 2, column = 3)
                    self.burnbutton.grid(row = 7, column = 3)

                    Label(self.croot, text = "",background='silver').grid(row=4, column = 1)
                    Label(self.croot, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver').grid(row=4, column=1, columnspan = 5)
              

                    self.shipispBox = Entry(self.croot, textvariable=self.shipispentry)
                    self.shipispBox.grid(row=6, column=1)
                    self.shipthrustBox = Entry(self.croot, textvariable=self.shipenginethrustentry)
                    self.shipthrustBox.grid(row=7, column=1)
                    self.shipfuelBox = Entry(self.croot, textvariable=self.shipfuelmassentry)
                    self.shipfuelBox.grid(row=8, column=1)

                    self.dvlab = Label(self.croot, text=("DeltaV=",0, "m/s"), background='silver')
                    self.dvlab.grid(row=29, column = 4)
                    self.btlab = Label(self.croot, text=("DeltaV=",0, "m/s"), background='silver')
                    self.btlab.grid(row=29, column = 4)
                    self.dvlab.grid_remove()
                    self.btlab.grid_remove()

                    self.combust = Button(self.croot, text = "Close", command = crootwindowclose)
                    self.combust.grid(row = 9, column = 1)

                    Label(self.croot,text = "Specific Impulse").grid( row=1, column = 2, sticky=W)
                    Label(self.croot,text = "Wet Mass").grid( row=2, column = 2, sticky=W)
                    Label(self.croot,text = "Dry Mass").grid( row=3, column = 2, sticky=W)

                    Label(self.croot,text = "Specific Impulse").grid( row=6, column = 2, sticky=W)
                    Label(self.croot,text = "Force of Engine").grid( row=7, column = 2, sticky=W)
                    Label(self.croot,text = "Mass of Fuel").grid( row=8, column = 2, sticky=W)

                    b.bind_widget(self.dvbutton, balloonmsg='Calulate Delta V (in metres pre second)')
                    b.bind_widget(self.burnbutton, balloonmsg='Calulate burn time (in seconds)')

                    b.bind_widget(self.shipfuelBox, balloonmsg="Mass of Spacecraft's fuel in Tons ")
                    b.bind_widget(self.shipthrustBox, balloonmsg='Force of Engine in kN')
                    b.bind_widget(self.shipispBox, balloonmsg='Specific Impulse of craft in seconds')

                    b.bind_widget(self.dryBox, balloonmsg="Mass of Spacecraft's when dry of Fuel")
                    b.bind_widget(self.wetBox, balloonmsg="Mass of Spacecraft's when full of Fuel")
                    b.bind_widget(self.ispBox, balloonmsg='Specific Impulse of craft in seconds')
                    
                    
                    b.bind_widget(self.dvlab, balloonmsg='Potential change in Velocity')
                    b.bind_widget(self.btlab, balloonmsg='Length of time engine can run before burnout')

                    b.bind_widget(self.combust, balloonmsg='Close Window')

            self.fM = 1
            self.fplanetradius = 1

            self.fMlab =Label(groot, text = self.fM)
            self.fMlab.grid(column=4, row=8, columnspan = 1)
            
            self.fplanetradiuslab = Label(groot, text = self.fplanetradius)
            self.fplanetradiuslab.grid(column=4, row=9, columnspan = 1)

            def planetdetails():
                self.fMlab.grid_remove()
                
                self.fplanetradiuslab.grid_remove()
                if self.planetcombobox.current() == 0:
                    
                 
                    self.fM = 1.988 * 10 ** 30
                    self.fplanetradius = 695000000
                    
                    
                    
                    #self.planetradius = 695000000
                    #self.V = ((self.G * self.M )/(self.UA + self.planetradius))**0.5
                 
                elif self.planetcombobox.current() == 1:
             
                    self.fM = 3.302 * 10 ** 23
                    self.fplanetradius = 2440000
                   
                
                elif self.planetcombobox.current() == 2:
                  
                    self.fM = 4.867 * 10 ** 24 
                    self.fplanetradius = 6050000
                    
                  
                elif self.planetcombobox.current() == 3:
                 
                    self.fM = 5.972 * 10 ** 24 
                    self.fplanetradius = 6370000
                    
                   
                elif self.planetcombobox.current() == 4:
                 
                    self.fM = 7.348 * 10 ** 22
                    self.fplanetradius = 1740000
                    
                 
                
                elif self.planetcombobox.current() == 5:
               
                    self.fM = 6.418 * 10 ** 23 
                    self.fplanetradius = 3390000
                    
                    
                elif self.planetcombobox.current() == 6:
                   
                    self.fM = 1.898 * 10 ** 27
                    self.fplanetradius = 69900000
                    
                    
                elif self.planetcombobox.current() == 7:
                   
                    self.fM = 5.683 * 10 ** 26
                    self.fplanetradius = 58200000
                    
                   
                elif self.planetcombobox.current() == 8:
                    
                    self.fM = 8.681 * 10 ** 25
                    self.fplanetradius = 25400000
                    
                    
                elif self.planetcombobox.current() == 9:
                   
                    self.fM = 1.024 * 10 ** 26
                    self.fplanetradius = 24600000
                    
                    
                elif self.planetcombobox.current() == 11:
                    
                    self.fM = 1.756 * 10 ** 28
                    self.fplanetradius = 262000000
                    
                   
                elif self.planetcombobox.current() == 12:
                   
                    self.fM = 2.526 * 10 ** 21
                    self.fplanetradius = 250000
                   
                  
                elif self.planetcombobox.current() == 13:
                   
                    self.fM = 1.224 * 10 ** 23
                    self.fplanetradius = 700000
                    
                   
                elif self.planetcombobox.current() == 14:
               
                    self.fM = 1.242 * 10 ** 17
                    self.fplanetradius = 13000
                    
                   
                elif self.planetcombobox.current() == 15:
                   
                    self.fM = 5.292 * 10 ** 22 
                    self.fplanetradius = 600000
                    
                    
                elif self.planetcombobox.current() == 16:
                    
                    self.fM = 9.76 * 10 ** 20
                    self.fplanetradius = 200000
                   
                   
                elif self.planetcombobox.current() == 17:
                   
                    self.fM = 2.646 * 10 ** 19
                    self.fplanetradius = 60000
                    
                elif self.planetcombobox.current() == 18:
                   
                    self.fM = 4.515 * 10 ** 21
                    self.fplanetradius = 320000
                    
                elif self.planetcombobox.current() == 19:
                    
                    self.fM = 2.782 * 10 ** 20
                    self.fplanetradius = 130000
                    
                elif self.planetcombobox.current() == 20:
                    
                    self.fM = 3.219 * 10 ** 20
                    self.fplanetradius = 138000
                    
                elif self.planetcombobox.current() == 21:
                    
                    self.fM = 4.233 * 10 ** 24
                    self.fplanetradius = 6000000
                     
                elif self.planetcombobox.current() == 22:
                    
                    self.fM = 2.939 * 10 ** 22
                    self.fplanetradius = 500000
                    
                elif self.planetcombobox.current() == 23:
                    
                    self.fM = 3.109 * 10 ** 21
                    self.fplanetradius = 300000
                   
                elif self.planetcombobox.current() == 24:
                    
                    self.fM = 4.233 * 10 ** 22
                    self.fplanetradius = 600000
                    
                elif self.planetcombobox.current() == 25:
                    
                    self.fM = 3.726 * 10 ** 19
                    self.fplanetradius = 65000
                   
                elif self.planetcombobox.current() == 26:
                   
                    self.fM = 1.081 * 10 ** 19
                    self.fplanetradius = 44000
                    
                elif self.planetcombobox.current() == 27:
                    
                    self.fM = 1.115 * 10 ** 21
                    self.fplanetradius = 210000
                   

                self.fMlab =Label(groot, text = ("Body_Mass=",self.fM,"kg"))
                self.fMlab.grid(column=4, row=11, columnspan = 2,sticky = W)
                
                self.fplanetradiuslab = Label(groot, text = ("Body_Radius=",self.fplanetradius,"m"))
                self.fplanetradiuslab.grid(column=4, row=12, columnspan = 2,sticky = W)


                pb = tkinter.tix.Balloon(groot)
                pb.bind_widget(self.fMlab, balloonmsg='Mass of selected Body')
                pb.bind_widget(self.fplanetradiuslab, balloonmsg='Radius of selected Body')  #DONT KNOW WHY THIS ISNT WORKING
                

                    
                #if self.planetcombobox.current() == 0:
                 #   Label(self.groot, text = "HEY").grid(column=4, row=8, columnspan = 1)
                if orbitcalcopen == 1:
                    groot.after(1000, planetdetails)
                else:
                    self.fplanetradiuslab.grid_remove()
                    self.fMlab.grid_remove()
                

            def burntimeCalculator():

                self.btlab.grid_remove()



                self.enginethrust = self.shipenginethrustentry.get() #In kN
                self.engineisp = self.shipispentry.get() #in s

                self.shipfuelmass = self.shipfuelmassentry.get() #in tons

                self.fuelrate = (1/((9.81* self.engineisp) /  self.enginethrust))

                self.burntime = self.shipfuelmass/self.fuelrate

                self.btlab = Label(self.croot, text=("Time=",round(self.burntime,1), "s"), background='silver')
                self.btlab.grid(row=8, column = 3, columnspan = 5, sticky=W)
                

                

                
                print (self.fuelrate)
                print (self.burntime)

            def dvCalculator():
                self.dvlab.grid_remove()

                self.dv += 1

                

                #self.isp = self.ispentry.get()
                #self.wetmass = self.wetmassentry.get()
                #self.drymass = self.drymassentry.get()

                self.dv = round((self.ispentry.get() * 9.8 * math.log(self.wetmassentry.get()/self.drymassentry.get())), 1)
                print (self.dv)

                #self.dvLab = Label(self.groot, text=self.dv)
                #self.dvLab.grid(row=20, column=1, columnspan = 4)
                #self.dvLab.configure(background='silver') #transparent

                self.dvlab = Label(self.croot, text=("DeltaV=",round(self.dv,1), "m/s"), background='silver')
                self.dvlab.grid(row=3, column = 3, columnspan = 5, sticky=W)
                


            
            self.spacecraftx = self.ovalheadway
            self.phase = 1
            self.reset = 1
            self.shipdraw = 0
            #self.psuedoplanet = 0
            self.shiptextV = 0
            self.shiptextA = 0
            self.shiptextg = 0
            self.shiptextD = 0
            self.shiptextL = 0
            self.shipdrawchange = 0
                #self.spacecraft_draw
            def spacecraft_draw(): #does not have loop but draws in right place for middle, but not ends of orbit ### ADD LIMIT OTHERWISE IS GOES COMPLEX- MAKE IT GO BACK TO POSTIVES GOING FAR TO CLOSE, SHORTEN NONSENSE
                
                self.enterbutton.configure (state = DISABLED)
                self.entercorebutton.configure (state = DISABLED)
                self.entermassbutton.configure (state = DISABLED)
                self.enteraltbutton.configure (state = DISABLED)
                self.enterorbbutton.configure (state = DISABLED)
                self.enterathbutton.configure (state = DISABLED)
                self.enterincbutton.configure (state = DISABLED)
                self.buttonrun.configure (state = DISABLED)
                self.shiprunbutton.configure (state = DISABLED)
                self.bodybutton.configure (state = DISABLED)
                self.ZoomSlide.configure (state = DISABLED)
                self.InclineSlide.configure (state =DISABLED)
                self.entershipmass.configure (state = DISABLED)
                self.resetdv.configure(state = DISABLED)
                global spacecraftx
                global shipdraw
                global shiptextV
                global shiptextD
                global shiptextL
                #self.w.create_image(self.canvasx - 95, 75,image=self.shipImage) #Banner
                self.w.delete(self.shipdraw) #Maybe make others like this, rpboably doesn't mateer
                #self.w.delete(self.psuedoplanet)
                self.w.delete(self.shiptextV)
                self.w.delete(self.shiptextg)
                self.w.delete(self.shiptextD)
                self.w.delete(self.shiptextL)
                self.w.delete(self.VELread)
                self.w.delete(self.ALTread)
                self.w.delete(self.gread)
                self.w.delete(self.shiptextA)

                

                
                #print (self.rl, "R")


                


                
                if self.phase == 1 and self.spacecraftx >= self.canvasx - self.ovalheadway - self.shipdrawchange:
                    self.phase = 2
                elif self.phase == 2 and self.spacecraftx <= self.ovalheadway + self.shipdrawchange:
                    self.phase = 0
                 #   != does not equal
                
                if self.phase == 1:
                    

                    if ((self.incline) >= 0 and (self.incline) <= 180):
                        self.rl = -1
                    else:
                        self.rl = 1

                    if (abs(self.incline) >= 90 and abs(self.incline) <= 180):
                        self.shipl = -1
                    else:
                        self.shipl = 1

                    #self.spacecraftx += self.shipdrawchange
                    #print ("phase 1")
                    #self.spacecrafty1 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 0.1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                    self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                elif self.phase == 2:
                    #print ("phase 2")
                    if self.reset == 1:
                        self.rl = self.rl * -1
                        self.shipl = self.shipl * -1
                        self.spacecraftx =  self.canvasx-self.ovalheadway
                        self.spacecrafty2 = self.canvasy/2
                        self.shipdraw = self.w.create_image(self.spacecraftx, self.spacecrafty2,image=self.shipImage)
                        self.reset = 0
                
                    
                    #self.spacecraftx -= self.shipdrawchange
                    
                    #self.spacecrafty1 = 1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                    self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                    self.w.delete(self.shipdraw)

                self.shipxdis = abs(self.ovalheadway + self.UA/self.S + self.planetsize - self.spacecraftx)
                self.shipydis = abs(self.spacecrafty2 - self.canvasy/2)
                #print (self.shipxdis, "X")
                #print (self.shipydis, "Y")
                

                self.shipdis = ((self.shipxdis **2 + self.shipydis**2)**0.5)
                self.shipR = self.shipdis * self.S

                self.shipg = (self.U)/(self.shipR**2)

                self.w.delete(self.smallban)
                self.w.delete(self.smalltext)
                


                self.Fc = (self.shipmass * self.shipg) *1000 # in N
                #self.w.tag_lower(self.shipdraw)

                
                    
                    
                

                if self.Fc != 0:
                    self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                    self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)
                #print (self.g, "G")
                
                
                

                #print (self.shipdis, "DIS")
                #print (self.shipR, "R")

                #self.shipR = self.planetradius + self.UA
                #self.L = (self.R + self.planetradius + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                self.shipV = (self.U * (2/self.shipR - 1/self.L))**0.5
                #print (self.shipV, "V")

                

                self.shipdrawchange = (((self.shipV*self.T**1.3) / (self.T*3000 * self.g))) * 0.8
                #self.shipdrawchange =  (self.shipV / (self.T*200 * self.g))
                #print (self.shipdrawchange)


                if self.phase == 1:
                    self.spacecraftx += self.shipdrawchange
                    
                            
                    #
                elif self.phase == 2:
                    self.spacecraftx -= self.shipdrawchange
                #self.spacecrafty1 = ((self.OvalH**2)*(1 - self.spacecraftx**2/(self.canvasx/2-self.ovalheadway)**2))**0.5
                #self.spacecrafty2 = ((self.OvalH**2)*(1 - self.spacecraftx**2/(self.canvasx/2-self.ovalheadway)**2))**0.5
                
               ## self.spacecrafty1 = ((((self.OvalH)**2)*(1-((self.spacecraftx-self.canvasx/2 + 0.5) + self.translate)/(self.canvasx/2-self.ovalheadway)**2))**0.5) -self.canvasy/2
               # self.spacecrafty2 = ((((self.OvalH)**2)*(1-((self.spacecraftx-self.canvasx/2 - 0.5) + self.translate)/(self.canvasx/2-self.ovalheadway)**2))**0.5) -self.canvasy/2 #REARRANGE
                #print (self.spacecraftx)
                #print (self.spacecrafty1)
                #print (self.spacecrafty2)
                #self.shipdraw = self.w.create_line(self.spacecraftx,self.spacecrafty1,self.spacecraftx + 10,self.spacecrafty2, width = 15) # PUT
                #self.shiptextV = self.w.create_text(self.canvasx-79  + self.x,50 + self.y, text=("Velocity(m/s)=", int(round(self.shipV,0))), font=self.ArialBVel)

                if self.shipV >= 100000000:
                    self.shiptextV = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(Mm/s)=", (round(self.shipV/1000000,2))), font=self.ArialBVel)
                elif self.shipV >= 100000:
                    self.shiptextV = self.w.create_text(self.canvasx-79 ,50 , text=("Velocity(km/s)=", (round(self.shipV/1000,1))), font=self.ArialBVel)
                else:
                    self.shiptextV = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(m/s)=", int(round(self.shipV,0))), font=self.ArialBVel)

                if self.shipR >= 1000000000:
                     self.shiptextA = self.w.create_text(79 ,60, text=("Altitude(Mm)=", int(round(self.shipR/1000000,0))), font=self.ArialBAlt)
                elif self.shipR >= 1000000:
                     self.shiptextA = self.w.create_text(79 ,60 , text=("Altitude(km)=", int(round(self.shipR/1000,0))), font=self.ArialBAlt)
                else:
                     self.shiptextA = self.w.create_text(79 ,60 , text=("Altitude(m)=", int(round(self.shipR,0))), font=self.ArialBAlt)

                if self.shipg >= 10000:
                    self.shiptextg= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.shipg/1000,2)),font=self.ArialBg)
                else:
                    self.shiptextg= self.w.create_text(self.canvasx-53,95 , text=("Grav(m/s)=", round(self.shipg,2)),font=self.ArialBg)

                
                #self.shiptextA = self.w.create_text(79  + self.x,60 + self.y, text=("Altitude(m)=", int(round(self.shipR,0))), font=self.ArialBAlt)
                #self.shiptextg = self.w.create_text(self.canvasx-53 + self.x,95 + self.y, text=("Grav(m/s)=", round(self.shipg,2)),font=self.ArialBg)
               # self.shiptextD = self.w.create_text(self.canvasx/2, self.canvasy/2 - 10, text=(int(self.shipR), "DIST"))
                #self.shiptextL = self.w.create_line(self.spacecraftx,self.spacecrafty2,self.canvasx/2, self.canvasy/2)

                
                
                self.shipdraw = self.w.create_image(self.spacecraftx, self.spacecrafty2,image=self.shipImage)

                if self.rl == 1:

                    if ((self.incline) <= -90 and (self.incline) >= -180):
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc1)
                        
                        self.w.tag_lower(self.planet)
                        
                        self.w.tag_lower(self.arc2)
                        #self.w.tag_raise(self.shipdraw)
                        self.w.tag_lower(self.athoval)

                    elif ((self.incline) <= 0 and (self.incline) >= -90):
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc2)
                        
                        self.w.tag_lower(self.planet)
                        
                        self.w.tag_lower(self.arc1)
                        #self.w.tag_raise(self.shipdraw)
                        self.w.tag_lower(self.athoval)
                        
                  #  elif (-1*((self.incline) >= 0 and (self.incline) >= -90)):
                    #    self.w.tag_raise(self.arc2)
                     #   print ("MWE")
                      #  self.w.tag_lower(self.arc1)

                    elif (((self.incline) >= 0 and (self.incline) <= 90)):

                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc1)
                        
                        self.w.tag_lower(self.planet)
                        
                        self.w.tag_lower(self.arc2)
                        #self.w.tag_raise(self.shipdraw)
                        self.w.tag_lower(self.athoval)

                    elif (((self.incline) >= 90 and (self.incline) <= 180)):
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc2)
                        
                        self.w.tag_lower(self.planet)
                        
                        self.w.tag_lower(self.arc1)
                        #self.w.tag_raise(self.shipdraw)
                        self.w.tag_lower(self.athoval)

                    
                        
                    

                    
                   
                elif self.rl == -1:
                    
                    if ((self.incline) <= -90 and (self.incline) >= -180):
                        self.w.tag_lower(self.arc1)
                        self.w.tag_lower(self.planet)
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc2)

                    elif ((self.incline) <= 0 and (self.incline) >= -90):
                        self.w.tag_lower(self.arc2)
                        self.w.tag_lower(self.planet)
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc1)
                        
                  #  elif (-1*((self.incline) >= 0 and (self.incline) >= -90)):
                    #    self.w.tag_raise(self.arc2)
                     #   print ("MWE")
                      #  self.w.tag_lower(self.arc1)

                    elif (((self.incline) >= 0 and (self.incline) <= 90)):

                        self.w.tag_lower(self.arc1)
                        self.w.tag_lower(self.planet)
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc2)

                    elif (((self.incline) >= 90 and (self.incline) <= 180)):
                        self.w.tag_lower(self.arc2)
                        self.w.tag_lower(self.planet)
                        self.w.tag_lower(self.shipdraw)
                        self.w.tag_lower(self.arc1)
                    
                    
                    
                    
                        
                    
                        
                #self.w.tag_lower(self.planet)
                
                self.w.tag_lower(self.athoval)
                    
                   
                #self.psuedoplanet = self.w.create_oval(self.ovalheadway + self.UA/self.S,self.canvasy/2 - self.planetsize,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize,self.canvasy/2 + self.planetsize, fill = self.planetcolor , outline = "white") #Planet

                #if abs(self.incline) < 180:
                   # self.w.tag_raise(self.shipdraw) #Or raise/lower
                #    self.rl = 1
               # else:
                    #self.w.tag_lower(self.shipdraw) #Or raise/lower
                #    self.rl = 2

                
                
                
               # else:
                 #   self.w.tag_raise(self.shipdraw)

                    
                
                if self.phase != 0:
                    #print ("HEY")
                    self.root.after(self.looptime, spacecraft_draw)
                elif self.phase == 0:
                    self.w.delete(self.shipdraw)
                    #self.w.delete(self.psuedoplanet)
                    
                    self.w.delete(self.shiptextV)
                    self.w.delete(self.shiptextA)
                    self.w.delete(self.shiptextg)
                    self.w.delete(self.shiptextD)
                    self.w.delete(self.shiptextL)

                    if self.V >= 100000000:
                        self.VELread = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(Mm/s)=", (round(self.V/1000000,2))), font=self.ArialBVel)
                    elif self.V >= 100000:
                        self.VELread = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(km/s)=", (round(self.V/1000,1))), font=self.ArialBVel)
                    else:
                        self.VELread = self.w.create_text(self.canvasx-79,50 , text=("Velocity(m/s)=", int(round(self.V,0))), font=self.ArialBVel)
                    
                    
                    if self.A >= 1000000000:
                         self.ALTread = self.w.create_text(79  ,60 , text=("Altitude(Mm)=", int(round(self.A/1000000,0))), font=self.ArialBAlt)
                    elif self.A >= 1000000:
                         self.ALTread = self.w.create_text(79 ,60 , text=("Altitude(km)=", int(round(self.A/1000,0))), font=self.ArialBAlt)
                    else:
                         self.ALTread = self.w.create_text(79  ,60 , text=("Altitude(m)=", int(round(self.A,0))), font=self.ArialBAlt)

                    
                    if self.g >= 10000:
                        self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.g/1000,2)),font=self.ArialBg)
                    else:
                        self.gread= self.w.create_text(self.canvasx-53 ,95, text=("Grav(m/s)=", round(self.g,2)),font=self.ArialBg)
                    
                    self.spacecraftx = self.ovalheadway
                    self.spacecrafty2 = self.canvasy/2
                    self.shipdraw = self.w.create_image(self.spacecraftx, self.spacecrafty2,image=self.shipImage)
                    #self.spacecrafty1 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 0.1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                    #self.spacecrafty2 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                    self.phase = 1
                    self.reset = 1
                    self.enterbutton.configure (state = NORMAL)
                    self.entercorebutton.configure (state = NORMAL)
                    self.entermassbutton.configure (state = NORMAL)
                    self.enteraltbutton.configure (state = NORMAL)
                    self.enterorbbutton.configure (state = NORMAL)
                    self.enterincbutton.configure (state = NORMAL)
                    self.enterathbutton.configure (state = NORMAL)
                    self.buttonrun.configure (state = NORMAL)
                    self.shiprunbutton.configure (state = NORMAL)
                    self.bodybutton.configure (state = NORMAL)
                    self.ZoomSlide.configure (state = NORMAL)
                    self.InclineSlide.configure (state =NORMAL)
                    self.entershipmass.configure (state = NORMAL)
                    self.resetdv.configure(state = NORMAL)

                    
                    #print (self.spacecraftx)
                    #print (self.spacecrafty1)
                    #print (self.spacecrafty2)
                    #self.shipdraw = self.w.create_line(self.spacecraftx,self.spacecrafty1,self.spacecraftx + 10,self.spacecrafty2, width = 15)
        
                        
            def zoom():

                self.zoom = self.ZoomSlide.get() * (self.canvasy/200) # + 100 # self.zoom
                if (self.zoom - self.oldzoom) != 0:
                    zoomcontrol()
                    

                #if self.zoom != 0:
                self.oldzoom = self.zoom
                

                self.root.after(100, zoom)

            
                    

                
                ##    self.ovalheadway -= 10
                 #   self.Vchange=0
                 #   self.Mchange=0
                  #  self.Pchange=0
                  #  self.Achange=0
                  #  self.Atchange=0
                   # self.update_frame()
                    
                    
            

            def zoomcontrol():
                
                self.ovalheadway = self.zoom
                userchangeclean()
                update_frame()

            def resetdv():
                self.tdvchange = 0
                self.tdvchangelab.grid_remove()

                #self.dvchangelab = Label(self.groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
                self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

                #self.dvchangelab.grid(row = 8, column = 3, columnspan = 2)
                
                self.tdvchangelab.grid(row = 9, column = 2, columnspan = 2, sticky = W)
                

                #self.dvchangelab.grid_remove()
                
                
                
            self.w = Canvas(self.root, width = self.canvasx, height = self.canvasy)
            self.w.pack()


            #button1 = tkinter.tix.Button(self.groot, text='Something Unexpected',command=spacecraft_draw)
            #button2 = tkinter.tix.Button(self.groot, text='Something Else Unexpected',command =spacecraft_draw)
            #button1.grid(row = 1, column = 1)
           # button2.grid(row=4, column = 1)
           # b = tkinter.tix.Balloon(self.groot)
            #b.bind_widget(button1, balloonmsg='Close Window')
            #b.bind_widget(button2, balloonmsg='Self-destruct button')

            self.planetcombobox = ttk.Combobox(groot, state= 'readonly')
            self.planetcombobox['values'] = ('Sun','Mercury', 'Venus', 'Earth', '      Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune' ,'-------', 'Kerbol', 'Moho', 'Eve', '      Gilly', 'Kerbin', '        Mun' , '        Minmus','Duna', '       Ike', 'Dres', 'Jool', '      Laythe', '      Vall', '      Tylo', '      Bop', '      Pol', 'Eeloo')
            self.planetcombobox.current(0)
        
            self.planetcombobox.grid(column=1, row=11, columnspan = 2)
            
            self.w.configure(background='white') #canvas background
            self.enterbutton = Button(groot,text = "Set Velocity", command=loopchangevel)
            self.entercorebutton = Button(groot,text = "Set Body Diameter", command=loopchangecore)
            self.entermassbutton = Button(groot,text = "Set Body Mass", command=loopchangemass)
            self.enteraltbutton = Button(groot,text = "Set Altitude", command=loopchangealt)
            self.enterorbbutton = Button(groot,text = "Set Apo/Peri", command=loopchangeorbit)
            self.enterathbutton = Button(groot,text = "Set Atmosphere", command=loopchangeath)
            self.enterincbutton = Button(groot,text = "Set Inclination", command=loopchangeincline)
            self.buttonrun = Button(groot,text='Run!',command=looprun) #buttons can interupt loop
            
            self.shiprunbutton = Button(groot,text = "Run Ship", command=spacecraft_draw)
            self.resetbutton = Button(groot,text = "Reset", command=reset,background = 'silver')
            self.bodybutton = Button(groot,text = "Confirm Body", command=planetbox)
            #self.zoominbutton = Button(self.groot, text = "Zoom In", command=zoomin)
            #self.zoomoutbutton = Button(self.groot, text = "Zoom Out", command=zoomout)
            self.entershipmass = Button(groot, text = "Optional - Confirm Mass", command = shipmassset)
            self.resetdv = Button(groot, text = "Reset Total dV", command = resetdv)
            self.changeposition = Button(groot, text = "Warp to Apo/Peri", command = loopchangeposition)
            self.crootwindowopen = Button(groot, text = "Calculator", command = crootwindow)
            self.prootwindowopen = Button(groot, text = "Orbital Characteristics", command = prootwindow)
            self.frootwindowopen = Button(groot, text = "FAQ", command = frootwindow)
            self.orootwindowopen = Button(groot, text = "Glossary", command = orootwindow)

                
            

            self.dv = 0
            self.dvchange = 0
            self.incline = 0
            self.tdvchange = 0
            


            self.Ventry = IntVar()
            
            self.PRdentry = DoubleVar()
            self.Mdentry = DoubleVar()
            self.Adentry = DoubleVar()
            self.Odentry = DoubleVar()
            self.Atdentry = DoubleVar()
            self.PReentry = IntVar()
            self.Meentry = IntVar()
            self.Aeentry = IntVar()
            self.Oeentry = IntVar()
            self.Ateentry = IntVar()
            self.ispentry = DoubleVar()
            self.wetmassentry = DoubleVar()
            self.drymassentry = DoubleVar()
            self.shipispentry = DoubleVar()
            self.shipenginethrustentry = DoubleVar()
            self.shipfuelmassentry = DoubleVar()
            self.shipmassentry = DoubleVar()
            self.VelBox = Entry(groot, textvariable=self.Ventry, width= 47)
            self.VelBox.grid(row=1, column=1,columnspan=5 , sticky=W) # add length
            self.PRBox = Entry(groot, textvariable=self.PRdentry)
            self.PRBox.grid(row=2, column=1)
            self.MBox = Entry(groot, textvariable=self.Mdentry)
            self.MBox.grid(row=3, column=1)
            self.ABox = Entry(groot, textvariable=self.Adentry)
            self.ABox.grid(row=4, column=1)
            self.OBox = Entry(groot, textvariable=self.Odentry)
            self.OBox.grid(row=5, column=1)
            self.AtBox = Entry(groot, textvariable=self.Atdentry)
            self.AtBox.grid(row=6, column=1)
            self.PReBox = Entry(groot, textvariable=self.PReentry)
            self.PReBox.grid(row=2, column=3)
            self.MeBox = Entry(groot, textvariable=self.Meentry)
            self.MeBox.grid(row=3, column=3)
            self.AeBox = Entry(groot, textvariable=self.Aeentry)
            self.AeBox.grid(row=4, column=3)
            self.OeBox = Entry(groot, textvariable=self.Oeentry)
            self.OeBox.grid(row=5, column=3)
            self.AteBox = Entry(groot, textvariable=self.Ateentry)
            self.AteBox.grid(row=6, column=3)

            self.shipmassBox = Entry(groot, textvariable=self.shipmassentry)
            self.shipmassBox.grid(row=13, column=1)
            
            
            
            self.PrLab = Label(groot, text="x10^")
            self.PrLab.grid(row=2, column=2)
            self.MLab = Label(groot, text="x10^")
            self.MLab.grid(row=3, column=2)
            self.ALab = Label(groot, text="x10^")
            self.ALab.grid(row=4, column=2)
            self.OLab = Label(groot, text="x10^")
            self.OLab.grid(row=5, column=2)
            self.AtLab = Label(groot, text="x10^")
            self.AtLab.grid(row=6, column=2)

            


            

            

            #Label(self.groot, text = "",background='silver').grid(row=11, column = 1)
            self.LINELAB1 = Label(groot, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB1.grid(row=14, column=1, columnspan = 5) #row?
            
           # Label(self.groot, text = "",background='silver').grid(row=24, column = 1)
           # Label(self.groot, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver').grid(row=25, column=1, columnspan = 5)

            self.enterbutton.grid(row=1, column=4, sticky=W)
            self.entercorebutton.grid(row=2, column=4, sticky=W)
            self.entermassbutton.grid(row=3, column=4, sticky=W)
            self.enteraltbutton.grid(row=4, column =4, sticky=W)
            self.enterorbbutton.grid(row=5, column =4, sticky=W)
            self.enterathbutton.grid(row=6, column =4, sticky=W)
            self.enterincbutton.grid(row=7, column =4, sticky = W)
            self.buttonrun.grid(row=8, column=2, columnspan = 1)
            self.shiprunbutton.grid(row=12, column=1, columnspan = 2)
            self.resetdv.grid(row=9, column=4, columnspan = 2, sticky = W)
            self.changeposition.grid(row=8, column=3, columnspan = 2)
            self.crootwindowopen.grid(row = 25, column = 3, columnspan = 4, sticky = W)
            self.prootwindowopen.grid(row = 25, column = 1, columnspan = 4, sticky = W)
            self.frootwindowopen.grid(row = 25, column = 2, columnspan = 4, sticky = W)
            self.orootwindowopen.grid(row = 25, column = 4, columnspan = 4, sticky = W)
            
            #self.zoominbutton.grid(row=8, column=1, columnspan = 3)
            #self.zoomoutbutton.grid(row=8, column=3, columnspan = 1)
            self.resetbutton.grid(row=8, column=5, columnspan = 4, sticky = W)
            #self.resetcover.grid(row=8, column=5, columnspan = 4, sticky = W)
            self.entershipmass.grid(column=2, row=13, columnspan = 2, sticky = W)

            self.InclineSlide = Scale(groot, from_=-180, to=180,length=280 ,orient=HORIZONTAL)
            self.InclineSlide.grid(row = 7, column =1 , columnspan = 4, sticky = W)

            self.ZoomSlide = Scale(groot, from_=0, to=(100),length=130)
            self.ZoomSlide.grid(row = 1, column =5 , columnspan = 1, rowspan = 6, sticky = W)

            self.zoomlab = Label(groot, text = "ZOOM")
            self.zoomlab.grid(row = 7, column = 5)


            #Label(self.groot, text = "",background='silver').grid(row=8, column = 1)
            self.LINELAB2 =  Label(groot, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB2.grid(row=10, column=1, columnspan = 4)
            
            self.bodybutton.grid(row=11, column=3, columnspan = 1, sticky=W)
            
            self.calccombust = Button(groot, text = "Close", command = grootwindowclose)
            self.calccombust.grid(row = 25, column = 5, sticky = W)
            
            
            


            
            self.waitnes = Label(groot, text =("Calculating..."), background = 'silver')
            self.waitnes.grid(row = 9, column = 1, columnspan = 3)

            

            self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
            self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

            self.dvchangelab.grid(row = 9, column = 1, columnspan = 1, sticky = W)
            self.tdvchangelab.grid(row = 9, column = 2, columnspan = 2)

            self.dvchangelab.grid_remove()
            self.tdvchangelab.grid_remove()

            


            

            b = tkinter.tix.Balloon(groot) #BINDS BUTTON TO BALLOON
            

            b.bind_widget(self.enterbutton, balloonmsg='Set Velocity in Metres/Second')
            b.bind_widget(self.entercorebutton, balloonmsg='Set Body Diameter in Metres') #BIT FOR BUTTON NAMES
            b.bind_widget(self.entermassbutton, balloonmsg='Set Body Mass in Kilograms')
            b.bind_widget(self.enteraltbutton, balloonmsg='Set Spacecraft Altitude in Metres')
            b.bind_widget(self. enterorbbutton, balloonmsg='Set Orbit Apoapsis/Periapsis in Metres from Body Surface')
            b.bind_widget(self.enterathbutton, balloonmsg='Set Body Atmosphere in Metres')
            b.bind_widget(self.enterincbutton, balloonmsg='Set Inclination from Horizontal in degrees')
            b.bind_widget(self.buttonrun, balloonmsg='Run Simulation')
            b.bind_widget(self.shiprunbutton, balloonmsg='Run Ship Orbit')
            b.bind_widget(self.resetbutton, balloonmsg='Reset if error')
            b.bind_widget(self.bodybutton, balloonmsg='Click to Set Body')
            #b.bind_widget(self.zoominbutton, balloonmsg='Zooms in World')
           # b.bind_widget(self.zoomoutbutton, balloonmsg='Zooms out World')
            b.bind_widget(self.entershipmass, balloonmsg='Optional - Enter mass of Spacecraft')

            b.bind_widget(self.ZoomSlide, balloonmsg='Zoom In/Out')
            b.bind_widget(self.InclineSlide, balloonmsg='Drag to set Inclination')
            
            b.bind_widget(self.PrLab, balloonmsg='Multiply by 10 times exponent...') #Bit for labels
            b.bind_widget(self.MLab, balloonmsg='Multiply by 10 times exponent...')
            b.bind_widget(self.ALab, balloonmsg='Multiply by 10 times exponent...')
            b.bind_widget(self.OLab, balloonmsg='Multiply by 10 times exponent...')
            b.bind_widget(self.AtLab, balloonmsg='Multiply by 10 times exponent...')

            

            b.bind_widget(self.PRBox, balloonmsg='Decimal Entry, Recommend 3 S.F') #bit for float input boxes
            b.bind_widget(self.MBox, balloonmsg='Decimal Entry, Recommend 4 S.F.')
            b.bind_widget(self.ABox, balloonmsg='Decimal Entry')
            b.bind_widget(self.OBox, balloonmsg='Decimal Entry')
            b.bind_widget(self.AtBox, balloonmsg='Decimal Entry')
            b.bind_widget(self.planetcombobox, balloonmsg='Select Body to Orbit')
            b.bind_widget(self.shipmassBox, balloonmsg='Optional - Enter mass of Spacecraft in Tons')
            
            
            
            b.bind_widget(self.VelBox, balloonmsg='Velocity Entry (m/s)')

            b.bind_widget(self.PReBox, balloonmsg='Exponent Entry') #bit for int input boxes
            b.bind_widget(self.MeBox, balloonmsg='Exponent Entry')
            b.bind_widget(self.AeBox, balloonmsg='Exponent Entry')
            b.bind_widget(self.OeBox, balloonmsg='Exponent Entry')
            b.bind_widget(self.AteBox, balloonmsg='Exponent Entry')
            
            b.bind_widget(self.resetdv, balloonmsg='Resets Total Delta V to 0')
            b.bind_widget(self.changeposition, balloonmsg='Warp to opposite side of orbit')
            

         
            
            
            

            
            

            
            self.planetradius = 6370000
            self.planetname = "Earth"
            self.atmospheresize = 100000
            #Core Variables
            self.G = 6.673*10**-11 # THIS IS A CONSTANT!

            
            #User Defined - NEEDED FOR INTIAL FRAME
            self.E = 0
            
            self.UA= 300000
            self.M = 5.972*10**24
            self.V = 8000 #Must be above 0. Bad screen error at escape velocity.
            self.A=6678000 #MAKE THIS VALUE CHANGE DEPEND ON STARTING MODEL PLANET

            self.g = 9.8



            
            
            self.loopvalue = 0
            self.loopvaluechange = 100 #defualt = 100 REDUNDANT AS OF NOW, MAKE USE IN VARIABLE VCHANGE
            self.loopcurrent = 0
            self.looptime = 5
            self.changeamount = 100
           
            self.Vchange = 0
            self.Pchange = 0
            self.Mchange = 0
            self.Achange = 0
            self.Ichange = 0
            self.Atchange = 0
            
            self.Velfontsize = 12
            self.orbfontsize = 17
            self.Altfontsize = 11
            self.gfontsize = 9
            self.ifontsize = 8

            self.ArialBVel = tkinter.font.Font(family='Arial',size=self.Velfontsize, weight='bold')
            self.ArialBorb = tkinter.font.Font(family='Arial',size=self.orbfontsize, weight='bold')
            self.ArialBg = tkinter.font.Font(family='Arial',size=self.gfontsize, weight='bold')
            self.ArialBi = tkinter.font.Font(family='Arial',size=self.ifontsize, weight='bold')
            self.ArialBAlt = tkinter.font.Font(family='Arial',size=self.Altfontsize, weight='bold')

            
            self.totalVchange = 0
            self.totalPRchange = 0
            self.totalMchange = 0
            self.totalAchange = 0
            self.totalIchange = 0
            self.totalAtchange = 0

            self.shipmass = 0

            
            userchangeclean()
            self.oldVuserchange = 0
            self.oldPRuserchange = 0
            self.oldMuserchange = 0
            self.oldAuserchange = 0
            self.oldAtuserchange = 0
            self.oldIuserchange = 0
            self.notification=""

            self.miniplanet = 25


            
            

           
            self.first = 1
            

            


            self.banImage = PhotoImage(file="Banner.png")
            self.altImage = PhotoImage(file="AltBanner.png")
            self.FcImage = PhotoImage(file="AltBannerBot.png")
            self.shipImage = PhotoImage(file="apollopixelartsmall.png")
            self.incImage = PhotoImage(file="InclineLayerLight.png")

            

            

            self.smallban = self.w.create_image(-1000, -100,image=self.FcImage)
            self.smalltext = self.w.create_text(95,125, text = "")
            
            #self.V -= (self.Vchange - 1 )#Here to make intial frame
            #self.V -= 1
            

            self.intVchange = 0
            self.loopcurrent -= 1 #Here to make intial frame
            self.zoom = 1
            self.oldzoom = 1
            zoom()

            planetdetails()
            
            update_frame() #This calls back and redraws objects
            
            #RunBalloon(self.root) 
            
            
            self.root.mainloop()
        def SIGround( x, n):
            if n < 1:
                raise ValueError("number of significant digits must be >= 1")
            # Use %e format to get the n most significant digits, as a string.
            format = "%." + str(n-1) + "e"
            SIGreturn = format % x
            return float(SIGreturn)
            
        def userchangeclean():
            self.Vuserchange=0
            self.Auserchange=0
            self.Iuserchange=0
            self.Muserchange=0
            self.PRuserchange=0
            self.Atuserchange= 0
            
            self.oldVuserchange=0
            self.oldAuserchange=0
            self.oldIuserchange=0
            self.oldMuserchange=0
            self.oldPRuserchange=0
            self.oldAtuserchange=0
            self.spacecraftx = self.ovalheadway
            self.notification=""

      
                    

            #elif self.incline <= 0:
            #    self.incline + 360
              #  if self.incline <= 0:
                #    root.after(1, self.lowerincline)
    #
            
        
            
            
        def update_frame():
            #ADD IF LOOP > 1

            #self.Velfontsize = int((1.557 * (10 ** -7) * self.V ** 2) - (1.816 * (10 ** -3) * self.V) + 14.613)
            #self.gfontsize = 10 - int(round(self.g/100 , 0))


            #print (self.SIGround(123.456789, 4))
            #FOR SIG FIGURES

            

            
            
            
            self.w.delete("all")
            
            
            global A
            global S
            global V
            global loopvalue
            #print (self.Vchange)
           # print (self.intVchange)
            if self.intVchange == 0:
                if self.totalVchange <= 0:
                    self.Vchange = abs(self.Vchange)*-1
                else:
                    self.Vchange = abs(self.Vchange)
                    
                if self.totalPRchange <= 0:
                    self.Pchange = abs(self.Pchange)*-1
                else:
                    self.Pchange = abs(self.Pchange)
                    
                if self.totalMchange <= 0:
                    self.Mchange = abs(self.Mchange)*-1
                else:
                    self.Mchange = abs(self.Mchange)

                if self.totalAchange <= 0:
                    self.Achange = abs(self.Achange)*-1
                else:
                    self.Achange = abs(self.Achange)
                    
                if self.totalIchange <= 0:
                    self.Ichange = abs(self.Ichange)*-1
                else:
                    self.Ichange = abs(self.Ichange)
                    
                if self.totalAtchange <= 0:
                    self.Atchange = abs(self.Atchange)*-1
                else:
                    self.Atchange = abs(self.Atchange) #SHORTEN THIS MESS ELSE
                    
                self.intVchange = 1
            if self.oldVuserchange == 0:
                self.V = self.V
            else:
                
                self.V += self.Vchange
            
            if self.oldPRuserchange ==0:
                self.planetradius = self.planetradius
            else:
                self.planetradius += self.Pchange
                
            if self.oldMuserchange ==0:
                self.M = self.M
            else:
                self.M += self.Mchange
            if self.oldAuserchange ==0:
                self.UA = self.UA
            else:
                self.UA += self.Achange

            if self.oldIuserchange ==0:
                self.incline = self.incline
            else:
                self.incline += self.Ichange
                
            if self.oldAtuserchange ==0:
                self.atmospheresize = self.atmospheresize
            else:
                self.atmospheresize += self.Atchange

           # print(self.SIGround(self.M, 4))
            #print(self.SIGround(self.planetradius, 4))

           #JOOL, NEPTUNE AND DUNA DONT RECOGNISE
           
            if (SIGround(self.M, 4)) == 1.988 * 10 ** 30 and (SIGround(self.planetradius, 3)) == 695000000: 
                self.planetname = "Sun"
                self.planetcolor = "darkorange"
            elif (SIGround(self.M, 4)) == 3.302 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 2440000: 
                self.planetname = "Mercury"
                self.planetcolor = "gray"
            elif (SIGround(self.M, 4))  == 4.867 * 10 ** 24 and (SIGround(self.planetradius, 3)) == 6050000:
                self.planetname = "Venus"
                self.planetcolor = "Burlywood"
            elif (SIGround(self.M, 4)) == 5.972 * 10 ** 24 and (SIGround(self.planetradius, 3)) == 6370000: 
                self.planetname = "Earth"
                self.planetcolor = "green"
            elif (SIGround(self.M, 4)) == 7.348 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 1740000:
                self.planetname = "Moon"
                self.planetcolor = "dimgray"
            elif (SIGround(self.M, 4)) == 6.418 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 3390000:
                self.planetname = "Mars"
                self.planetcolor = "chocolate"
            elif (SIGround(self.M, 4)) == 1.898 * 10 ** 27 and (SIGround(self.planetradius, 3)) == 69900000:
                self.planetname = "Jupiter"
                self.planetcolor = "darkkhaki"
            elif (SIGround(self.M, 4)) == 5.683 * 10 ** 26 and (SIGround(self.planetradius, 3)) == 58200000:
                self.planetname = "Saturn"
                self.planetcolor = "khaki"
            elif (SIGround(self.M, 4)) == 8.681 * 10 ** 25 and (SIGround(self.planetradius, 3)) == 25400000:
                self.planetname = "Uranus"
                self.planetcolor = "powderblue"
            elif (SIGround(self.M, 4)) == 1.024 * 10 ** 26 and (SIGround(self.planetradius, 3)) == 24600000:
                self.planetname = "Neptune"
                self.planetcolor = "royalblue"
                
            elif (SIGround(self.M, 4)) == 1.756 * 10 ** 28 and (SIGround(self.planetradius, 3)) == 262000000:
                self.planetname = "Kerbol"
                self.planetcolor = "yellow"
            elif (SIGround(self.M, 4)) == 2.526 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 250000:
                self.planetname = "Moho"
                self.planetcolor = "Darkgoldenrod"
            elif (SIGround(self.M, 4)) == 1.224 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 700000:
                self.planetname = "Eve"
                self.planetcolor = "purple"
            elif (SIGround(self.M, 4)) == 1.242 * 10 ** 17 and (SIGround(self.planetradius, 3)) == 13000:
                self.planetname = "Gilly"
                self.planetcolor = "Navajowhite"
            elif (SIGround(self.M, 4))  == 5.292 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 600000: 
                self.planetname = "Kerbin"
                self.planetcolor = "forestgreen"
            elif (SIGround(self.M, 4)) == 9.76 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 200000:
                self.planetname = "Mun"
                self.planetcolor = "gray"
            elif (SIGround(self.M, 4)) == 2.646 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 60000:
                self.planetname = "Minmus"
                self.planetcolor = "Palegreen"
            elif (SIGround(self.M, 4)) == 4.515 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 320000:
                self.planetname = "Duna"
                self.planetcolor = "Sienna"
            elif (SIGround(self.M, 4)) == 2.782 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 130000:
                self.planetname = "Ike"
                self.planetcolor = "Dimgray"
            elif (SIGround(self.M, 4)) == 3.219 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 138000:
                self.planetname = "Dres"
                self.planetcolor = "Silver"
            elif (SIGround(self.M, 4)) == 4.233 * 10 ** 24 and (SIGround(self.planetradius, 3)) == 6000000:
                self.planetname = "Jool"
                self.planetcolor = "OliveDrab"
            elif (SIGround(self.M, 4)) == 2.939 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 500000:
                self.planetname = "Laythe"
                self.planetcolor = "SteelBlue"
            elif (SIGround(self.M, 4)) == 3.109 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 300000:
                self.planetname = "Vall"
                self.planetcolor = "Lightseagreen"
            elif (SIGround(self.M, 4)) == 4.233 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 600000:
                self.planetname = "Tylo"
                self.planetcolor = "Antiquewhite"
            elif (SIGround(self.M, 4)) == 3.726 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 65000:
                self.planetname = "Bop"
                self.planetcolor = "Maroon"
            elif (SIGround(self.M, 4)) == 1.081 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 44000:
                self.planetname = "Pol"
                self.planetcolor = "Moccasin"
            elif (SIGround(self.M, 4)) == 1.115 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 210000:
                self.planetname = "Eeloo"
                self.planetcolor = "Whitesmoke"

            
            else:
                self.planetname = "Custom"
                self.planetcolor = "SlateGray"

                
                            
            self.V = abs(self.V) #FORCE NON NEGATIVES
          #  print (self.Vchange)
           # print (self.intVchange)
           
            self.loopvaluechange = 0
            self.dM = self.M / 1000000000000000000000 #divide by a zetta THIS IS WRONG
            self.planetdiameter = self.planetradius * 2
            self.U = self.G*self.M
            self.A= self.planetradius+self.UA
            self.B = (2*self.A*self.U - self.A*(2*self.U - self.A * self.V ** 2))/(2*self.U - self.A * self.V ** 2)
            self.L = (self.A+self.B)/2
            self.S = 2*self.L/(self.canvasx-self.ovalheadway*2)
            self.planetsize = self.planetradius / self.S
            self.E = abs(self.L - self.A)
            self.H = (self.L**2 - self.E**2)** 0.5
            self.tH = self.H * math.cos(self.incline * (math.pi/180))
            #print (self.incline)
            #print (self.H)
            #print (self.tH, "TH")
            #self.Htest = ((((((self.L/2)**2)/self.L**2 )+ ((self.H)**2)))**0.5)
            #self.Htest = (((((((999999/2)*self.S)**2)/self.L**2 )+ (((self.canvasy/2)*self.S)**2)))**0.5)
            self.D =  self.L/self.tH
            self.OvalH = (self.canvasx-self.ovalheadway*2)/self.D
            self.T = (2*math.pi * ( ((self.L)) **3 / self.U )**0.5)
            self.Ec = self.E/self.L

            
            
                

            #print (self.T, "PEROID")
            #print (self.B)
            ##print (self.A)
            #print (self.U)

            self.miniplanet = self.planetradius/ (self.L / 55)
            

            #self.SOI = 384400*((5.972 * 10 **24 )/(1.989* 10 **30))** 0.4
            #print (self.SOI)
            
            self.g = (self.G * self.M)/(self.A**2)
            self.shipg = self.g
            self.eV = ((2*self.G*self.M)/self.A)**0.5

            self.Fc = (self.shipmass * self.shipg) *1000 # in N
            

            if self.Fc != 0:
                self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)

            
            if self.A>=self.B:
                self.apov = "Periapsis="
                self.periv = "Apoapsis="
            else:
                self.apov = "Apoapsis="
                self.periv = "Periapsis="
            #CONIC FOR SHIP
                
      
            
            
            
            # ADD THIS BACK FOR ROCKET IMAGE- WONT USE PIL :(
        
            
            

            

            #Label(self.groot, text=("Gravational_Constant"),background='silver').grid(row=14, column = 3, sticky=W)
            #Label(, text=("Altitude_to_surface"),background='silver').grid(row=15, column = 3, sticky=W)
            #Label(self.groot, text=("Altitude"),background='silver').grid(row=16, column = 3, sticky=W)
            #Label(self.groot, text=("Mass_of_Body"),background='silver').grid(row=17, column = 3, sticky=W)
            #Label(self.groot, text=("Velocity"),background='silver').grid(row=18, column = 3, sticky=W)
            #Label(self.groot, text=("Gravational_Parameter"),background='silver').grid(row=19, column = 3, sticky=W)
            #Label(self.groot, text=("Value_of_Apo/Peri"),background='silver').grid(row=20, column = 3, sticky=W)
            #Label(self.groot, text=("SemiMajor_Axis"),background='silver').grid(row=21, column = 3, sticky=W)
            #Label(self.groot, text=("Focal_Length"),background='silver').grid(row=22, column = 3, sticky=W)
            #Label(self.groot, text=("SemiMinor_Axis"),background='silver').grid(row=23, column = 3, sticky=W)

            #self.sp.grid_remove()

            #self.n = (self.M/self.L**3)**0.5

            #print (self.n, "N")

            #self.idv = (2 * math.sin((10 / 57.3)/2)* ((1-(self.E/self.L)**2)**0.5) * math.cos(180 / 57.3)*self.L * self.n) / (1 + (self.E/self.L)* math.cos(0) )
            #print (self.idv, "idv")

            

            

            #LAYERING 

            
           # Label(self.groot, text=(self.D,"Altitude to surface"),background='silver').grid(row=24)
            
            #print (self.canvasy/2, "canvas")
            #print (self.G, "Gravational Constant")
            #print (self.UA, "Altitude to surface")
            #print (self.A, "Altitude to centre of body")background='sbackground='silver'ilver'
            #print (self.M, "Mass of body")
            #print (self.V, "Velocity")
            #print (self.U, "Gravational Parameter")
            #print (self.B, "Value of apo/peri")
            #print (self.L, "Addendum)
            #print (self.E, "Focal length")
            #print (self.H, "Orbit height")              #KEEP THIS HERE BECAUSE I FORGET :P
            #print (self.D, "Ratio between Orbit length vs height")
            #print (self.OvalH, "Oval height value")
            #print (self.S, "Scale down value")
            #print (self.planetsize, "Size of scale planet")
            #print ("loop test check")
            self.ox1 = self.ovalheadway
            self.oy1 = self.canvasy/2 - self.OvalH/2
            self.ox2 = self.canvasx - self.ovalheadway #STICK THIS BACK INTO CODE
            self.oy2 = self.canvasy/2 + self.OvalH/2
            self.spacecraftx = self.ovalheadway
            self.spacecrafty2 = self.canvasy/2
           # print ("RESET") #ISSUE WITH SELF.H, Self.L < self. A

           
           # print (self.OvalH, "O")
           # print (self.OvalH/2, "OH")

           # print ((self.canvasx-self.ovalheadway*2)/self.D, "OHHH")
           # print ((self.canvasx-self.ovalheadway*2), "OHHHHHH")
           # print (self.D, "OHHH")
            
           # print (self.H, "H")
           # print ((self.L**2 - self.E**2)** 0.5,"HH")
         #3   print ((self.L**2 - self.E**2),"HHH")
         ##   print ((self.L**2 - self.E**2)** 0.5,"HH")
          #  print (self.L, "L")
         #  print (self.E, "E")
          #  print (self.L - self.A, "CHECL")
          #  print (self.A, "LEL")
           # print (self.planetradius, "PR")
           # print (self.UA, "LELO")


           # print (self.H, "REAL")

           # print (self.ox1, "ox1")
            #print (self.oy1)
            #print (self.ox2, "ox2")
           # print (self.oy2)

            
        
            
            self.athoval = self.w.create_oval(self.ovalheadway + (self.UA-self.atmospheresize)/self.S,self.canvasy/2 - self.planetsize - self.atmospheresize/self.S,self.ovalheadway + (self.UA+self.atmospheresize)/self.S + 2 * self.planetsize,self.canvasy/2 + self.planetsize + self.atmospheresize/self.S, fill = "skyblue", outline = "") #Athmosphere
            self.planet = self.w.create_oval(self.ovalheadway + self.UA/self.S,self.canvasy/2 - self.planetsize,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize,self.canvasy/2 + self.planetsize, fill = self.planetcolor , outline = "") #Planet
            self.w.create_oval(self.ovalheadway + self.A - self.planetradius/10, self.canvasy/2 - self.planetradius/10,self.ovalheadway + self.UA + self.A + self.planetradius/10,self.canvasy/2 + self.planetradius/10, fill = 'red' , outline = "") #Planetcaps
            self.arc1 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit\
            self.arc2 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  -180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit\
            #self.w.create_oval(self.ox1,self.oy1,self.ox2,self.oy2,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3) # Orbit\
            print (self.incline)
            if self.B >= self.planetradius:
                if ((self.incline) <= -90 and (self.incline) >= -180):
                    self.w.tag_raise(self.arc1)
                    print ("MW543E")
                    self.w.tag_lower(self.arc2)

                elif ((self.incline) <= 0 and (self.incline) >= -90):
                    self.w.tag_raise(self.arc2)
                    print ("MW543E")
                    self.w.tag_lower(self.arc1)
                    
              #  elif (-1*((self.incline) >= 0 and (self.incline) >= -90)):
                #    self.w.tag_raise(self.arc2)
                 #   print ("MWE")
                  #  self.w.tag_lower(self.arc1)

                elif (((self.incline) >= 0 and (self.incline) <= 90)):

                    self.w.tag_raise(self.arc1)
                    print ("ME")
                    self.w.tag_lower(self.arc2)

                elif (((self.incline) >= 90 and (self.incline) <= 180)):
                    self.w.tag_raise(self.arc2)
                    print ("MW544353E")
                    self.w.tag_lower(self.arc1)
                    
                    
                

            
                    
            else:
                self.w.tag_lower(self.arc1)
                self.w.tag_lower(self.arc2)

            self.w.tag_lower(self.athoval)
                

    #INCLINE PLANET #MAKE IT REPOSITONABLE BASED ON THINGS LIKE SCREENSIZE< ALSO MAKE TI RESIZE

            #(55 * math.sin (self.incline)) ADD COSINE CHANGE TO X BIT

            #self.w.create_rectangle( self.canvasx - 50, self.canvasy - 50, self.canvasx - 200, self.canvasy -200, fill = "white") #Make this a funky futuristic image

            #self.w.create_oval(self.canvasx - 100, self.canvasy -100 , self.canvasx - 150, self.canvasy -150, fill = self.planetcolor)
            #self.w.create_line(self.canvasx - 125 +  (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) + (55 * ( math.sin (self.incline *( math.pi/180)))) , self.canvasx - 125 - (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) - (55 * ( math.sin (self.incline *( math.pi/180)))), fill = "dodgerblue" , width = 3)
            #self.w.create_text (self.canvasx - 100, self.canvasy -200 , text = self.incline)
            
    #BASELINES   
            
            self.w.create_line(self.ovalheadway, self.canvasy  - self.canvasy/100, self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy  - self.canvasy/100, width = 10, fill = "gray") #Baseline for planet
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100 - 80, self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100 - 80, width = 10, fill = "darkgray") # BaselineOpposing Ship
            self.w.create_line(self.ovalheadway, self.canvasy - self.canvasy/100 - 40, self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy - self.canvasy/100 - 40, width = 10, fill = "darkgray") #Baseline With ship
    #UP LINES
            
            self.w.create_line(self.ovalheadway, self.canvasy - self.canvasy/100, self.ovalheadway, self.canvasy  - self.canvasy/100- 60, width = 5, fill = "silver")# Ship/ Orbit Start
            self.w.create_line(self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100, self.canvasx - self.ovalheadway, self.canvasy  - self.canvasy/100- 100, width = 5, fill = "silver")# Orbit End
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100, self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100- 100, width = 5, fill = "lightgray") #Panet cen
            self.w.create_line(self.ovalheadway + self.UA/self.S, self.canvasy - self.canvasy/100, self.ovalheadway + self.UA/self.S, self.canvasy - self.canvasy/100- 20, width = 5, fill = "black") #Planet line start
            self.w.create_line(self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy - self.canvasy/100,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy- self.canvasy/100- 20, width = 5, fill = "black") #Planet line end
    #TRUE BASELINE
            self.w.create_line(self.ovalheadway, self.canvasy  - self.canvasy/100, self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100, width = 10, fill = "gray") #Baseline
            #CHANGE ORDER OF RENDERING, GETTING BASES ABOUT LINES
            self.w.create_image(self.canvasx - 95, 75,image=self.banImage) #Banner
            self.w.tag_raise(self.smallban)
            self.w.tag_raise(self.smalltext)
            self.w.create_image(95, 65,image=self.altImage) #MOVE THESE UP


            

            

            

            #DIAG ONES
            #self.w.create_text(200 + self.x,10 + self.y, text=(self.G,"     Gravational Constant"))
            #self.w.create_text(200 + self.x,20+ self.y, text=(self.UA, "    Radar Altitude"))
            #self.w.create_text(200 + self.x,30 + self.y, text=(self.A, "     True Altitude"))
            #self.w.create_text(200 + self.x,40 + self.y, text=(self.M, "       Planet Mass"))
            #self.w.create_text(200  + self.x,50 + self.y, text=(self.V, "     Velocity"))
            ##self.w.create_text(200 + self.x,60 + self.y, text=(self.U, "       Gravational Parameter"))
            #self.w.create_text(200 + self.x,70 + self.y, text=(self.B, "      Planet Centre to end of orbit"))
            #self.w.create_text(200 + self.x,80 + self.y, text=(self.L, "      Semi-Major Axis"))
            #self.w.create_text(200 + self.x,90 + self.y, text=(self.E, "           Focal Length"))
            #self.w.create_text(200 + self.x,100 + self.y, text=(self.H, "       Semi-Minor Axis"))
            #self.w.create_text(200 + self.x,110 + self.y, text=(self.D, "        Ratio Between Orbit length vs height"))
            #self.w.create_text(200 + self.x,120 + self.y, text=(self.OvalH, "      Height of ellipse"))
            #self.w.create_text(200 + self.x,130 + self.y, text=(self.S, "      Scale down value"))
            #self.w.create_text(200 + self.x,self.dvLab = Label140 + self.y, text=(self.planetsize, "          Size of planetradius"))
            ##self.w.create_text(200 + self.x,160 + self.y, text=(self.g, "          Gravational Acceleration"))
            #self.w.create_text(200 + self.x,170 + self.y, text=(self.eV, "          Escape Velocity"))

            self.w.create_oval(self.ovalheadway + self.UA/self.S + self.planetsize + 10, self.canvasy/2  + 10,self.ovalheadway + self.UA/self.S + self.planetsize - 10, self.canvasy/2  - 10,fill="maroon", outline = '')

            
            self.w.create_text(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy/2 + 20 , text=self.planetname, font = self.ArialBVel) #planetname

            #print (self.ovalheadway + self.UA/self.S + self.planetsize  + self.x)


            #if (self.ovalheadway + self.UA/self.S + self.planetsize  + self.x) >= (self.canvasx/2):
                #self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  + self.x
            self.planetdetailsy = (self.canvasy / (self.planetsize / 1300 + 2)) -  80
       

            #else:
                
                #self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  + self.x + 150
                #self.planetdetailsy = self.canvasy/2 + self.y - self.planetsize*1.3 + self.planetsize - 50


            self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  - self.planetsize/4 + 100 # CHAGNE LAST VALUE LESSE AGGRESSIVE


            
            
            self.w.create_text(self.planetdetailsx, self.planetdetailsy - 20, text=("Mass=",(SIGround(self.dM, 4)), "Zkg"), font = self.ArialBg) #planetdetails
            self.w.create_text(self.planetdetailsx, self.planetdetailsy, text=("Planet_Diameter=",int(self.planetdiameter), "m"), font = self.ArialBg) #planetdetails
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize  , self.canvasy/2  - 20, self.planetdetailsx, self.planetdetailsy + 10 , width = 1) #TO PLANETDETAILS

            
            self.w.create_text(self.canvasx/2  , self.canvasy  - self.canvasy/100 - 10 , text=("Orbit_length=", int(2*self.L), "m"), font = self.ArialBg) #orbit text
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize)/2 + self.ovalheadway/2  , self.canvasy  - self.canvasy/100 - 50 , text = (self.periv , self.A,"m"), font = self.ArialBg) #A
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize + self.canvasx - self.ovalheadway)/2  , self.canvasy  - self.canvasy/100 - 90 , text = (self.apov,int(self.B),"m"), font = self.ArialBg) # B
            self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes it doubles up ssh, make font settings go on both
            #MAKE THOSE NOT BE SO STATIC AND CHANGABLE DEPENDING ON VARAIBLE CHANGE
            # PROPER ONES

            if self.V >= 100000000:
                self.VELread = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(Mm/s)=", (round(self.V/1000000,2))), font=self.ArialBVel)
            elif self.V >= 100000:
                self.VELread = self.w.create_text(self.canvasx-79  ,50 , text=("Velocity(km/s)=", (round(self.V/1000,1))), font=self.ArialBVel)
            else:
                self.VELread = self.w.create_text(self.canvasx-79 ,50 , text=("Velocity(m/s)=", int(round(self.V,0))), font=self.ArialBVel)
            
            
            if self.A >= 1000000000:
                 self.ALTread = self.w.create_text(79  ,60 , text=("Altitude(Mm)=", int(round(self.A/1000000,0))), font=self.ArialBAlt)
            elif self.A >= 1000000:
                 self.ALTread = self.w.create_text(79 ,60 , text=("Altitude(km)=", int(round(self.A/1000,0))), font=self.ArialBAlt)
            else:
                 self.ALTread = self.w.create_text(79  ,60, text=("Altitude(m)=", int(round(self.A,0))), font=self.ArialBAlt)

            
            if self.g >= 10000:
                self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.g/1000,2)),font=self.ArialBg)
            else:
                self.gread= self.w.create_text(self.canvasx-53,95 , text=("Grav(m/s)=", round(self.g,2)),font=self.ArialBg)
           # self.w.create_text(self.canvasx-53 + ,195 + self.y, text=("Cp Force(Nm^2/kg^2)=", round(self.Fn,2)),font=self.ArialBg)
            self.shipdraw = self.w.create_image(self.spacecraftx, self.spacecrafty2,image=self.shipImage)



            #INCLINE PLANET

            #(55 * math.sin (self.incline)) ADD COSINE CHANGE TO X BIT DONE. NOW MAKE PLANET CHANGE IN SIZE

            self.inclayers = self.w.create_image(self.canvasx - 85, self.canvasy - 137,image=self.incImage)

            self.w.create_text(self.canvasx -125, self.canvasy - 218,text = "Orbital Inclination",  font = self.ArialBorb)

            #self.w.create_rectangle( self.canvasx - 50, self.canvasy - 50, self.canvasx - 200, self.canvasy -200, fill = "white") #Make this a funky futuristic image

            #self.tri1 = self.canvasx - 125 +  (40 * ( math.cos (self.incline *( math.pi/180))))
            #self.tri2 = (self.canvasy -125) + (40 * ( math.sin (self.incline *( math.pi/180))))
            #self.tri3 = self.canvasx - 125 +  (30 * ( math.cos (self.incline *( math.pi/180))))self.tri4 = (self.canvasy -125) + (20 * ( math.sin (self.incline *( math.pi/180))))
            #self.tri1 = self.canvasx - 125 +  (40 * ( math.cos (self.incline *( math.pi/180))))
           # self.tri2 = (self.canvasy -125) + (40 * ( math.sin (self.incline *( math.pi/180))))
            #self.theta1 = math.asin (10/30) + (self.incline *( math.pi/180))
           # self.theta2 = math.asin (-10/30) + (self.incline *( math.pi/180))
            #self.hypot = (10**2 + 30**2)**0.5
           # print (self.hypot)
           # print (self.theta1)
           # self.tri3 = self.canvasx - 125 +  (self.hypot * ( math.cos (self.theta1)))
           # self.tri4 = (self.canvasy -125) + (self.hypot * ( math.sin (self.theta1)))
            #self.tri5 = self.canvasx - 125 +  (self.hypot * ( math.cos (self.theta2)))
           # self.tri6 =  (self.canvasy -125) + (self.hypot * ( math.sin (self.theta2)))
            #if int(abs(self.dvchange)) != 0:
             #   self.w.create_text(self.canvasx/2, self.canvasy/2 + 100, text = ("F=",int(abs(self.dvchange)),"m/s"), font = self.ArialBVel)

            #if int(abs(self.tdvchange)) != 0:
            #self.w.create_text(self.canvasx/2, self.canvasy/2 + 150, text = ("tdV_Change=",int(abs(self.tdvchange)),"m/s"), font = self.ArialBVel)
            

            self.w.create_oval(self.canvasx - 125+ self.miniplanet, self.canvasy -125 + self.miniplanet, self.canvasx - 125- self.miniplanet, self.canvasy -125 - self.miniplanet, fill = self.planetcolor, outline = "white")
            self.w.create_arc(self.canvasx - 85, self.canvasy -85 , self.canvasx - 165, self.canvasy -165, extent = -1 * self.incline, width = 2, style = ARC)
            self.w.create_line(self.canvasx - 200, self.canvasy -125, self.canvasx - 50, self.canvasy -125, width = 3, fill = "darkred", dash = (20,5))
            self.w.create_line(self.canvasx - 125 +  (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) + (55 * ( math.sin (self.incline *( math.pi/180)))) , self.canvasx - 125 - (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) - (55 * ( math.sin (self.incline *( math.pi/180)))), fill = "dodgerblue" , width = 3)
            #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4 + 10,self.tri3 , self.tri4 - 10, width = 100, fill="red")
            #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4,self.tri5, self.tri6, width = 100, fill="steelblue")
            self.w.create_polygon(self.canvasx - 125 +  (40 * ( math.cos (self.incline *( math.pi/180)))),(self.canvasy -125) + (40 * ( math.sin (self.incline *( math.pi/180)))),self.canvasx - 125 +  ((10**2 + 30**2)**0.5 * ( math.cos (math.asin (10/30) + (self.incline *( math.pi/180))))),(self.canvasy -125) + ((10**2 + 30**2)**0.5 * ( math.sin (math.asin (10/30) + (self.incline *( math.pi/180))))),self.canvasx - 125 +  ((10**2 + 30**2)**0.5 * ( math.cos (math.asin (-10/30) + (self.incline *( math.pi/180))))), (self.canvasy -125) + ((10**2 + 30**2)**0.5* ( math.sin (math.asin (-10/30) + (self.incline *( math.pi/180))))), width = 100, fill="royalblue")
            self.w.create_polygon(self.canvasx -125, self.canvasy -125 - self.miniplanet,self.canvasx -130, self.canvasy -140 - self.miniplanet,self.canvasx -120, self.canvasy -140 - self.miniplanet, fill="maroon")
            self.w.create_polygon(self.canvasx -125, self.canvasy -125 + self.miniplanet,self.canvasx -130, self.canvasy -110 + self.miniplanet,self.canvasx -120, self.canvasy -110 + self.miniplanet, fill="maroon")

            #self.w.create_polygon((0, 200, 50, 0, 100, 100), fill="red")
            self.w.create_text (self.canvasx - 170, self.canvasy -56 , text =("Orbital Inclination ="), justify = LEFT, font = self.ArialBi)
            self.w.create_text (self.canvasx - 100, self.canvasy -56 , text =((-1 *( round(self.incline, 1)))), justify = LEFT, font = self.ArialBi)

            
            

            
            self.loopcurrent += 1
            #print (self.loopcurrent)
            
            if self.loopcurrent <= abs(self.loopvalue)-1:
                
                self.root.after(self.looptime, update_frame)
            else:
                self.loopvalue = 0
                self.loopcurrent = 0
                self.enterbutton.configure (state = NORMAL)
                self.entercorebutton.configure (state = NORMAL)
                self.entermassbutton.configure (state = NORMAL)
                self.enteraltbutton.configure (state = NORMAL)
                self.enterorbbutton.configure (state = NORMAL)
                self.enterathbutton.configure (state = NORMAL)
                self.enterincbutton.configure (state = NORMAL)
                self.buttonrun.configure (state = NORMAL)
                self.shiprunbutton.configure (state = NORMAL)
                self.resetbutton.configure (state = NORMAL)
                self.bodybutton.configure (state = NORMAL)
                self.ZoomSlide.configure (state = NORMAL)
                self.InclineSlide.configure (state = NORMAL)
                self.entershipmass.configure (state = NORMAL)
                self.resetdv.configure(state = NORMAL)


                #
                

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()
                
                print (self.dvchange, "DV")

                

                print (self.tdvchange, "DV")

                print (self.incline)

                

                
                userchangeclean()

                if self.prootopen == 1:
                    self.sua =Label(self.proot, text=(round((self.UA),1),"m"))
                    self.sua.grid(row=2, column = 1, sticky=W, columnspan = 3)
                    self.sa =Label(self.proot, text=(round((self.A),1),"m"))
                    self.sa.grid(row=3, column = 1, sticky=W, columnspan = 3)
                    self.sm =Label(self.proot, text=(round((self.M),1),"kg"))
                    self.sm.grid(row=4, column = 1, sticky=W, columnspan = 3)
                    self.sv =Label(self.proot, text=(round((self.V),1),"m/s")) 
                    self.sv.grid(row=5, column = 1, sticky=W, columnspan = 3)
                    self.su =Label(self.proot, text=(round((self.U),1),"m^3/s"))
                    self.su.grid(row=6, column = 1, sticky=W, columnspan = 3)
                    self.sb =Label(self.proot, text=(round((self.B),1),"m"))
                    self.sb.grid(row=7, column = 1, sticky=W, columnspan = 3)
                    self.sl =Label(self.proot, text=(round((self.L),1),"m"))
                    self.sl.grid(row=8, column = 1, sticky=W, columnspan = 3)
                    self.se =Label(self.proot, text=(round((self.E),1),"m"))
                    self.se.grid(row=9, column = 1, sticky=W, columnspan = 3)
                    self.sh =Label(self.proot, text=(round((self.H),1),"m"))
                    self.sh.grid(row=10, column = 1, sticky=W, columnspan = 3)
                    self.sp =Label(self.proot, text= (round((self.T),1),"s"))
                    self.sp.grid(row=11, column = 1, sticky=W, columnspan = 3)
                    self.sd =Label(self.proot, text= (round((self.Ec),1)))
                    self.sd.grid(row=12, column = 1, sticky=W, columnspan = 3)
                   
                    
                    
                    self.suat =Label(self.proot, text=("Radar Altitude"))
                    self.suat.grid(row=2, column = 3, sticky=W, columnspan = 3)
                    self.sat =Label(self.proot, text=("Altitude"))
                    self.sat.grid(row=3, column = 3, sticky=W, columnspan = 3)
                    self.smt =Label(self.proot, text=("Body Mass"))
                    self.smt.grid(row=4, column = 3, sticky=W, columnspan = 3)
                    self.svt =Label(self.proot, text=("Spacecraft Velocity"))
                    self.svt.grid(row=5, column = 3, sticky=W, columnspan = 3)
                    self.sut =Label(self.proot, text=("Gravational Parameter"))
                    self.sut.grid(row=6, column = 3, sticky=W, columnspan = 3)

                    if self.A >= self.B:
                        self.sbt =Label(self.proot, text=("Value of Periapsis"))

                    else:
                        self.sbt =Label(self.proot, text=("Value of Apoapsis"))
                    self.sbt.grid(row=7, column = 3, sticky=W, columnspan = 3)
                    self.slt =Label(self.proot, text=("Semi-Major Axis"))
                    self.slt.grid(row=8, column = 3, sticky=W, columnspan = 3)
                    self.set =Label(self.proot, text=("Focal Length"))
                    self.set.grid(row=9, column = 3, sticky=W, columnspan = 3)
                    self.sht =Label(self.proot, text=("Semi-Minor Axis"))
                    self.sht.grid(row=10, column = 3, sticky=W, columnspan = 3)
                    self.spt =Label(self.proot, text=("Orbital Period"))
                    self.spt.grid(row=11, column = 3, sticky=W, columnspan = 3)
                    self.sdt =Label(self.proot, text=("Eccentricity"))
                    self.sdt.grid(row=12, column = 3, sticky=W, columnspan = 3)

                    db = tkinter.tix.Balloon(groot)


                    db.bind_widget(self.suat, balloonmsg='Altitude above Body Surface')
                    
                    db.bind_widget(self.smt, balloonmsg='Body Mass')
                    db.bind_widget(self.svt, balloonmsg='Velocity of Spacecraft')
                    db.bind_widget(self.sut, balloonmsg='Gravational Parameter')
                    if self.A >= self.B:
                        db.bind_widget(self.sbt, balloonmsg='Height of Periapsis')
                        db.bind_widget(self.sat, balloonmsg='Altitude from Body Centre. Also height of Apoapsis')

                    else:
                        db.bind_widget(self.sbt, balloonmsg='Height of Apoapsis')
                        db.bind_widget(self.sat, balloonmsg='Altitude from Body Centre. Also height of Periapsis')
                        
                    
                    db.bind_widget(self.slt, balloonmsg='Half the distance of the longest part of the Orbit')
                    db.bind_widget(self.set, balloonmsg='Distance from the middle of the Orbit from the centre of the Body')
                    db.bind_widget(self.sht, balloonmsg='Half the distance of the shortest part of the Orbit')
                    db.bind_widget(self.spt, balloonmsg='Time it takes to comeplete one Orbit (in seconds)')
                    db.bind_widget(self.sdt, balloonmsg='Eccentrictiy of the Orbit')

                    

                    



                   

                    

                    

                    
                    self.waitmes.grid_remove()
                

                if self.first != 1:
                
                    


                    self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
                    self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

                    self.dvchangelab.grid(row = 9, column = 1, columnspan = 1, sticky = W)
                    self.tdvchangelab.grid(row = 9, column = 2, columnspan = 2, sticky = W)

                    sb = tkinter.tix.Balloon(groot)

                    sb.bind_widget(self.dvchangelab, balloonmsg='Delta V change of previous manoeuvre')
                    sb.bind_widget(self.tdvchangelab, balloonmsg='Total Delta V change')
                    
                   
                    
                    self.resetbutton.configure(background = 'silver', foreground = 'silver',borderwidth=0, state = DISABLED,disabledforeground='silver')
                else:
                    self.first += 1
                
                self.waitnes.grid_remove()
            
            
            
            
            
        def orbitcalccommand():
            global orbitcalcopen
            print (orbitcalcopen)
            if orbitcalcopen == 0:
                
                
                orbitcalcopen = 1
                
                
                
                orbitcalc()
                
            else:
                print ("nope")
        def orbittutcommand():
            print ("learn skrub")
  
        orbitopen = Button(groot, text="Open Calculator", command=orbitcalccommand)
        orbitopen.grid(row = 1, column = 1)
        tutopen = Button(groot, text="Open Tutorial - Not Currently Added", command=orbittutcommand)
        tutopen.grid(row = 2, column = 1)
     

        groot.mainloop()

 
app=App(groot)

