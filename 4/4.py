#created for https://genuary.art/ prompt #4: Black on black.
from vpython import *
import datetime

def draw_axes():
    arrow(pos = vec(-1,1,0), axis = vec(0.5,0,0), color = color.red)
    label(pos = vec(-0.5,1,0),text="x",xoffset= 0.1, yoffset = 0.1)
    arrow(pos = vec(-1,1,0), axis = vec(0,0.5,0), color = color.green)
    label(pos = vec(-1,1.5,0),text="y",xoffset= 0.1, yoffset = 0.1)
    arrow(pos = vec(-1,1,0), axis = vec(0,0,0.5), color = color.blue)
    label(pos = vec(-1,1,0.5),text="z",xoffset= 0.1, yoffset = 0.1)

def draw_car():
    #chassis = box(size = vec(1,0.5,0.5), color = color.black, texture = textures.metal)
    car_shape = [[21,50],[207,7],[362,11],[419,54],[557,68],[612,87],[627,119],[632,120],[632,131],[570,131],[553,106],[531,98],[504,97],[482,103],[466,117],[456,151],[242,149],[197,136],[185,103],[170,90],[126,91],[105,100],[88,127],[29,120],[12,108],[0,88],[6,65],[21,50]]
    front_window = [[261,20],[349,19],[388,54],[297,55],[260,48],[261,20]]
    back_window = [[257,21],[257,49],[200,35],[220,24],[257,21]]
    linepath = [ vec(0,0,-120), vec(0,0,120)]
    car_extruded = extrusion( shape=[car_shape, front_window, back_window], path=linepath, color = vec(0.05, 0.05, 0.05) )
    wheel1 = cylinder(pos = vec(-150,142,70),axis = vec(0,0,40), radius = 45, color = color.white*0.1)
    wheel2 = cylinder(pos = vec(-150,142,-110),axis = vec(0,0,40), radius = 45, color = color.white*0.1)
    wheel3 = cylinder(pos = vec(-510,136,70),axis = vec(0,0,40), radius = 45, color = color.white*0.1)
    wheel4 = cylinder(pos = vec(-510,136,-110),axis = vec(0,0,40), radius = 45, color = color.white*0.1)
    return compound([car_extruded, wheel1,wheel2,wheel3,wheel4])

rot_rate = 0.01

scene.background = color.black
#draw_axes()
car = draw_car()
car.rotate(angle=pi, axis= vec(1,0,0))
car.rotate(angle=pi, axis= vec(0,1,0))
car.pos = vec(0,0,0)

current_time = datetime.datetime.now()
end_time = current_time + datetime.timedelta(0,140)
while current_time < end_time:
    rate(100)
    current_time = datetime.datetime.now()
    car.rotate(angle = rot_rate, axis = vec(0,1,0))
