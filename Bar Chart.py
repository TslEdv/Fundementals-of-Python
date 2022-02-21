import matplotlib.pyplot as plt
people = ["Adam", "Eve", "Paul", "Rassel", "Kate", "Peter"]
ages = [45, 25, 67, 70, 21, 34]
amountofppl = range(len(people))
plt.bar(amountofppl, ages)
plt.xticks(amountofppl, people)
plt.ylabel("Ages")
plt.title("Names & Ages")
plt.show()
