import drone

drone_ip = ""
drone_port = 0

Drone = drone.Drone(drone_ip, drone_port)

# Connect to UDP endpoint.
# Use returned Vehicle object to query device state - e.g. to get the mode:
# print("Mode: %s" % vehicle.mode.name)