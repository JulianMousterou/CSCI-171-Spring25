
numlist = [] 
abslist=[]


print("Add a number to the list to find abs value and closest num to 0, press 0 to end loop.")

numhold=int(input())

while numhold!=0:
    
    numlist.append(numhold)
    numhold = int(input())
    
    if numhold==0: 
        break


for num in numlist:

   abslist.append(abs(num))
   closest_number=min(abslist)

   print("\nList of absolute values:\n",abslist,"\nThe closest number is:\n",closest_number) 
    
