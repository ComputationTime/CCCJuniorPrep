# Matplotlib

## Install
on your terminal, run pip install matplotlib
## Data
Put what you wanna graph in the following format

If you have a bunch of points (x1, y1), (x2, y2), (x3, y3), ...

Put them in lists

x = [x1,x2,x3,...]

y = [y1,y2,y3,...]

## Run
The following code should display a line drawn from point to point in order, and a dot where each point is located

import matplotlib.pyplot as plt
plt.plot(x, y, '-o')
plt.show()