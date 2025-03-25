import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
beta=0.3
gamma=0.05
time=100

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Initial")
plt.show()

for i in range(1,time+1):
    new_population = np.copy(population)
    infect=np.where(population==1)
    for j in range(len(infect[0])):
        x,y=infect[0][j],infect[1][j]
        for x_change in range(-1,2):
            for y_change in range(-1,2):
                x_side,y_side=x+x_change,y+y_change
                if 0<=x_side<100 and 0<=y_side<100 and population[x_side,y_side]==0:
                    new_population[x_side,y_side]=np.random.choice(range(0,2),1,p=[1-beta,beta])
        new_recover=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
        new_population[x,y]=new_recover
    population=new_population
    if i in [10,50,100]:
        plt.imshow(population,cmap="viridis",interpolation="nearest")
        plt.title(f"day {i}")
        plt.show()