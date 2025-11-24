import planet_database as pd
import math


def calculate_acc(bodies):
    
    """
    Calculates the acceleration vector (ax, ay) for every body 
    based on the gravitational force exerted by ALL other bodies (N-body problem).
    """
    accelerations = []

    for i, currentbody in enumerate(bodies):
        net_ax = 0.0 
        net_ay = 0.0

        # Skip calculating acceleration for the stationary Sun
        if currentbody['name'] == 'Sun':
            accelerations.append((0.0, 0.0))
            continue
        
        for j, otherbody in enumerate(bodies):
            if i == j:
                continue
            
            dx = otherbody['x'] - currentbody['x']
            dy = otherbody['y'] - currentbody['y']
            
            r_sq = dx**2 + dy**2 + pd.SOFTENING_FACTOR_SQ 
            r = math.sqrt(r_sq)

            # Acceleration magnitude: a = G * m2 / r^2
            a_mag = pd.G_SCALED * otherbody['mass'] / r_sq

            # Decompose acceleration into components:
            net_ax += a_mag * dx / r
            net_ay += a_mag * dy / r

        accelerations.append((net_ax, net_ay))

    return accelerations


def update_motion(bodies, new_accelerations):
    """
    Implements the Velocity Verlet Method for numerical integration.
    """
    dt = pd.TIME_STEP 
    
    for i, body in enumerate(bodies):
        # The Sun is assumed to be stationary
        if body['name'] == 'Sun':
             continue
        
        ax_old = body['ax']
        ay_old = body['ay']
        ax_new = new_accelerations[i][0]
        ay_new = new_accelerations[i][1]

        # 1. Update Position
        body['x'] += body['vx'] * dt + 0.5 * ax_old * dt**2
        body['y'] += body['vy'] * dt + 0.5 * ay_old * dt**2

        # 2. Update Velocity
        body['vx'] += 0.5 * (ax_old + ax_new) * dt
        body['vy'] += 0.5 * (ay_old + ay_new) * dt
        
        # 3. Store new acceleration
        body['ax'] = ax_new
        body['ay'] = ay_new

        # 4. Update Trail for Orbit Path
        body['trail'].append((int(body['x']), int(body['y'])))
        if len(body['trail']) > pd.MAX_TRAIL_LENGTH: 
            body['trail'].pop(0)
