# 📝 Project Statement: Solar System N-Body Gravity Simulator

## Problem Statement

The challenge is to accurately model and visualize the gravitational interactions and resulting orbital mechanics of the major celestial bodies within the Solar System[cite: 31]. While simple models (like the two-body problem) are straightforward, accurately solving the complex, coupled **N-Body Problem**—where every planet gravitationally affects every other planet—requires robust numerical methods to maintain stability and realistic behavior over time.

The project addresses this by:
1.  Implementing a stable numerical integrator (**Velocity Verlet**) to solve the $N$-body equations of motion.
2.  Visualizing the resulting orbits in a clear, interactive 2D environment.
3.  Displaying key physical data (relative distance and orbital period in Earth years) to enhance the educational value.

## Scope of the Project

The project focuses on building a computationally efficient simulation engine confined to the following boundaries:

* **Inclusion:** The Sun and the eight major planets (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune).
* **Dimensionality:** The simulation is **2D** (all bodies orbit in a single plane).
* **Physics:** Uses a scaled version of **Newton's Law of Universal Gravitation** and the **Velocity Verlet Method** for time integration.
* **Exclusions:** The simulation does not model non-gravitational forces, relativistic effects, atmospheric drag, or minor celestial bodies (moons, asteroids, comets).

## Target Users

The primary users of this simulation are individuals who need to understand or visualize complex physics concepts:

* **Students:** Those studying introductory physics, mechanics, or computational science to visualize abstract gravitational concepts.
* **Educators:** Teachers and professors who require a demonstrative tool to explain Kepler's Laws and the N-Body problem in a visual context.
* **Hobbyists/Enthusiasts:** Individuals interested in astronomy and the technical aspects of orbit modeling.

## High-Level Features

The system's capabilities are divided into three primary functional modules[cite: 21]:

1.  **Data Input & Initialization:** Initializes planets with calculated initial velocities (V = $\sqrt{GM/R}$) necessary for stable, near-circular orbits, using Kepler's Third Law to pre-calculate accurate orbital periods in Earth Years.
2.  **Physics Computation Engine:** The core module that continuously calculates the net force and acceleration on every body (the N-Body calculation) and updates position/velocity using the highly stable Velocity Verlet integration method.
3.  **Visualization & Reporting:** Renders the 2D environment, draws the planets and their **long trails**, and displays a real-time table of orbital parameters (Distance relative to Earth, Period in Earth Years).