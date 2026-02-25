import time

def traffic_light(red_time, yellow_time, green_time):
    while True:
        
        print("RED light ON - STOP 🚦")
        time.sleep(red_time)

        print("YELLOW light ON - READY TO MOVE ⚠️")
        time.sleep(yellow_time)

        
        print("GREEN light ON - YOU CAN GO ✅")
        time.sleep(green_time)


red = int(input("Enter time for RED light (seconds): "))
yellow = int(input("Enter time for YELLOW light (seconds): "))
green = int(input("Enter time for GREEN light (seconds): "))


traffic_light(red, yellow, green)
