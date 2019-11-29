import sys
import math
import numpy as np
import matplotlib.pyplot as plt


def file_input(input_file,x,y):

    i = 0

    a = 11
    b = 9
    c = 11
    d = 4108


    for lines in input_file.readlines():

        items = lines.split()

        if i == d:
            break

        elif i > a:
            y.append(float(lines))

        elif i == b:
            time = float(items[0])

        elif i == c:
            for j in range(int(items[1])+1):
                x.append(j)

        i = i + 1

    return x,y,time



def frequency(y,time):

    y_new = []

    for i in range(len(y)):
        y_new.append(y[i]/time)

    return y_new


def identify(x):

    num = []
    peak = 0

    while not peak == "n":
        peak = input("X-Coordinate of Peak: ")
        if not peak == "n":
            num.append(int(peak))

    peaks = np.zeros([len(num),2])

    for i in range(len(num)):

        peaks[i,0] = x[num[i]-10]
        peaks[i,1] = x[num[i]+10]

    print(" ")

    return peaks,len(num)



def peak_sum(x,y,minx,maxx,t):

    x_peak = []
    y_peak = []

    a = (-y[int(minx)]+y[int(maxx)])/(-x[int(minx)]+x[int(maxx)])
    b = y[int(minx)]-a*x[int(minx)]
    b = b + y[int(minx)+1]-a*x[int(minx)+1]
    b = b + y[int(minx)+2]-a*x[int(minx)+2]
    b = b + y[int(minx)+3]-a*x[int(minx)+3]
    b = b + y[int(maxx)]-a*x[int(maxx)]
    b = b + y[int(maxx)-1]-a*x[int(maxx)-1]
    b = b + y[int(maxx)-2]-a*x[int(maxx)-2]
    b = b + y[int(maxx)-3]-a*x[int(maxx)-3]
    b = b/8


    for i in range(int(minx),int(maxx)):
        x_peak.append(x[i])
        y_peak.append(y[i]-a*x[i]-b)

    area = 0
    unc = 0

    for j in range(len(x_peak)):
        area = area + y_peak[j]
        unc = unc + y_peak[j]/t


    unc = np.sqrt(unc)

    return area,unc



def graph(x,y):

    plt.plot(x,y)
    plt.title("Gamma Ray Spectrum")
    plt.ylabel("Number of Events")
    plt.xlabel("Energy of Events/keV")
    plt.show()



def main():

    input_file = open(sys.argv[1],"r")

    x = []
    y = []

    x,y,t = file_input(input_file,x,y)

    input_file.close()

    graph(x,y)

    y = frequency(y,t)
    peaks,num = identify(x)

    area = []
    unc = []

    for i in range(num):
        a,b = peak_sum(x,y,peaks[i,0],peaks[i,1],t)
        area.append(a)
        unc.append(b)

    output_file = open(sys.argv[2],"w+")
    output_file.write("Areas of Peaks in Spectrum" + "\n")
    output_file.write(" " + "\n")

    for j in range(len(area)):
        output_file.write(str(peaks[j,0]+10) + " keV Peak: " + str(area[j]) + " +- " + str(unc[j]) + "\n")


main()