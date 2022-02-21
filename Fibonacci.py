number= int(input("Enter the number: "))
fibo = 1
print(0)
previous = fibo
print(fibo)
while(fibo<=number):
        print(fibo)
        oldfibo = fibo
        fibo = fibo + previous
        previous = oldfibo