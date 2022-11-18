import matplotlib.pyplot as plt

def graph_era(poplist,cyclelist):
    fig,ax = plt.subplots()
    ax.plot(cyclelist,poplist)
    plt.ylabel("Population")
    plt.xlabel("Life Cycles")
    plt.show()
