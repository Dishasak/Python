first_name = input("enter the first_name")
last_name = input("enter the second name")

revfname = first_name[::-1]
revlname = last_name[:: -1]

print(revlname," ",revfname)