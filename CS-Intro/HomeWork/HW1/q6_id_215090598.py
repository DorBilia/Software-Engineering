pulse = int(input("enter your pulse while resting: "))
weeks = int(input("how many weeks have your already trained? "))
if 1 <= weeks <= 2 or pulse > 70:
    print("you should run 3 km")
elif pulse <= 70 and 3 <= weeks <= 4:
    print("you should run 5 km")
elif weeks >= 5:
    if 60 <= pulse <= 70:
        print("you should run 8 km")
    elif pulse < 60:
        print("you should run 10 km")
