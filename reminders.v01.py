userTime = float(input("What hour is it? (0-23)"))

if userTime <= 5:
    print("Its early go back to sleep")
elif userTime <= 7:
    print("Wake up")
elif userTime <= 9:
    print("go work")
elif userTime <= 12:
    print("You should be working!")
elif userTime <= 13:
        print("Take your lunch break!")
elif userTime <= 17:
        print("Do you feel that afternoon lull?")
elif userTime <= 19:
        print("Time to hit the gym…")
elif userTime <= 21:
        print("Time to hit the gym…")
elif userTime <= 23:
        print("Get that SLEEP. And rePEAT!")
else:
    print("You didn’t type an acceptable value! (0-23)")
