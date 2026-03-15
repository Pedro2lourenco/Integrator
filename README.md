# Hamiltonian Dynamics Simulation with Suzuki–Yoshida Integrator

Author: Pedro Lourenço

## Overview

This project implements a numerical simulation of a **2D Hamiltonian system** using a **fourth-order symplectic integrator (Suzuki–Yoshida method)**.

The system evolves according to a Hamiltonian of the form:

H = K + V

where:

- K is the kinetic energy
- V is a periodic potential based on cosine functions

The simulation integrates Hamilton's equations and visualizes the trajectory in phase space.

---

## Hamiltonian of the System

The Hamiltonian used in this simulation is:

K = Px² + Py²

V = U (cos²(x) + cos²(y) − 2a cos(x)cos(y))

where:

- `U` is the potential strength
- `a` controls the coupling between the two directions

---

## Numerical Method

The integration is performed using a **4th-order symplectic integrator** based on the **Suzuki–Yoshida decomposition**.

Symplectic integrators are important because they:

- preserve the Hamiltonian structure
- reduce long-term energy drift
- are widely used in molecular dynamics and celestial mechanics.

---

## Requirements

The code uses the following Python libraries:

- numpy
- matplotlib

Install them with:

```bash
pip install numpy matplotlib
