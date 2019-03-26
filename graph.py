import matplotlib.pyplot as plt
import numpy as np

def Linegraph():
    plt.plot([1,2,3,4,9,7,1])
    plt.show()

def Bargraph():
    x = range(4)
    y = ([100,20,50,150])
    plt.bar(x,y)
    plt.show()

def Piechart():
    label = ("Citizens State","For Thailand","New Anad")
    vel = (10,70,20)
    plt.pie(vel,labels=label)
    plt.show()

def Mixedgraph_Y2():
    labels = np.array(["A","B","C","D"])
    x = np.arange(labels.size)
    y1 = np.random.normal(800,90,labels.size)
    fig, axl = plt.subplots()
    axl.bar(x,y1)
    axl.set_ylabel("ton")
    axl.tick_params("y",color="green")


    axl.set_xticks(x)
    axl.set_xticklabels(labels)
    axl.legend()
    axl.set_title("grech")

    ax2 = axl.twinx()
    y2 = np.random.normal(800,90,labels.size)
    ax2.plot(x, y2, marker="o" , color="green")
    ax2.tick_params("y",color="green")
    ax2.set_ylabel("profile",color="green" ,fontsize=18)
    ax2.set_ylim(ymin=0)

    plt.show()










print("MANU")
print("1. Linegraph")
print("2. Bargraph")
print("3. Piechart")
print("4. Mixedgraph")

n = int(input("Manu : "))
if n == 1:
    print(Linegraph())
elif n == 2:
    print(Bargraph())
elif n == 3:
    print(Piechart())
else:
    print(Mixedgraph_Y2())





