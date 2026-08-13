 # -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:28:54 2023

@author: Mauricio Sanchez
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
from pathlib import Path
import imageio.v2 as imageio

def move_RK2(f, y, dt):
    ydot = f(y)
    y_half = y + ydot * dt/2
    ydot_half = f(y_half)
    y = y + ydot_half * dt
    return y
    
dt = 0.001
t1i = np.pi
w1i = 0
t2i = np.pi/2
w2i = 0
g = 9.81
l = 1
m = 2
t = 30
t_range = np.arange(0,t,dt)
y0 = [t1i,w1i,t2i,w2i]
to_list = [y0]
    
def diffeq(y):
    theta1 , omega1 , theta2, omega2 = y
    ydot = np.array([omega1, -((omega1)**2 * np.sin(2 * theta1 - 2 * theta2) + (2*(omega2)**2 * np.sin(theta1 - theta2)) + (g/l) * (np.sin(theta1 - 2 * theta2) + \
    3 * np.sin(theta1)))/(3 - np.cos(2*theta1 - 2*theta2)), omega2, (4 * (omega1)**2 * np.sin(theta1 - theta2) + (omega2)**2 * np.sin(2*theta1 - 2*theta2) + 2 * \
    (g/l) * (np.sin(2*theta1 - theta2) - np.sin(theta2)))/(3 - np.cos(2*theta1 - 2*theta2))])
    return ydot

# choose an ODE solver to propagate the equations of motion
for t in t_range[:-1]:
    temp_array = move_RK2( diffeq, to_list[-1], dt )
    to_list.append(temp_array)


to = np.array(to_list) 

KE = (1/2)*m*(l**2)*(to[:,1]**2) + (1/2)*m*((l**2)*(to[:,1]**2) + \
(l**2)*(to[:,3]**2) + 2*(l**2)*to[:,1]*to[:,3]*np.cos(to[:,0] - to[:,2]))
PE = -2*m*g*l*np.cos(to[:,0]) - m*g*l*np.cos(to[:,2])

TE = KE + PE

# Evaluate numerical energy conservation. For an ideal double pendulum,
# total mechanical energy should remain constant. Numerical integration
# introduces a small amount of energy drift.
E0 = TE[0]
energy_error = TE - E0
relative_energy_error = np.abs((TE - E0) / E0)
energy_time = np.arange(len(TE)) * dt

fig_energy = plt.figure(figsize=(6, 4))
plt.plot(energy_time, relative_energy_error)
plt.xlabel("Time (s)")
plt.ylabel("Relative Energy Error")
plt.title("RK2 Relative Energy Error")
plt.grid()


x1_list = l * np.sin(to[:, 0])
y1_list = -l * np.cos(to[:, 0])
x2_list = l * np.sin(to[:, 0]) + l * np.sin(to[:, 2])
y2_list = -l * np.cos(to[:, 0]) - l * np.cos(to[:, 2])
pygame.init()


width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

background = (16, 24, 38)
rod_color = (120, 190, 255)
bob1_color = (255, 210, 70)
bob2_color = (255, 80, 100)
trail_color = (255, 100, 130)

scale = 250                 # pixels per meter
origin = (width // 2, 220)  # pivot location in pixels
animation_step = 10         # show every 10th solver point = 0.01 s
trail_length = 250

trail_points = []
running = True
paused = False
speed = 1
j = 0

while running and j < len(to):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_r:
                j = 0
                trail_points = []
            elif event.key == pygame.K_UP:
                speed = min(speed + 1, 10)
            elif event.key == pygame.K_DOWN:
                speed = max(speed - 1, 1)

    x1 = origin[0] + int(scale * x1_list[j])
    y1 = origin[1] - int(scale * y1_list[j])
    x2 = origin[0] + int(scale * x2_list[j])
    y2 = origin[1] - int(scale * y2_list[j])

    trail_points.append((x2, y2))
    if len(trail_points) > trail_length:
        trail_points.pop(0)

    screen.fill(background)

    if len(trail_points) > 1:
        pygame.draw.lines(screen, trail_color, False, trail_points, 2)

    pygame.draw.circle(screen, (230, 230, 230), origin, 7)
    pygame.draw.line(screen, rod_color, origin, (x1, y1), 5)
    pygame.draw.line(screen, rod_color, (x1, y1), (x2, y2), 5)
    pygame.draw.circle(screen, bob1_color, (x1, y1), 15)
    pygame.draw.circle(screen, bob2_color, (x2, y2), 17)

    current_time = j * dt
    label = font.render(f"Time: {current_time:.2f} s", True, (255, 255, 255))
    status = "Paused" if paused else f"{speed}x speed"
    status_label = font.render(status, True, (255, 255, 255))

    screen.blit(label, (25, 25))
    screen.blit(status_label, (25, 55))
    pygame.display.flip()
    if not paused:
        j += animation_step * speed

    clock.tick(100)


pygame.quit()

plt.show()