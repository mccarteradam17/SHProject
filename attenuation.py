import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



def graph(x,y):

    plt.scatter(x,y)
    plt.title("Gamma Ray Spectrum")
    plt.ylabel("Number of Events")
    plt.xlabel("Energy of Events/keV")
    plt.show()



def graph3D(x,y,z):

    ax = plt.axes(projection="3d")

    ax.scatter3D(x, y, z)
    
    ax.set_xlabel('x/cm')
    ax.set_ylabel('y/cm')
    ax.set_zlabel('z/cm')
    plt.xlim(-12.5,12.5)
    plt.ylim(-12.5,12.5)
    
    plt.show()



def glass_bottle():

    x_list = []
    y_list = []
    z_list = []

    z = 0

    while True:

        if z == 0:
            for y in range(7):
                x_range = int(11 - 2*np.absolute(y-3))
                x_step = 5 - np.absolute(y-3)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-3)
                    z_list.append(z)
            
            z = z + 1

        elif z > 0 and z <= 10:
            for y in range(7):
                x_range = int(11 - 2*np.absolute(y-3))
                x_step = 5 - np.absolute(y-3)
                for x in range(x_range):
                    if x == 0 or x == (x_range-1):
                        x_list.append(x-x_step)
                        y_list.append(y-3)
                        z_list.append(z)
                    elif y == 0 or y == 6:
                        x_list.append(x-x_step)
                        y_list.append(y-3)
                        z_list.append(z)
            
            z = z + 1

        elif z > 10 and z < 19:
            for y in range(7):
                x_range = int(10 - 2*np.absolute(y-3))
                x_step = 4.5 - np.absolute(y-3)
                for x in range(x_range):
                    if x == 0 or x == (x_range-1):
                        x_list.append(x-x_step)
                        y_list.append(y-3)
                        z_list.append(z)
                    elif y == 0 or y == 6:
                        x_list.append(x-x_step)
                        y_list.append(y-3)
                        z_list.append(z)
            
            z = z + 1

        elif z == 19:
            for y in range(7):
                x_range = int(10 - 2*np.absolute(y-3))
                x_step = 4.5 - np.absolute(y-3)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-3)
                    z_list.append(z)
            
            z = z + 1

        elif z > 19 and z < 26:
            for y in range(4):
                x_range = int(4 - 2*np.absolute(y-1.5))
                x_step = 1.5 - np.absolute(y-1.5)
                for x in range(x_range):
                    if x == 0 or x == (x_range-1):
                        x_list.append(x-x_step)
                        y_list.append(y-1.5)
                        z_list.append(z)
                    elif y == 0 or y == 3:
                        x_list.append(x-x_step)
                        y_list.append(y-1.5)
                        z_list.append(z)
            
            z = z + 1

        elif z == 26:
            for y in range(4):
                x_range = int(4 - 2*np.absolute(y-1.5))
                x_step = 1.5 - np.absolute(y-1.5)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-1.5)
                    z_list.append(z)
            
            z = z + 1

        elif z > 26:
            break



    #graph(x_list,y_list)
    #graph(y_list,z_list)
    #graph(x_list,z_list)
    #graph3D(x_list,y_list,z_list)


    model = np.zeros([len(x_list),6])
    input_filename = "solid_angle_cherry_glass.txt"

    thick = 0.5
    a = input("Whisky in Bottle? y/n: ")
    if a == "y":
        whisky = 1
    else:
        whisky = 0

    for i in range(len(x_list)):
        model[i,0] = x_list[i]
        model[i,1] = y_list[i]
        model[i,2] = z_list[i]
        z_val = model[i,1]*10 - min(y_list)*10 + 20
        r_val = np.sqrt((model[i,0]*10)**2 + (model[i,2]*10)**2)
        if y_list[i] < 0:
            model[i,4] = thick
            if whisky > 0:
                model[i,5] = ((np.sqrt((r_val)**2 + z_val**2))-25)/10
            else:
                model[i,5] = 0
        elif y_list[i] == 0:
            model[i,4] = thick
        model[i,3] = read2(r_val,z_val,input_filename)

    #print(model)

    eff_sum = 0
    output_list = []
    att_whisky = 1
    att_w = []

    for m in range(22):
        att_whisky = float(input("Attenuation coefficient of Whisky: "))
        att_w.append(att_whisky)


    for k in range(22):
        att_coeff = float(input("Attenuation coefficient of Bottle: "))

        for j in range(len(x_list)):
            att = np.exp(att_coeff*model[j,4])*np.exp(att_w[k]*model[j,5])
            eff = model[j,3]/att
            eff_sum = eff_sum + eff

        output_list.append(len(x_list)/eff_sum)
        eff_sum = 0

    print(" ")
    print("Total Geometric and Attenuation Efficiency:")

    for l in range(len(output_list)):
        print(str(output_list[l]))



def polyethylene_bottle():

    x_list = []
    y_list = []
    z_list = []

    z = 0

    while True:

        if z == 0 or z == 18:
            for y in range(9):
                x_range = int(9 - 2*np.absolute(y-4))
                x_step = 4 - np.absolute(y-4)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-4)
                    z_list.append(z)
            
            z = z + 1

        elif z > 0 and z < 18:
            for y in range(9):
                x_range = int(9 - 2*np.absolute(y-4))
                x_step = 4 - np.absolute(y-4)
                for x in range(x_range):
                    if x == 0 or x == (x_range-1):
                        x_list.append(x-x_step)
                        y_list.append(y-4)
                        z_list.append(z)
                    elif y == 0 or y == 8:
                        x_list.append(x-x_step)
                        y_list.append(y-4)
                        z_list.append(z)
            
            z = z + 1

        elif z > 18 and z < 21:
            for y in range(4):
                x_range = int(4 - 2*np.absolute(y-1.5))
                x_step = 1.5 - np.absolute(y-1.5)
                for x in range(x_range):
                    if x == 0 or x == (x_range-1):
                        x_list.append(x-x_step)
                        y_list.append(y-1.5)
                        z_list.append(z)
                    elif y == 0 or y == 3:
                        x_list.append(x-x_step)
                        y_list.append(y-1.5)
                        z_list.append(z)
            
            z = z + 1

        elif z == 21:
            for y in range(4):
                x_range = int(4 - 2*np.absolute(y-1.5))
                x_step = 1.5 - np.absolute(y-1.5)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-1.5)
                    z_list.append(z)
            
            z = z + 1

        elif z > 21 and z < 26:
            x_list.append(0)
            y_list.append(0)
            z_list.append(z)

            z = z + 1

        elif z == 26:
            for y in range(9):
                x_list.append(0)
                y_list.append(y)
                z_list.append(z)

            z = z + 1

        elif z > 26:
            break



    #graph(x_list,y_list)
    #graph(y_list,z_list)
    #graph(x_list,z_list)
    #graph3D(x_list,y_list,z_list)


    model = np.zeros([len(x_list),6])
    input_filename = "solid_angle_cherry_poly.txt"

    thick = 0.2

    a = input("Whisky in Bottle? y/n: ")
    if a == "y":
        whisky = 1
    else:
        whisky = 0

    for i in range(len(x_list)):
        model[i,0] = x_list[i]
        model[i,1] = y_list[i]
        model[i,2] = z_list[i]
        z_val = model[i,1]*10 - min(y_list)*10 + 20
        r_val = np.sqrt((model[i,0]*10)**2 + (model[i,2]*10)**2)
        if y_list[i] < 0:
            model[i,4] = thick
            if whisky > 0:
                model[i,5] = ((np.sqrt((r_val)**2 + z_val**2))-25)/10
            else:
                model[i,5] = 0
        elif y_list[i] == 0:
            model[i,4] = thick
        model[i,3] = read2(r_val,z_val,input_filename)
        
    #print(model)

    eff_sum = 0
    output_list = []
    att_whisky = 1
    att_w = []

    for m in range(22):
        att_whisky = float(input("Attenuation coefficient of Whisky: "))
        att_w.append(att_whisky)


    for k in range(22):
        att_coeff = float(input("Attenuation coefficient of Bottle: "))

        for j in range(len(x_list)):
            att = np.exp(att_coeff*model[j,4])*np.exp(att_w[k]*model[j,5])
            eff = model[j,3]/att
            eff_sum = eff_sum + eff

        output_list.append(len(x_list)/eff_sum)
        eff_sum = 0

    print(" ")
    print("Total Geometric and Attenuation Efficiency:")

    for l in range(len(output_list)):
        print(str(output_list[l]))



def glass_whisky():

    x_list = []
    y_list = []
    z_list = []

    z = 0

    while True:

        if z <= 10:
            for y in range(6):
                x_range = int(10 - 2*np.absolute(y-2.5))
                x_step = 4.5 - np.absolute(y-2.5)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-2.5)
                    z_list.append(z)
            
            z = z + 1

        elif z > 10 and z <= 19:
            for y in range(6):
                x_range = int(9 - 2*np.absolute(y-2.5))
                x_step = 4 - np.absolute(y-2.5)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-2.5)
                    z_list.append(z)
        
            z = z + 1

        elif z > 19 and z <= 20:
            for y in range(3):
                x_range = int(3 - 2*np.absolute(y-1))
                x_step = 1 - np.absolute(y-1)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-1)
                    z_list.append(z)
            
            z = z + 1

        elif z > 20:
            break



    #graph(x_list,y_list)
    #graph(y_list,z_list)
    #graph(x_list,z_list)
    #graph3D(x_list,y_list,z_list)


    model = np.zeros([len(x_list),6])
    input_filename = "solid_angle_whisky_glass.txt"

    #output_file = open(input_filename,"w+")
    #output_file.write("r, z, data" + "\n")

    thick = 0.5
    
    for i in range(len(x_list)):
        model[i,0] = x_list[i]
        model[i,1] = y_list[i]
        model[i,2] = z_list[i]
        z_val = model[i,1]*10 - min(y_list)*10 + 20
        r_val = np.sqrt((model[i,0]*10)**2 + (model[i,2]*10)**2)
        model[i,4] = thick
        model[i,5] = ((np.sqrt(r_val**2 + z_val**2))-25)/10
        model[i,3] = read2(r_val,z_val,input_filename)
        #r_val = r_val/40
        #r_val = float(int(r_val*10))/10
        #if r_val == 6.3 or r_val == 6.4:
        #    r_val = 6.5
        #z_val = z_val/40
        #z_val = float(int(z_val*10))/10
        #model[i,3] = 0.43
        #output_file.write(str(r_val) + " " + str(z_val) + " " + "\n")


    #output_file.close()
    #print(model)

    eff_sum = 0
    output_list = []
    att_whisky = 1
    att_w = []

    for m in range(22):
        att_whisky = float(input("Attenuation coefficient of Whisky: "))
        att_w.append(att_whisky)


    for k in range(22):
        att_coeff = float(input("Attenuation coefficient of Bottle: "))

        for j in range(len(x_list)):
            att = np.exp(att_coeff*model[j,4])*np.exp(att_w[k]*model[j,5])
            eff = model[j,3]/att
            eff_sum = eff_sum + eff

        output_list.append(len(x_list)/eff_sum)
        eff_sum = 0

    print(" ")
    print("Total Geometric and Attenuation Efficiency:")

    for l in range(len(output_list)):
        print(str(output_list[l]))



def polyethylene_whisky():

    x_list = []
    y_list = []
    z_list = []

    z = 0

    while True:

        if z <= 17:
            for y in range(8):
                x_range = int(8 - 2*np.absolute(y-3.5))
                x_step = 3.5 - np.absolute(y-3.5)
                for x in range(x_range):
                    x_list.append(x-x_step)
                    y_list.append(y-3.5)
                    z_list.append(z)
            
            z = z + 1

        elif z > 17:
            break


    #graph(x_list,y_list)
    #graph(y_list,z_list)
    #graph(x_list,z_list)
    #graph3D(x_list,y_list,z_list)


    model = np.zeros([len(x_list),6])
    input_filename = "solid_angle_whisky_polyethylene.txt"

    #output_file = open(input_filename,"w+")
    #output_file.write("r, z, data" + "\n")

    thick = 0.2
    
    for i in range(len(x_list)):
        model[i,0] = x_list[i]
        model[i,1] = y_list[i]
        model[i,2] = z_list[i]
        z_val = model[i,1]*10 - min(y_list)*10 + 20
        r_val = np.sqrt((model[i,0]*10)**2 + (model[i,2]*10)**2)
        model[i,4] = thick
        model[i,5] = ((np.sqrt(r_val**2 + z_val**2))-25)/10
        model[i,3] = read2(r_val,z_val,input_filename)
        #r_val = r_val/40
        #r_val = float(int(r_val*10))/10
        #if r_val == 6.3 or r_val == 6.4:
        #    r_val = 6.5
        #z_val = z_val/40
        #z_val = float(int(z_val*10))/10
        #model[i,3] = 0.43
        #output_file.write(str(r_val) + " " + str(z_val) + " " + "\n")


    #output_file.close()
    #print(model)

    eff_sum = 0
    output_list = []
    att_whisky = 1
    att_w = []

    for m in range(22):
        att_whisky = float(input("Attenuation coefficient of Whisky: "))
        att_w.append(att_whisky)


    for k in range(22):
        att_coeff = float(input("Attenuation coefficient of Bottle: "))

        for j in range(len(x_list)):
            att = np.exp(att_coeff*model[j,4])*np.exp(att_w[k]*model[j,5])
            eff = model[j,3]/att
            eff_sum = eff_sum + eff

        output_list.append(len(x_list)/eff_sum)
        eff_sum = 0

    print(" ")
    print("Total Geometric and Attenuation Efficiency:")

    for l in range(len(output_list)):
        print(str(output_list[l]))



def read2(r,z,input_filename):

    input_file = open(input_filename,"r")

    r = r/40
    r = float(int(r*10))/10
    if r == 6.3 or r == 6.4:
        r = 6.5
    z = z/40
    z = float(int(z*10))/10

    length = (57/25.4)/((55.7/2)/25.4)
    length = float(int(length*10))/10

    i = 0

    for line in input_file.readlines():

        items = line.split()

        if i > 0:
            if r <= 1.0:
                if r == float(items[0]) and z == float(items[1]):
                    data = items[2]
                    data = decode(data)
            else:
                if r == float(items[0]) and z == float(items[1]):
                    data1 = items[2]
                    data2 = items[3]
                    data3 = items[4]
                    data1 = decode(data1)
                    data2 = decode(data2)
                    data3 = decode(data3)
                    data = data3 - data2 + data1

        i = i + 1

    input_file.close()

    data = data/3.47326

    return data



def decode(data2):

    a = str(data2)
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
    data2 = float(value)

    return data2



def main():

    print("Glass Bottle?: gb")
    print("Polyethylene Bottle?: pb")
    print("Whisky in Glass Bottle?: gw")
    print("Whisky in Polyethylene Bottle?: pw")
    data = input("What is being calculated?: ")
    print(" ")

    if data == "gb":
        glass_bottle()
    elif data == "pb":
        polyethylene_bottle()
    elif data == "gw":
        glass_whisky()
    elif data == "pw":
        polyethylene_whisky()
    else:
        print("Oops. Try Again.")
    

main()