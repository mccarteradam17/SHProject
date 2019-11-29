import sys
import numpy as np
import math
import matplotlib.pyplot as plt

def input_file(a):

    y_sum = [0]*4096
    y_av = []

    for l in range(a):
        input_data = open(sys.argv[2+l],"r")

        i = 0

        a2 = 11
        b = 9
        c = 11
        d = 4108

        x = []
        y = []


        for lines in input_data.readlines():

            items = lines.split()

            if i == d:
                break

            elif i > a2:
                y.append(float(lines))

            elif i == b:
                time = float(items[0])

            elif i == c:
                for j in range(int(items[1])+1):
                    x.append(j)

            i = i + 1

        y = frequency(y,time)

        for m in range(len(y)):
            y_sum[m] = y_sum[m] + y[m]

        input_data.close()

    for n in range(len(y_sum)):
        y_av.append(y_sum[n]/a)

    return x,y_av,time


def frequency(y,time):

    y_new = []

    for i in range(len(y)):
        y_new.append(y[i]/time)

    return y_new


def graph(x,y):

    plt.plot(x,y)
    plt.title("Gamma Ray Spectrum")
    plt.ylabel("Frequency of Events/s^-1")
    plt.xlabel("Energy of Events/keV")
    plt.show()



def identify(x,y):

    total = 0
    average = []

    for i in range(len(x)):
        if i < 5:

            for j in range(i+6):
                total = total + y[j]
            ave = total/(i+6)
            total = 0

        elif i > (len(x) - 5):

            for k in range(i-5,len(x)):
                total = total + y[k]
            ave = total/(len(x)-(i-5))
            total = 0

        else:

            for l in range(i-5,i+5):
                total = total + y[l]
            ave = total/((i+5)-(i-5))
            total = 0

        average.append(ave)

    num = []

    threshold = float(input("Minimum peak threshold: "))

    a_list = []

    for m in range(len(x)):
        
        a = y[m]-average[m]
        a_list.append(a)

        if a > threshold:
            num.append(m)

    #graph(x,a_list)

    num2 = [num[0]]

    for o in range(1,len(num)):

        p = num[o]

        if (num[o-1]-p)**2 > 1:
            num2.append(p)


    peaks = np.zeros([len(num2),2])


    for n in range(len(num2)):

        peaks[n,0] = x[num2[n]-10]
        peaks[n,1] = x[num2[n]+10]


    return peaks,len(num2)



def identify2(x):

    num2 = []
    peak = 0

    while not peak == "n":
        peak = input("X-Coordinate of Peak: ")
        if not peak == "n":
            num2.append(int(peak))

    peaks = np.zeros([len(num2),2])

    for i in range(len(num2)):

        peaks[i,0] = x[num2[i]-10]
        peaks[i,1] = x[num2[i]+10]

    print(" ")

    return peaks,len(num2)



def chi_square(x,y,minx,maxx,peak_no,output_file,time):

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

    u0 = (float(minx+maxx))/2
    A0 = y[int(u0)]

    unc = 10
    step = 1

    s0 = step

    for j in range(4):
        u0,s0,A0 = chi_loop(u0,s0,A0,(unc/(10**j)),(step/10**j),x_peak,y_peak,time,a,b)

    u_min = u0
    s_min = s0
    A_min = A0

    #print("Mean: " + str(u_min))
    #print("Standard Deviation: " + str(s_min))
    #print("Amplitude: " + str(A_min))

    y_chi = []
    x_chi = []

    for k in range(len(x_peak)):
        x_chi.append(x_peak[k])
        x_chi.append(x_peak[k]+0.25)
        x_chi.append(x_peak[k]+0.5)
        x_chi.append(x_peak[k]+0.75)


    for l in range(len(x_chi)):
        n = A_min*math.exp((-1/2)*(1/(s_min**2))*((x_chi[l]-u_min)**2))
        y_chi.append(n)


    plt.plot(x_peak,y_peak,color="r",label="Data")
    plt.plot(x_chi,y_chi,color="b",label="Fit")
    plt.title("Gamma Ray Spectrum of measured peak with associated Minimum Chi-Squared Fit")
    plt.ylabel("Frequency of Events/s^-1")
    plt.xlabel("Energy of Events/keV")
    plt.legend()
    plt.show()

    test = input("Save? ")

    if test == "y":
        output_file.write("Peak " + str(peak_no+1) + ":" + "\n")
        output_file.write("Mean: " + str(u_min) + "\n")
        output_file.write("Standard Deviation: " + str(s_min) + "\n")
        output_file.write("Amplitude: " + str(A_min) + "\n")
        output_file.write("\n")




def chi_loop(u0,s0,A0,unc,step,x_peak,y_peak,time,sub,sub2):

    chi2 = 0

    chi3 = []
    chiu = []
    chis = []
    chiA = []

    u = u0-unc
    A = A0-unc

    if s0-unc <= 0:
        s = step
    else:
        s = s0-unc


    while u <= (u0+unc):
        while s <= (s0+unc):
            while A <= (A0+unc):
                for z in range(len(y_peak)):
                    b = float(y_peak[z])
                    #sigma = (b+sub*x_peak[z]+sub)/time
                    sigma = 1
                    a = (1/(sigma**2))
                    d = float(x_peak[z])

                    chi1 = a*((b - A*math.exp((-1/2)*(1/(s**2))*((d-u)**2)))**2)
                    chi2 = chi2 + chi1

                chi3.append(chi2)
                chis.append(s)
                chiu.append(u)
                chiA.append(A)

                chi2 = 0

                A = A + step

            s = s + step
            A = A0 - unc

        u = u + step

        if s0-unc <= 0:
            s = step
        else:
            s = s0-unc


    minchi = chi3[0]
    minind = 0

    for m in range(len(chi3)):

        if chi3[m] < minchi:
            minchi = chi3[m]
            minind = m


    A_min = chiA[minind]
    s_min = chis[minind]
    u_min = chiu[minind]


    return u_min,s_min,A_min



def main():

    a = int(sys.argv[1])

    x,y,time = input_file(a)

    graph(x,y)

    peaks,num = identify(x,y)
    #peaks,num = identify2(x)

    output_file = open(sys.argv[a+2],"w+")

    output_file.write("Chi-Squared Fit Data" + "\n")
    output_file.write("\n")

    for i in range(num):
        #print("[" + str(peaks[i,0]) + "," + str(peaks[i,1]) + "]")
        chi_square(x,y,peaks[i,0],peaks[i,1],i,output_file,time)

    output_file.close()


main()