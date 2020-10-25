import datetime

now = datetime.datetime.now()
#datetime.datetime.now()
# <module>, <class>, <classmethod> ()

#print some attributes
print(now.year, now.month, now.hour, now.minute, now.second)



now.hour = float(input("What hour is it? (0-23)"))

if now.hour <= 5:
    print("Its early go back to sleep")
elif now.hour <= 7:
    print("Wake up")
elif now.hour <= 9:
    print("go work")
elif now.hour <= 12:
    print("You should be working!")
elif now.hour <= 13:
        print("Take your lunch break!")
elif now.hour <= 17:
        print("Do you feel that afternoon lull?")
elif now.hour <= 19:
        print("Time to hit the gym…")
elif now.hour <= 21:
        print("Time to hit the gym…")
elif now.hour <= 23:
        print("Get that SLEEP. And rePEAT!")
else:
    print("You didn’t type an acceptable value! (0-23)")
