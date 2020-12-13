from math import ceil


data = open("input.txt").read().splitlines()


#part one
time = int(data[0])
bus_list = [int(bus) for bus in data[1].split(',') if bus.isdigit()]
res = min([(ceil(time/bus)*bus, bus) for bus in bus_list])
print(f'Part one: {(res[0]-time) * res[1]}')