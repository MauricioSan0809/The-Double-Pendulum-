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

The double pendulum equations of motion form a system of coupled nonlinear ordinary differential equations. Because these equations generally do not have a simple closed-form solution, the system is solved numerically.

This project uses the **second-order Runge-Kutta midpoint method (RK2)** to propagate the state of the double pendulum through time.

The state vector is

$$
\mathbf{y} = \begin{bmatrix} \theta_1 \ \omega_1 \ \theta_2 \ \omega_2 \end{bmatrix}
$$

and the system of differential equations can be written in the general form

$$
\frac{d\mathbf{y}}{dt} = f(\mathbf{y})
$$

where $f(\mathbf{y})$ contains the angular velocities and angular accelerations of both pendulums.

---

### Step 1: Evaluate the Initial Slope

At the beginning of each timestep, the derivative of the current state is evaluated:

$$
\mathbf{k}_1 = f(\mathbf{y}_n)
$$

This derivative represents the instantaneous rate of change of the system at the current state $\mathbf{y}_n$.

---

### Step 2: Estimate the Midpoint

Using the initial slope, an estimate of the state halfway through the timestep is calculated:

$$
\mathbf{y}_{\mathrm{mid}} = \mathbf{y}_n + \frac{\Delta t}{2}\mathbf{k}_1
$$

where $\Delta t$ is the numerical timestep.

Evaluating the system at this midpoint provides a better estimate of how the state changes over the entire timestep.

---

### Step 3: Evaluate the Midpoint Slope

The derivative is evaluated again using the estimated midpoint state:

$$
\mathbf{k}*2 = f(\mathbf{y}*{\mathrm{mid}})
$$

The midpoint slope $\mathbf{k}_2$ is used as the approximation to the average rate of change over the timestep.

---

### Step 4: Update the State

The state is advanced through one complete timestep using the midpoint slope:

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + \Delta t,\mathbf{k}_2
$$

Combining the steps gives the RK2 midpoint algorithm:

$$
\mathbf{k}_1 = f(\mathbf{y}_n)
$$

$$
\mathbf{y}_{\mathrm{mid}} = \mathbf{y}_n + \frac{\Delta t}{2}\mathbf{k}_1
$$

$$
\mathbf{k}*2 = f(\mathbf{y}*{\mathrm{mid}})
$$

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + \Delta t,\mathbf{k}_2
$$

---

## Implementation

The RK2 method is implemented in Python as:

```python
def move_RK2(f, y, dt):
    ydot = f(y)
    y_half = y + ydot * dt/2
    ydot_half = f(y_half)
    y = y + ydot_half * dt
    return y
```

Here:

* `f(y)` evaluates the double pendulum equations of motion.
* `ydot` corresponds to the initial slope $\mathbf{k}_1$.
* `y_half` represents the estimated midpoint state $\mathbf{y}_{\mathrm{mid}}$.
* `ydot_half` corresponds to the midpoint slope $\mathbf{k}_2$.
* `dt` represents the timestep $\Delta t$.

The simulation uses a timestep of

$$
\Delta t = 0.001\ \text{s}
$$

and propagates the equations of motion over a total simulation time of $10$ seconds.

---

## Why RK2?

The standard Euler method estimates the next state using only the derivative at the beginning of the timestep:

$$
\mathbf{y}_{n+1} = \mathbf{y}_n + \Delta t,f(\mathbf{y}_n)
$$

RK2 improves on this approach by evaluating the derivative at an estimated midpoint of the interval. The midpoint slope provides a better approximation of the system's behavior over the timestep.

This is particularly useful for the double pendulum because its equations are nonlinear and the motion can be highly sensitive to changes in the system state.

For this simulation, the numerical timestep was chosen to be small enough to accurately resolve the pendulum motion while limiting numerical error.


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
