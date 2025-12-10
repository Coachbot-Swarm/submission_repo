"""
Lab 4. Trial 1.

"""

import numpy as np
import math
import struct

def usr(robot):
    
    def wrap_to_pi(angle):
        """ Wraps angle to [-pi to pi]. """
        return (angle + math.pi) % (2 * math.pi) - math.pi

    def normalize(x, y):
        """ Normalizes vector (x, y). """
        magnitude = math.hypot(x, y)
        if magnitude > 0:
            return x / magnitude, y / magnitude
        return 0.0, 0.0
    
    robot.delay(3000) # ensures that the camera and all other peripherals are up and running before your code begins
    
    # any set up variables or code before looping can go here
    log = open("experiment_log.txt", "wb")
    
    log.write("Starting a Coachbot program for Robot 1 to orbit Robot 0.\n")
    log.flush()
    
    while True:
        
        robot.delay() # defaults to 20 ms which is sufficient
    
        robot.set_led(0, 0, 255) # make robots blue :)
        
        # communication range limit
        comm_range_limit = 1.0 # changed # also tried 2.0, 2.5, 3,0 and they all worked in simulation
        
        # weights from paper
        w_align = 1.0
        w_cohesion = 1.0
        w_separation = 2.5 # 1.2 # gonna try 2.5 next
        
        migration_scale = 1.0 / 1.5 # changed # 1.0 / 5.0 # paper uses 1/500 for 500 m arena.
        migration_target = (0.0, 0.0) # origin
        base_speed = 15.0 # 30.0 # 12.0 
        k_turn = 4.0

        neighbors = {}

        while True:
            # get pose
            current_pose = robot.get_pose()
            if not current_pose:
                robot.delay(0.01)
                continue
            x, y, theta = current_pose

            # send msg
            msg = struct.pack('fffi', x, y, theta, robot.virtual_id())
            robot.send_msg(msg)
            robot.delay(50)

            neighbors = {} # clear previous neighbors
            
            msgs = robot.recv_msg()
            robot.delay(50)
            
            for m in msgs:
                if len(m) == 16:
                    nbr_x, nbr_y, nbr_theta, nbr_id = struct.unpack('fffi', m)
                    
                    if nbr_id == robot.virtual_id():
                        continue
                    
                    # check communication range
                    dist = math.hypot(x - nbr_x, y - nbr_y)
                    if dist < comm_range_limit:
                        neighbors[nbr_id] = (nbr_x, nbr_y, nbr_theta, dist)

            # initialize vectors
            align_x, align_y = 0.0, 0.0
            coh_x, coh_y = 0.0, 0.0
            sep_x, sep_y = 0.0, 0.0

            num_neighbors = len(neighbors)

            if num_neighbors > 0:
                
                # initilaize sums for alignment and cohesion
                avg_cos = 0.0
                avg_sin = 0.0
                center_x = 0.0
                center_y = 0.0

                for nid, (nx, ny, ntheta, ndist) in neighbors.items():
                    # alignment avg
                    avg_cos += math.cos(ntheta)
                    avg_sin += math.sin(ntheta)
                    
                    # cohesion avg
                    center_x += nx
                    center_y += ny
                    
                    # separation
                    if ndist > 0:
                        # point away from neighbor
                        dx = x - nx
                        dy = y - ny
                        
                        # seperation = (dx, dy) / dist^2
                        sep_x += dx / (ndist**2)
                        sep_y += dy / (ndist**2)

                # alignment
                avg_heading = math.atan2(avg_sin, avg_cos)
                align_x, align_y = math.cos(avg_heading), math.sin(avg_heading)
                
                # cohesion
                center_x /= num_neighbors
                center_y /= num_neighbors
                coh_x, coh_y = normalize(center_x - x, center_y - y)
                
                # separation
                # sep_x, sep_y = normalize(sep_x, sep_y) # changed: commented it out
                    
            # migration
            mig_dx = migration_target[0] - x
            mig_dy = migration_target[1] - y
            
            # combine weighted vectors
            final_x = (w_align * align_x) + (w_cohesion * coh_x) + (w_separation * sep_x) + (mig_dx * migration_scale) 
            final_y = (w_align * align_y) + (w_cohesion * coh_y) + (w_separation * sep_y) + (mig_dy * migration_scale)

            # calculate wheel speeds
            desired_theta = math.atan2(final_y, final_x)
            angle_error = wrap_to_pi(desired_theta - theta)
            
            turn_speed = k_turn * angle_error # p control
            left_wheel = base_speed - turn_speed
            right_wheel = base_speed + turn_speed
            
            robot.set_vel(left_wheel, right_wheel)
            robot.delay(0.05)

    log.write("Done.\n")
    log.flush()
    
    # clean up before ending the experiment
    log.close() # closing the log file
    return