s = int(input())
w = int(input())

healthy = True

if s > 23 or s < 20:
    healthy = False

if w > 9 or w < 6:
    healthy = False

pm_time = 24 - s


sleep_time = pm_time + w


if sleep_time > 10 or sleep_time < 8:
    healthy = False


if healthy:
    print('Healthy')
else:
    print('Unhealthy')