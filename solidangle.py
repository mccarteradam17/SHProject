import sys
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt


def input_data(input_file):

    r = []
    z = []
    data = []
    i = 0
    r_ax = []

    for lines in input_file.readlines():

        item = lines.split()

        if i == 0:
            for j in range(1,len(item)):
                r_ax.append(float(item[j]))

        else:
            for k in range(1,len(item)):
                z.append(float(item[0]))
                data.append(item[k])
            for n in range(len(r_ax)):
                r.append(r_ax[n])

        i = i + 1


    for m in range(len(data)):
            a = str(data[m])
            sign = a[0]
            if sign == "0":
                sign = 1
            elif sign == "F":
                sign = -1
            b = a[1:7]
            value = float(b)
            value = value/(10**6)
            powersign = a[7]
            if powersign == "0":
                powersign = 1
            elif powersign == "F":
                powersign = -1
            power = a[8:10]
            power = float(power)
            value = sign*value*(10**(powersign*power))
            data[m] = float(value)


    return r,z,data


def input_data2(input_file1,input_file2):

    r1 = []
    z1 = []
    data1 = []
    i1 = 0
    r_ax1 = []
    r2 = []
    z2 = []
    data2 = []
    i2 = 0
    r_ax2 = []

    for lines1 in input_file1.readlines():

        item = lines1.split()

        if i1 == 0:
            for j in range(1,len(item)):
                r_ax1.append(float(item[j]))

        else:
            for k in range(1,len(item)):
                z1.append(float(item[0]))
                data1.append(item[k])
            for n in range(len(r_ax1)):
                r1.append(r_ax1[n])

        i1 = i1 + 1

    for lines2 in input_file2.readlines():

        item = lines2.split()

        if i2 == 0:
            for l in range(1,len(item)):
                r_ax2.append(float(item[l]))

        else:
            for m in range(1,len(item)):
                z2.append(float(item[0]))
                data2.append(item[m])
            for o in range(len(r_ax2)):
                r2.append(r_ax2[o])

        i2 = i2 + 1


    for s in range(len(data1)):
            a = str(data1[s])
            sign = a[0]
            if sign == "0":
                sign = 1
            elif sign == "F":
                sign = -1
            b = a[1:7]
            value = float(b)
            value = value/(10**6)
            powersign = a[7]
            if powersign == "0":
                powersign = 1
            elif powersign == "F":
                powersign = -1
            power = a[8:10]
            power = float(power)
            value = sign*value*(10**(powersign*power))
            data1[s] = float(value)


    for t in range(len(data2)):
            a = str(data2[t])
            sign = a[0]
            if sign == "0":
                sign = 1
            elif sign == "F":
                sign = -1
            b = a[1:7]
            value = float(b)
            value = value/(10**6)
            powersign = a[7]
            if powersign == "0":
                powersign = 1
            elif powersign == "F":
                powersign = -1
            power = a[8:10]
            power = float(power)
            value = sign*value*(10**(powersign*power))
            data2[t] = float(value)



    length = (57/25.4)/((55.7/2)/25.4)
    length = float(int(length*10))/10
    maxm = 7.6 - length

    r = []
    z = []
    data = []

    for p in range(len(data2)):
        if z2[p] <= maxm:

            for q in range(len(data2)):
                if z2[q] == z2[p] + length and r2[q] == r2[p]:
                    val = data2[q] - data2[p] + data1[p]
                    data.append(val)
                    r.append(r2[p])
                    z.append(z2[p])
                    

    return r,z,data


def mydata():

    x = []
    y = []
    z = []
    unc = []

    input_file = open("geo_eff_data.txt","r")
    n = 3

    for line in input_file.readlines():
        if line == "\n":
            n = n-1

        elif n < 0:
            break

        elif n == 3:
            x.append(float(line))

        elif n == 2:
            y.append(float(line))

        elif n == 1:
            z.append(float(line))

        elif n == 0:
            unc.append(float(line))

    input_file.close()


    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    unc = np.array(unc)

    radius = 41.6

    x = x/radius
    y = y/radius
    z = z*3.47326


    return x,y,z,unc





def main():

    input_file = open("solid_angle_raw.txt","r")
    input_file2 = open("solid_angle_raw2.txt","r")
    input_file3 = open("solid_angle_raw3.txt","r")


    r,z,data = input_data(input_file)
    r2,z2,data2 = input_data2(input_file2,input_file3)

    input_file.close()
    input_file2.close()
    input_file3.close()

    r.extend(r2)
    z.extend(z2)
    data.extend(data2)

    r = np.array(r)
    z = np.array(z)
    data = np.array(data)

    r3,z3,data3,unc = mydata()

    
    ax = plt.axes(projection="3d")

    ax.scatter3D(z, r, data, marker=".")
    ax.scatter3D(z3, r3, data3, color="r")
    
    ax.set_xlabel('z')
    ax.set_ylabel('rho')
    ax.set_zlabel('Solid Angle/steradians')
    
    plt.title("Solid Angle against position of source for a unit detector")
    plt.show()


main()