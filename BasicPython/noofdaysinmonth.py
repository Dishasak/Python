month = input("enter the month: ")

if month in ("Jan","Mar","May","Jul","Aug","Oct","Dec"):
    print("number of days is 31")

elif month in ("Apr","Jun","Sep","Nov"):
    print("number of days is 30")

elif month == "Feb":
    print("number of days is 28 or 29 ")
    


