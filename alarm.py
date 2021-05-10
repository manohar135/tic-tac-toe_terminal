import time

massage = input("Enter the massage that u want to show: ")
give_time = input("Enter the time(HH-MM-SS) when u want to see this Massage: ")

while True:
    now = time.strftime("%H-%M-%S")
    print(now, end='\r')
    if now == give_time:
        break
    time.sleep(1)

print("Ure Massage is:")
print(massage)