# Write your code here :-)
i=1
print("Even number")
while i<=100:
  if i%2==0:
    print(i)
  i=i+1
print("Odd number")
i=1
while i<=100:
  if i%2!=0:
    print(i)
  i+=1
num=1
print("Prime numbers")
while num<=100:
 count=0
 i=2
 while i<=num//2:
   if num%i==0:
     count+=1
     break
   i+=1
 if(count==0)and(num!=1):
     print(num)
 num+=1
