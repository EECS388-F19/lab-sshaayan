import random

print("Shaayan", end='\n')

rand1 = random.randint(1, 101)
print(rand1, end='\n')

rand2 = random.randint(1, 101)
print(rand2, end='\n')

output = "Sum = " + str(rand1 + rand2)
print(output, end='\n')

avg = "Average = " + str((rand1 + rand2) / 2)
print(avg, end='\n')
