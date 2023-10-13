import time

my_time = int(input("Enter time in seconds: "))

for x in reversed(range(0 , my_time)):
 print(x+1)
 time.sleep(1)

print("0")
print("time is up !")