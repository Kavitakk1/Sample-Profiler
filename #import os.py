import os 
print(os.getpid())
input("Enter to begin>")
import random
z = range(100)
while True:
    n = [random.randint(1,100) for _ in z]
    n.sort()
    print (n)
    

    