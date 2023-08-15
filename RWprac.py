guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
#with open("test.txt","a") as file:
 #   for i in guests:
  #   file.write(i)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("test.txt","r") as file:
 for g in guests:
    checked_in.append(g.strip())   #transfers all the elements in the list
    print(checked_in)
 for guests in guests_to_check:
     if guests in checked_in:
         print("{} has checked in".format(guests))
     else:
         print("{} has not checked in".format(guests))



