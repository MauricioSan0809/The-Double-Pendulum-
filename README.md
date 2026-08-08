# The-Double-Pendulum-
Python simulation of a nonlinear double pendulum using a second-order Runge-Kutta (RK2) ODE solver. Explores chaotic motion, timestep selection, energy conservation, numerical accuracy, and animated visualization of the coupled pendulum system.
## Objectives
- Model a nonlinear double pendulum
- Solve the equations of motion numerically
- Investigate chaotic behavior
- Evaluate numerical accuracy
- Visualize the motion

## Physics Model
## Physics Model and Derivation

The double pendulum is modeled as two point masses of equal mass (m), connected by two massless rods of equal length (l). The generalized coordinates are the angular positions

[
\theta_1(t), \qquad \theta_2(t)
]

measured from the downward vertical direction.

The corresponding angular velocities are

[
\omega_1 = \dot{\theta}_1,
\qquad
\omega_2 = \dot{\theta}_2.
]

---

### Position of the First Mass

The Cartesian coordinates of the first pendulum mass are

[
x_1 = l\sin\theta_1
]

[
y_1 = -l\cos\theta_1.
]

Differentiating with respect to time gives

[
\dot{x}_1
=========

l\dot{\theta}_1\cos\theta_1
]

and

[
\dot{y}_1
=========

l\dot{\theta}_1\sin\theta_1.
]

The squared velocity is therefore

[
v_1^2
=====

\dot{x}_1^2+\dot{y}_1^2.
]

Substituting the velocity components,

[
v_1^2
=====

l^2\dot{\theta}_1^2
\left(
\cos^2\theta_1+\sin^2\theta_1
\right).
]

Using

[
\sin^2\theta+\cos^2\theta=1,
]

we obtain

[
v_1^2=l^2\dot{\theta}_1^2.
]

Therefore, the kinetic energy of the first mass is

[
T_1
===

\frac{1}{2}ml^2\dot{\theta}_1^2.
]

---

### Position of the Second Mass

Because the second mass is attached to the end of the first pendulum, its coordinates depend on both angles:

[
x_2
===

l\sin\theta_1+l\sin\theta_2
]

[
y_2
===

-l\cos\theta_1-l\cos\theta_2.
]

Differentiating gives

[
\dot{x}_2
=========

l\dot{\theta}_1\cos\theta_1
+
l\dot{\theta}_2\cos\theta_2
]

and

[
\dot{y}_2
=========

l\dot{\theta}_1\sin\theta_1
+
l\dot{\theta}_2\sin\theta_2.
]

The squared velocity of the second mass is

[
v_2^2
=====

\dot{x}_2^2+\dot{y}_2^2.
]

Expanding,

[
\begin{aligned}
v_2^2 ={}&
l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2 \
&+
2l^2\dot{\theta}_1\dot{\theta}_2
\left(
\cos\theta_1\cos\theta_2+
\sin\theta_1\sin\theta_2
\right).
\end{aligned}
]

Using the identity

[
\cos(\theta_1-\theta_2)
=======================

\cos\theta_1\cos\theta_2+
\sin\theta_1\sin\theta_2,
]

this becomes

[
v_2^2
=====

l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2).
]

Therefore,

[
T_2
===

\frac{1}{2}m
\left[
l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
\right].
]

---

## Total Kinetic Energy

The total kinetic energy is

[
T=T_1+T_2.
]

Thus,

[
\boxed{
T
=

ml^2\dot{\theta}_1^2
+
\frac{1}{2}ml^2\dot{\theta}_2^2
+
ml^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
}
]

The final term couples the two pendulums because the velocity of the second mass depends on the motion of both links.

---

## Potential Energy

Taking the pivot as the coordinate origin, the vertical positions of the two masses are

[
y_1=-l\cos\theta_1
]

and

[
y_2=-l\cos\theta_1-l\cos\theta_2.
]

The total gravitational potential energy is

[
V=mgy_1+mgy_2.
]

Substituting the vertical positions gives

[
V
=

mg(-l\cos\theta_1)
+
mg(-l\cos\theta_1-l\cos\theta_2).
]

Therefore,

[
\boxed{
V
=

## -2mgl\cos\theta_1

mgl\cos\theta_2
}
]

The factor of (2) multiplying the first term appears because changing (\theta_1) changes the vertical position of both masses.

---

## Lagrangian

The Lagrangian of the system is defined as

[
L=T-V.
]

Substituting the kinetic and potential energies,

[
\boxed{
L
=

ml^2\dot{\theta}_1^2
+
\frac{1}{2}ml^2\dot{\theta}_2^2
+
ml^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
+
2mgl\cos\theta_1
+
mgl\cos\theta_2
}
]

The equations of motion are then obtained using the Euler-Lagrange equation for each generalized coordinate:

[
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot{\theta}_i}
\right)
-------

# \frac{\partial L}{\partial \theta_i}

0,
\qquad i=1,2.
]

Solving the resulting coupled equations for

[
\ddot{\theta}_1
\qquad \text{and} \qquad
\ddot{\theta}_2
]

produces the nonlinear equations of motion used in the numerical simulation.

---

## Numerical State

For numerical integration, the second-order equations are converted into a first-order system using the state vector

[
\mathbf{y}
==========

\begin{bmatrix}
\theta_1 \
\omega_1 \
\theta_2 \
\omega_2
\end{bmatrix},
]

where

[
\omega_1=\dot{\theta}_1,
\qquad
\omega_2=\dot{\theta}_2.
]

Therefore,

[
\frac{d\mathbf{y}}{dt}
======================

\begin{bmatrix}
\omega_1 \
\dot{\omega}_1 \
\omega_2 \
\dot{\omega}_2
\end{bmatrix}.
]

This system is propagated numerically using a second-order Runge-Kutta midpoint method (RK2).


## Numerical Method
Explain the second-order Runge-Kutta (RK2) method.

## Implementation
Explain how the Python simulation works.

## Numerical Validation
Explain how timestep selection and total-energy error
were used to evaluate numerical accuracy.

## Results
Include animation, plots, and observations.

## Technologies
Python
NumPy
Matplotlib

## Running the Project
Installation and execution instructions.

## My Contributions
Clearly state your individual work.

## Contributors
Credit the other project members.
