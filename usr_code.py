import struct
import math

def usr(robot):

    robot.delay(3000) # ensures that the camera and all other peripherals are up and running before your code begins
    # any set up variables or code before looping can go here
    log = open("experiment_log.txt", "w")
    
    log.write("Lab1b Assignment\n")
    log.flush()

    write_str = "I am robot " + str(robot.virtual_id())
    log.write(write_str)
    log.flush()

    desired_distance = 0.5 #will vary from 0.3-0.5

    prev_distance = 0   # Initializing previous distance 
    led_colors = [0,0,0]    # Starting LED color is black

    while True:
        if (robot.virtual_id() == 0):
            # if we received a message, print out info
            msgs = robot.recv_msg()
            if len(msgs) > 0:
                pose_rxed = struct.unpack('ffi', msgs[0][:12])

                # Check if there is a valid pose
                if pose_t:
                    
                    # Compute distances between the two robots
                    computed_distance = math.sqrt((pose_t[0] - pose_rxed[0])**2 + (pose_t[1] - pose_rxed[1])**2)
                    
                    # Print out the distance values to terminal
                    # print('robot ', robot.virtual_id(), 'to robot ', pose_rxed[2], 'distance: ', computed_distance)

                    # Change LED according to how large the distance is
                    if computed_distance > desired_distance:
                        led_colors = [100,0,0]
                    else: 
                        led_colors = [0,100,0]

                #blink led if message is received  
                robot.set_led(0,0,0)
                robot.delay(10)
                robot.set_led(*led_colors)

            # if there is a new postion sensor update transmit info
            pose_t = robot.get_pose()
            if pose_t:  # check pose is valid before using
                robot.send_msg(struct.pack('ffi', pose_t[0], pose_t[1], robot.virtual_id()))  # send pose x,y in message
            
        if (robot.virtual_id() == 1):
            # if we received a message, print out info in message
            msgs = robot.recv_msg()
            if len(msgs) > 0:
                pose_rxed = struct.unpack('ffi', msgs[0][:12])

                # Check if there is a valid pose
                if pose_t:
                    
                    # Compute distances between the two robots
                    computed_distance = math.sqrt((pose_t[0] - pose_rxed[0])**2 + (pose_t[1] - pose_rxed[1])**2)
                    
                    # If robots are too far apart
                    if computed_distance > desired_distance:

                        # Change LED color to red
                        led_colors = [100,0,0]
                        
                        # If getting closer move in wide circle
                        if (desired_distance - prev_distance) > (desired_distance - computed_distance):

                            # Difference between desired and computed distances
                            error = computed_distance - desired_distance
                            # Proportional term
                            # P = 1950
                            P = 1100

                            # Update velocity according to P-term
                            # robot.set_vel(100, (P * error))
                            robot.set_vel(50, (P * error))

                        # If getting farther move in tight circle
                        else: 

                            # Difference between desired and computed distances
                            error = computed_distance - desired_distance
                            # Proportional term
                            # P = 6000
                            P = 2000

                            # Update velocity according to P-term
                            # robot.set_vel(100,(P * error)) 
                            robot.set_vel(50,(P * error)) 

                    # If robots are too close
                    else: 

                        # Change LED color to green
                        led_colors = [0,100,0]

                        # If getting closer move in wide circle
                        if (desired_distance - prev_distance) > (desired_distance - computed_distance):

                            # Difference between desired and computed distances
                            error = desired_distance - computed_distance 
                            # Proportional term
                            # P = 19900
                            P = 2000

                            # Change of velocity between time steps
                            der = computed_distance-prev_distance
                            # Derivative term
                            # D = 20000 
                            D = 10000 

                            # Update velocity according to P-term and D-term
                            # robot.set_vel(100,(P * error) - D * der)
                            robot.set_vel(50,(P * error) - D * der)

                        # If getting farther move in straight line
                        else: 
                            # robot.set_vel(100,100)
                            robot.set_vel(50,50)

                    # Update previous distance to compare how distance are changing
                    prev_distance = computed_distance

                #blink led if message is received 
                robot.set_led(0,0,0)
                robot.delay(10)
                robot.set_led(*led_colors)

            # if there is a new postion sensor update, print out and transmit the info
            pose_t = robot.get_pose()
            if pose_t:  # check pose is valid before using
                robot.send_msg(struct.pack('ffi', pose_t[0], pose_t[1], robot.virtual_id()))  # send pose x,y in message

        # clean up before ending the experiment
        log.close() # closing the log file
        return
