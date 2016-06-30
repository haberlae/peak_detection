from __future__ import division, print_function
from detect_peaks import detect_peaks
import numpy as np

#%matplotlib notebook
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, r'./../functions')  # add to pythonpath



def main():

    x = np.sin(2*np.pi*5*np.linspace(0, 1, 200)) + np.random.randn(200)/5
    # set minimum peak height = 0 and minimum peak distance = 20
    ind = detect_peaks(x, mph=0, mpd=20, show=True)
    print(ind)

if __name__ == '__main__':
    main()
