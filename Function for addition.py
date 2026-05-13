print("Addition using functions")
n=int(input("Enter how many numbers to add: "))
def add(n):
    sum=0
    for i in range(n):
        num=int(input(f"Enter number {i+1}: "))
        sum+=num
    return sum
result=add(n)
print("The sum is: ",result)