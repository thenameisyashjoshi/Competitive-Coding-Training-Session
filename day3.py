 #write a program to accept three paper marks and check maximum marks using nested if else

# marks1 = int(input("Enter marks1: "))
# marks2 = int(input("Enter marks2: "))
# marks3 = int(input("Enter marks3: "))

# if marks1 > marks2:
#     if marks1 > marks3:
#         print("Marks1 is the highest")
#     else:
#         print("Marks3 is the highest")
# else:
#     if marks2 > marks3:
#         print("Marks2 is the highest")
#     else:
#         print("Marks3 is the highest")


 #write a program to accept three paper marks and check Minimum marks using nested if else

# marks1 = int(input("Enter marks1: "))
# marks2 = int(input("Enter marks2: "))
# marks3 = int(input("Enter marks3: "))

# if marks1 < marks2:
#     if marks1 < marks3:
#         print("Marks1 is the Lowest")
#     else:
#         print("Marks3 is the lowest")
# else:
#     if marks2 < marks3:
#         print("Marks2 is the lowest")
#     else:
#         print("Marks3 is the lowest")


 #write a program to accepet percentage and 1) if per>90:A 2)if per>80:b 3)if per>70:c 4)else fail

# per = float(input("Enter percentage: "))

# if per > 90:
#     print("Grade: a")
# elif per > 80:
#     print("Grade: b")
# elif per > 70:
#     print("Grade: c")
# else:
#     print("Fail")



# mydict = {
#     "name":"prashant",
#     "Profession":"Developer",
#     "EmpID":1001
# }
# print(mydict)
# print(type(mydict))



# mydict={
#     101:"Prashant",
#     102:"Anish",
#     "103":"Mohini",
#     101:"Ashish",
#     104:"Ashish"
# }
# mydict.pop(101)
# print(mydict)


# name="Prashan jha"
# print(name[0])
# print(name[-1])
# print(name[2])


# s="Help4code is a best platform for practicing programming"
# print(s.find("Help4code"))
# print(s.find("python"))

# name="yashjoshi"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[1:5])
# print(name[:5])
# print(name[1:])
# print(name[1:8:2])
# print(name[::-1])

# s="this is such a boring day"
# print(s.find("boring"))
# print(s.find("day"))
# print(s.find("good"))
# s="yash","joshi","string"
# m='|'.join(s)
# print(m)

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())

# print('sunject marks:')
# phy=56
# maths=44
# chem=56
# print("physics={} maths={} chemistry={}".format(phy,maths,chem))
# print("physics={0} maths={1} chemistry={2}".format(phy,maths,chem))
# print("physics={x} maths={y} chemistry={z}".format(phy,maths,chem))
# total=phy+maths+chem
# print(total)

# a=50
# b=90
# c=57
# d=34
# print((a+b)*c/d)
# print((a-b)*(c/d))

name="Yash"
data=['a','e','i','o','u']
vowels=0
con=0
for i in name:
    if i in data:
        vowels+=1
    else:
        con +=1

