import time

x = int(input("Enter the initial countdown time(in seconds): "))
while x >= 0:
    print(x, end="\r")
    x -= 1
    time.sleep(1)