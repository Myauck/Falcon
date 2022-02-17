from textwrap import indent
from tello import Tello
from datetime import datetime
import time
import json

start_time = str(datetime.now())

config_file = "config.json"
file_name = 'command.txt'

j = open(config_file, 'r')
data = json.loads(j.read())
n = data['variables']['n']
j.close()

f = open(file_name, "r")
commands = f.readlines()
tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        if command.find('delay') != -1:
            test =command.partition('delay')[2]
            sec = float(test)
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()
f.close()

n+=1
with open(f'log/{n}.txt', 'w+') as out:
    for stat in log:
        stat.print_stats()
        str = stat.return_stats()
        out.write(str)

data['logs'].append(start_time)
data['variables']['n'] = n

k = open('config.json', 'w+')
k.write(json.dumps(data, indent=4))
k.close()