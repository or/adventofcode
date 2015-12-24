#!/usr/bin/python3
import re
import sys

lines = list(line.strip() for line in sys.stdin if line.strip())

reindeers = []
for line in lines:
    mo = re.match(r'^(.+)? can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$', line)
    name, speed, dash, rest = mo.groups()
    reindeers.append((int(speed), int(dash), int(rest)))

def calc(time, speed, dash, rest):
    period = dash + rest
    distance = (time // period) * speed * dash
    period_rest = time % period
    distance += min(period_rest, dash) * speed

    return distance

def solve(time, reindeers):
    distances = [calc(time, speed, dash, rest) for (speed, dash, rest) in reindeers]
    distances.sort()
    return distances[-1]

def solve2(time, reindeers):
    points = [0 for _ in reindeers]
    for secs in range(1, time + 1):
        distances = [calc(secs, speed, dash, rest) for (speed, dash, rest) in reindeers]
        winner = max(distances)
        for i in range(len(reindeers)):
            if distances[i] == winner:
                points[i] += 1

    return max(points)

print(solve(2503, reindeers))
print(solve2(2503, reindeers))
