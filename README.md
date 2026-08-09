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
v_1^2 = l^2\dot{\theta}_1^2\cos^2(\theta_1) + l^2\dot{\theta}_1^2\sin^2(\theta_1)
$$

Factor out the common terms:

$$
v_1^2 = l^2\dot{\theta}_1^2\left[\cos^2(\theta_1) + \sin^2(\theta_1)\right]
$$

Using the trigonometric identity

$$
\sin^2(\theta) + \cos^2(\theta) = 1
$$

we obtain

$$
v_1^2 = l^2\dot{\theta}_1^2
$$

Therefore, the kinetic energy of the first mass is

$$
T_1 = \frac{1}{2}ml^2\dot{\theta}_1^2
$$

---

## Position of the Second Mass

Because the second mass is attached to the first pendulum, its position depends on both angles:

$$
x_2 = l\sin(\theta_1) + l\sin(\theta_2)
$$

$$
y_2 = -l\cos(\theta_1) - l\cos(\theta_2)
$$

Differentiating with respect to time gives

$$
\dot{x}_2 = l\dot{\theta}_1\cos(\theta_1) + l\dot{\theta}_2\cos(\theta_2)
$$

and

$$
\dot{y}_2 = l\dot{\theta}_1\sin(\theta_1) + l\dot{\theta}_2\sin(\theta_2)
$$

The squared speed of the second mass is

$$
v_2^2 = \dot{x}_2^2 + \dot{y}_2^2
$$

Substituting the velocity components gives

$$
v_2^2 = \left[l\dot{\theta}_1\cos(\theta_1) + l\dot{\theta}_2\cos(\theta_2)\right]^2 + \left[l\dot{\theta}_1\sin(\theta_1) + l\dot{\theta}_2\sin(\theta_2)\right]^2
$$

Expanding and collecting terms,

$$
v_2^2 = l^2\dot{\theta}_1^2 + l^2\dot{\theta}_2^2 + 2l^2\dot{\theta}_1\dot{\theta}_2\left[\cos(\theta_1)\cos(\theta_2) + \sin(\theta_1)\sin(\theta_2)\right]
$$

Using the identity

$$
\cos(\theta_1-\theta_2) = \cos(\theta_1)\cos(\theta_2) + \sin(\theta_1)\sin(\theta_2)
$$

we obtain

$$
v_2^2 = l^2\dot{\theta}_1^2 + l^2\dot{\theta}_2^2 + 2l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2)
$$

Therefore, the kinetic energy of the second mass is

$$
T_2 = \frac{1}{2}m\left[l^2\dot{\theta}_1^2 + l^2\dot{\theta}_2^2 + 2l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2)\right]
$$

---

## Total Kinetic Energy

The total kinetic energy is

$$
T = T_1 + T_2
$$

Substituting the expressions for $T_1$ and $T_2$,

$$
T = \frac{1}{2}ml^2\dot{\theta}_1^2 + \frac{1}{2}m\left[l^2\dot{\theta}_1^2 + l^2\dot{\theta}_2^2 + 2l^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2)\right]
$$

Combining terms gives

$$
T = ml^2\dot{\theta}_1^2 + \frac{1}{2}ml^2\dot{\theta}_2^2 + ml^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2)
$$

The final term represents the coupling between the two pendulums because the velocity of the second mass depends on the motion of both links.

---

## Potential Energy

The gravitational potential energy of each mass depends on its vertical position.

For the first mass,

$$
y_1 = -l\cos(\theta_1)
$$

so its potential energy is

$$
V_1 = mgy_1 = -mgl\cos(\theta_1)
$$

For the second mass,

$$
y_2 = -l\cos(\theta_1) - l\cos(\theta_2)
$$

so its potential energy is

$$
V_2 = mgy_2 = -mgl\cos(\theta_1) - mgl\cos(\theta_2)
$$

The total potential energy is

$$
V = V_1 + V_2
$$

Therefore,

$$
V = -mgl\cos(\theta_1) - mgl\cos(\theta_1) - mgl\cos(\theta_2)
$$

which simplifies to

$$
V = -2mgl\cos(\theta_1) - mgl\cos(\theta_2)
$$

The factor of $2$ multiplying the first term appears because changing $\theta_1$ changes the vertical position of both masses.

---

## Lagrangian

The Lagrangian is defined as

$$
L = T - V
$$

Substituting the kinetic and potential energy expressions gives

$$
L = ml^2\dot{\theta}_1^2 + \frac{1}{2}ml^2\dot{\theta}_2^2 + ml^2\dot{\theta}_1\dot{\theta}_2\cos(\theta_1-\theta_2) + 2mgl\cos(\theta_1) + mgl\cos(\theta_2)
$$

The equations of motion are obtained using the Euler-Lagrange equation:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}_i}\right) - \frac{\partial L}{\partial \theta_i} = 0
$$

for $i=1,2$.

---

## Coupled Equations of Motion

Applying the Euler-Lagrange equation to $\theta_1$ gives

$$
2\ddot{\theta}_1 + \ddot{\theta}_2\cos(\theta_1-\theta_2) + \dot{\theta}_2^2\sin(\theta_1-\theta_2) + 2\frac{g}{l}\sin(\theta_1) = 0
$$

Applying the Euler-Lagrange equation to $\theta_2$ gives

$$
\ddot{\theta}_2 + \ddot{\theta}_1\cos(\theta_1-\theta_2) - \dot{\theta}_1^2\sin(\theta_1-\theta_2) + \frac{g}{l}\sin(\theta_2) = 0
$$

These two coupled equations can be solved for $\ddot{\theta}_1$ and $\ddot{\theta}_2$ to obtain the nonlinear equations implemented in the numerical simulation.

---

## Numerical State Representation

To integrate the equations numerically, define the state vector

$$
\mathbf{y} = \begin{bmatrix} \theta_1 \ \omega_1 \ \theta_2 \ \omega_2 \end{bmatrix}
$$

where

$$
\omega_1 = \dot{\theta}_1
$$

and

$$
\omega_2 = \dot{\theta}_2
$$

The derivative of the state vector is therefore

$$
\frac{d\mathbf{y}}{dt} = \begin{bmatrix} \omega_1 \ \dot{\omega}_1 \ \omega_2 \ \dot{\omega}_2 \end{bmatrix}
$$

The resulting nonlinear system of ordinary differential equations is integrated numerically using a second-order Runge-Kutta midpoint method (RK2).

## Numerical Method: Second-Order Runge-Kutta (RK2)

The double pendulum equations of motion form a system of coupled nonlinear ordinary differential equations. Because the equations generally do not have a simple analytical solution, the motion is calculated numerically.

This project uses the **second-order Runge-Kutta midpoint method (RK2)** to propagate the state of the double pendulum through time.

The state vector is

$$
\mathbf{y} = \begin{bmatrix} \theta_1 \ \omega_1 \ \theta_2 \ \omega_2 \end{bmatrix}
$$

and its time derivative is

$$
\dot{\mathbf{y}} = \begin{bmatrix} \omega_1 \ \dot{\omega}_1 \ \omega_2 \ \dot{\omega}_2 \end{bmatrix}
$$

where $\dot{\omega}_1$ and $\dot{\omega}_2$ are the angular accelerations obtained from the equations of motion.

---

### Step 1: Evaluate the Current Derivative

At the beginning of each timestep, the derivative of the current state $\mathbf{y}_n$ is calculated:

$$
\dot{\mathbf{y}}*n = \begin{bmatrix} \omega*{1,n} \ \dot{\omega}*{1,n} \ \omega*{2,n} \ \dot{\omega}_{2,n} \end{bmatrix}
$$

This represents the instantaneous rate of change of the double pendulum at the beginning of the timestep.

---

### Step 2: Estimate the Midpoint State

The current derivative is used to estimate the state halfway through the timestep:

$$
\mathbf{y}_{\mathrm{half}} = \mathbf{y}_n + \frac{\Delta t}{2}\dot{\mathbf{y}}_n
$$

where $\Delta t$ is the numerical timestep.

This midpoint estimate gives an approximation of the state of the double pendulum halfway between $\mathbf{y}*n$ and $\mathbf{y}*{n+1}$.

---

### Step 3: Evaluate the Midpoint Derivative

The equations of motion are evaluated again using the midpoint state to obtain

$$
\dot{\mathbf{y}}*{\mathrm{half}} = \begin{bmatrix} \omega*{1,\mathrm{half}} \ \dot{\omega}*{1,\mathrm{half}} \ \omega*{2,\mathrm{half}} \ \dot{\omega}_{2,\mathrm{half}} \end{bmatrix}
$$

Because this derivative is evaluated halfway through the interval, it provides a better estimate of the average rate of change over the entire timestep than using only the derivative at the beginning.

---

### Step 4: Update the State

The midpoint derivative is then used to advance the system through the full timestep:

$$
\mathbf{y}_{n+1} = \mathbf{y}*n + \Delta t,\dot{\mathbf{y}}*{\mathrm{half}}
$$

The complete RK2 midpoint procedure can therefore be summarized as

$$
\dot{\mathbf{y}}_n = \text{derivative evaluated at } \mathbf{y}_n
$$

$$
\mathbf{y}_{\mathrm{half}} = \mathbf{y}_n + \frac{\Delta t}{2}\dot{\mathbf{y}}_n
$$

$$
\dot{\mathbf{y}}*{\mathrm{half}} = \text{derivative evaluated at } \mathbf{y}*{\mathrm{half}}
$$

$$
\mathbf{y}_{n+1} = \mathbf{y}*n + \Delta t,\dot{\mathbf{y}}*{\mathrm{half}}
$$

---

## Python Implementation

The RK2 midpoint method is implemented as

```python
def move_RK2(f, y, dt):
    ydot = f(y)
    y_half = y + ydot * dt/2
    ydot_half = f(y_half)
    y = y + ydot_half * dt
    return y
```

The variables in the code correspond directly to the mathematical expressions:

* `y` represents the current state $\mathbf{y}_n$.
* `ydot` represents the current derivative $\dot{\mathbf{y}}_n$.
* `y_half` represents the estimated midpoint state $\mathbf{y}_{\mathrm{half}}$.
* `ydot_half` represents the midpoint derivative $\dot{\mathbf{y}}_{\mathrm{half}}$.
* `dt` represents the timestep $\Delta t$.

The simulation uses

$$
\Delta t = 0.001\ \text{s}
$$

over a total simulated time of $10$ seconds.

---

## Why Use RK2?

A basic Euler method advances the state using only the derivative at the beginning of each timestep:

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + \Delta t,\dot{\mathbf{y}}_n
$$

The RK2 midpoint method improves this estimate by first calculating an approximate state halfway through the timestep and then using the derivative at that midpoint to advance the system.

For a nonlinear system such as the double pendulum, the state can change significantly during a timestep. Evaluating the derivative at the midpoint provides a more accurate approximation of the system's motion than using only the initial derivative.



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
