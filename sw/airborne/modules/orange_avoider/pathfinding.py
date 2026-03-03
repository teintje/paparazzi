# inputs GPS, speed, heading
# cyberzoo coordinates      <waypoint lat="51.9906006" lon="4.3767764" name="_OZ1"/>
#                           <waypoint lat="51.9906405" lon="4.3767316" name="_OZ2"/>
#                           <waypoint lat="51.9906687" lon="4.3768025" name="_OZ3"/>
#                           <waypoint lat="51.9906273" lon="4.3768438" name="_OZ4"/>

import matplotlib.pyplot as plt
import numpy as np
import random
Cyber_zoo_latitude = [51.9906006,51.9906405,51.9906687,51.9906273]
Cyber_zoo_longitude = [4.3767764,4.3767316,4.3768025,4.3768438]
Cyber_zoo_y = []
Cyber_zoo_x = []
R_earth = 6738137
Latitude = 51.99065
Longitude = 4.3768
V = 3
heading = np.pi/180*75
for i in Cyber_zoo_latitude:
    Cyber_zoo_y.append(np.pi/180*(i - Cyber_zoo_latitude[0])*R_earth)
for i in Cyber_zoo_longitude:
    Cyber_zoo_x.append(np.pi/180*(i - Cyber_zoo_longitude[0])*R_earth*np.cos(np.pi/180*Cyber_zoo_latitude[0]))
y = np.pi/180*(Latitude - Cyber_zoo_latitude[0])*R_earth
x = np.pi/180*(Longitude - Cyber_zoo_longitude[0])*R_earth*np.cos(np.pi/180*Cyber_zoo_latitude[0])
X_lst = []
Y_lst = []
print(random.random)
waypoints = []
for i in range(7):
    waypoints.append([random.random() * 10,random.random() * 10])
waypoint_count = 0
X_waypoint = [waypoints[0][0]]
Y_waypoint = [waypoints[0][1]]
t = 0
tend = 600
dt = 0.1

while t< tend:

    x = x + dt*V*np.sin(heading)
    y = y + dt*V*np.cos(heading)
    if (waypoints[waypoint_count][1]-y)**2 + (waypoints[waypoint_count][0]-x)**2 <1:
        waypoint_count = waypoint_count + 1
        X_waypoint.append(waypoints[waypoint_count][0])
        Y_waypoint.append(waypoints[waypoint_count][1])
    delta_heading = np.arctan2((waypoints[waypoint_count][1]-y),(waypoints[waypoint_count][0]-x)) - heading
    if delta_heading > np.pi:
        delta_heading = delta_heading - np.pi
    elif delta_heading < - np.pi:
        delta_heading = delta_heading + np.pi
    print(delta_heading*180/np.pi)
    heading = heading -0.01*delta_heading

    X_lst.append(x)
    Y_lst.append(y)
    t = t +dt




plt.plot(Cyber_zoo_x,Cyber_zoo_y)
plt.plot(X_lst,Y_lst)
plt.scatter(X_waypoint,Y_waypoint,color = 'r')

plt.show()