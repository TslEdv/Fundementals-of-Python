list = []
for i in range (5):
    a = int(input("Enter number: "))
    list.append(a)
print("Ascending order: ", sorted(list))
print("Descending order: ", sorted(list, reverse=True))
        
    