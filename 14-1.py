import re
data = open('14.txt').read()

deers = re.findall(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', data)
target = 2503

max_distance = None

for name, speed, run_time, rest_time in deers:
    speed, run_time, rest_time = int(speed), int(run_time), int(rest_time)
    number_of_cycles = target//(run_time + rest_time)
    time_in_cycle = target%(run_time + rest_time)
    distance = speed*(number_of_cycles*run_time + min(run_time, time_in_cycle))

    if max_distance == None or distance > max_distance:
        max_distance = distance

print max_distance
