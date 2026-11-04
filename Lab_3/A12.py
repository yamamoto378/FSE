x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 >0 and y1 > 0) and (x2>0 and y2 >0):
   print("Yes,1")
elif (x1 < 0 and y1 > 0) and (x2 < 0 and y2 > 0):
   print("Yes,2")
elif (x1 < 0 and y1 <0) and (x2 < 0 and y2 <0):
   print("Yes,3")
elif (x1 >0 and y1<0) and (x2 >0 and y2<0):
   print("Yes,4")
else:
   print("No")