import matplotlib.pyplot as plt


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


print("MANU")
print("1. Linegraph")
print("2. Bargraph")
print("3. Piechart")

n = int(input("Manu : "))
if n == 1:
    print(Linegraph())
elif n == 2:
    print(Bargraph())
else:
    print(Piechart())






