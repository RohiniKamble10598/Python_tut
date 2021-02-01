m1 =int(input("Enter marks of sub_1\n "))
m2 =int(input("Enter marks of sub_2\n"))
m3 =int(input("Enter marks of sub_3\n "))

if(m1<33 or m2<33 or m3<33):
    print("You Are FAil due to percentage less than 33")

elif(m1+m2+m3)/3 < 40:
    print("you are fail due to percentage less than 40")

else:
    print("Congratulations! you are Passed")