import numpy as np
from scipy import integrate

def solvr(Y, t):
    return [Y[1], -2 * Y[0]-Y[1]]

def main():
    a_t = np.arange(0, 25.0, 0.01)
    asol = integrate.odeint(solvr, [1, 0], a_t)
    print(asol)

if __name__ == '__main__':
    main()
