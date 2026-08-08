# The-Double-Pendulum-
Python simulation of a nonlinear double pendulum using a second-order Runge-Kutta (RK2) ODE solver. Explores chaotic motion, timestep selection, energy conservation, numerical accuracy, and animated visualization of the coupled pendulum system.
## Objectives
- Model a nonlinear double pendulum
- Solve the equations of motion numerically
- Investigate chaotic behavior
- Evaluate numerical accuracy
- Visualize the motion

## Physics Model

The double pendulum is modeled as two point masses of equal mass $m$ connected by massless rods of equal length $l$.

The angular positions of the two pendulums are

$$
\theta_1(t), \qquad \theta_2(t)
$$

with angular velocities

$$
\omega_1 = \dot{\theta}_1,
\qquad
\omega_2 = \dot{\theta}_2.
$$

The angles are measured from the downward vertical direction.

---

## Position of the First Mass

The Cartesian coordinates of the first mass are

$$
x_1 = l\sin(\theta_1)
$$

$$
y_1 = -l\cos(\theta_1).
$$

Differentiating with respect to time gives the velocity components

$$
\dot{x}_1
=========

l\dot{\theta}_1\cos(\theta_1)
$$

and

$$
\dot{y}_1
=========

l\dot{\theta}_1\sin(\theta_1).
$$

The squared speed of the first mass is

$$
v_1^2
=====

\dot{x}_1^2+\dot{y}_1^2.
$$

Substituting the velocity components,

$$
v_1^2
=====

l^2\dot{\theta}_1^2\cos^2(\theta_1)
+
l^2\dot{\theta}_1^2\sin^2(\theta_1).
$$

Factor out the common terms:

$$
v_1^2
=====

l^2\dot{\theta}_1^2
\left[
\cos^2(\theta_1)+\sin^2(\theta_1)
\right].
$$

Using the identity

$$
\sin^2(\theta)+\cos^2(\theta)=1,
$$

we obtain

$$
v_1^2=l^2\dot{\theta}_1^2.
$$

Therefore, the kinetic energy of the first mass is

$$
T_1
===

\frac{1}{2}ml^2\dot{\theta}_1^2.
$$

---

## Position of the Second Mass

The position of the second mass depends on both pendulum angles:

$$
x_2
===

l\sin(\theta_1)+l\sin(\theta_2)
$$

and

$$
y_2
===

-l\cos(\theta_1)-l\cos(\theta_2).
$$

Differentiating with respect to time gives

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
l\dot{\theta}_2\sin(\theta_2).
$$

The squared speed is

$$
v_2^2
=====

\dot{x}_2^2+\dot{y}_2^2.
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
\right]^2.
$$

Expanding and grouping terms gives

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
\right].
$$

Using the trigonometric identity

$$
\cos(\theta_1-\theta_2)
=======================

\cos(\theta_1)\cos(\theta_2)
+
\sin(\theta_1)\sin(\theta_2),
$$

the expression simplifies to

$$
v_2^2
=====

l^2\dot{\theta}_1^2
+
l^2\dot{\theta}_2^2
+
2l^2\dot{\theta}_1\dot{\theta}_2
\cos(\theta_1-\theta_2).
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
\right].
$$

---

## Total Kinetic Energy

The total kinetic energy is

$$
T=T_1+T_2.
$$

Substituting the expressions for $T_1$ and $T_2$ gives

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
\right].
$$

Combining terms,

$$
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
$$

The final term represents the coupling between the two pendulums. The velocity of the second mass depends on the motion of both links.

---

## Potential Energy

The gravitational potential energy of a point mass is determined by its vertical position.

For the first mass,

$$
y_1=-l\cos(\theta_1),
$$

so its potential energy is

$$
V_1
===

# mgy_1

-mgl\cos(\theta_1).
$$

For the second mass,

$$
y_2
===

-l\cos(\theta_1)-l\cos(\theta_2),
$$

so

$$
V_2
===

# mgy_2

## -mgl\cos(\theta_1)

mgl\cos(\theta_2).
$$

The total potential energy is therefore

$$
V=V_1+V_2.
$$

Substituting,

$$
V
=

-mgl\cos(\theta_1)
-mgl\cos(\theta_1)
-mgl\cos(\theta_2).
$$

Thus,

$$
\boxed{
V
=

## -2mgl\cos(\theta_1)

mgl\cos(\theta_2)
}
$$

The factor of $2$ multiplying the first term occurs because the motion of the first pendulum changes the vertical position of both masses.

---

## Lagrangian

The equations of motion can be obtained using Lagrangian mechanics.

The Lagrangian is defined as

$$
L=T-V.
$$

Substituting the kinetic and potential energies gives

$$
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
2mgl\cos(\theta_1)
+
mgl\cos(\theta_2)
}
$$

The Euler-Lagrange equation is then applied to each generalized coordinate $\theta_i$:

$$
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot{\theta}_i}
\right)
-------

# \frac{\partial L}{\partial \theta_i}

0.

$$

Applying this equation for $\theta_1$ and $\theta_2$ produces two coupled nonlinear differential equations that describe the motion of the double pendulum.

---

## Numerical State Representation

To solve the equations numerically, the second-order differential equations are rewritten as a system of first-order equations.

Define the state vector as

$$
\mathbf{y}
==========

\begin{bmatrix}
\theta_1 \
\omega_1 \
\theta_2 \
\omega_2
\end{bmatrix},
$$

where

$$
\omega_1=\dot{\theta}_1
$$

and

$$
\omega_2=\dot{\theta}_2.
$$

The derivative of the state vector is therefore

$$
\frac{d\mathbf{y}}{dt}
======================

\begin{bmatrix}
\omega_1 \
\dot{\omega}_1 \
\omega_2 \
\dot{\omega}_2
\end{bmatrix}.
$$

The resulting system of nonlinear ordinary differential equations is integrated numerically using a second-order Runge-Kutta midpoint method (RK2).



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
