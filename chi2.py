import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



def func(x,a,b):
    return b*(1 - x/np.sqrt(x**2 + a**2))


def main():

    x_data = np.array([20,30,40,50,60,70])
    y_data = np.array([1,0.718066978,0.527828476,0.40583859,0.318547302,0.249600888])
    yerr = np.array([0.046086343,0.033097016,0.024329392,0.018709778,0.014688256,0.011518657])
    xerr = np.array([0.5,0.5,0.5,0.5,0.5,0.5])

    popt,pcov = curve_fit(func,x_data,y_data,sigma=yerr) 

    print("[r, A]")
    print(popt)
    perr = np.sqrt(np.diag(pcov))
    print("[r uncertainty, A uncertainty]")
    print(perr)

    plt.errorbar(x_data,y_data,yerr=yerr,xerr=xerr,fmt="none",color="black",capsize=5.0)
    plt.title("Relative Efficiency at each point against Distance from Detector")
    plt.xlabel("On-axis Distance from Detector/mm")
    plt.ylabel("Relative Efficieny to point @ 20mm")
    plt.plot(x_data,func(x_data,*popt),color="r")
    plt.show()

    y_res = y_data - func(x_data,*popt)

    plt.errorbar(x_data,y_res,yerr=yerr,fmt="none",color="black",capsize=5.0)
    plt.scatter(x_data,y_res)
    plt.plot([-10,100],[0,0],color="black")
    plt.xlim(10,80)
    plt.title("Residuals of Relative Efficiency against Distance from Detector")
    plt.xlabel("On-axis Distance from Detector/mm")
    plt.ylabel("Residuals")
    plt.show()
    
main()