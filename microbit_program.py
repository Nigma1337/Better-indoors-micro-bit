# Add your Python code here. E.g.
from microbit import *


while True:
    #temperature
    temp = temperature()
    #vis temperatur og luftkvalitet på displayet
    display.scroll("temperature: ")
    display.scroll(temp)
    display.scroll("air quality: "):
    #hvis analog inputtet fra mq-135 er for højt, siger vi at det er for højt.
    if microbit.pin3.read_analog() > 900:
        display.scroll("bad lol")
    #hvis analog inputtet er mellem 900 og 600 (elif), siger vi at det er ok
    elif microbit.pin3.read_analog() > 600:
        display.scroll("okish")
    #ellers er det godt.
    else:
        display.scroll("ur good nigga")
    #her skrives temperatur og luft kvalitet ud så vi kan logge det på fx en raspberry pi
    microbit.pin4.write_analog(temp)
    microbit.pin4.write_analog(microbit.pin3.read_analog())