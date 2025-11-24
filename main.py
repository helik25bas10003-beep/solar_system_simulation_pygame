import math
import pygame
import planet_database as pd
import physics_engine as ph


def initialize_bodies():
    """Creates the list of body dictionaries with initial positions and velocities."""
    bodies = []
    
    # Kepler's Third Law (T^2 is proportional to R^3) is used for period in Earth Years.
    
    for data in pd.PLANETS_DATA:
        R_au = data['AU']
        R_pix = R_au * pd.AU_PIXELS
        
        V_pix = 0.0
        # NEW: Orbital period in Earth Years (T = R^1.5)
        T_earth_years = 0.0 
        
        if R_pix != 0.0:
            # Calculate the velocity for a perfect circular orbit: V = sqrt(G * M_sun / R)
            V_pix = math.sqrt(pd.G_SCALED * pd.SUN_MASS_SCALED / R_pix)
            
            # Calculate the period in Earth Years
            T_earth_years = math.pow(R_au, 1.5)
        
        body = {
            'name': data['name'],
            'x':pd. CENTER_X + R_pix, 
            'y': pd.CENTER_Y, 
            'radius': data['radius'],
            'color': data['color'],
            'mass': data['mass'], 
            'vx': 0.0, 
            'vy': V_pix, 
            'ax': 0.0,   
            'ay': 0.0,   
            'trail': [],
            'initial_au': R_au,
            'earth_years': T_earth_years # Storing the period in Earth Years
        }
        
        # Sun is at the center
        if data['name'] == 'Sun':
            body['x'] = pd.CENTER_X
            body['y'] = pd.CENTER_Y
            body['vy'] = 0.0
        
        bodies.append(body)
        
    return bodies


def draw_info_box(screen, bodies, font):
    """Draws the orbital data table in the top-left corner."""
    text_color = (200, 200, 200)
    start_x, start_y = 20, 50
    line_spacing = 30
    
    # Header: Updated to display Earth Years
    header_text = font.render("Planet | Distance (AU) | Period (Earth Years)", True, (255, 255, 255))
    screen.blit(header_text, (start_x, start_y))
    
    current_y = start_y + line_spacing

    for body in bodies:
        if body['name'] == 'Sun':
            continue
            
        # Current distance from Sun (in pixels, converted back to AU)
        dx = body['x'] - pd.CENTER_X
        dy = body['y'] - pd.CENTER_Y
        current_distance_pix = math.sqrt(dx**2 + dy**2)
        current_distance_au = current_distance_pix / pd.AU_PIXELS
        
        # Display name, current distance, and period in Earth Years
        info_line = (
            f"{body['name']:<10} | "
            f"{current_distance_au:.3f} AU   | "
            f"{body['earth_years']:.3f}"
        )
        
        info_surface = font.render(info_line, True, body['color'])
        screen.blit(info_surface, (start_x, current_y))
        current_y += line_spacing


def draw_elements(screen, bodies, font):
    """Draws the background, trails, bodies, and labels."""
    screen.fill((0,0,0)) 

    # Trail drawing
    for body in bodies:
        if len(body['trail']) > 1 and body['name'] != 'Sun':
            # Draw the path using the body's color
            pygame.draw.lines(screen, body['color'], False, body['trail'], 1)

    # Body drawing
    for body in bodies:
        # Position coordinates must be integers for pygame.draw.circle
        pygame.draw.circle(screen, body['color'], (int(body['x']), int(body['y'])), body['radius'])

        # Draw Labels
        name_text = font.render(body['name'], True, body['color'])
        screen.blit(name_text, (int(body['x']) - body['radius'], int(body['y']) + body['radius'] + 5))
        
    # Draw the information box
    draw_info_box(screen, bodies, font)

def main():
    """The main game loop setup and execution."""
    
    celestial_bodies = initialize_bodies()

    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((pd.WIDTH, pd.HEIGHT))
    pygame.display.set_caption("Realistic Solar System N-Body Simulation (Velocity Verlet)")
    
    font = pygame.font.Font(None, 24)
    
    clock = pygame.time.Clock()
    
    # Initial calculation of acceleration for the first step of Verlet
    initial_accelerations = ph.calculate_acc(celestial_bodies)
    for i, body in enumerate(celestial_bodies):
        body['ax'] = initial_accelerations[i][0]
        body['ay'] = initial_accelerations[i][1]
    
    # --- Main Loop ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 1. Calculate Acceleration at t+dt (the 'new' acceleration)
        new_accelerations = ph.calculate_acc(celestial_bodies)
        
        # 2. Physics Update using Velocity Verlet
        ph.update_motion(celestial_bodies, new_accelerations)
        
        # 3. Drawing
        draw_elements(screen, celestial_bodies, font)
        
        # 4. Update the full display surface to the screen
        pygame.display.flip()
        
        # 5. Cap the frame rate
        clock.tick(pd.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()