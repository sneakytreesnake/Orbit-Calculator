from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font

import math
from math import log10, floor
import webbrowser
import re
import time


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
#Inclination board is not generating correct values for linelength and maybe mini planet FIXSED
#DONT SHRINK DONE
#Make inclination window work different, make orbit smaller when planet sets certain size
#add one more layer of rounding on HUD DONE
#Make a minimum yres DONE
#word ecentricity better DONE
#Balance ship speed DONE
#Maybe make option menu close when openning script, probably not though DONE



#SCRAPPED

#SOI RADIUS - TOO MANY USERS VARIBALES NEEDED AND MUCH MORE COMPLICATED THAN IT NEEDS TO BE
#add orbital velocity to gloassary WONT NEED
#Make inclination middle of page and offset to work with all screensizes and inimize overlap - too much time needed to recode it
#SOMEHOPW MAKE ORBIT CHANGES JUMP GAP FROM 180 to -180
#Make ship crash into planet - cant figure out a way to make it solve equations for itself. Also difficult as canvas isnt a graphics calculator
#Make Windows not have close button at top - NOT POSSIBLE WITHOUT MAKING OBJECTS APPEAR ON TASKBAR, ALSO WINDOWS EXCLUSIVE




#WORK BOARD
#MAKE TUTORIAL DAMNIT
#Bug check
#Read over explanations for mistakes
#get people to bug test and critique tutorial, dont have time to change much else.

#BUG BOARD
#Screen error when reasching far side of orbit with certain higher zoom levels at lower resolutions (<1080p)
#Orbital period may be inacccurate, calculations  are correct but im not sure.



            
groot = tkinter.Tk()
groot.wm_title("Menu")
groot.resizable(0,0)




groot.configure(background = 'silver')
orbitcalcopen = 0
reschange = 0
fullscreen = 0

#message = Toplevel()
#message.wm_title("README")
#Label(message, text = "Do not click the red cross to close a window.").grid(row= 1)
#Label(message, text = "Please select 'Close' instead. Only click the").grid(row= 2)
#Label(message, text = "red cross if you want to close the script entirely.").grid(row= 3)
#Label(message, text = "Thank You.").grid(row= 4)

#def closemessage():
#    message.destroy()

#sButton(message, text = "Close", command = closemessage).grid(row = 5)

global credrootwindow

t1 = time.time()

benchroot = Toplevel()
benchroot.wm_title("Benchmark")

Label(benchroot, text = ("Startup benchmark started.") ).grid(row=1)
Label(benchroot, text = ("Level 1. 2 ** 1 =" , (2 ** 1) )).grid(row=1)
Label(benchroot, text = ("Level 2. 2 ** 2 =" , (2 ** 2))).grid(row=1)
Label(benchroot, text = ("Level 3. 2 ** 3 =" , (2 ** 3))).grid(row=1)
Label(benchroot, text = ("Level 4. 2 ** 4 =" , (2 ** 4))).grid(row=1)
Label(benchroot, text = ("Level 5. 2 ** 5 =" , (2 ** 5))).grid(row=1)
Label(benchroot, text = ("Level 6. 2 ** 6 =" , (2 ** 6))).grid(row=1)
Label(benchroot, text = ("Level 7. 2 ** 7 =" , (2 ** 7))).grid(row=1)
Label(benchroot, text = ("Level 8. 2 ** 8 =" , (2 ** 8))).grid(row=1)
Label(benchroot, text = ("Level 9. 2 ** 9 =" , (2 ** 9))).grid(row=1)
Label(benchroot, text = ("Level 10. 2 ** 10 =" , (2 ** 10))).grid(row=1)
Label(benchroot, text = ("Level 11. 2 ** 11 =" , (2 ** 11))).grid(row=1)
Label(benchroot, text = ("Level 12. 2 ** 12 =" , (2 ** 12))).grid(row=1)
Label(benchroot, text = ("Level 13. 2 ** 13 =" , (2 ** 13))).grid(row=1)
Label(benchroot, text = ("Level 14. 2 ** 14 =" , (2 ** 14))).grid(row=1)
Label(benchroot, text = ("Level 15. 2 ** 15 =" , (2 ** 15))).grid(row=1)
Label(benchroot, text = ("Level 16. 2 ** 16 =" , (2 ** 16))).grid(row=1)
Label(benchroot, text = ("Level 17. 2 ** 17 =" , (2 ** 17))).grid(row=1)
Label(benchroot, text = ("Level 18. 2 ** 18 =" , (2 ** 18))).grid(row=1)
Label(benchroot, text = ("Level 19. 2 ** 19 =" , (2 ** 19))).grid(row=1)





Label(benchroot, text = ("Level 20. 2 ** 20 =" , (2 ** 20))).grid(row=1)
Label(benchroot, text = ("Level 21. 2 ** 21 =" , (2 ** 21))).grid(row=1)
Label(benchroot, text = ("Level 22. 2 ** 22 =" , (2 ** 22))).grid(row=1)
Label(benchroot, text = ("Level 23. 2 ** 23 =" , (2 ** 23))).grid(row=1)
Label(benchroot, text = ("Level 24. 2 ** 24 =" , (2 ** 24))).grid(row=1)
Label(benchroot, text = ("Level 25. 2 ** 25 =" , (2 ** 25))).grid(row=1)
Label(benchroot, text = ("Level 26. 2 ** 26 =" , (2 ** 26))).grid(row=1)
Label(benchroot, text = ("Level 27. 2 ** 27 =" , (2 ** 27))).grid(row=1)
Label(benchroot, text = ("Level 28. 2 ** 28 =" , (2 ** 28))).grid(row=1)
Label(benchroot, text = ("Level 29. 2 ** 29 =" , (2 ** 29))).grid(row=1)
Label(benchroot, text = ("Level 30. 2 ** 30 =" , (2 ** 30))).grid(row=1)
Label(benchroot, text = ("Level 31. 2 ** 31 =" , (2 ** 31))).grid(row=1)
Label(benchroot, text = ("Level 32. 2 ** 32 =" , (2 ** 32))).grid(row=1)
Label(benchroot, text = ("Level 33. 2 ** 33 =" , (2 ** 33))).grid(row=1)
Label(benchroot, text = ("Level 34. 2 ** 34 =" , (2 ** 34))).grid(row=1)
Label(benchroot, text = ("Level 35. 2 ** 35 =" , (2 ** 35))).grid(row=1)
Label(benchroot, text = ("Level 36. 2 ** 36 =" , (2 ** 36))).grid(row=1)
Label(benchroot, text = ("Level 37. 2 ** 37 =" , (2 ** 37))).grid(row=1)
Label(benchroot, text = ("Level 38. 2 ** 38 =" , (2 ** 38))).grid(row=1)
Label(benchroot, text = ("Level 39. 2 ** 39 =" , (2 ** 39))).grid(row=1)
Label(benchroot, text = ("Level 40. 2 ** 40 =" , (2 ** 40))).grid(row=1)
Label(benchroot, text = ("Level 41. 2 ** 41 =" , (2 ** 41))).grid(row=1)
Label(benchroot, text = ("Level 42. 2 ** 42 =" , (2 ** 42))).grid(row=1)
Label(benchroot, text = ("Level 43. 2 ** 43 =" , (2 ** 43))).grid(row=1)
Label(benchroot, text = ("Level 44. 2 ** 44 =" , (2 ** 44))).grid(row=1)
Label(benchroot, text = ("Level 45. 2 ** 45 =" , (2 ** 45))).grid(row=1)
Label(benchroot, text = ("Level 46. 2 ** 46 =" , (2 ** 46))).grid(row=1)
Label(benchroot, text = ("Level 47. 2 ** 47 =" , (2 ** 47))).grid(row=1)
Label(benchroot, text = ("Level 48. 2 ** 48 =" , (2 ** 48))).grid(row=1)
Label(benchroot, text = ("Level 49. 2 ** 49 =" , (2 ** 49))).grid(row=1)
Label(benchroot, text = ("Level 50. 2 ** 50 =" , (2 ** 50))).grid(row=1)
Label(benchroot, text = ("Level 51. 2 ** 51 =" , (2 ** 51))).grid(row=1)
Label(benchroot, text = ("Level 52. 2 ** 52 =" , (2 ** 52))).grid(row=1)
Label(benchroot, text = ("Level 53. 2 ** 53 =" , (2 ** 53))).grid(row=1)
Label(benchroot, text = ("Level 54. 2 ** 54 =" , (2 ** 54))).grid(row=1)
Label(benchroot, text = ("Level 55. 2 ** 55 =" , (2 ** 55))).grid(row=1)
Label(benchroot, text = ("Level 56. 2 ** 56 =" , (2 ** 56))).grid(row=1)
Label(benchroot, text = ("Level 57. 2 ** 57 =" , (2 ** 57))).grid(row=1)
Label(benchroot, text = ("Level 58. 2 ** 58 =" , (2 ** 58))).grid(row=1)
Label(benchroot, text = ("Level 59. 2 ** 59 =" , (2 ** 59))).grid(row=1)
Label(benchroot, text = ("Level 60. 2 ** 60 =" , (2 ** 60))).grid(row=1)
Label(benchroot, text = ("Level 61. 2 ** 61 =" , (2 ** 61))).grid(row=1)
Label(benchroot, text = ("Level 62. 2 ** 62 =" , (2 ** 62))).grid(row=1)
Label(benchroot, text = ("Level 63. 2 ** 63 =" , (2 ** 63))).grid(row=1)
Label(benchroot, text = ("Level 64. 2 ** 64 =" , (2 ** 64))).grid(row=1)
Label(benchroot, text = ("Level 65. 2 ** 65 =" , (2 ** 65))).grid(row=1)
Label(benchroot, text = ("Level 66. 2 ** 66 =" , (2 ** 66))).grid(row=1)
Label(benchroot, text = ("Level 67. 2 ** 67 =" , (2 ** 67))).grid(row=1)
Label(benchroot, text = ("Level 68. 2 ** 68 =" , (2 ** 68))).grid(row=1)
Label(benchroot, text = ("Level 69. 2 ** 69 =" , (2 ** 69))).grid(row=1)
Label(benchroot, text = ("Level 70. 2 ** 70 =" , (2 ** 70))).grid(row=1)
Label(benchroot, text = ("Level 71. 2 ** 71 =" , (2 ** 71))).grid(row=1)
Label(benchroot, text = ("Level 72. 2 ** 72 =" , (2 ** 72))).grid(row=1)
Label(benchroot, text = ("Level 73. 2 ** 73 =" , (2 ** 73))).grid(row=1)
Label(benchroot, text = ("Level 74. 2 ** 74 =" , (2 ** 74))).grid(row=1)
Label(benchroot, text = ("Level 75. 2 ** 75 =" , (2 ** 75))).grid(row=1)
Label(benchroot, text = ("Level 76. 2 ** 76 =" , (2 ** 76))).grid(row=1)
Label(benchroot, text = ("Level 77. 2 ** 77 =" , (2 ** 77))).grid(row=1)
Label(benchroot, text = ("Level 78. 2 ** 78 =" , (2 ** 78))).grid(row=1)
Label(benchroot, text = ("Level 79. 2 ** 79 =" , (2 ** 79))).grid(row=1)
Label(benchroot, text = ("Level 80. 2 ** 80 =" , (2 ** 80))).grid(row=1)
Label(benchroot, text = ("Level 81. 2 ** 81 =" , (2 ** 81))).grid(row=1)
Label(benchroot, text = ("Level 82. 2 ** 82 =" , (2 ** 82))).grid(row=1)
Label(benchroot, text = ("Level 83. 2 ** 83 =" , (2 ** 83))).grid(row=1)
Label(benchroot, text = ("Level 84. 2 ** 84 =" , (2 ** 84))).grid(row=1)
Label(benchroot, text = ("Level 85. 2 ** 85 =" , (2 ** 85))).grid(row=1)
Label(benchroot, text = ("Level 86. 2 ** 86 =" , (2 ** 86))).grid(row=1)
Label(benchroot, text = ("Level 87. 2 ** 87 =" , (2 ** 87))).grid(row=1)
Label(benchroot, text = ("Level 88. 2 ** 88 =" , (2 ** 88))).grid(row=1)
Label(benchroot, text = ("Level 89. 2 ** 89 =" , (2 ** 89))).grid(row=1)
Label(benchroot, text = ("Level 90. 2 ** 90 =" , (2 ** 90))).grid(row=1)
Label(benchroot, text = ("Level 91. 2 ** 91 =" , (2 ** 91))).grid(row=1)
Label(benchroot, text = ("Level 92. 2 ** 92 =" , (2 ** 92))).grid(row=1)
Label(benchroot, text = ("Level 93. 2 ** 93 =" , (2 ** 93))).grid(row=1)
Label(benchroot, text = ("Level 94. 2 ** 94 =" , (2 ** 94))).grid(row=1)
Label(benchroot, text = ("Level 95. 2 ** 95 =" , (2 ** 95))).grid(row=1)
Label(benchroot, text = ("Level 96. 2 ** 96 =" , (2 ** 96))).grid(row=1)
Label(benchroot, text = ("Level 97. 2 ** 97 =" , (2 ** 97))).grid(row=1)
Label(benchroot, text = ("Level 98. 2 ** 98 =" , (2 ** 98))).grid(row=1)
Label(benchroot, text = ("Level 99. 2 ** 99 =" , (2 ** 99))).grid(row=1)
Label(benchroot, text = ("Level 100. 2 ** 100 =" , (2 ** 100))).grid(row=1)

      




t2 = time.time()


total =  t2-t1




global changeamount
if total <= 0.00000000001:
    total = 0.01

changeamount = int((10/ (total ))/8) 



benchroot.destroy()

print ("PC Score = ",changeamount)


if changeamount <= 1:
    changeamount = 1
elif changeamount >= 500:
    changeamount = 500





#neptuune/jool/duna have weird issue.

global blurbwindow
blurbwindow = Toplevel()
blurbwindow.wm_title("Blurb")
blurbwindow.configure(background = 'silver')
blurbwindow.resizable(0,0)

#Label(blurbwindow, text = "change options in opeionts").pack()
Label(blurbwindow, text = "This program simulates orbital motion under the").grid(row = 1,sticky = W)
Label(blurbwindow, text = "influence of Newtonian gravity. It displays how").grid(row = 2,sticky = W)
Label(blurbwindow, text = "factors such as orbital velocity, orbit radius").grid(row = 3,sticky = W)
Label(blurbwindow, text = "and gravational parameters of bodies affect an").grid(row = 4,sticky = W)
Label(blurbwindow, text = "orbit in a visual way. This program has been").grid(row = 5,sticky = W)
Label(blurbwindow, text = "designed to be easily editible with many variables").grid(row = 6,sticky = W)
Label(blurbwindow, text = "that a user can edit and change, to control many").grid(row = 7,sticky = W)
Label(blurbwindow, text = "characteristics of an orbit.").grid(row = 8,sticky = W)
Label(blurbwindow, text = "",background = 'silver').grid(row = 99,sticky = W)
Label(blurbwindow, text = "Things to Note:").grid(row = 100,sticky = W)




Label(blurbwindow, text = "•To run the simulation, enter a variable into a").grid(row = 101,sticky = W)
Label(blurbwindow, text = "box, and then select 'Set xxxxx'. Then click 'Run!'").grid(row = 102,sticky = W)
Label(blurbwindow, text = "to run the simulation.").grid(row = 103,sticky = W)
Label(blurbwindow, text = "•The simulation is set to basic mode by default.").grid(row = 121,sticky = W)
Label(blurbwindow, text = "To set unlock extra features, set the program to ").grid(row = 122,sticky = W)
Label(blurbwindow, text = "advanced mode in the options.").grid(row = 123,sticky = W)
Label(blurbwindow, text = "•There is a chance of crashing the program due").grid(row = 141,sticky = W)
Label(blurbwindow, text = "to variables that excedd escape velocity. To fix this").grid(row = 142,sticky = W)
Label(blurbwindow, text = "just press the red 'Reset' button.").grid(row = 143,sticky = W)

Label(blurbwindow, text = "•You can only edit the spacecraft variable group or").grid(row = 151,sticky = W)
Label(blurbwindow, text = "the body variable group at a time. Please refer to the").grid(row = 152,sticky = W)
Label(blurbwindow, text = "tutorial for more information.").grid(row = 153,sticky = W)
#Label(blurbwindow, text = "•").pack()
##Label(blurbwindow, text = "•").pack()
#Label(blurbwindow, text = "•").pack()
#Label(blurbwindow, text = "•").pack()

def blurbclose():
    blurbwindow.destroy()

blurbcombust = Button(blurbwindow, text = "Close", command = blurbclose)
blurbcombust.grid(row = 200)




global mode
mode = 1



                      






class App():
    def __init__(self, groot):

        

        

        def orbitcalc():
            global blurbwindow
            global canvasshrink
            global root
            global reschange
            global tcanvasx
            global tcanvasy
            global fullscreen
            global orbitopen
            global oprootopen
            global tutrootopen
            global optopen
            
            global EMbutton
            global tutopen
            global credopen

            global credroot

            global CALCmenu
            global CREDmenu
            global TUTmenu
            global OPmenu
            global menuspacelab1

            blurbwindow.destroy()

            

            menuspacelab1.grid_remove()
            
                    
            self.root = Toplevel()
            

            #groot.protocol('WM_TAKE_FOCUS')

            credopen.grid_remove()
            

            orbitopen.grid_remove()
            #orbitopen.grid_remove()
            #torbitopen.grid_remove()
            tutopen.grid_remove()
            optopen.grid_remove()
            EMbutton.grid_remove()
            
            global oprootopen
            if oprootopen == 1:
                global oproot
                oproot.destroy()
                
                oprootopen = 0
            global credrootopen
            if credrootopen == 1:
                global credroot
                credroot.destroy()
                credrootopen = 0


            if fullscreen == 1:
                self.root.overrideredirect(1)
            self.root.focus_set() # <-- move focus to this widget
            self.root.bind("<Escape>", lambda e: e.widget.quit())

            if reschange != 1:
                global tcanvasx
                global tcanvasy

            
    



                tcanvasx = self.root.winfo_screenwidth()/1.3
                tcanvasy = self.root.winfo_screenheight()/1.3

                if tcanvasx <= 960 or tcanvasy <= 560:
                    tcanvasx = 960
                    tcanvasy = 540
             

    
        
            
            
            groot.attributes("-topmost", True)
            groot.resizable(0,0)
            
                
            
            def loopchangecore():

                self.Vuserchange=0
                self.Auserchange=0
                self.Iuserchange=0
                
                
                self.oldVuserchange=0
                self.oldAuserchange=0
                self.oldIuserchange=0
                


                #userchangeclean()

                self.PRshorta = self.PRdentry.get()
                self.PRshortb = self.PReentry.get()
                self.PRshort = abs(int(self.PRshorta * 10** self.PRshortb))
                                
                self.PRuserchange= (self.PRshort) - self.planetradius
                self.oldPRuserchange = self.PRuserchange



                self.Pchange =  abs(self.PRuserchange/self.changeamount)

                


           
                self.loopvaluechange = self.PRuserchange/abs(self.Pchange)
                    
                
                self.totalPRchange = self.loopvaluechange * abs(self.Pchange)

                if self.PRuserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0
                


            def loopchangemass():


                self.Vuserchange=0
                self.Auserchange=0
                self.Iuserchange=0
                
                
                self.oldVuserchange=0
                self.oldAuserchange=0
                self.oldIuserchange=0
                

                #userchangeclean()
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




            
            global loopchangeath
            def loopchangeath():


                self.Vuserchange=0
                self.Auserchange=0
                self.Iuserchange=0
                
                
                self.oldVuserchange=0
                self.oldAuserchange=0
                self.oldIuserchange=0
                




                #userchangeclean()
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
                

            global loopchangealt  
            def loopchangealt():


                
                self.Muserchange=0
                self.PRuserchange=0
                self.Atuserchange= 0
                
                
                self.oldMuserchange=0
                self.oldPRuserchange=0
                self.oldAtuserchange=0





                #userchangeclean()
                self.Ashorta = self.Adentry.get()
                self.Ashortb = self.Aeentry.get()
                self.Ashort =  abs(self.Ashorta * 10** self.Ashortb)
                

                
                if self.Ashort <= self.A:
                    self.notification = "Cannot have an altitude below body surface."
                    self.w.create_text(self.canvasx/2, self.canvasy - 130, text=self.notification, font = self.ArialBg)
                    self.Ashort = self.planetradius

                self.Auserchange= self.Ashort - self.A
                self.oldAuserchange = self.Auserchange

                



                self.Achange = abs(self.Auserchange/self.changeamount)

                self.loopvaluechange = self.Auserchange/abs(self.Achange)

                
                self.totalAchange = self.loopvaluechange * abs(self.Achange)

                if self.Auserchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0


            def loopchangeincline():

                
                self.Muserchange=0
                self.PRuserchange=0
                self.Atuserchange= 0
                
                
                self.oldMuserchange=0
                self.oldPRuserchange=0
                self.oldAtuserchange=0



                #userchangeclean()

                self.Ishort = -1* self.InclineSlide.get()
                

                self.Iuserchange= self.Ishort - self.incline
                self.oldIuserchange = self.Iuserchange



                self.Ichange = abs(self.Iuserchange/self.changeamount)

                self.loopvaluechange = self.Iuserchange/abs(self.Ichange)

                
                self.totalIchange = self.loopvaluechange * abs(self.Ichange)

                if self.Iuserchange != 0:
                    self.dvchange = ((2*self.V**2 )*(1- math.cos (self.Iuserchange*( math.pi/180))))**0.5
                    self.tdvchange = self.dvchange + self.tdvchange

                

                
                #self.incline = -1 * self.InclineSlide.get()
                #self.Vchange=0
                #self.Mchange=0
                #self.Pchange=0
                #self.Achange=0  #MAKE ALL THIS INSIDE A DEFINE
                #self.Atchange=0
                #self.update_frame()
            global loopchangeorbit
            
            def loopchangeorbit():

                
                self.Muserchange=0
                self.PRuserchange=0
                self.Atuserchange= 0
                
                
                self.oldMuserchange=0
                self.oldPRuserchange=0
                self.oldAtuserchange=0


                #add function for too much orbit

              
               # userchangeclean()
                #self.userchange

                self.Oshorta = self.Odentry.get()
                self.Oshortb = self.Oeentry.get()
                self.Oshort =  abs(self.Oshorta * 10** self.Oshortb)
                if self.Oshort <= 1:
                    self.Oshort = 1

                self.R = self.planetradius + self.UA
                self.L = (self.R + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                self.Vshort = (self.U * (2/self.R - 1/self.L))**0.5
          
                if self.Vshort >= self.eV:
                    self.Vshort = math.trunc(self.eV)
                    self.notification = "Escape velocity exceeded, setting velocity to highest possible orbital velocity."
                    self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                    

                else:
                    self.Vshort = self.Vshort
                

                
                self.Vuserchange= self.Vshort - self.V
                        

                self.oldVuserchange = self.Vuserchange


                self.Vchange = abs(self.Vuserchange/self.changeamount)

                self.loopvaluechange = self.Vuserchange/abs(self.Vchange)

                
                self.totalVchange = self.loopvaluechange * abs(self.Vchange)
           
                self.dvchange = self.Vuserchange
                self.tdvchange = self.dvchange + self.tdvchange
        

                

            global loopchangeposition
            def loopchangeposition():

                

       

                if self.B >= self.planetradius:

                    
                    self.Muserchange=0
                    self.PRuserchange=0
                    self.Atuserchange= 0
                    
                    
                    self.oldMuserchange=0
                    self.oldPRuserchange=0
                    self.oldAtuserchange=0

                    #userchangeclean()
                    self.Auserchange = self.B - self.A
                    self.oldAuserchange = self.Auserchange
                    self.R = self.B
                   # self.L = (self.R + self.planetradius)/2 #From planetsurface, remove self.planetradius to do from planet centre
                    self.Vshort = (self.U * (2/self.R - 1/self.L))**0.5
                    # (self.Vshort)
                    self.Vuserchange= self.Vshort - self.V
                    self.oldVuserchange = self.Vuserchange
                    self.Iuserchange= -2 * self.incline
                    self.oldIuserchange = self.Iuserchange

                    self.Ichange = (self.Iuserchange/1)

                    self.totalIchange = self.loopvaluechange * abs(self.Ichange)


                    
                    self.Vchange = (self.Vuserchange/1)

                   
                    self.Achange = (self.Auserchange/1)

                   

                   

                    

                    

                    self.loopvalue = 1#  self.Auserchange/abs(self.Achange)

                    ##self.Achange = abs(self.Auserchange/self.changeamount)
                    self.totalVchange = self.loopvalue * abs(self.Vchange)
                       
                    
                    self.totalAchange = self.loopvalue* abs(self.Achange)
                    
                    update_frame()
                else:
                    self.notification = "Cannot warp inside body."
                    self.w.create_text(self.canvasx/2, self.canvasy - 170, text=self.notification, font = self.ArialBg) #Yes I know it doubles up



                ###################
                #userchangeclean()
                #self.Auserchange = self.B - self.A
                #self.oldAuserchange = self.Auserchange
                #self.R = self.B
                #self.L = (self.R + self.planetradius + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                #self.Vshort = (self.U * (2/self.R - 1/self.L))**0.5
                ## (self.Vshort)
                #self.Vuserchange= self.Vshort - self.V
                #self.oldVuserchange = self.Vuserchange

                #self.Iuserchange= -2 * self.incline
                #self.oldIuserchange = self.Iuserchange

                #self.Ichange = (self.Iuserchange/self.changeamount)

                #self.totalIchange = self.loopvaluechange * abs(self.Ichange)


                
                #self.Vchange = (self.Vuserchange/self.changeamount)

             

               
                #self.Achange = (self.Auserchange/self.changeamount)

             

               

                

                

                #self.loopvalue = self.changeamount#  self.Auserchange/abs(self.Achange)

                ##self.Achange = abs(self.Auserchange/self.changeamount)
                #self.totalVchange = self.loopvalue * abs(self.Vchange)
                   
                
                #self.totalAchange = self.loopvalue* abs(self.Achange)
                
                #update_frame()
            
            def loopchangevel():


                
                self.Muserchange=0
                self.PRuserchange=0
                self.Atuserchange= 0
                
                
                self.oldMuserchange=0
                self.oldPRuserchange=0
                self.oldAtuserchange=0




             
                #userchangeclean()
                if self.Ventry.get() > self.eV:
                    self.Vuserchange =math.trunc(self.eV - self.V) #for safety
                    self.notification = "Escape velocity exceeded, setting velocity to highest possible orbital velocity."
                    self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                else:
                    if abs(self.Ventry.get()) == 0:
                        self.Vuserchange = 1 - self.V
                        self.notification = "Setting velocity to nearest value of 1."
                        self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
                    else:
                        self.Vuserchange =abs(self.Ventry.get()) - self.V
                        
                        
              
                self.oldVuserchange = self.Vuserchange

                self.Vchange =  abs(self.Vuserchange/self.changeamount)
          
                
                self.loopvaluechange = self.Vuserchange/abs(self.Vchange)

                
                self.totalVchange = self.loopvaluechange * abs(self.Vchange)
              
                self.dvchange = self.Vuserchange
                self.tdvchange = self.dvchange + self.tdvchange
          
                
            def shipmassset():
                self.w.delete(self.smallban)
                self.w.delete(self.smalltext)
                self.shipmass =  abs(self.shipmassentry.get())

                self.Fc = (self.shipmass * self.shipg) *1000 # in N
             
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
                self.loopcurrent = 100
                userchangeclean()

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
                    self.sev.grid_remove()
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
                    self.sevt.gird_remove()

                update_frame()

            
                
                

                
            def looprun():
                global loopvalue
                global loopcurrent

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()

                self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
                self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

                self.dvchangelab.grid(row = 13, column = 1, columnspan = 1, sticky = W)
                self.tdvchangelab.grid(row = 13, column = 2, columnspan = 2, sticky = W)

                global mode
                if mode == 1:
                    self.dvchangelab.grid_remove()
                    self.tdvchangelab.grid_remove()
                    
                    

               

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
                self.changeposition.configure(state = DISABLED)
                

                

                self.waitnes = Label(groot, text =("Calculating..."), background = 'silver')
                self.waitnes.grid(row = 13, column = 1, columnspan = 3)

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
                    self.sev.grid_remove()
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
                    self.sevt.grid_remove()
                    

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()

                update_frame()
                

            
                
            def planetbox():
                planetdetails()

                if self.odd == 1:
                    
                    self.fM = self.n
                #orbitmath()
                #(self.planetcombobox.current())
                #SUN,Merc, VEnus, EARTH, MON, MAARS,JUPITER,SATURN, URANUS, NEPTUNE, .... , KERBOL, Moho, Eve, gilly, Kerbin, mun,minmud, duna, ike, dres, jool, laythe, vall, tylo, bop, pol , eeloo
    #GOES UP BOT NOT DOWN


        

                
                   
           

                self.Muserchange = (self.fM) - self.M
                self.PRuserchange = self.fplanetradius - self.planetradius
                self.Vuserchange = ((self.G * self.fM )/(self.UA + self.fplanetradius))**0.5 - self.V
        

                self.Mchange =  (self.Muserchange/self.changeamount)
                self.Pchange =  (self.PRuserchange/self.changeamount)
                #self.Pchange = 100
                self.Vchange =  (self.Vuserchange/self.changeamount)

          

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

               

                
                
                looprun()

         

            
            global Ventry

            
            
            
            

            
            

            self.root.wm_title("Orbital Calculator v 0.9")
      
            groot.wm_title("Mission Control")
            
            
            self.root.configure(background='silver') # windoow background
            groot.configure(background='silver')
            self.root.resizable(0,0)
       



        
            
            self.canvasx = int(tcanvasx)
            self.canvasy = int(tcanvasy)
            
            #self.canvasx = 900
            #self.canvasy = 700
    

            
            self.ovalheadway = 200 #higher is more headway MUST NOT BE MORE THAN OR EQUAL TO CANVASY/2\

            self.crootopen = 0
            self.prootopen = 0
            self.frootopen = 0
            self.orootopen = 0
            self.mrootopen = 0
            

            def frootwindowclose():
                self.froot.destroy()
                self.frootopen = 0

            def orootwindowclose():
                self.oroot.destroy()
                self.orootopen = 0

            def grootwindowclose():
                global orbitcalcopen
                global tutopen
                global optopen
                global credopen

                global credrootwindow
                
                
                global orbitopen
                global oprootopen
                global tutrootopen

                global speedSlide
                global speedLab

             
             
                
                global EMbutton

                global CALCmenu
                global CREDmenu
                global TUTmenu
                global OPmenu
                global Emenu

                global menuspacelab1

                groot.attributes("-topmost", False)

            
         

          

                
                if self.orootopen == 1:
                    self.oroot.destroy()
                if self.frootopen == 1:
                    self.froot.destroy()
                if self.prootopen == 1:
                    self.proot.destroy()
                if self.crootopen == 1:
                    self.croot.destroy()
                if self.mrootopen == 1:
                    self.mroot.destroy()
                
                
                self.root.destroy()

                self.waitnes.grid_remove()

                self.speedSlide.grid_remove()
                self.speedLab.grid_remove()
              

                self.SPACELAB1.grid_remove()

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
                self.mrootwindowopen.grid_remove()

                self.uplab.grid_remove()
                self.downlab.grid_remove()
                
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
                self.LINELAB3.grid_remove()
                self.LINELAB4.grid_remove()

                self.calccombust.grid_remove()

                orbitcalcopen = 0
               

                

               
                
                global oprootopen
               
                oprootopen = 0
                tutrootopen = 0
          
                orbitopen = Button(groot, text="Open Calculator", command=orbitcalccommand, image = CALCmenu,background = 'silver',borderwidth=0)
                orbitopen.grid(row = 1, column = 1,sticky=W)
                

                tutopen = Button(groot, text="Open Tutorial", command=orbittutcommand, image = TUTmenu,background = 'silver',borderwidth=0)
                tutopen.grid(row = 20, column = 1,sticky=W)
                
                optopen = Button(groot, text="Open Options", command=optionmenu, image = OPmenu,background = 'silver',borderwidth=0)
                optopen.grid(row = 30, column = 1,sticky=W)

                credopen = Button(groot, text="Open Credits", command = credrootwindow,image = CREDmenu,background = 'silver',borderwidth=0)
                credopen.grid(row = 40,column = 1,sticky=W)

                menuspacelab1 = Label(groot, text = "", background = 'silver')
                menuspacelab1.grid(row=22, column = 2)

                

           

                
                EMbutton = Label(groot, image=Emenu)
                EMbutton.Emenu =Emenu
                EMbutton.grid(row = 1, column = 3,rowspan = 1000)
                EMbutton.configure(background = 'silver')
                groot.wm_title("Menu")

            def mrootwindowclose():
                self.mroot.destroy()
                self.mrootopen = 0
                
            
            def mrootwindow():
                global Vbutton
                global Vlab
                global FGbutton
                global FGlab
                global Gbutton
                global Glab
                global Tbutton
                global Tlab
                global Ebutton
                global Elab
                if self.mrootopen == 0:
                    self.mroot = Toplevel()
                    self.mrootopen = 1
                    self.mroot.protocol('WM_DELETE_WINDOW',mrootwindowclose)
                    self.mroot.wm_title("Math")
                    self.mroot.resizable(0,0)
                    self.mroot.configure(background='silver')
                    #self.mroot.resizable(0,0)
                    self.mathslideshow = 1

                    def GravationalConstant():
                        webbrowser.open('https://en.wikipedia.org/wiki/Gravitational_constant#Laws_and_constants')
                    
                    

                    def ForceGravity():
                        webbrowser.open('https://en.wikipedia.org/wiki/Gravitational_acceleration#For_point_masses')


                    

                    def TsiolkovskyRE():
                        webbrowser.open('https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation')

                    

                    def ExhaustVelocity():
                        webbrowser.open('https://en.wikipedia.org/wiki/Specific_impulse#Specific_impulse_as_a_speed_.28effective_exhaust_velocity.29')

                    

                    

                    def VisViva():
                        webbrowser.open('https://en.wikipedia.org/wiki/Vis-viva_equation#Equation')

                    

                    

                    self.mathcombust = Button(self.mroot, text = "Close", command = mrootwindowclose)
                    self.mathcombust.grid(row = 6, column = 1, sticky = W)


                    def mathresetslide():
                        global Vbutton
                        global Vlab
                        global FGbutton
                        global FGlab
                        global Gbutton
                        global Glab
                        global Tbutton
                        global Tlab
                        global Ebutton
                        global Elab
                        

                        if self.mathslideshow ==1:
                            Vbutton.grid_remove()
                            Vlab.grid_remove()
                            FGbutton.grid_remove()
                            FGlab.grid_remove()
                            Gbutton.grid_remove()
                            Glab.grid_remove()
        
                        else:

                            
                            Tbutton.grid_remove()
                            Tlab.grid_remove()
                            
                            Ebutton.grid_remove()
                            Elab.grid_remove()
                            
                            
                    def mathslide():
                        global Vbutton
                        global Vlab
                        global FGbutton
                        global FGlab
                        global Gbutton
                        global Glab
                        global Tbutton
                        global Tlab
                        global Ebutton
                        global Elab
                        
                        
                        
                        if self.mathslideshow ==1:
                            Vviva= PhotoImage(file="VISVIVA.png")
                            Vbutton = Button(self.mroot, image=Vviva,command=VisViva)
                            Vbutton.Vviva =Vviva
                            Vbutton.grid(row = 3, column = 2)
                            global Vlab
                            Vlab = Label(self.mroot, text = "Vis - Viva Equation")
                            Vlab.grid(row=3,column=1)
                            Vbutton.configure(background = 'gray90', foreground = 'silver',borderwidth=5,disabledforeground='silver')

                            FGrav = PhotoImage(file="FGRAV.png")
                            FGbutton = Button(self.mroot, image=FGrav,command=ForceGravity)
                            FGbutton.FGrav = FGrav
                            FGbutton.grid(row = 2, column = 2)
                            FGlab = Label(self.mroot, text = "Force of Gravity")
                            FGlab.grid(row=2,column=1)
                            FGbutton.configure(background = 'gray90', foreground = 'silver',borderwidth=5,disabledforeground='silver')

                            Gconstant = PhotoImage(file="GCONSTANT.png")
                            Gbutton = Button(self.mroot, image=Gconstant,command= GravationalConstant)
                            
                            Gbutton.Gconstant = Gconstant
                            Gbutton.grid(row = 1, column = 2)
                            Glab = Label(self.mroot, text = "Gravational Constant")
                            Glab.grid(row=1,column=1)
                            Gbutton.configure(background = 'gray90', foreground = 'silver',borderwidth=5,disabledforeground='silver')
                            
                        elif self.mathslideshow ==2:

                            Trocket = PhotoImage(file="ROCKEQ.png")
                            Tbutton = Button(self.mroot, image=Trocket,command=TsiolkovskyRE)
                            Tbutton.Trocket = Trocket
                            Tbutton.grid(row = 1, column = 2)
                            Tlab = Label(self.mroot, text = "Tsiolkovsky Rocket Equation")
                            Tlab.grid(row=1,column=1)
                            Tbutton.configure(background = 'gray90', foreground = 'silver',borderwidth=5,disabledforeground='silver')

                            
                            Evelocity = PhotoImage(file="EFFEXHVEL.png")
                            Ebutton = Button(self.mroot, image=Evelocity,command=ExhaustVelocity)
                            Ebutton.Evelocity = Evelocity
                            Ebutton.grid(row = 2, column = 2)
                            Elab = Label(self.mroot, text = "Effective Exhaust Velocity")
                            Elab.grid(row=2,column=1)
                            Ebutton.configure(background = 'gray90', foreground = 'silver',borderwidth=5,disabledforeground='silver')
                       
                        

                    def mathplusone():
                        
                        mathresetslide()
                        if self.mathslideshow == 1:
                            self.mathslideshow += 1
                        mathslide()

                    def mathminusone():
                        
                        mathresetslide()
                        if self.mathslideshow == 2:
                            self.mathslideshow -= 1
                        mathslide()

                    mathslide()

                    self.nextbutton = Button(self.mroot, text='Next',command = mathplusone)
                    self.nextbutton.grid(row=5,column=1, sticky = E)

                    self.backbutton = Button(self.mroot, text='Back',command = mathminusone)
                    self.backbutton.grid(row=5,column=1, sticky = W)


                    Label(self.mroot, text = "* Click on formulae to link to web source.", background = 'silver', font = (tkinter.font.Font(family='Arial',size=10))).grid(row = 6, column = 2, sticky = E)
                    #Label(self.mroot,text = " MATH AND STUFF ",background='silver').grid(row = 1 , column = 3)
            
                
            def orootwindow():
                if self.orootopen == 0:
                    self.oroot = Toplevel()
                    self.oroot.protocol('WM_DELETE_WINDOW',orootwindowclose)
                    self.orootopen = 1 
                    self.oroot.wm_title("Glossary")
                    self.oroot.configure(background='silver')
                    self.oroot.resizable(0,0)
                    
                        

                    Label(self.oroot,text = " ",background='silver').grid(row = 1 , column = 3)
                

                    Label(self.oroot,text = "|").grid(row = 1 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 2 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 3 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 4 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 5 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 6 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 7 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 8 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 9 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 10 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 11 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 12 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 13 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 14 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 15 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 16 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 17 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 18 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 19 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 20 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 21 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 22 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 23 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 24 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 25 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 26 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 27 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 28 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 29 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 30 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 31 , column = 2)
                    Label(self.oroot,text = "|").grid(row = 32 , column = 2)

                    Label(self.oroot, text = "Altitude",font = self.ArialBg).grid(row = 1 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Distance from the current position to bodies centre of mass.").grid(row = 1 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Apoapsis",font = self.ArialBg).grid(row = 2 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point of orbit that is furthest from the body. Lowest possible orbital speed is here.").grid(row = 2 , column = 4, columnspan = 1, sticky = W)
                    

                    Label(self.oroot, text = "Body",font = self.ArialBg).grid(row = 3 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The planet/sun/moon a satellite is orbiting.").grid(row = 3 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Burnout",font = self.ArialBg).grid(row = 4 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Shutdown of engine due to lack of fuel.").grid(row = 4 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Burn Time",font = self.ArialBg).grid(row = 5 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How long an engine can run for before burnout.").grid(row = 5 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Centre of Mass",font = self.ArialBg).grid(row = 6 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point where all mass is concentrated. Assumed Centre of Mass in centre of body for calculations.").grid(row = 6 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Centripetal Force",font = self.ArialBg).grid(row = 7 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much force is acting on an object to keep it in the circle/ellipse that it is travelling in. Expressed as Fc.").grid(row = 7 , column = 4, columnspan = 1, sticky = W )

                    Label(self.oroot, text = "Delta V",font = self.ArialBg).grid(row = 8 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Change in velocity.").grid(row = 8 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Dry Mass",font = self.ArialBg).grid(row = 9 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Mass of a spacecraft when fuel is empty.").grid(row = 9 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Eccentricity",font = self.ArialBg).grid(row = 10 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "A measure of how much a conic section deviates from being circular.").grid(row = 10 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Equatorial Plane",font = self.ArialBg).grid(row = 11 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Plane parrellel with equatorial line.").grid(row = 11 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Escape Velocity",font = self.ArialBg).grid(row = 12 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Velocity needed to escape orbit of the body being orbited.").grid(row = 12 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Focal Length",font = self.ArialBg).grid(row = 13 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Distance from the centre of orbit to where the orbiting body is.").grid(row = 13 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Fuel Mass",font = self.ArialBg).grid(row = 14 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much mass of a spacecraft is fuel.").grid(row = 14 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Acceleration",font = self.ArialBg).grid(row = 15 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Measurement of how much acceleration an object will inherit when no other forces are active.").grid(row = 15 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Constant",font = self.ArialBg).grid(row = 16 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Use to calculate the attractive forces of two bodies as proportionate to their own mass. Approximately 6.674x 10 ^ -11 Nm^2/kg^2.").grid(row = 16 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Gravational Parameter",font = self.ArialBg).grid(row = 17 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Expressed as μ and and shown in unit m^3/s. Product of Gravational Constant and mass of body.").grid(row = 17 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Inclination",font = self.ArialBg).grid(row = 18 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Angle of orbit measured from equatorial plane.").grid(row = 18 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Manoeuvre",font = self.ArialBg).grid(row = 19 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "A movement.").grid(row = 19 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Mass",font = self.ArialBg).grid(row = 20 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much matter is in an object. The more matter the 'heavier' when combined with gravational acceleration.").grid(row = 20 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Orbit",font = self.ArialBg).grid(row = 21 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Path of satellite around a body.").grid(row = 21 , column = 4, columnspan = 1, sticky = W)     

                    Label(self.oroot, text = "Periapsis",font = self.ArialBg).grid(row = 22 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Point of orbit that is closest to body. Highest possible orbital speed is here.").grid(row = 22 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Period",font = self.ArialBg).grid(row = 23 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Time required for one circuit of orbit.").grid(row = 23 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Prograde",font = self.ArialBg).grid(row = 24 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The direction in the orbit is travelling.").grid(row = 24 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Radar Altitude",font = self.ArialBg).grid(row = 25 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How high something is from the surface beneath it. Eg. Atltiude of spacecraft from sea level of body.").grid(row = 25 , column = 4, columnspan = 1, sticky = W)
                    
                    Label(self.oroot, text = "Retrograde",font = self.ArialBg).grid(row = 26 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "The direction opposite from the direction the orbit is travelling.").grid(row = 26 , column = 4, columnspan = 1, sticky = W)
                    
                    Label(self.oroot, text = "Semi-Major Axis",font = self.ArialBg).grid(row = 27 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Half of the longest part of an orbit.").grid(row = 27 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Semi-Minor Axis",font = self.ArialBg).grid(row = 28 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Half of the shortest part of an orbit.").grid(row = 28 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Specific Impulse",font = self.ArialBg).grid(row = 29 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Expressed as Isp, and measured in seconds. It is a measurement of how effeciency of converting fuel into thrust.").grid(row = 29 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Thrust",font = self.ArialBg).grid(row = 30, column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How much force an engine can exhert.").grid(row = 30, column = 4, columnspan = 1, sticky = W)                    

                    Label(self.oroot, text = "Velocity",font = self.ArialBg).grid(row = 31 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "How fast an object is travelling in a praticular direction.").grid(row = 31 , column = 4, columnspan = 1, sticky = W)

                    Label(self.oroot, text = "Wet Mass",font = self.ArialBg).grid(row = 32 , column = 1, columnspan = 1, sticky = W)
                    Label(self.oroot, text = "Mass of a spacecraft when full of fuel.").grid(row = 32 , column = 4, columnspan = 1, sticky = W)

                    

                    

                    

                    

                    

                    

                    

                    

                    
                    
                    self.glosscombust = Button(self.oroot, text = "Close", command = orootwindowclose)
                    self.glosscombust.grid(row = 33, column = 2)

            def frootwindow():
                if self.frootopen == 0:
                    self.froot = Toplevel()
                    self.frootopen = 1
                    self.froot.protocol('WM_DELETE_WINDOW',frootwindowclose)
                    self.froot.wm_title("Frequently Asked Questions")
                    self.froot.configure(background='silver')
                    self.froot.resizable(0,0)
                   
                    
                    self.OBERTHOP = -1
                    self.SHIPSPEEDOP = -1
                    self.INCLINEDVEXPOP = -1
                    self.MASSEXPOP = -1
                    self.RADIUSEXPOP = -1
                    self.CRAFTMASSEXPOP = -1

                    

                    def OBERTHOPEN():
                        self.OBERTHOP = self.OBERTHOP * -1
                        if self.OBERTHOP == 1:
                            self.l11 = Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time")
                            self.l11.grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                            self.l12 = Label(self.froot, text = "to perform a 'burn' is at orbital periapsis, where orbital speed is the highest. When burning,")
                            self.l12.grid(row = 3 , column = 1, columnspan = 10, sticky = W)
                            self.l13 = Label(self.froot, text = "kinetic energy is increased as speed increases. However, since the equation for kinetic energy")
                            self.l13.grid(row = 4 , column = 1, columnspan = 10, sticky = W)
                            self.l14 = Label(self.froot, text = "is increased as speed increases. However, since the equation for kinetic energy is Ek = 0.5mv^2,")
                            self.l14.grid(row = 5 , column = 1, columnspan = 10, sticky = W)
                            self.l15 = Label(self.froot, text = "velocity is squared. So going from 10m/s to 20m/s will produce significantly more energy than")
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

                    def SHIPSPEEDOPEN():
                        self.SHIPSPEEDOP = self.SHIPSPEEDOP * -1
                        if self.SHIPSPEEDOP == 1:
                            self.l21 = Label(self.froot, text = "A ship will gain a higher velocity when coming closer to a planet because it is getting")
                            self.l21.grid(row = 11 , column = 1, columnspan = 10, sticky = W)
                            self.l22 = Label(self.froot, text = "pulled by gravity. When a ball is thrown into the air, it is slowest when furthest from")
                            self.l22.grid(row = 12 , column = 1, columnspan = 10, sticky = W)
                            self.l23 = Label(self.froot, text = "the ground, and fastest when closest. The same thing happens in orbits. A spacecraft is")
                            self.l23.grid(row = 13 , column = 1, columnspan = 10, sticky = W)
                            self.l24 = Label(self.froot, text = "slowest at its apoapsis (furthest point from planet) and fastest at its periapsis")
                            self.l24.grid(row = 14 , column = 1, columnspan = 10, sticky = W)
                            self.l25 = Label(self.froot, text = "(closest point to planet). The spacecraft uses its kinetic energy to get ‘flung’ to the")
                            self.l25.grid(row = 15 , column = 1, columnspan = 10, sticky = W)
                            self.l26 = Label(self.froot, text = "furthest point in its orbit, and while doing so is losing speed as it is fighting against")
                            self.l26.grid(row = 16 , column = 1, columnspan = 10, sticky = W)
                            self.l27 = Label(self.froot, text = "gravity in doing so. One it reaches its furthest point, gravity is now helping the craft")
                            self.l27.grid(row = 17 , column = 1, columnspan = 10, sticky = W)
                            self.l28 = Label(self.froot, text = "speed up and it accelerates faster and faster until it reaches periapsis. In this stage it")
                            self.l28.grid(row = 18 , column = 1, columnspan = 10, sticky = W)
                            self.l29 = Label(self.froot, text = "is the longest period of acceleration and therefore it is fastest.")
                            self.l29.grid(row = 19 , column = 1, columnspan = 10, sticky = W)
                        else:
                            self.l21.grid_remove()
                            self.l22.grid_remove()
                            self.l23.grid_remove()
                            self.l24.grid_remove()
                            self.l25.grid_remove()
                            self.l26.grid_remove()
                            self.l27.grid_remove()
                            self.l28.grid_remove()
                            self.l29.grid_remove()

                    def INCLINEDVEXPOPEN():
                        self.INCLINEDVEXPOP = self.INCLINEDVEXPOP * -1
                        if self.INCLINEDVEXPOP == 1:
                            self.l31 = Label(self.froot, text = "Inclination changes are directly related to the current velocity. Making a velocity change")
                            self.l31.grid(row = 21 , column = 1, columnspan = 10, sticky = W)
                            self.l32 = Label(self.froot, text = "at periapsis (where the spacecraft is at its fastest point) is much less efficient than at")
                            self.l32.grid(row = 22 , column = 1, columnspan = 10, sticky = W)
                            self.l33 = Label(self.froot, text = "apoapsis (where the spacecraft is at its slowest point) because it is travelling much faster.")
                            self.l33.grid(row = 23 , column = 1, columnspan = 10, sticky = W)
                            self.l34 = Label(self.froot, text = "The most efficient time for an inclination change is at apoapsis because that is when orbital")
                            self.l34.grid(row = 24 , column = 1, columnspan = 10, sticky = W)
                            self.l35 = Label(self.froot, text = "velocity is it its lowest. Sometimes it is even more efficient to perform a bi-elliptical")
                            self.l35.grid(row = 25 , column = 1, columnspan = 10, sticky = W)
                            self.l36 = Label(self.froot, text = "manoeuvre (making the orbit much bigger than it needs to be, so the orbital speed is even")
                            self.l36.grid(row = 26 , column = 1, columnspan = 10, sticky = W)
                            self.l37 = Label(self.froot, text = "lower than otherwise. After which an inclination change is performed and then slowed back")
                            self.l37.grid(row = 27 , column = 1, columnspan = 10, sticky = W)
                            self.l38 = Label(self.froot, text = "down to the desired altitude)")
                            self.l38.grid(row = 28 , column = 1, columnspan = 10, sticky = W)
               
                        else:
                            self.l31.grid_remove()
                            self.l32.grid_remove()
                            self.l33.grid_remove()
                            self.l34.grid_remove()
                            self.l35.grid_remove()
                            self.l36.grid_remove()
                            self.l37.grid_remove()
                            self.l38.grid_remove()

                    def MASSEXPOPEN():
                        self.MASSEXPOP = self.MASSEXPOP * -1
                        if self.MASSEXPOP == 1:
                            self.l41 = Label(self.froot, text = "With a higher mass, the gravitational parameter increases (product of the Gravitational Constant")
                            self.l41.grid(row = 31 , column = 1, columnspan = 10, sticky = W)
                            self.l42 = Label(self.froot, text = "and mass of the body). With a higher gravitational parameter, a higher gravitational acceleration is ")
                            self.l42.grid(row = 32 , column = 1, columnspan = 10, sticky = W)
                            self.l43 = Label(self.froot, text = "present. To obtain an orbit with a higher gravitational acceleration, there is more centripetal")
                            self.l43.grid(row = 33 , column = 1, columnspan = 10, sticky = W)
                            self.l44 = Label(self.froot, text = "force ‘pulling’ the spacecraft toward the planet. To combat this, a higher orbital velocity")
                            self.l44.grid(row = 34 , column = 1, columnspan = 10, sticky = W)
                            self.l45 = Label(self.froot, text = "is needed to obtain an orbit. If the velocity stays the same but the mass of the planet")
                            self.l45.grid(row = 35 , column = 1, columnspan = 10, sticky = W)
                            self.l46 = Label(self.froot, text = "increases, the orbit will appear to ‘shrink’.")
                            self.l46.grid(row = 36 , column = 1, columnspan = 10, sticky = W)
          
               
                        else:
                            self.l41.grid_remove()
                            self.l42.grid_remove()
                            self.l43.grid_remove()
                            self.l44.grid_remove()
                            self.l45.grid_remove()
                            self.l46.grid_remove()

                    def RADIUSEXPOPEN():
                        self.RADIUSEXPOP = self.RADIUSEXPOP * -1
                        if self.RADIUSEXPOP == 1:
                            self.l51 = Label(self.froot, text = "When there is a larger planet radius, there is a larger distance between the spacecraft and")
                            self.l51.grid(row = 41 , column = 1, columnspan = 10, sticky = W)
                            self.l52 = Label(self.froot, text = "the CoM of the planet. This results in a lower gravitational acceleration. As shown by the")
                            self.l52.grid(row = 42 , column = 1, columnspan = 10, sticky = W)
                            self.l53 = Label(self.froot, text = "equation g = GM/r^2, when the value of r (distance to CoM) increases, the values of g will")
                            self.l53.grid(row = 43 , column = 1, columnspan = 10, sticky = W)
                            self.l54 = Label(self.froot, text = "shrink. Since there is less gravitational acceleration, there is less centripetal force")
                            self.l54.grid(row = 44 , column = 1, columnspan = 10, sticky = W)
                            self.l55 = Label(self.froot, text = "pulling the spacecraft toward the planet. Thus, a lower velocity is needed to obtain orbit.")
                            self.l55.grid(row = 45 , column = 1, columnspan = 10, sticky = W)
                            self.l56 = Label(self.froot, text = "If the velocity stays the same but the radius of the planet increases, the orbit will appear")
                            self.l56.grid(row = 46 , column = 1, columnspan = 10, sticky = W)
                            self.l57 = Label(self.froot, text = "to ‘grow’.")
                            self.l57.grid(row = 47 , column = 1, columnspan = 10, sticky = W)
           
               
                        else:
                            self.l51.grid_remove()
                            self.l52.grid_remove()
                            self.l53.grid_remove()
                            self.l54.grid_remove()
                            self.l55.grid_remove()
                            self.l56.grid_remove()
                            self.l57.grid_remove()

                    def CRAFTMASSEXPOPEN():
                        self.CRAFTMASSEXPOP = self.CRAFTMASSEXPOP * -1
                        if self.CRAFTMASSEXPOP == 1:
                            self.l61 = Label(self.froot, text = "The mass of the spacecraft is irrelevant when considering gravitational acceleration. In a perfect")
                            self.l61.grid(row = 51 , column = 1, columnspan = 10, sticky = W)
                            self.l62 = Label(self.froot, text = "vacuum, a feather and a bowling ball will fall at the exact same rate, assuming no force other than")
                            self.l62.grid(row = 52 , column = 1, columnspan = 10, sticky = W)
                            self.l63 = Label(self.froot, text = "gravitation is acting. In space, there is almost no atmosphere and so the only relevant force is")
                            self.l63.grid(row = 53 , column = 1, columnspan = 10, sticky = W)
                            self.l64 = Label(self.froot, text = "gravity. Whether a spacecraft is 100 tons or 1 kg, the orbit of the two crafts will be exactly the")
                            self.l64.grid(row = 54 , column = 1, columnspan = 10, sticky = W)
                            self.l65 = Label(self.froot, text = "same assuming all other variables are the same.")
                            self.l65.grid(row = 55 , column = 1, columnspan = 10, sticky = W)
                            
               
                        else:
                            self.l61.grid_remove()
                            self.l62.grid_remove()
                            self.l63.grid_remove()
                            self.l64.grid_remove()
                            self.l65.grid_remove()
                            
                            
     
            


                    self.OBERTH = Button(self.froot, text = "Why does the orbit get much larger when the ship is travelling faster?",  font = self.ArialBg,command = OBERTHOPEN)
                    self.OBERTH.grid(row = 1 , column = 1, columnspan = 10, sticky = W)

                    self.SHIPSPEED = Button(self.froot, text = "Why does the ship speed up when getting closer to the planet?",  font = self.ArialBg,command = SHIPSPEEDOPEN)
                    self.SHIPSPEED.grid(row = 10 , column = 1, columnspan = 10, sticky = W)
                    #PERIAPSIS IS FASTEST PART OF ORBIT

                    self.INCLINEDVEXP = Button(self.froot, text = "Why is the inclination dV change so much higher when travelling at faster speeds?",  font = self.ArialBg,command = INCLINEDVEXPOPEN)
                    self.INCLINEDVEXP.grid(row = 20 , column = 1, columnspan = 10, sticky = W)
                    #INCLINATION IS DIRECTLY RELATED TO SPEED. MOST EFFECIENT AT APO
                    #SOMETIMES BIELLIPTAICAL IS MORE EFFECIENT
                    self.MASSEXP = Button(self.froot, text = "Why does the orbit shrink when the body has a higher mass?",  font = self.ArialBg,command = MASSEXPOPEN)
                    self.MASSEXP.grid(row = 30 , column = 1, columnspan = 10, sticky = W)
                    #Because higher grav accel so more centripetal force pulling the shuip down. higher orbital velocity is needed to stay in orbit

                    self.RADIUSEXP = Button(self.froot, text = "Why does the orbit get bigger when the radius of body increases?",  font = self.ArialBg,command = RADIUSEXPOPEN)
                    self.RADIUSEXP.grid(row = 40 , column = 1, columnspan = 10, sticky = W)
                    #It is further from the CoM and therefore less grav accel thereoe a larger orbit

                    self.CRAFTMASSEXP = Button(self.froot, text = "How come when the spacecraft's mass changes the orbit doesn't change?",  font = self.ArialBg,command = CRAFTMASSEXPOPEN)
                    self.CRAFTMASSEXP.grid(row = 50 , column = 1, columnspan = 10, sticky = W)
                    #all based of grav accel

                    


                    #GLOSSARY
                    

                        

                    

                    
                        
                    
                    #Label(self.froot, text = "Heading",  font = self.ArialBg,background='silver').grid(row = 1 , column = 1, columnspan = 10)
                   # Label(self.froot, text = "Body",background='silver').grid(row = 2 , column = 2, columnspan = 10)

                    
                    
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)
                    #Label(self.froot, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most effecient time",background='silver').grid(row = 2 , column = 1, columnspan = 10, sticky = W)


                    

                    

                    self.faqcombust = Button(self.froot, text = "Close", command = frootwindowclose)
                    self.faqcombust.grid(row = 100, column = 1, columnspan = 3)

                    
                    

            def prootwindowclose():
                self.proot.destroy()
                self.prootopen = 0

            def prootwindow():
                if self.prootopen == 0:
                    self.proot = Toplevel()
                    self.prootopen = 1
                    self.proot.protocol('WM_DELETE_WINDOW',prootwindowclose)
                    self.proot.wm_title("Orbital Characteristics")
                    self.proot.resizable(0,0)
                
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
                    Label(self.proot, text = "",background='silver').grid(row=14, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=14, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=15, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=16, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=17, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=18, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=19, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=20, column = 5)
                    #Label(self.proot, text = "",background='silver').grid(row=21, column = 5)
       
                    
                    self.sua =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.UA,1))),"m"))
                    self.sua.grid(row=2, column = 1, sticky=W, columnspan = 3)
                    self.sa =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.A,1))),"m"))
                    self.sa.grid(row=3, column = 1, sticky=W, columnspan = 3)
                    self.sm =Label(self.proot, text=(round(self.M,1),"kg"))
                    self.sm.grid(row=6, column = 1, sticky=W, columnspan = 3)
                    self.sv =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.V,1))),"m/s"))
                    self.sv.grid(row=5, column = 1, sticky=W, columnspan = 3)
                    self.su =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.U,1))),"m^3/s"))
                    self.su.grid(row=7, column = 1, sticky=W, columnspan = 2)
                    self.sb =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.B,1))),"m"))
                    self.sb.grid(row=4, column = 1, sticky=W, columnspan = 3)
                    self.sl =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.L,1))),"m"))
                    self.sl.grid(row=8, column = 1, sticky=W, columnspan = 3)
                    self.se =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.E,1))),"m"))
                    self.se.grid(row=9, column = 1, sticky=W, columnspan = 3)
                    self.sh =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.H,1))),"m"))
                    self.sh.grid(row=10, column = 1, sticky=W, columnspan = 3)
                    self.sp =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.T,1))),"s"))
                    self.sp.grid(row=11, column = 1, sticky=W, columnspan = 3)
                    self.sd =Label(self.proot, text=((round(self.Ec,1))))
                    self.sd.grid(row=12, column = 1, sticky=W, columnspan = 3)
                    self.sev =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.eV,1))), "m/s"))
                    self.sev.grid(row=13, column = 1, sticky=W, columnspan = 3)
                   
                    
                    
                    self.suat =Label(self.proot, text=("Radar Altitude"))
                    self.suat.grid(row=2, column = 3, sticky=W, columnspan = 3)
                    
                    
                    self.smt =Label(self.proot, text=("Body Mass"))
                    self.smt.grid(row=6, column = 3, sticky=W, columnspan = 3)
                    self.svt =Label(self.proot, text=("Spacecraft Velocity"))
                    self.svt.grid(row=5, column = 3, sticky=W, columnspan = 3)
                    self.sut =Label(self.proot, text=("Gravational Parameter"))
                    self.sut.grid(row=7, column = 3, sticky=W, columnspan = 3)

                    if self.A >= self.B:
                        self.sbt =Label(self.proot, text=("Periapsis"))
                        self.sat =Label(self.proot, text=("Apoapsis"))

                    else:
                        self.sbt =Label(self.proot, text=("Apoapsis"))
                        self.sat =Label(self.proot, text=("Periapsis"))
                    self.sat.grid(row=3, column = 3, sticky=W, columnspan = 3)
                    self.sbt.grid(row=4, column = 3, sticky=W, columnspan = 3)
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
                    self.sevt =Label(self.proot, text=("Escape Velocity"))
                    self.sevt.grid(row=13, column = 3, sticky=W, columnspan = 3)

                    

                    self.waitmes = Label(self.proot, text =("Calculating..."), background = 'silver')
                    self.waitmes.grid(row = 6, column = 1, columnspan = 3)
                    self.waitmes.grid_remove()

                   


                    

                    

                    self.pcombust = Button(self.proot, text = "Close", command = prootwindowclose)
                    self.pcombust.grid(row = 20, column = 1, columnspan = 3)

                    

            def crootwindowclose():
                self.croot.destroy()
                self.crootopen = 0

            def crootwindow():
                if self.crootopen == 0:
                    self.croot = Toplevel()
                    self.crootopen = 1
                    self.croot.protocol('WM_DELETE_WINDOW',crootwindowclose)
                    self.croot.wm_title("Calculator")
                    self.croot.resizable(0,0)
                    
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

                    Label(self.croot,text = "Specific Impulse (s)").grid( row=1, column = 2, sticky=W)
                    Label(self.croot,text = "Wet Mass (t)").grid( row=2, column = 2, sticky=W)
                    Label(self.croot,text = "Dry Mass (t)").grid( row=3, column = 2, sticky=W)

                    Label(self.croot,text = "Specific Impulse (s)").grid( row=6, column = 2, sticky=W)
                    Label(self.croot,text = "Force of Engine (kN)").grid( row=7, column = 2, sticky=W)
                    Label(self.croot,text = "Mass of Fuel (t)").grid( row=8, column = 2, sticky=W)

                    
            self.fM = 1
            self.fplanetradius = 1

            self.fMlab =Label(groot, text = self.fM)
            self.fMlab.grid(column=4, row=8, columnspan = 1)
            
            self.fplanetradiuslab = Label(groot, text = self.fplanetradius)
            self.fplanetradiuslab.grid(column=4, row=9, columnspan = 1)

            def planetdetails():
                self.fMlab.grid_remove()
                self.odd = 0
                
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
                    self.n = 102400000000000000000000000.0
                    self.odd = 1
                    self.fM = "{:.3E}".format(self.n)
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
                    self.n = 4515000000000000000000
                    self.odd = 1
                    self.fM = "{:.3E}".format(self.n)
                    self.fplanetradius = 320000
                    
                elif self.planetcombobox.current() == 19:
                    
                    self.fM = 2.782 * 10 ** 20
                    self.fplanetradius = 130000
                    
                elif self.planetcombobox.current() == 20:
                    
                    self.fM = 3.219 * 10 ** 20
                    self.fplanetradius = 138000
                    
                elif self.planetcombobox.current() == 21:
                    self.n = 4233000000000000000000000
                    self.odd = 1
                    self.fM = "{:.3E}".format(self.n)
                 
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
                self.fMlab.grid(column=4, row=15, columnspan = 2,sticky = W)
                
                
                self.fplanetradiuslab = Label(groot, text = ("Body_Radius=",(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.fplanetradius,1)))),"m"))
                self.fplanetradiuslab.grid(column=4, row=16, columnspan = 2,sticky = W)

                global mode
                if mode == 1:
                    self.fMlab.grid_remove()
                    self.fplanetradiuslab.grid_remove()


                
                

                    
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
                

                

                
            

            def dvCalculator():
                self.dvlab.grid_remove()

                self.dv += 1

                

                #self.isp = self.ispentry.get()
                #self.wetmass = self.wetmassentry.get()
                #self.drymass = self.drymassentry.get()

                self.dv = round((self.ispentry.get() * 9.8 * math.log(self.wetmassentry.get()/self.drymassentry.get())), 1)
            
                #self.dvLab = Label(self.groot, text=self.dv)
                #self.dvLab.grid(row=20, column=1, columnspan = 4)
                #self.dvLab.configure(background='silver') #transparent

                self.dvlab = Label(self.croot, text=("DeltaV=",round(self.dv,1), "m/s"), background='silver')
                self.dvlab.grid(row=3, column = 3, columnspan = 5, sticky=W)
                


            
            self.spacecraftx = self.ovalheadway
            self.phase = 1
            self.reset = 1
            self.repeat = 1
            self.stopall = 0
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
                if self.B >= self.planetradius:
                    
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
                    self.changeposition.configure(state = DISABLED)
                    
                   
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
                    global stopanimation
                    global repeat

                    self.animationstop.configure(background = 'crimson',foreground = 'snow',borderwidth=2,state = NORMAL)
                    

                    

                    

                  
                   

                   # self.collision = abs((((self.OvalH/2)**2)*(1-((( X - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 - ((self.planetsize**2 - ( X - (self.ovalheadway + self.UA/self.S + self.planetsize))**2)**0.5 + self.canvasy/2))#((self.planetsize**2 - (self.ovalheadway - self.planetsize)**2)**0.5 + self.canvasy/2)
                    
                  #  self.w.create_line (self.collisionx, 100,self.collisionx, 200)
                 
                   # if self.zoom >= 98:
                    #    self.zoom = 98 * (int(self.canvasy)/300)
                     #   self.ovalheadway = self.zoom
                        

                    

              


                    


                    
                    if self.phase == 1 and self.spacecraftx >= self.canvasx - self.ovalheadway - self.shipdrawchange:
                        self.phase = 2
                    elif self.phase == 2 and self.spacecraftx <= self.ovalheadway + self.shipdrawchange:
                        self.phase = 1
                        self.reset = 1
                        if self.repeat != 1:
                            self.stopall = 1
                        #self.ovalheadway = self.oldzoom
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
                       
                        #self.spacecrafty1 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 0.1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                        self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 
                    elif self.phase == 2:
                   
                        if self.reset == 1:
                            self.rl = self.rl * -1
                            self.shipl = self.shipl * -1
                            self.spacecraftx =  self.canvasx-self.ovalheadway
                            self.spacecrafty2 = self.canvasy/2
                            self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)
                            self.reset = 0
                    
                        
                        #self.spacecraftx -= self.shipdrawchange
                        
                        #self.spacecrafty1 = 1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                        self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                        self.w.delete(self.shipdraw)

                    self.shipxdis = abs(self.ovalheadway + self.UA/self.S + self.planetsize - self.spacecraftx)
                    self.shipydis = abs(self.spacecrafty2 - self.canvasy/2)
                 
                    

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
               
                    
                    

                   

                    #self.shipR = self.planetradius + self.UA
                    #self.L = (self.R + self.planetradius + self.Oshort)/2 #From planetsurface, remove self.planetradius to do from planet centre
                    self.shipV = ((self.U * (2/self.shipR - 1/self.L))**0.5)
                    self.shipVinit = self.shipV
                   

                    self.sR = self.B
                    self.sL = (self.B + self.A)/2 #From planetsurface, remove self.planetradius to do from planet centre
                    self.sVshort = (self.U * (2/self.sR - 1/self.sL))**0.5

                   

                    self.avgshipspeed = (self.V +self.sVshort)/2
                    

                    ##8000 = shipV * self.shipspeedratio
                   
                    global speedSlide

                    
                    
                    self.shipdrawchange = (self.speedSlide.get()) * ((int((self.shipV / self.avgshipspeed)*10))/10 + 0.1) * (100 / self.changeamount)
                    
                    #self.shipdrawchange = (((self.shipV*self.T**1.3) / (self.T*3000 * self.g))) * 0.8
                    #self.shipdrawchange =  (self.shipV / (self.T*200 * self.g))
          


                    if self.phase == 1:
                        self.spacecraftx += self.shipdrawchange
                        
                                
                        #
                    elif self.phase == 2:
                        self.spacecraftx -= self.shipdrawchange
                    #self.spacecrafty1 = ((self.OvalH**2)*(1 - self.spacecraftx**2/(self.canvasx/2-self.ovalheadway)**2))**0.5
                    #self.spacecrafty2 = ((self.OvalH**2)*(1 - self.spacecraftx**2/(self.canvasx/2-self.ovalheadway)**2))**0.5
                    
                   ## self.spacecrafty1 = ((((self.OvalH)**2)*(1-((self.spacecraftx-self.canvasx/2 + 0.5) + self.translate)/(self.canvasx/2-self.ovalheadway)**2))**0.5) -self.canvasy/2
                   # self.spacecrafty2 = ((((self.OvalH)**2)*(1-((self.spacecraftx-self.canvasx/2 - 0.5) + self.translate)/(self.canvasx/2-self.ovalheadway)**2))**0.5) -self.canvasy/2 #REARRANGE
                  
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
                  
                    if self.shipg >= 10000000000:
                        self.shiptextg= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Gm/s)=", round(self.shipg/1000000000,2)),font=self.ArialBg)
                    elif self.shipg >= 10000000 and (self.shipg <= 10000000000):
                        self.shiptextg= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Mm/s)=", round(self.shipg/1000000,2)),font=self.ArialBg)
                    elif self.shipg >= 10000 and (self.shipg <= 10000000):
                        self.shiptextg= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.shipg/1000,2)),font=self.ArialBg)
                    else:
                        self.shiptextg= self.w.create_text(self.canvasx-53,95 , text=("Grav(m/s)=", round(self.shipg,2)),font=self.ArialBg)

                    
                    #self.shiptextA = self.w.create_text(79  + self.x,60 + self.y, text=("Altitude(m)=", int(round(self.shipR,0))), font=self.ArialBAlt)
                    #self.shiptextg = self.w.create_text(self.canvasx-53 + self.x,95 + self.y, text=("Grav(m/s)=", round(self.shipg,2)),font=self.ArialBg)
                   # self.shiptextD = self.w.create_text(self.canvasx/2, self.canvasy/2 - 10, text=(int(self.shipR), "DIST"))
                    #self.shiptextL = self.w.create_line(self.spacecraftx,self.spacecrafty2,self.canvasx/2, self.canvasy/2)
              
                    
                    
                    self.shipdraw = self.w.create_image((self.spacecraftx + 5), self.spacecrafty2,image=self.shipImage)
                    if self.B >= self.planetradius:
                        if self.rl == 1:
                            if int(self.incline) == 0:
                                self.w.tag_lower(self.shipdraw)
                                
                                
                                self.w.tag_lower(self.planet)
                                
                                self.w.tag_lower(self.arc1)
                                self.w.tag_lower(self.arc2)
                                #self.w.tag_raise(self.shipdraw)
                                self.w.tag_lower(self.athoval)

                            elif ((self.incline) <= -90 and (self.incline) >= -180):
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

                            if int(self.incline) == 0:
                                self.w.tag_lower(self.shipdraw)
                                
                                
                                self.w.tag_lower(self.planet)
                                
                                self.w.tag_lower(self.arc1)
                                self.w.tag_lower(self.arc2)
                                #self.w.tag_raise(self.shipdraw)
                                self.w.tag_lower(self.athoval)
                            
                            elif ((self.incline) <= -90 and (self.incline) >= -180):
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

                           
                    else:
                        self.w.tag_lower(self.shipdraw)
                        
                        self.w.tag_lower(self.planet)
                        
                        self.w.tag_lower(self.arc1)
                        self.w.tag_lower(self.arc2)
                        self.w.tag_lower(self.athoval)
                        #FIX THIS RODER
                    
                

                    
            
                            
                            
                            
                           
                        
                        
                        
                        
                            
                        
                            
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

                    
                    
                    if self.stopall == 0:
                       
                        self.root.after(self.looptime, spacecraft_draw)
                    elif self.stopall != 0:
                        
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


                     

                        if self.g >= 10000000000:
                            self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Gm/s)=", round(self.g/1000000000,2)),font=self.ArialBg)
                        elif self.g >= 10000000 and (self.g <= 10000000000):
                            self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Mm/s)=", round(self.g/1000000,2)),font=self.ArialBg)
                        elif self.g >= 10000 and (self.g <= 10000000):
                            self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.g/1000,2)),font=self.ArialBg)
                        else:
                            self.gread= self.w.create_text(self.canvasx-53 ,95, text=("Grav(m/s)=", round(self.g,2)),font=self.ArialBg)
                        
                        self.spacecraftx = self.ovalheadway
                        self.spacecrafty2 = self.canvasy/2
                        self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)
                        #self.spacecrafty1 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx + 0.1 - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 #THIS WORKS
                        #self.spacecrafty2 = -1*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                        self.phase = 1
                        self.reset = 1
                        self.stopall = 0
                        self.repeat = 1
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
                        self.changeposition.configure(state = NORMAL)
                        self.animationstop.configure(background = 'silver', foreground = 'silver',borderwidth=0, state = DISABLED,disabledforeground='silver')

                        
                        
                        #self.shipdraw = self.w.create_line(self.spacecraftx,self.spacecrafty1,self.spacecraftx + 10,self.spacecrafty2, width = 15)
            
                else:
                    self.notification = "Collision Imminent."
                    self.w.create_text(self.canvasx/2, self.canvasy - 17, text=self.notification, font = self.ArialBg) #Yes I know it doubles up
              
            def zoom():

                self.zoom = self.ZoomSlide.get() * (int(self.canvasx)/300) # + 100 # self.zoom
                if (self.zoom - self.oldzoom) != 0:
                    zoomcontrol()
                    

                #if self.zoom != 0:
                self.oldzoom = self.zoom
                

                self.root.after(100, zoom)
            

            
           
                    
            

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
                
                self.tdvchangelab.grid(row = 13, column = 2, columnspan = 2, sticky = W)
                

                #self.dvchangelab.grid_remove()
                
                
                
            self.w = Canvas(self.root, width = self.canvasx, height = self.canvasy)
            self.w.pack()


  
 

            self.planetcombobox = ttk.Combobox(groot, state= 'readonly',width= 15)
            self.planetcombobox['values'] = ('Sun','Mercury', 'Venus', 'Earth', '      Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune' ,'-------', 'Kerbol', 'Moho', 'Eve', '      Gilly', 'Kerbin', '        Mun' , '        Minmus','Duna', '       Ike', 'Dres', 'Jool', '      Laythe', '      Vall', '      Tylo', '      Bop', '      Pol', 'Eeloo')
            self.planetcombobox.current(0)

            global enterbutton
            global entercorebutton
            global entermassbutton
            global enteraltbutton
            global enterorbbutton
            global enterathbutton
            global enterincbutton
            global buttonrun
            global shiprunbutton
            global bodybutton
            global entershipmass
            global changeposition
        
            self.planetcombobox.grid(column=1, row=15, columnspan = 2, sticky = E)      
            self.w.configure(background='white') #canvas background    
            self.enterbutton = Button(groot,text = "Set Velocity (m/s)", command=loopchangevel)   
            self.entercorebutton = Button(groot,text = "Set Body Radius (m)", command=loopchangecore)  
            self.entermassbutton = Button(groot,text = "Set Body Mass (kg)", command=loopchangemass)
            self.enteraltbutton = Button(groot,text = "Set Altitude (m)", command=loopchangealt)
            self.enterorbbutton = Button(groot,text = "Set Apo/Peri (m)", command=loopchangeorbit) 
            self.enterathbutton = Button(groot,text = "Set Atmosphere (m)", command=loopchangeath)
            self.enterincbutton = Button(groot,text = "Set Inclination (°)", command=loopchangeincline)
            self.buttonrun = Button(groot,text='Run!',command=looprun) #buttons can interupt loo  
            self.shiprunbutton = Button(groot,text = "Run Ship Animation", command=spacecraft_draw)
            self.resetbutton = Button(groot,text = "Reset", command=reset,background = 'silver')          
            self.bodybutton = Button(groot,text = "Confirm Body", command=planetbox)
            #self.zoominbutton = Button(self.groot, text = "Zoom In", command=zoomin)
            #self.zoomoutbutton = Button(self.groot, text = "Zoom Out", command=zoomout)
            self.entershipmass = Button(groot, text = "Optional - Confirm Mass (t)", command = shipmassset)
            self.resetdv = Button(groot, text = "Reset Total dV", command = resetdv)
            
           
        
            self.changeposition = Button(groot, text = "Warp to Apo/Peri", command = loopchangeposition)
            
            self.crootwindowopen = Button(groot, text = "Calculator", command = crootwindow)
            self.prootwindowopen = Button(groot, text = "Orbital Characteristics", command = prootwindow)
            self.frootwindowopen = Button(groot, text = "FAQ", command = frootwindow)
            self.orootwindowopen = Button(groot, text = "Glossary", command = orootwindow)
            self.mrootwindowopen = Button(groot, text = "Math", command = mrootwindow)

            global stopanimation
            def stopanimation():
                global repeat
                
                self.repeat = 0
                
                

            self.animationstop = Button(groot, text = "Stop Animation", command = stopanimation)
            self.animationstop.grid(row = 19, column = 3)
            self.animationstop.configure(background = 'silver', foreground = 'silver',borderwidth=0, state = DISABLED,disabledforeground='silver')

                
            

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
            self.PRBox.grid(row=6, column=1)
            self.MBox = Entry(groot, textvariable=self.Mdentry)
            self.MBox.grid(row=5, column=1)
            self.ABox = Entry(groot, textvariable=self.Adentry)
            self.ABox.grid(row=3, column=1)
            self.OBox = Entry(groot, textvariable=self.Odentry)
            self.OBox.grid(row=2, column=1)
            self.AtBox = Entry(groot, textvariable=self.Atdentry)
            self.AtBox.grid(row=7, column=1)
            self.PReBox = Entry(groot, textvariable=self.PReentry)
            self.PReBox.grid(row=6, column=3)
            self.MeBox = Entry(groot, textvariable=self.Meentry)
            self.MeBox.grid(row=5, column=3)
            self.AeBox = Entry(groot, textvariable=self.Aeentry)
            self.AeBox.grid(row=3, column=3)
            self.OeBox = Entry(groot, textvariable=self.Oeentry)
            self.OeBox.grid(row=2, column=3)
            self.AteBox = Entry(groot, textvariable=self.Ateentry)
            self.AteBox.grid(row=7, column=3)

            self.shipmassBox = Entry(groot, textvariable=self.shipmassentry,width= 12)
            self.shipmassBox.grid(row=20, column=1,sticky = E)
            
            
            
            self.PrLab = Label(groot, text="x10^")
            self.PrLab.grid(row=6, column=2)
            self.MLab = Label(groot, text="x10^")
            self.MLab.grid(row=5, column=2)
            self.ALab = Label(groot, text="x10^")
            self.ALab.grid(row=3, column=2)
            self.OLab = Label(groot, text="x10^")
            self.OLab.grid(row=2, column=2)
            self.AtLab = Label(groot, text="x10^")
            self.AtLab.grid(row=7, column=2)

            


            

            

            #Label(self.groot, text = "",background='silver').grid(row=11, column = 1)
            self.LINELAB1 = Label(groot, text="- - - - - - - - - - - - - - - - - Run Ship Animation - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB1.grid(row=17, column=1, columnspan = 5) #row?

            self.LINELAB3 = Label(groot, text="- - - - - - - - - - - - - - - - - - - Run Simulation - - - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB3.grid(row=10, column=1, columnspan = 5)

            self.LINELAB4 = Label(groot, text="- - - - - - - - - - - - - - - - - - - - - Navigation - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB4.grid(row=21, column=1, columnspan = 5)

            #self.SPACELAB2 = Label(groot, text=" ", font="arial", background='silver')
            #self.SPACELAB2.grid(row=17, column=3)
            
           # Label(self.groot, text = "",background='silver').grid(row=24, column = 1)
           # Label(self.groot, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",background='silver').grid(row=25, column=1, columnspan = 5)

            self.enterbutton.grid(row=1, column=4, sticky=W)
            
            self.enterorbbutton.grid(row=2, column =4, sticky=W)
            self.enterorbbutton.grid_remove()
            self.enteraltbutton.grid(row=3, column =4, sticky=W)
            self.enteraltbutton.grid_remove()
            self.SPACELAB1 = Label(groot, text="", font="arial",background='silver')
            self.SPACELAB1.grid(row=4, column=1, columnspan = 5)

            
            self.entermassbutton.grid(row=5, column=4, sticky=W)
            self.entercorebutton.grid(row=6, column=4, sticky=W)
            
            self.enterathbutton.grid(row=7, column =4, sticky=W)
            
            
            #self.enterorbbutton.grid_remove()
            
            self.enterincbutton.grid(row=9, column =4, sticky = W)
            self.buttonrun.grid(row=12, column=2, columnspan = 1)
            self.shiprunbutton.grid(row=19, column=1, columnspan = 2)
            self.resetdv.grid(row=13, column=4, columnspan = 2, sticky = W)
            self.changeposition.grid(row=12, column=4, columnspan = 2, sticky = W)
            self.changeposition.grid_remove()
            self.crootwindowopen.grid(row = 29, column = 1, columnspan = 2)
            self.prootwindowopen.grid(row = 29, column = 2, columnspan = 4, sticky = W)
            self.frootwindowopen.grid(row = 29, column = 4, columnspan = 4, sticky = W)
            self.orootwindowopen.grid(row = 29, column = 4, columnspan = 2)
            
            self.mrootwindowopen.grid(row = 29, column = 1, columnspan = 1,sticky = W)
            
            #self.zoominbutton.grid(row=8, column=1, columnspan = 3)
            #self.zoomoutbutton.grid(row=8, column=3, columnspan = 1)
            self.resetbutton.grid(row=8, column=5, columnspan = 4, sticky = W)
            #self.resetcover.grid(row=8, column=5, columnspan = 4, sticky = W)
            self.entershipmass.grid(column=2, row=20, columnspan = 2, sticky = W)

            self.InclineSlide = Scale(groot, from_=-180, to=180,length=280 ,orient=HORIZONTAL)
            self.InclineSlide.grid(row = 9, column =1 , columnspan = 4, sticky = W)

            self.ZoomSlide = Scale(groot, from_=0, to=(100),length=130)
            self.ZoomSlide.grid(row = 1, column =5 , columnspan = 1, rowspan = 6, sticky = W)

            self.zoomlab = Label(groot, text = "ZOOM",background='silver')
            self.zoomlab.grid(row = 7, column = 5)


            #Label(self.groot, text = "",background='silver').grid(row=8, column = 1)
            self.LINELAB2 =  Label(groot, text="- - - - - - - - - - - - - - - - - - - Body Selection - - - - - - - - - - - - - - - - - - -", font="arial",background='silver')
            self.LINELAB2.grid(row=14, column=1, columnspan = 5)
            
            self.bodybutton.grid(row=15, column=3, columnspan = 1, sticky=W)
            
            self.calccombust = Button(groot, text = "Close", command = grootwindowclose)
            self.calccombust.grid(row = 29, column = 5, sticky = W)
            
            
            


            
            self.waitnes = Label(groot, text =("Calculating..."), background = 'silver')
            self.waitnes.grid(row = 14, column = 1, columnspan = 3)

            

            self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
            self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

            self.dvchangelab.grid(row = 14, column = 1, columnspan = 1, sticky = W)
            self.tdvchangelab.grid(row = 14, column = 2, columnspan = 2)

            self.dvchangelab.grid_remove()
            self.tdvchangelab.grid_remove()

            self.uplab = Label(groot, text = "Spacecraft variables. ↑", background = 'silver')
            self.uplab.grid(row=4, column =1)
            self.downlab = Label(groot, text = "↓ Body variables.", background = 'silver')
            self.downlab.grid(row=4, column =3)

            self.speedLab = Label(groot, text = "Animation Speed", background = 'silver')
            self.speedLab.grid(row = 19 , column=4, columnspan = 2)

            global speedSlide

            self.speedSlide = Scale(groot, from_=1, to=(50),length=165, orient = HORIZONTAL)
            self.speedSlide.grid(row = 20, column =4 , columnspan = 2, sticky = W)

                

            


            

            
            

         
            
            
            

            
            

            
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
            global changeamount
             # make this change depending on computer speed, 1 - 1000

            self.looptime = int(1500/ self.changeamount) # as close as possible to 16.667777777777
    
            self.Vchange = 0
            self.Pchange = 0
            self.Mchange = 0
            self.Achange = 0
            self.Ichange = 0
            self.Atchange = 0
            
            self.Velfontsize = 11
            self.orbfontsize = 17
            self.Altfontsize = 11
            self.gfontsize = 8
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
            global mode
            if mode == 1:

                self.shiprunbutton.grid_remove()
                self.entershipmass.grid_remove()
                self.bodybutton.grid_remove()
                self.animationstop.grid_remove()
                self.LINELAB1.grid_remove()
                self.LINELAB2.grid_remove()
                self.LINELAB3.grid_remove()
                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()
                self.speedSlide.grid_remove()
                self.speedLab.grid_remove()
                self.shipmassBox.grid_remove()
                self.planetcombobox.grid_remove()
                self.resetdv.grid_remove()
                
                
                

            
            

            self.intVchange = 0
            self.loopcurrent -= 1 #Here to make intial frame
            self.zoom = 1
            self.oldzoom = 1
            zoom()

            planetdetails()
            
            update_frame() #This calls back and redraws objects
            
           
            
            
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


            
            #FOR SIG FIGURES

            

            
            
            
            self.w.delete("all")
            
            
            global A
            global S
            global V
            global loopvalue
            
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
            elif (SIGround(self.M, 4)) == 4515000000000000000000 and (SIGround(self.planetradius, 3)) == 320000:
                self.planetname = "Duna"
                self.planetcolor = "Sienna"
            elif (SIGround(self.M, 4)) == 2.782 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 130000:
                self.planetname = "Ike"
                self.planetcolor = "Dimgray"
            elif (SIGround(self.M, 4)) == 3.219 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 138000:
                self.planetname = "Dres"
                self.planetcolor = "Silver"
            elif (SIGround(self.M, 4)) == 4233000000000000000000000 and (SIGround(self.planetradius, 3)) == 6000000:
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
                self.planetcolor = "firebrick4"
            elif (SIGround(self.M, 4)) == 1.081 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 44000:
                self.planetname = "Pol"
                self.planetcolor = "Moccasin"
            elif (SIGround(self.M, 4)) == 1.115 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 210000:
                self.planetname = "Eeloo"
                self.planetcolor = "Whitesmoke"

            elif self.planetcombobox.current() == 9:

                self.planetname = "Neptune"
                self.planetcolor = "royalblue"

            elif self.planetcombobox.current() == 18:

                self.planetname = "Duna"
                self.planetcolor = "Sienna"

            elif self.planetcombobox.current() == 21:
                self.planetname = "Jool"
                self.planetcolor = "OliveDrab"

            
            else:
                self.planetname = "Custom"
                self.planetcolor = "SlateGray"

            
                            
            self.V = abs(self.V) #FORCE NON NEGATIVES
 
           
            self.loopvaluechange = 0
            
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
          
            self.D =  self.L/self.tH
            self.OvalH = (self.canvasx-self.ovalheadway*2)/self.D
            self.T = (2*math.pi * (( (self.L ** 3)/ self.U )**0.5)) #DONT KNOW
            self.Ec = self.E/self.L

            
	    

            
            

            

            

            if self.M >= 1000000000000000000000000000:
                self.dM = self.M / 1000000000000000000000000 
                self.pdsign = 'Ykg'
            elif self.M >= 1000000000000000000000000:
                self.dM = self.M / 1000000000000000000000
                self.pdsign = 'Zkg'
            elif self.M >= 1000000000000000000000:
                self.dM = self.M / 1000000000000000000 
                self.pdsign = 'Ekg'
            elif self.M >= 1000000000000000000:
                self.dM = self.M / 1000000000000000
                self.pdsign = 'Pkg'
            elif self.M >= 1000000000000000:
                self.dM = self.M / 1000000000000
                self.pdsign = 'Tkg'
            elif self.M >= 1000000000000000:
                self.dM = self.M / 1000000000000
                self.pdsign = 'Gkg'


            
            
                

      
            self.miniplanet = self.planetradius/ (self.H / 55)
            
            self.LineLength = 1/((self.planetradius/44.26)/self.H)
 
            
        
            
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
                
            
            self.ox1 = self.ovalheadway
            self.oy1 = self.canvasy/2 - self.OvalH/2
            self.ox2 = self.canvasx - self.ovalheadway #STICK THIS BACK INTO CODE
            self.oy2 = self.canvasy/2 + self.OvalH/2
            self.spacecraftx = self.ovalheadway
            self.spacecrafty2 = self.canvasy/2
           

            
        
            
            self.athoval = self.w.create_oval(self.ovalheadway + (self.UA-self.atmospheresize)/self.S,self.canvasy/2 - self.planetsize - self.atmospheresize/self.S,self.ovalheadway + (self.UA+self.atmospheresize)/self.S + 2 * self.planetsize,self.canvasy/2 + self.planetsize + self.atmospheresize/self.S, fill = "skyblue", outline = "") #Athmosphere
            self.planet = self.w.create_oval(self.ovalheadway + self.UA/self.S,self.canvasy/2 - self.planetsize,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize,self.canvasy/2 + self.planetsize, fill = self.planetcolor , outline = "") #Planet
            self.w.create_oval(self.ovalheadway + self.A - self.planetradius/10, self.canvasy/2 - self.planetradius/10,self.ovalheadway + self.UA + self.A + self.planetradius/10,self.canvasy/2 + self.planetradius/10, fill = 'red' , outline = "") #Planetcaps
            self.arc1 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit\
            self.arc2 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  -180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit\
            #self.w.create_oval(self.ox1,self.oy1,self.ox2,self.oy2,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3) # Orbit\
          
            if self.B >= self.planetradius:
                if ((self.incline) <= -90 and (self.incline) >= -180):
                    self.w.tag_raise(self.arc1)
                   
                    self.w.tag_lower(self.arc2)

                elif ((self.incline) <= 0 and (self.incline) >= -90):
                    self.w.tag_raise(self.arc2)
            
                    self.w.tag_lower(self.arc1)
            

                elif (((self.incline) >= 0 and (self.incline) <= 90)):

                    self.w.tag_raise(self.arc1)
                   
                    self.w.tag_lower(self.arc2)

                elif (((self.incline) >= 90 and (self.incline) <= 180)):
                    self.w.tag_raise(self.arc2)
                
                    self.w.tag_lower(self.arc1)
                else:
                    self.w.tag_lower(self.arc1)
                    self.w.tag_lower(self.arc2)
                    
                    
                

            
                    
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

            self.w.create_oval(self.ovalheadway + self.UA/self.S +  self.planetsize  + self.planetsize  * 0.01, self.canvasy/2 + self.planetsize* 0.01 ,self.ovalheadway + self.UA/self.S +self.planetsize -  self.planetsize * 0.01, self.canvasy/2 -   self.planetsize* 0.01,fill="maroon", outline = '')

            
            self.w.create_text(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy/2 + 20 , text=self.planetname, font = self.ArialBVel) #planetname

            


            #if (self.ovalheadway + self.UA/self.S + self.planetsize  + self.x) >= (self.canvasx/2):
                #self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  + self.x
            self.planetdetailsy = (self.canvasy / (self.planetsize / 1300 + 2)) -  80
       

            #else:
                
                #self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  + self.x + 150
                #self.planetdetailsy = self.canvasy/2 + self.y - self.planetsize*1.3 + self.planetsize - 50


            self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  - self.planetsize/4 + 100 # CHAGNE LAST VALUE LESSE AGGRESSIVE


            
           
            self.w.create_text(self.planetdetailsx, self.planetdetailsy - 20, text=("Mass=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (SIGround(self.dM, 4))))), self.pdsign), font = self.ArialBg) #planetdetails
            self.w.create_text(self.planetdetailsx, self.planetdetailsy, text=("Body_Radius=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.planetradius,1))))), "m"), font = self.ArialBg) #planetdetails
            self.w.create_text(self.planetdetailsx, self.planetdetailsy + 20, text=("Atmosphere_Altitude=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.atmospheresize,1))))), "m"), font = self.ArialBg) 
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize  , self.canvasy/2  - 20, self.planetdetailsx, self.planetdetailsy + 30 , width = 1) #TO PLANETDETAILS

            
            self.w.create_text(self.canvasx/2  , self.canvasy  - self.canvasy/100 - 10 , text=("Orbit_length=", ((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(2*self.L,1))))), "m"), font = self.ArialBg) #orbit text
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize)/2 + self.ovalheadway/2  , self.canvasy  - self.canvasy/100 - 50 , text = (self.periv , ((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.A,1))))),"m"), font = self.ArialBg) #A
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize + self.canvasx - self.ovalheadway)/2  , self.canvasy  - self.canvasy/100 - 90 , text = (self.apov,((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.B,1))))),"m"), font = self.ArialBg) # B
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

            if self.g >= 10000000000:
                self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Gm/s)=", round(self.g/1000000000,2)),font=self.ArialBg)
            elif self.g >= 10000000 and (self.g <= 10000000000):
                self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(Mm/s)=", round(self.g/1000000,2)),font=self.ArialBg)
            elif self.g >= 10000 and (self.g <= 10000000):
                self.gread= self.w.create_text(self.canvasx-53 ,95 , text=("Grav(km/s)=", round(self.g/1000,2)),font=self.ArialBg)
            else:
                self.gread= self.w.create_text(self.canvasx-53 ,95, text=("Grav(m/s)=", round(self.g,2)),font=self.ArialBg)
           # self.w.create_text(self.canvasx-53 + ,195 + self.y, text=("Cp Force(Nm^2/kg^2)=", round(self.Fn,2)),font=self.ArialBg)
            self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)



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
       
           # self.tri3 = self.canvasx - 125 +  (self.hypot * ( math.cos (self.theta1)))
           # self.tri4 = (self.canvasy -125) + (self.hypot * ( math.sin (self.theta1)))
            #self.tri5 = self.canvasx - 125 +  (self.hypot * ( math.cos (self.theta2)))
           # self.tri6 =  (self.canvasy -125) + (self.hypot * ( math.sin (self.theta2)))
            #if int(abs(self.dvchange)) != 0:
             #   self.w.create_text(self.canvasx/2, self.canvasy/2 + 100, text = ("F=",int(abs(self.dvchange)),"m/s"), font = self.ArialBVel)

            #if int(abs(self.tdvchange)) != 0:
            #self.w.create_text(self.canvasx/2, self.canvasy/2 + 150, text = ("tdV_Change=",int(abs(self.tdvchange)),"m/s"), font = self.ArialBVel)

       
            if self.miniplanet <= 44.26:
            

                self.w.create_oval(self.canvasx - 125+ self.miniplanet, self.canvasy -125 + self.miniplanet, self.canvasx - 125- self.miniplanet, self.canvasy -125 - self.miniplanet, fill = self.planetcolor, outline = "")
                self.w.create_arc(self.canvasx - 85, self.canvasy -85 , self.canvasx - 165, self.canvasy -165, extent = -1 * self.incline, width = 2, style = ARC)
                self.w.create_line(self.canvasx - 200, self.canvasy -125, self.canvasx - 50, self.canvasy -125, width = 3, fill = "darkred", dash = (20,5))
                self.w.create_line(self.canvasx - 125 +  (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) + (55 * ( math.sin (self.incline *( math.pi/180)))) , self.canvasx - 125 - (55 * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) - (55 * ( math.sin (self.incline *( math.pi/180)))), fill = "dodgerblue" , width = 3)
                #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4 + 10,self.tri3 , self.tri4 - 10, width = 100, fill="red")
                #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4,self.tri5, self.tri6, width = 100, fill="steelblue")
                self.w.create_polygon(self.canvasx - 125 +  (40 * ( math.cos (self.incline *( math.pi/180)))),(self.canvasy -125) + (40 * ( math.sin (self.incline *( math.pi/180)))),self.canvasx - 125 +  ((10**2 + 30**2)**0.5 * ( math.cos (math.asin (10/30) + (self.incline *( math.pi/180))))),(self.canvasy -125) + ((10**2 + 30**2)**0.5 * ( math.sin (math.asin (10/30) + (self.incline *( math.pi/180))))),self.canvasx - 125 +  ((10**2 + 30**2)**0.5 * ( math.cos (math.asin (-10/30) + (self.incline *( math.pi/180))))), (self.canvasy -125) + ((10**2 + 30**2)**0.5* ( math.sin (math.asin (-10/30) + (self.incline *( math.pi/180))))), width = 100, fill="deep sky blue")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 - self.miniplanet,self.canvasx -130, self.canvasy -140 - self.miniplanet,self.canvasx -120, self.canvasy -140 - self.miniplanet, fill="maroon")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 + self.miniplanet,self.canvasx -130, self.canvasy -110 + self.miniplanet,self.canvasx -120, self.canvasy -110 + self.miniplanet, fill="maroon")

                #self.w.create_polygon((0, 200, 50, 0, 100, 100), fill="red")
                self.w.create_text (self.canvasx - 170, self.canvasy -56 , text =("Orbital Inclination ="), justify = LEFT, font = self.ArialBi)
                self.w.create_text (self.canvasx - 100, self.canvasy -56 , text =((-1 *( round(self.incline, 1)))), justify = LEFT, font = self.ArialBi)
            else:
               
                self.w.create_oval(self.canvasx - 125+ 44.26, self.canvasy -125 + 44.26, self.canvasx - 125- 44.26, self.canvasy -125 - 44.26, fill = self.planetcolor, outline = "")
                self.w.create_arc(self.canvasx - 85, self.canvasy -85 , self.canvasx - 165, self.canvasy -165, extent = -1 * self.incline, width = 2, style = ARC)
                self.w.create_line(self.canvasx - 200, self.canvasy -125, self.canvasx - 50, self.canvasy -125, width = 3, fill = "darkred", dash = (20,5))
                self.w.create_line(self.canvasx - 125 +  (self.LineLength * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) + (self.LineLength * ( math.sin (self.incline *( math.pi/180)))) , self.canvasx - 125 - (self.LineLength * ( math.cos (self.incline *( math.pi/180)))), (self.canvasy -125) - (self.LineLength * ( math.sin (self.incline *( math.pi/180)))), fill = "dodgerblue" , width = 3)
                #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4 + 10,self.tri3 , self.tri4 - 10, width = 100, fill="red")
                #self.w.create_polygon(self.tri1,self.tri2,self.tri3 ,self.tri4,self.tri5, self.tri6, width = 100, fill="steelblue")
                    #self.shrink = 2
                
                self.shrink = self.LineLength / 150
      
               # if self.LineLength >= 1:
               #     self.shrink = 0.5
               # else:
               #     self.shrink = 2
                self.w.create_polygon(self.canvasx - 125 +  (((self.shrink*1.65) * self.LineLength+10) * ( math.cos (self.incline *( math.pi/180)))),(self.canvasy -125) + (((self.shrink*1.65) * self.LineLength+10) * ( math.sin (self.incline *( math.pi/180)))),self.canvasx - 125 +  ((10**2 + (self.shrink*self.LineLength+10)**2)**0.5 * ( math.cos (math.asin (10/(self.shrink * self.LineLength+10)) + (self.incline *( math.pi/180))))),(self.canvasy -125) + ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5 * ( math.sin (math.asin (10/(self.shrink * self.LineLength+10)) + (self.incline *( math.pi/180))))),self.canvasx - 125 +  ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5 * ( math.cos (math.asin (-10/(self.shrink * self.LineLength+10)) + (self.incline *( math.pi/180))))), (self.canvasy -125) + ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5* ( math.sin (math.asin (-10/(self.shrink* self.LineLength+10)) + (self.incline *( math.pi/180))))), width = 100, fill="deep sky blue")

                #self.w.create_polygon(self.canvasx - 125 +  ((1250/self.LineLength) * ( math.cos (self.incline *( math.pi/180)))),(self.canvasy -125) + ((1250/self.LineLength) * ( math.sin (self.incline *( math.pi/180)))),self.canvasx - 125 +  ((10**2 + (750/self.LineLength)**2)**0.5 * ( math.cos (math.asin (10/(750/self.LineLength)) + (self.incline *( math.pi/180))))),(self.canvasy -125) + ((10**2 + (750/self.LineLength)**2)**0.5 * ( math.sin (math.asin (10/(750/self.LineLength)) + (self.incline *( math.pi/180))))),self.canvasx - 125 +  ((10**2 + (750/self.LineLength)**2)**0.5 * ( math.cos (math.asin (-10/(750/self.LineLength)) + (self.incline *( math.pi/180))))), (self.canvasy -125) + ((10**2 + (750/self.LineLength)**2)**0.5* ( math.sin (math.asin (-10/(750/self.LineLength)) + (self.incline *( math.pi/180))))), width = 100, fill="royalblue")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 - 44.26,self.canvasx -130, self.canvasy -140 - 44.26,self.canvasx -120, self.canvasy -140 - 44.26, fill="maroon")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 + 44.26,self.canvasx -130, self.canvasy -110 + 44.26,self.canvasx -120, self.canvasy -110 + 44.26, fill="maroon")

                 

                #self.w.create_polygon((0, 200, 50, 0, 100, 100), fill="red")
                self.w.create_text (self.canvasx - 170, self.canvasy -56 , text =("Orbital Inclination ="), justify = LEFT, font = self.ArialBi)
                self.w.create_text (self.canvasx - 100, self.canvasy -56 , text =((-1 *( round(self.incline, 1)))), justify = LEFT, font = self.ArialBi)

            
            

            
            self.loopcurrent += 1

            
           
        
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
                self.changeposition.configure(state = NORMAL)

                


                #
                

                self.dvchangelab.grid_remove()
                self.tdvchangelab.grid_remove()
                
            
                

                
                userchangeclean()

                if self.prootopen == 1:
                    self.sua =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.UA,1))),"m"))
                    self.sua.grid(row=2, column = 1, sticky=W, columnspan = 3)
                    self.sa =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.A,1))),"m"))
                    self.sa.grid(row=3, column = 1, sticky=W, columnspan = 3)
                    self.sm =Label(self.proot, text=(round(self.M,1),"kg"))
                    self.sm.grid(row=6, column = 1, sticky=W, columnspan = 3)
                    self.sv =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.V,1))),"m/s"))
                    self.sv.grid(row=5, column = 1, sticky=W, columnspan = 3)
                    self.su =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.U,1))),"m^3/s"))
                    self.su.grid(row=7, column = 1, sticky=W, columnspan = 2)
                    self.sb =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.B,1))),"m"))
                    self.sb.grid(row=4, column = 1, sticky=W, columnspan = 3)
                    self.sl =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.L,1))),"m"))
                    self.sl.grid(row=8, column = 1, sticky=W, columnspan = 3)
                    self.se =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.E,1))),"m"))
                    self.se.grid(row=9, column = 1, sticky=W, columnspan = 3)
                    self.sh =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.H,1))),"m"))
                    self.sh.grid(row=10, column = 1, sticky=W, columnspan = 3)
                    self.sp =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.T,1))),"s"))
                    self.sp.grid(row=11, column = 1, sticky=W, columnspan = 3)
                    self.sd =Label(self.proot, text=((round(self.Ec,1))))
                    self.sd.grid(row=12, column = 1, sticky=W, columnspan = 3)
                    self.sev =Label(self.proot, text=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.eV,1))), "m/s"))
                    self.sev.grid(row=13, column = 1, sticky=W, columnspan = 3)
                   
                    
                    
                    self.suat =Label(self.proot, text=("Radar Altitude"))
                    self.suat.grid(row=2, column = 3, sticky=W, columnspan = 3)
                    
                    
                    self.smt =Label(self.proot, text=("Body Mass"))
                    self.smt.grid(row=6, column = 3, sticky=W, columnspan = 3)
                    self.svt =Label(self.proot, text=("Spacecraft Velocity"))
                    self.svt.grid(row=5, column = 3, sticky=W, columnspan = 3)
                    self.sut =Label(self.proot, text=("Gravational Parameter"))
                    self.sut.grid(row=7, column = 3, sticky=W, columnspan = 3)

                    if self.A >= self.B:
                        self.sbt =Label(self.proot, text=("Periapsis"))
                        self.sat =Label(self.proot, text=("Apoapsis"))

                    else:
                        self.sbt =Label(self.proot, text=("Apoapsis"))
                        self.sat =Label(self.proot, text=("Periapsis"))
                    self.sat.grid(row=3, column = 3, sticky=W, columnspan = 3)
                    self.sbt.grid(row=4, column = 3, sticky=W, columnspan = 3)
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
                    self.sevt =Label(self.proot, text=("Escape Velocity"))
                    self.sevt.grid(row=13, column = 3, sticky=W, columnspan = 3)

                                      

                    



                   

                    

                    

                    
                    self.waitmes.grid_remove()
                    
                global changeposition
                global enterorbbutton
                global enteraltbutton
                self.changeposition.grid_remove()
                self.enterorbbutton.grid_remove()
                self.enteraltbutton.grid_remove()
                
                global loopchangeposition
                global loopchangeorbit
                global loopchangealt
                
                if self.A >= self.B:

                    

                    
                    

                    self.changeposition = Button(groot, text = "Warp to Periapsis", command = loopchangeposition)
                    self.enterorbbutton = Button(groot,text = "Set Periapsis (m)", command=loopchangeorbit)
                    self.enteraltbutton = Button(groot,text = "Set Apoapsis (m)", command=loopchangealt)
                    
                else:
                    
                    
                    self.changeposition = Button(groot, text = "Warp to Apoapsis", command = loopchangeposition)
                    self.enterorbbutton = Button(groot,text = "Set Apoapsis (m)", command=loopchangeorbit)
                    self.enteraltbutton = Button(groot,text = "Set Periapsis (m)", command=loopchangealt)
                    
                self.changeposition.grid(row=12, column=4, columnspan = 2, sticky = W)
                self.enterorbbutton.grid(row=2, column =4, sticky=W)
                self.enteraltbutton.grid(row=3, column =4, sticky=W)

                if self.first != 1:
                
                    


                    self.dvchangelab = Label(groot, text =( "Delta_V=" , abs(round(self.dvchange,1))))
                    self.tdvchangelab = Label(groot, text =( "Total_Delta_V=",abs(round(self.tdvchange,1))))

                    self.dvchangelab.grid(row = 13, column = 1, columnspan = 1, sticky = W)
                    self.tdvchangelab.grid(row = 13, column = 2, columnspan = 2, sticky = W)

                    global mode
                    if mode == 1:
                        self.dvchangelab.grid_remove()
                        self.tdvchangelab.grid_remove()

            
                   
                    
                    self.resetbutton.configure(background = 'silver', foreground = 'silver',borderwidth=0, state = DISABLED,disabledforeground='silver')

                    #self.button = Button(groot,text='Run!',command=looprun())

                    
                    #self.button.grid()
                else:
                    self.first += 1
                    
                
                self.waitnes.grid_remove()
            
            
            
        
            
        def tutwindowopen():

            global nextbutton
            global backbutton
            global PhotoLabel
            
            tutroot = Toplevel()

            def tutrootwindowclose():
                tutroot.destroy()
                global tutrootopen
                tutrootopen = 0
            tutcombust = Button(tutroot, text = "Close", command = tutrootwindowclose)
            tutcombust.grid(row = 200, column = 1, columnspan = 1,sticky = W)
            
            
            tutroot.protocol('WM_DELETE_WINDOW',tutrootwindowclose)
            tutroot.configure(background = 'silver')
       
            tutroot.wm_title("Tutorial")
            tutroot.resizable(0,0)

            self.slideshow = 0

            # Pictures
            #Basic
                #Basic menu
                # next then buttons
                # next then orbital menu
            #Types of windows
                #gloss
                #next
                #next
            #Full control window
                                          
            def resetslide():
                global currenttutmenu
                global CurrentImage
                global PhotoLabel
                print (self.slideshow)
                if currenttutmenu == 1:
                
                    if self.slideshow == 1:
                        CurrentImage= PhotoImage(file="BASICMISSIONTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = DISABLED)
                    elif self.slideshow ==2:
                        CurrentImage= PhotoImage(file="VARMISSIONTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = NORMAL)
                    elif self.slideshow ==3:
                        CurrentImage= PhotoImage(file="DISPLAYTUT.png")
                        self.nextbutton.configure(state = DISABLED)
                        self.backbutton.configure(state = NORMAL)
                
                elif currenttutmenu == 2:
                
                    if self.slideshow == 1:
                        CurrentImage= PhotoImage(file="MATHTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = DISABLED)
                    elif self.slideshow ==2:
                        CurrentImage= PhotoImage(file="CALCTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = NORMAL)
                    elif self.slideshow ==3:
                        CurrentImage= PhotoImage(file="ORBTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = NORMAL)
                    elif self.slideshow ==4:
                        CurrentImage= PhotoImage(file="FAQTUT.png")
                        self.nextbutton.configure(state = NORMAL)
                        self.backbutton.configure(state = NORMAL)
                    elif self.slideshow ==5:
                        CurrentImage= PhotoImage(file="GLOSSTUT.png")
                        self.nextbutton.configure(state = DISABLED)
                        self.backbutton.configure(state = NORMAL)
                elif currenttutmenu == 3:
                    
                
                    if self.slideshow == 1:
                        CurrentImage= PhotoImage(file="FULLMISISONTUT.png")
                        self.backbutton.configure(state = DISABLED)
                        self.nextbutton.configure(state = DISABLED)
                        

                PhotoLabel.grid_remove()
                PhotoLabel = Label(tutroot, image=CurrentImage)
                PhotoLabel.CurrentImage = CurrentImage
                PhotoLabel.grid(row = int((10 * currenttutmenu) + 8), column = 2)
                PhotoLabel.configure(background = 'silver')
                        
                
                  
                

            def plusone():
                if currenttutmenu == 1:
                    if self.slideshow <= 2:
                        self.slideshow += 1
                elif currenttutmenu == 2:
                    if self.slideshow <= 4:
                        self.slideshow += 1

                print (self.slideshow)
                        
                resetslide()

            def minusone():
                
                if self.slideshow >= 2:
                    self.slideshow -= 1
                        
                print (self.slideshow)
                resetslide()

            def basictut():
                global nextbutton
                global backbutton
                global PhotoLabel
                global currenttutmenu
                global CurrentImage
                currenttutmenu = 1
                self.slideshow = 1
                resetslide()
                self.nextbutton.grid_remove()
                self.backbutton.grid_remove()
                HintLabel.grid_remove()
                #PhotoLabel.grid_remove()

                
                
                

                self.backbutton = Button(tutroot, text='Back',command = minusone)
                self.backbutton.grid(row=19,column=1,columnspan = 2)

                self.nextbutton = Button(tutroot, text='Next',command = plusone)
                self.nextbutton.grid(row=19,column=2, columnspan = 2)

                self.nextbutton.configure(state = NORMAL)
                self.backbutton.configure(state = DISABLED)

                

                
                
            def windowtut():
                global nextbutton
                global backbutton
                global PhotoLabel
                global currenttutmenu
                global CurrentImage
                currenttutmenu = 2
                self.slideshow = 1
                resetslide()
                self.nextbutton.grid_remove()
                self.backbutton.grid_remove()
                HintLabel.grid_remove()
                #PhotoLabel.grid_remove()

                
                
                

                self.backbutton = Button(tutroot, text='Back',command = minusone)
                self.backbutton.grid(row=29,column=1,columnspan = 2)

                self.nextbutton = Button(tutroot, text='Next',command = plusone)
                self.nextbutton.grid(row=29,column=2, columnspan = 2)

                self.nextbutton.configure(state = NORMAL)
                self.backbutton.configure(state = DISABLED)

                
             
            
            def allcommand():
                global nextbutton
                global backbutton
                global PhotoLabel
                global currenttutmenu
                global CurrentImage
                currenttutmenu = 3
                self.slideshow = 1
                resetslide()
                self.nextbutton.grid_remove()
                self.backbutton.grid_remove()
                HintLabel.grid_remove()
                #PhotoLabel.grid_remove()

                
                
                #self.nextbutton = Button(tutroot, text='Next',command = plusone)
                #self.nextbutton.grid(row=39,column=2)

                #self.backbutton = Button(tutroot, text='Back',command = minusone)
                #self.backbutton.grid(row=39,column=1,columnspan = 2)

                

                
                

            self.Basicbutton = Button(tutroot, text = 'Basic Window Controls', command = basictut)
            self.Basicbutton.grid(row = 10, column = 1,sticky = W)
            
            self.Windowbutton = Button(tutroot, text = 'Miscellaneous Window Controls', command = windowtut)
            self.Windowbutton.grid(row = 20, column = 1,sticky = W)

            self.Allbutton = Button(tutroot, text = 'Advanced Window Controls', command = allcommand)
            self.Allbutton.grid(row = 30, column = 1,sticky = W)

            self.nextbutton = Button(tutroot, text='Next',command = plusone)
            self.nextbutton.grid(row=100,column=2)

            self.backbutton = Button(tutroot, text='Back',command = minusone)
            self.backbutton.grid(row=100,column=1)

            self.nextbutton.grid_remove()
            self.backbutton.grid_remove()

            
            CurrentImage= PhotoImage(file="MENUEARTH.png")
            
            PhotoLabel = Label(tutroot, image=CurrentImage)
            PhotoLabel.CurrentImage = CurrentImage
            PhotoLabel.grid(row = 1, column = 3,rowspan = 1000)
            PhotoLabel.configure(background = 'silver')
            PhotoLabel.grid_remove()

            HintImage= PhotoImage(file="TUThints.png")
                
            HintLabel = Label(tutroot, image=HintImage)
            HintLabel.HintImage = HintImage
            HintLabel.grid(row = 10, column = 3, rowspan =30)
            HintLabel.configure(background = 'silver')
            

            

            #webbrowser.open('http://reddit.com/r/youdontsurf')
            
        def orbitcalccommand():
            global orbitcalcopen
           
            if orbitcalcopen == 0:
                
                
                orbitcalcopen = 1
                
                
                
                orbitcalc()
                
            
        
        global credrootwindow
        
        def credrootwindow():
            global credrootwindow

            global credrootopen
            if credrootopen == 0:
           
                
                credrootopen = 1
                global credroot

                credroot = Toplevel()

                def credrootwindowclose():
                    credroot.destroy()
                    global credrootopen
                    credrootopen = 0
                credroot.protocol('WM_DELETE_WINDOW',credrootwindowclose)
                
                credroot.configure(background = 'silver')
                credroot.wm_title("Credits")

                Label(credroot, text = "Martin Lambrechtse - Reid", background = 'silver').grid(row = 1,column = 1)
                Label(credroot, text = "", background = 'silver').grid(row = 2,column = 1)
                Label(credroot, text = "Created on Python 3 as a demonstration on Celestial Mechanics", background = 'silver').grid(row = 3,column = 1)
                Label(credroot, text = "to L3 NCEA students. This script is free to be edited as long", background = 'silver').grid(row = 4,column = 1)
                Label(credroot, text = "as credit is given. This project has been created to comply", background = 'silver').grid(row = 5,column = 1)
                Label(credroot, text = "with NCEA unit standard AS91354 and AS91370. This program was created", background = 'silver').grid(row = 6,column = 1)
                Label(credroot, text = "created by a L2 student that is fascinated by space and its theory.", background = 'silver').grid(row = 7,column = 1)
                Label(credroot, text = "", background = 'silver').grid(row = 8,column = 1)
                Label(credroot, text = "Assumptions:", background = 'silver').grid(row = 50,column = 1,sticky = W)
                Label(credroot, text = "•The spacecraft exherts no gravational pull on the body it orbits.", background = 'silver').grid(row = 51,column = 1,sticky = W)
                Label(credroot, text = "•Langrange points are not modelled.", background = 'silver').grid(row = 52,column = 1,sticky = W)
                Label(credroot, text = "•No external forces are acting.", background = 'silver').grid(row = 53,column = 1,sticky = W)
                Label(credroot, text = "•Number rounding is used when displaying, usually 4 s.f. or 1-2 dp.", background = 'silver').grid(row = 54,column = 1,sticky = W)
                Label(credroot, text = "•The default atmosphere height is 100km, based on the Karman line.", background = 'silver').grid(row = 55,column = 1,sticky = W)
                Label(credroot, text = "•Atmospheres are not changed when changing body like mass or radius.", background = 'silver').grid(row = 56,column = 1,sticky = W)
                Label(credroot, text = "•Orbit speed of spacecraft is scaled down.", background = 'silver').grid(row = 57,column = 1,sticky = W)
                Label(credroot, text = "•No SOI radius implented. It's possible to make an orbit 'too big'.", background = 'silver').grid(row = 58,column = 1,sticky = W)
                Label(credroot, text = "•A very small inaccuracy is present, but very minute.", background = 'silver').grid(row = 59,column = 1,sticky = W)
                Label(credroot, text = "", background = 'silver').grid(row = 99, column = 1,sticky = W)
                Label(credroot, text = "Known bugs:", background = 'silver').grid(row = 100,column = 1,sticky = W)
                Label(credroot, text = "•The spacecraft animation freezes the script at low resolutions & high zoom.", background = 'silver').grid(row = 101,column = 1,sticky = W)
                Label(credroot, text = "••Fix - Close and reopen script. Use a lower zoom level next time.", background = 'silver').grid(row = 102,column = 1,sticky = W)
                #Label(credroot, text = "", background = 'silver').grid(row = 103,column = 1,sticky = W)
                Label(credroot, text = "•Orbital Window goes white when changing altitude too much.", background = 'silver').grid(row = 103,column = 1,sticky = W)
                Label(credroot, text = "••Cause - Orbit exceeds escape velocity and therefore cannot physically exist.", background = 'silver').grid(row = 104,column = 1,sticky = W)
                Label(credroot, text = "••Fix - Click the red reset button.", background = 'silver').grid(row = 105,column = 1,sticky = W)
                #Label(credroot, text = "", background = 'silver').grid(row = 107,column = 1,sticky = W)
                Label(credroot, text = "•Inclination animates -170° to 170° the long way rather than the short.", background = 'silver').grid(row = 108,column = 1,sticky = W)
                Label(credroot, text = "••Fix - None, it's a visual bug. Delta V calculations work properly.", background = 'silver').grid(row = 109,column = 1,sticky = W)
                #Label(credroot, text = "", background = 'silver').grid(row = 110,column = 1,sticky = W)
                Label(credroot, text = "•Neptune in planet selection gives a long decimal string rather than 4 s.f.", background = 'silver').grid(row = 111,column = 1,sticky = W)
                Label(credroot, text = "••Cause - Sometimes 1=/= 1 due to the way floating point numbers work.", background = 'silver').grid(row = 112,column = 1,sticky = W)
                Label(credroot, text = "••Fix - It is as inaccurate as anything else due to computing rounding errors.", background = 'silver').grid(row = 113,column = 1,sticky = W)
                
                




                
                Label(credroot, text = "", background = 'silver').grid(row = 499, column = 1)
                credcombust = Button(credroot, text = "Close", command = credrootwindowclose)
                credcombust.grid(row = 500, column = 1)
                
        def orbittutcommand():
           
            global tutrootopen
            if tutrootopen == 0:
                
                tutrootopen = 1
                tutwindowopen()

        def optionmenu():
            global oprootopen
            
            if oprootopen == 0:
           
              
                oprootopen = 1

                #def fullscreen():
                #    global P
                #    P = 1.1
                #    
                #def halfscreen():
                    #global P
                    #P = 2
                   
                def fullscreen():
           
                 

                    global tcanvasx
                    global tcanvasy

                    global reschange
                    global fullscreen
                    fulopen.configure(state=DISABLED)
                    winopen.configure(state=NORMAL)

                    reschange = 1
                    fullscreen = 1
                    

                    global root

                  

         

                    tcanvasx = oproot.winfo_screenwidth()
                    tcanvasy = oproot.winfo_screenheight()
                    currentres()

                def windowed():
           
                 

                    global tcanvasx
                    global tcanvasy

                    global reschange
                    global fullscreen

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)

                    reschange = 1
                    fullscreen = 0
                    currentres()
                    

                    
             

                def resscreen():

                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0
                 
                    
                    tcanvasx = abs(int(self.xBox.get()))
                    tcanvasy = abs(int(self.yBox.get()))
                    if abs(int(tcanvasy)) <= 400:
                        tcanvasy = 400 #TEMP NUMBER
                      
                   
                        
                 

                    if abs(int(tcanvasx)) <= 400:
                        tcanvasx = 400 #TEMP NUMBER
                 
                        
                     

                    self.xBox.grid_remove()
                    self.yBox.grid_remove()
                    global resset
                    resset.grid_remove()
                    currentres()

                def autoscreen():

                    global tcanvasx
                    global tcanvasy

                    global reschange
                    global fullscreen
               

                    reschange = 1
                    fullscreen = 0
                    

                    global root
                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)

                    


                    tcanvasx = oproot.winfo_screenwidth()/1.3
                    tcanvasy = oproot.winfo_screenheight()/1.3
                    currentres()
                    

            

                def custombox():
                    self.xBox = Entry(oproot, textvariable=desxres, width = 25)
                    self.xBox.grid(row=6, column=1, columnspan = 2, sticky = W)

                    self.yBox = Entry(oproot, textvariable=desyres, width = 25)
                    self.yBox.grid(row=7, column=1, columnspan = 2, sticky = W)
                    global resset

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)

                    resset = Button(oproot, text="Confirm Resolution", command=resscreen)
                    resset.grid(row = 6, column = 3, columnspan = 2, rowspan = 2, sticky = W)

                def r960x540():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                   
                    
                    tcanvasx = 960
                    tcanvasy = 540
                    currentres()
                def r1280x720():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                   
                    
                    tcanvasx = 1280
                    tcanvasy = 720
                    currentres()
                def r1366x768():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                   
                    
                    tcanvasx = 1366
                    tcanvasy = 768
                    currentres()

                def r1600x900():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                   
                    
                    tcanvasx = 1600
                    tcanvasy = 900
                    currentres()
                def r1920x1080():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                    
                   
                    
                    tcanvasx = 1920
                    tcanvasy = 1080
                    currentres()
                def r2560x1440():
                    global tcanvasx
                    global tcanvasy
                    global reschange
                    global fullscreen
                    reschange = 1
                    fullscreen = 0

                    fulopen.configure(state=NORMAL)
                    winopen.configure(state=DISABLED)
                   
                    
                    tcanvasx = 2560
                    tcanvasy = 1440
                    currentres()
                    
                def oprootwindowclose():
                    oproot.destroy()
                    global oprootopen
                    oprootopen = 0
                    
                    
                    #
                def currentres():
                    global tcanvasx
                    global tcanvasy
                    global reslab
                    global fullscreen
                    if fullscreen == 0:
                        self.message = "Windowed"
                    else:
                        self.message = "Fullscreen"
                    self.reslab.grid_remove()
                    self.reslab = Label(oproot,text = ("Current_Resolution=", int(tcanvasx),"x",int(tcanvasy),"@", self.message))
                    self.reslab.grid(row=39,column = 1, columnspan =4, sticky = W)

                def animationoverride():
                    global changeamount

                    self.changeamount = AmountSlide.get()
                    print (self.changeamount)

               
                    
                global oproot
                oproot = Toplevel()

                oproot.protocol('WM_DELETE_WINDOW',oprootwindowclose)
                
                
                oproot.configure(background = 'silver')
                oproot.wm_title("Options")
                #oproot.resizable(0,0)



                    

                

                #self.ScreenSlide = Scale(oproot, from_=1, to=2, orient=HORIZONTAL, resolution=0.1)
                #self.ScreenSlide.grid(row = 1, column =1 , columnspan = 1, sticky = W)

                desxres = IntVar()
                desyres = IntVar()
                
                self.qHD = Button(oproot, text="960x540",command=r960x540)
                self.qHD.grid(row=4,column = 1)
                
                self.HD = Button(oproot, text="1280x720",command=r1280x720)
                self.HD.grid(row=4,column = 2)

                self.fHD = Button(oproot, text="1366x768",command=r1366x768)
                self.fHD.grid(row=4,column = 3)

                self.HDp = Button(oproot, text="1600x900",command=r1600x900)
                self.HDp.grid(row=5,column = 1)

                self.FHD = Button(oproot, text="1920x1080",command=r1920x1080)
                self.FHD.grid(row=5,column = 2)
                
                self.QHD = Button(oproot, text="2560x1440",command=r2560x1440)
                self.QHD.grid(row=5,column = 3)

                self.auto = Button(oproot, text="Auto", command = autoscreen)
                self.auto.grid(row=4,column = 4)

                self.custom = Button(oproot, text="Custom", command = custombox)
                self.custom.grid(row=5,column = 4)

                Label(oproot, text = "- - - - - -  - - Resolution- - - - - - - - - - - - - - - - - -",background = 'silver').grid(row = 2, column = 1, columnspan = 4)
                

                

                Label(oproot, text = "  Display Mode  ", background = 'silver').grid(row=1,column = 2)
                
                fulopen = Button(oproot, text="FullScreen", command=fullscreen)
                fulopen.grid(row = 1, column = 1, columnspan = 2, sticky = W)

                
                
                winopen = Button(oproot, text="Windowed", command=windowed)
                winopen.grid(row = 1, column = 3, columnspan = 2, sticky = W)

                

                
                

             

                

                
                self.reslab = Label(oproot, text = "",background = 'silver')
                self.reslab.grid(row=100,column = 2)

                global changeamount
                #self.changeamount = changeamount

                print (self.changeamount)

                AmountSlide = Scale(oproot, from_=1, to=(500),length=150, orient = HORIZONTAL)
                AmountSlide.grid(row = 101, column =1 , columnspan = 2, sticky = W)

                confirmcalc = Button(oproot, text = "Confirm Animation Quality", command = animationoverride)
                confirmcalc.grid(row = 101, column = 3, columnspan = 2, sticky = W)


                Label(oproot, text = "", background = 'silver').grid(row=147,column = 2)
                Label(oproot, text = "- - - - - -  - - Program Mode - - - - - - - - - - - - - - - - - -", background = 'silver').grid(row=148,column = 1, columnspan = 4)


                def basics():
                    global mode
                    mode = 1
                    

                def advanceds():
                    global mode
                    mode = 2
                #Label(oproot, text = "", background = 'silver').grid(row=149,column = 2)

                BasicMode = Button(oproot, text = "Basic", command = basics)
                BasicMode.grid(row = 150, column = 2, sticky = W)

                AdvancedMode = Button(oproot, text = "Advanced", command  = advanceds)
                AdvancedMode.grid(row = 150, column = 3, sticky = W)

                Label(oproot, text = '', background = 'silver').grid(row = 199, column =1)

                optioncombust = Button(oproot, text = "Close", command = oprootwindowclose)
                optioncombust.grid(row = 200, column = 1, columnspan = 2)

                

                oproot.resizable(0,0)

                
                #optopen = Button(oproot, text="Full", command=fullscreen)
                #optopen.grid(row = 1, column = 2)

                #optopen = Button(oproot, text="Half", command=halfscreen) # make this a slider
                #optopen.grid(row = 1, column = 3)
                
                
                
        global oprootopen
        global orbitopen
        global tutrootopen
        global optopen
        global credopen
        global credrootopen
        #global credrootwindow

        
        global menuspacelab1
        
        global EMbutton
        global shipspeedmulti
        global credopen
        global CALCmenu
        global CREDmenu
        global TUTmenu
        global OPmenu
        global Emenu

        global changeamount

        self.changeamount = changeamount

        global tutopen
        oprootopen = 0
        tutrootopen = 0
        credrootopen = 0

        
        CALCmenu = PhotoImage(file="OPENCALCPs.png")
        CREDmenu = PhotoImage(file="OPENCREDPs.png")
        TUTmenu = PhotoImage(file="OPENTUTPs.png")
        OPmenu = PhotoImage(file="OPENOPTPs.png")
        Emenu= PhotoImage(file="MENUEARTH.png")
  
        orbitopen = Button(groot, text="Open Calculator", command=orbitcalccommand, image = CALCmenu,background = 'silver',borderwidth=0)
        orbitopen.grid(row = 1, column = 1,sticky=W)
        

        tutopen = Button(groot, text="Open Tutorial", command=orbittutcommand, image = TUTmenu,background = 'silver',borderwidth=0)
        tutopen.grid(row = 20, column = 1,sticky=W)
        
        optopen = Button(groot, text="Open Options", command=optionmenu, image = OPmenu,background = 'silver',borderwidth=0)
        optopen.grid(row = 30, column = 1,sticky=W)

        
        credopen = Button(groot, text="Open Credits", command = credrootwindow,image = CREDmenu,background = 'silver',borderwidth=0)
        credopen.grid(row = 40,column = 1,sticky=W)

        menuspacelab1 = Label(groot, text = "", background = 'silver')
        menuspacelab1.grid(row=22, column = 2)

        

   

        
        EMbutton = Label(groot, image=Emenu)
        EMbutton.Emenu =Emenu
        EMbutton.grid(row = 1, column = 3,rowspan = 1000)
        EMbutton.configure(background = 'silver')

        blurbwindow.attributes("-topmost", True)

        



        

        groot.mainloop()

 
app=App(groot)

