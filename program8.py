import math
x1 , y1 = map(int,input ("Enter first coordinate: ").split())
x2 , y2 = map(int,input ("Enter second coordinate: ").split())
distance = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print (f"The euclidean distance is: {round(distance,2)}")