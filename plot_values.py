import random
import matplotlib.pyplot as plt

num = random.randrange(900,1001)
tempo = [0]
array = []
for y in range(0,num):
    array.insert(y,random.randrange(0,256))
    tempo.insert(y,tempo[y-1]+1)
tempo.pop()
print(tempo)
print(array)
plt.plot(tempo,array)
plt.show()
