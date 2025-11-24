# 🪐 Solar System N-Body Gravity Simulator

## Project Overview

This project is a 2D simulation built using Python and Pygame that models the orbital mechanics of the eight major planets around the Sun. It serves as a powerful visualization tool demonstrating the complex **N-Body gravitational problem** and core computational physics concepts. The goal is to apply subject concepts in a real-world context by designing and implementing a technical solution


## ✨ Key Features 

This simulation meets the requirement for **three major functional modules** (Data Input, Physics Engine, and Rendering)[cite: 21].

* **N-Body Gravity Simulation:** Calculates the mutual gravitational acceleration between **all** celestial bodies simultaneously, providing a high degree of realism.
* **Velocity Verlet Integration:** Uses the Velocity Verlet numerical integration method, which offers superior stability and better energy conservation compared to simpler Euler methods.
* **Orbital Visualization:** Renders all planets with distinct colors, sizes, and **long, continuous orbital trails** (`MAX_TRAIL_LENGTH = 8000`) for clear path visualization.
* **Real-time Orbital Data:** Displays critical information in the top-left corner:
    * **Distance (Relative to Earth):** The current distance from the Sun as a ratio where Earth's orbit is 1.0.
    * **Orbital Period (Earth Years):** The period calculated directly using **Kepler's Third Law** ($T \propto R^{1.5}$).

***

## 🛠️ Technologies and Architecture 

The project is implemented with a **modular and clean structure** , separating physics, rendering, and data into distinct files, meeting the minimum requirement of **5+ meaningful modules/files**[cite: 57].

* **Language:** Python 3.x
* **Visualization/Tools:** Pygame
* **Architecture:** Modular/Component-based Structure
    * `main.py`: Entry point and main game loop.
    * `physics_engine.py`: Core logic for `calculate_acc` and `update_motion` (Velocity Verlet).
    * `render_system.py`: Handles all drawing, labels, and the information box.
    * `planet_database.py`: Stores all constants, scaling factors, and initial planet data.

***

## 🚀 Steps to Install & Run [cite: 94]

1.  **Clone the Repository:**
    ```bash
    git clone [your-repository-url]
    cd solar_system_simulator
    ```

2.  **Install Dependencies:**
    This project requires the `pygame` library.
    ```bash
    pip install pygame
    ```

3.  **Run the Simulation:**
    Execute the main entry script.
    ```bash
    python main.py
    ```

***

## ✅ Instructions for Testing & Validation [cite: 95]

The primary testing approach is visual and conceptual validation, critical for a simulation project.

1.  **Initial Condition Check:** Upon startup, verify that Earth is positioned at `1.000 R_Earth` and has a Period of `1.000 Earth Years`.
2.  **Kepler's Law Check:** Observe that outer planets (e.g., Neptune) move visibly slower than inner planets (e.g., Mercury) and maintain their expected periods (e.g., Jupiter's period should be approximately 11.858 years).
3.  **Stability Check (Non-Functional Requirement):** Run the simulation for an extended period. The orbits should remain stable without significant spiraling inward or outward, which validates the use of the **Velocity Verlet Integrator** and the optimized `TIME_STEP` (Reliability requirement).
4.  **Trail Check:** Confirm that the planetary trails are long and continuous, confirming the `MAX_TRAIL_LENGTH` setting.