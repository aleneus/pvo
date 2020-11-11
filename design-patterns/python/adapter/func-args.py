import numpy as np

def smooth(smoother, *args, **kwargs):
    return smoother(*args, **kwargs)

def simple_average(x):
    x_new = []
    for i in range(len(x)-1):
        x_new.append((x[i]+x[i+1])/2)
    return x_new

def smooth_hanning(x, window_width):
    win = np.hanning(window_width)
    x_new = np.convolve(x, win) / sum(win)
    return x_new

x = [1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5]

x_new = smooth(simple_average, x)
print(x_new)

x_new = smooth(smooth_hanning, x, 3)
print(x_new)

x_new = smooth(smooth_hanning, x, window_width=3)
print(x_new)
