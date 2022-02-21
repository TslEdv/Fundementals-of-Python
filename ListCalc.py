list=[]
print("Enter a negative number to stop")
while True:
    n = float(input("Enter Num: "))
    if n < 0:
        break
    else:
        list.append(n)
def average(list): 
    return sum(list) / len(list) 
print("The sum is ", sum(list))
print("The average is ", average(list))
print("The maximum is ", max(list))
print("The minimum is ", min(list))