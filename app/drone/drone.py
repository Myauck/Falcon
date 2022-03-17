from tellodrone import TelloDrone

drone = TelloDrone()

while True:
    cmd = input("")
    if(cmd == "end"):
        break
    drone.send_command(cmd)