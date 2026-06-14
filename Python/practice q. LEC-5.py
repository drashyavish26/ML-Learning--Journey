#print the multiplication table of a number n. 
n = int(input("enter the number:"))
i =1
while i <= 10:
    print(n*i)
    i +=1

  #  search for a number x in this tuple using loop 
nums= (1,4,9,16,25,36,49,64,81,100)
x=36
i=0 #i=index
while i<len(nums):
    if(nums[i]==x):
        print("found at idx", i)
        break
        i+=1
    else:
        print('finding...')
        i +=1

i=1 
while i <= 10:
    if (i%2==0):
        i+=1
        continue
    print(i)
    i+=1

# print the multiplication of a number n
n= int(input("enter a number"))
for i in range (1,11):
    print(n*i)


#WAP to find the factorial of first n natural numbers (using while)
n=int(input("enter a number:"))
sum = 0
i =1
while i <=n:
    sum+=i
    i+=1

print("the total sum=", sum)


#WAP to 
