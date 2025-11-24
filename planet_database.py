
# The real G is 6.674e-11 N(m/kg)^2. We use a SCALED G value.
G_SCALED = 0.0001
# The scale factor for position (1 AU = 150 pixels)
AU_PIXELS = 150 
# CRITICAL FIX: Drastically reduced TIME_STEP for stability and accurate integration.
TIME_STEP = 0.005 
# SOFTENING_FACTOR is critical for numerical stability when objects get close
SOFTENING_FACTOR_SQ = 500 

# --- Pygame Setup Constants ---
WIDTH, HEIGHT = 1400, 900 
FPS = 60
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
# NEW: Longer Trail Length
MAX_TRAIL_LENGTH = 3000

# --- PLANET DATA (Scaled Initial Conditions) ---
SUN_MASS_SCALED = 198900000.0

# [Planet Name, Radius (pix), Color, Mass (scaled), Distance (AU)]
PLANETS_DATA = [
    # Sun is the central body
    {'name': 'Sun', 'radius': 20, 'color': (255, 255, 0), 'mass': SUN_MASS_SCALED, 'AU': 0.0},
    
    # Inner Planets
    {'name': 'Mercury', 'radius': 4, 'color': (180, 180, 180), 'mass': 330.0, 'AU': 0.387},
    {'name': 'Venus', 'radius': 7, 'color': (255, 165, 0), 'mass': 4870.0, 'AU': 0.723},
    {'name': 'Earth', 'radius': 8, 'color': (50, 50, 255), 'mass': 5972.0, 'AU': 1.000},
    {'name': 'Mars', 'radius': 5, 'color': (255, 0, 0), 'mass': 641.0, 'AU': 1.520},
    
    # Outer Planets
    {'name': 'Jupiter', 'radius': 15, 'color': (255, 200, 100), 'mass': 1898000.0, 'AU': 5.200},
    {'name': 'Saturn', 'radius': 13, 'color': (255, 255, 150), 'mass': 568300.0, 'AU': 9.580},
    {'name': 'Uranus', 'radius': 11, 'color': (150, 200, 255), 'mass': 86810.0, 'AU': 19.200},
    {'name': 'Neptune', 'radius': 10, 'color': (50, 50, 150), 'mass': 102400.0, 'AU': 30.000},
]
