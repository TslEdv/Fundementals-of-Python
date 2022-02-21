import matplotlib.pyplot as plt

categories= 'Comedy', 'Action', 'Romance', 'Drama', 'SciFi'
ratings = [4, 5, 6, 1, 4]

fig1, ax1 = plt.subplots()
ax1.pie(ratings, labels=categories, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
