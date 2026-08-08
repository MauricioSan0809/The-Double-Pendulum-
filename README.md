# The-Double-Pendulum-
Python simulation of a nonlinear double pendulum using a second-order Runge-Kutta (RK2) ODE solver. Explores chaotic motion, timestep selection, energy conservation, numerical accuracy, and animated visualization of the coupled pendulum system.
## Objectives
- Model a nonlinear double pendulum
- Solve the equations of motion numerically
- Investigate chaotic behavior
- Evaluate numerical accuracy
- Visualize the motion

## Physics Model

The double pendulum is modeled as two point masses of equal mass $m$ connected by massless rods of equal length $l$. The angular positions are $\theta_1(t)$ and $\theta_2(t)$, measured from the downward vertical direction.

The corresponding angular velocities are $\omega_1 = \dot{\theta}_1$ and $\omega_2 = \dot{\theta}_2$.

---

## Position of the First Mass

The Cartesian coordinates of the first mass are

$$
x_1 = l\sin(\theta_1)
$$

$$
y_1 = -l\cos(\theta_1)
$$

Differentiating with respect to time gives

$$
\dot{x}_1 = l\dot{\theta}_1\cos(\theta_1)
$$

and

$$
\dot{y}_1 = l\dot{\theta}_1\sin(\theta_1)
$$

The squared speed is

$$
v_1^2 = \dot{x}_1^2 + \dot{y}_1^2
$$

Substituting the velocity components,

$$
v_1^2
=====

l^2\dot{\theta}_1^2\cos^2(\theta_1)
+
l^2\dot{\theta}_1^2\sin^2(\theta_1)
$$

Factor out the common terms:

$$
v_1^2
=====

l^2\dot{\theta}_1^2
\left[
\cos^2(\theta_1)
+
\sin^2(\theta_1)
\right]
$$

Using

$$
\sin^2(\theta) + \cos^2(\theta) = 1
$$

we obtain

$$
v_1^2 = l^2\dot{\theta}_1^2
$$

Therefore, the kinetic energy of the first mass is

$$
T_1
===

\frac{1}{2}ml^2\dot{\theta}_1^2
$$

---

## Position of the Second Mass

The position of the second mass depends on both pendulum angles:

$$
x_2
===

l\sin(\theta_1)
+
l\sin(\theta_2)
$$

$$
y_2
===

## -l\cos(\theta_1)

l\cos(\theta_2)
$$

Differentiating gives

$$
\dot{x}_2
=========

l\dot{\theta}_1\cos(\theta_1)
+
l\dot{\theta}_2\cos(\theta_2)
$$

and

$$
\dot{y}_2
=========

l\dot{\theta}_1\sin(\theta_1)
+
l\dot{\theta}_2\sin(\theta_2)
$$

The squared speed is

$$
v_2^2
=====

\dot{x}_2^2
+
\dot{y}_2^2
$$

Substituting the velocity components,

$$
v_2^2
=====

\left[
l\dot{\theta}_1\cos(\theta_1)
+
l\dot{\theta}_2\cos(\theta_2)
\right]^2
+
\left[
l\dot{\theta}_1\sin(\theta_1)
+
l\dot{\theta}_2\sin(\theta_2)
\right]^2
$$

Expanding and collecting terms gives

$$
v_2^2
=====

l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\left[
\cos(\theta_1)\cos(\theta_2)
+
\sin(\theta_1)\sin(\theta_2)
\right]
$$

Using the identity

$$
\cos(\theta_1-\theta_2)
=======================

\cos(\theta_1)\cos(\theta_2)
+
\sin(\theta_1)\sin(\theta_2)
$$

we obtain

$$
v_2^2
=====

l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
$$

Therefore, the kinetic energy of the second mass is

$$
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
\right]
$$

---

## Total Kinetic Energy

The total kinetic energy is

$$
T = T_1 + T_2
$$

Substituting $T_1$ and $T_2$,

$$
T
=

\frac{1}{2}ml^2\dot{\theta}_1^2
+
\frac{1}{2}m
\left[
l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
\right]
$$

Combining terms gives

$$
T
=

ml^2\dot{\theta}_1^2
+
\frac{1}{2}ml^2\dot{\theta}_2^2
+
ml^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
$$

The final term represents the coupling between the two pendulums because the velocity of the second mass depends on the motion of both links.

---

## Potential Energy

The gravitational potential energy of each mass is determined by its vertical position.

For the first mass,

$$
y_1 = -l\cos(\theta_1)
$$

so

$$
V_1 = mgy_1
$$

which gives

$$
V_1
===

-mgl\cos(\theta_1)
$$

For the second mass,

$$
y_2
===

## -l\cos(\theta_1)

l\cos(\theta_2)
$$

so

$$
V_2 = mgy_2
$$

which gives

$$
V_2
===

## -mgl\cos(\theta_1)

mgl\cos(\theta_2)
$$

The total potential energy is

$$
V = V_1 + V_2
$$

Therefore,

$$
V
=

## -mgl\cos(\theta_1)

## mgl\cos(\theta_1)

mgl\cos(\theta_2)
$$

and finally,

$$
V
=

## -2mgl\cos(\theta_1)

mgl\cos(\theta_2)
$$

The factor of $2$ multiplying the first term appears because changing $\theta_1$ changes the vertical position of both masses.

---

## Lagrangian

The Lagrangian is defined as

$$
L = T - V
$$

Substituting the kinetic and potential energies,

$$
L
=

ml^2\dot{\theta}_1^2
+
\frac{1}{2}ml^2\dot{\theta}_2^2
+
ml^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2)
+
2mgl\cos(\theta_1)
+
mgl\cos(\theta_2)
$$

The equations of motion are obtained by applying the Euler-Lagrange equation to each generalized coordinate:

$$
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot{\theta}_i}
\right)
-------

# \frac{\partial L}{\partial \theta_i}

0
$$

for $i=1,2$.

---

## Coupled Equations Before Solving for Acceleration

Applying the Euler-Lagrange equation to $\theta_1$ gives

$$
2\ddot{\theta}_1
+
\ddot{\theta}_2\cos(\theta_1-\theta_2)
+
\dot{\theta}_2^2\sin(\theta_1-\theta_2)
+
2\frac{g}{l}\sin(\theta_1)
==========================

0
$$

Applying it to $\theta_2$ gives

$$
\ddot{\theta}_2
+
\ddot{\theta}_1\cos(\theta_1-\theta_2)
--------------------------------------

\dot{\theta}_1^2\sin(\theta_1-\theta_2)
+
\frac{g}{l}\sin(\theta_2)
=========================

0
$$

Solving these two coupled equations for $\ddot{\theta}_1$ and $\ddot{\theta}_2$ gives the equations of motion used in the numerical simulation.

---

## Numerical State Representation

To solve the equations numerically, define the state vector

$$
\mathbf{y}
==========

\begin{bmatrix}
\theta_1 \
\omega_1 \
\theta_2 \
\omega_2
\end{bmatrix}
$$

where

$$
\omega_1 = \dot{\theta}_1
$$

and

$$
\omega_2 = \dot{\theta}_2
$$

Therefore,

$$
\frac{d\mathbf{y}}{dt}
======================

\begin{bmatrix}
\omega_1 \
\dot{\omega}_1 \
\omega_2 \
\dot{\omega}_2
\end{bmatrix}
$$

The resulting nonlinear system is integrated numerically using a second-order Runge-Kutta midpoint method (RK2).



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
