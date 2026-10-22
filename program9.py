a1 , a2 , a3 = map(int,input("Enter three angles: ").split())
if (a1>0 and a2>0 and a3>0):
    if(a1+a2+a3 == 180):
	    print("It can form a triangle")
    else :
	    print("It cannot form a triangle")
else :
	print("It cannot form a triangle")