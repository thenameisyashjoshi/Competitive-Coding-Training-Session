# mylist  = ["prashant","Ashish","Komal","Anshka","Ashish",77,"Sandip",60.52,"prashant"]
# print(mylist)
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2])

# mylist.append("john")
# mylist.append("moon")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("Sandip")
# print(mylist)

# newlist = mylist.copy()
# print(mylist)
# print(newlist)

# mylist = [["prashant","jha"] , ["85.56"] , [440022 , "yyy"]]
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["prashant","jha"]
# print(list1*2)

# list2 = [50,25.50]
# print(list1+list2)

# list3 = [50,25.50,"prashant"]
# del list3[2]
# print(list3)
# del list3
# print(list3) #it will gave error because list 3 is deleted 

# list4 = [50,25.50,"prashant"]
# list4.clear()
# print(list4)

# name = "prashant"
# print(name)
# myname = list(name) #typecasting
# print(myname)

# mylist = [9,5,4,3,7,8]
# mylist.sort()
# print(mylist) 
"""default sorthing order for number is acending order
default sorting order for string is alphabetical order 
we should know that list should contain homogenious data otherwise we will get type error
python2 first short number then string follow"""

# math = 50
# phy = 50
# print(id(math)) #return the address of variable
# print(id(phy))

# mylist = [44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist)) #this concept is Alising

"""there are 2 types of special operator membership and """
#membership operator = in , not in
# name = "prashant"
# print("Z" in name)
# print("Z" not in name)

# for i in range(6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(5,0,-1):
#     print(i)


# for i in range(1,11):
    # print(i*2 ,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10,"\t",i*11,"\t",i*12,"\t",i*13,"\t",i*14,"\t",i*15,"\t",i*16,"\t",i*17,"\t",i*18,"\t",i*19,"\t",i*20)

# no = int(input("Enter any Number: "))
# if no>0:
#     print("positive")
# elif no<0:
#     print("negative")
# elif n==0:
#     print("zero")

# day = str(input("Enter Day: "))
# if day == "Saturday" or "saturday" or "Sunday" or "sunday":
#     print("Off Day")
# else:
#     print("Working Day")

# Marks1 = int(input("Enter Marks: "))
# Marks2 = int(input("Enter Marks: "))
# Marks3 = int(input("Enter Marks: "))

# total = Marks1+Marks2+Marks3
# percentage = (total/300)*100

# print(percentage)

# if percentage >= 60:
#     print("He/she is Eligible")
# else:
#     print("not Eligible")

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))
e = int(input("Enter Fifth Number: "))

if a>b and a>c and a>d and a>e:
    print("First Number is Maximum")
elif b>a and b>c and b>d and b>e:
    print("Second Number is Maximum")
elif c>b and c>a and c>d and c>e:
    print("Third Number is Maximum")
elif d>b and d>a and d>c and d>e:
    print("Fourth Number is Maximum")
else:
    print("Fifth Number is Maximum")