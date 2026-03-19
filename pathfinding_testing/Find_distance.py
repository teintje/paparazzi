
import numpy as np
orange_px = 100
below_orange_px = 100
screen_height = 240
alt = 1.1
FoV = np.pi/2
Camera_tilt = np.pi/6
FoV_down = FoV + Camera_tilt
FoV_up = FoV - Camera_tilt
angle_of_attack = 0

theta = FoV_down + angle_of_attack - below_orange_px/screen_height*FoV
print(theta*180/np.pi)
beta = np.pi - theta

distance = alt/np.sin(theta)*np.sin(beta)
print(distance)
