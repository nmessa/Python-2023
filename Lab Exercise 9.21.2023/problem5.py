##Lab Exercise 9.21.2023 Problem 5
##Author: nmessa

def waveCat(f):
    wl = 3e8/f
    if wl<= 1e3 and wl > 1e-1:
        return "Radio Wave"
    elif wl<= 1e-1 and wl > 1e-3:
        return "Microwave"
    elif wl<= 1e-3 and wl > 1e-6:
        return "Infrared Radiation"
    elif wl<= 0.8e-6 and wl > 0.5e-6:
        return "Visible Light"
    elif wl<= 1e-7 and wl > 1e-8:
        return "Ultraviolet Radiation"
    elif wl<= 1e-8 and wl > 1e-11:
        return "X-Rays"
    elif wl<= 1e-11 and wl > 1e-13:
        return "Gamma Rays"
    else:
        return "Not in EM spectrum"

#Test Code
print(waveCat(100.3e6)) #WHEB
print(waveCat(4.77e9)) #Microwave oven
print(waveCat(6e12)) #Thermal Imaging camera
print(waveCat(4e14)) #Lightbulb
print(waveCat(6e15))#Tanning bed
print(waveCat(3e18)) #Chest X-Ray
print(waveCat(3e20)) #Cobalt 60 Decay

##Sample Output
##Radio Wave
##Microwave
##Infrared Radiation
##Visible Light
##Ultraviolet Radiation
##X-Rays
##Gamma Rays
