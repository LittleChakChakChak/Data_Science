import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

plt.style.use('seaborn-whitegrid') # стиль графиков

# --------------------------figur1-------------------------------------

fig = plt.subplots() # один график

# --------------------------figur2-------------------------------------

fig, axes = plt.subplots(2, 2) # 4 графика

# --------------------------figur3-------------------------------------

fig, ax = plt.subplots()

x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]

ax.plot(x, y)

# --------------------------figur4-------------------------------------

fig, ax = plt.subplots()

x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]
x_abs = [3, 2, 1, 0, 1, 2, 3]

ax.plot(x, y)
ax.plot(x, x_abs)

# --------------------------figur5-------------------------------------

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y)

ax.plot(x, np.sin(x), color=(1.0,0.2,0.3),linestyle='-')

ax.plot(x, x + 5, color='blue', linestyle='--')

ax.plot(x, x + 3, color='g',linestyle=':')

ax.plot(x, np.cos(x), color='0.75',linestyle='-.')

ax.plot(x, x, color='#FFDD44',linestyle='--')

# --------------------------figur6-------------------------------------

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y, color='red', linestyle='-', marker='o', label='y=x^2')

ax.plot(0.5 * x, y, color='green', linestyle='-', marker='*', label='y=0.5 * x^2')

ax.set_title('Заголовок нашего графика', fontsize=20)

ax.set_xlabel("Ось х")
ax.set_ylabel("Ось у")

ax.legend(loc='lower left')

# --------------------------figur7-------------------------------------

fig, ax = plt.subplots()

N = 50

x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

ax.scatter(x, y, s=area, c=colors, alpha=0.5, marker='*', cmap='viridis')

# --------------------------figur8-------------------------------------

fig = plt.figure(figsize=(10,6))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, s=area, c=colors, alpha=0.5, marker='*', cmap='viridis')

# --------------------------figur9-------------------------------------

fig, axes = plt.subplots(1, 2)

axes[0].bar([1,2,3],[3,4,5], color='red',  label='vertical bar', alpha=0.8)

axes[1].barh([0.5,1,2.5],[0,1,2])

axes[0].legend()

# --------------------------figur10-------------------------------------

fig, ax = plt.subplots()

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

ax.hist(x, 50, density=True, facecolor='g', alpha=0.75)

# --------------------------figur11-------------------------------------

user_1 = [10, 3, 15, 21, 17, 14]
user_2 = [5, 13, 10, 7, 9, 12]
data = [user_1, user_2]
fig = plt.figure(figsize=(8, 6))

ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(data)

plt.xticks([1, 2], ['user_1', 'user_2'])

# --------------------------figur12-------------------------------------

fig, ax = plt.subplots()

x = np.arange(0,100,1)
y = x * 2
ax.fill_between( x, y, color="skyblue", alpha=0.2)
ax.plot(x, y, color="Slateblue", alpha=0.6)

# --------------------------figur13-------------------------------------

fig, ax = plt.subplots(figsize=(8,8))

labels = 'Jan', 'Feb', 'March', 'April', 'May', 'June'
user_1 = [10, 3, 15, 21, 17, 14]

ax.pie(user_1, labels=labels, explode=(0.07, 0, 0, 0, 0, 0), autopct='%1.1f%%', startangle=130, shadow=True)

# --------------------------figur14-------------------------------------

plt.figure(figsize=(8,6))
ts = pd.Series(np.random.randn(100), index = pd.date_range(
                                '1/1/2020', periods = 100))

ts = ts.cumsum()


ts.plot()


plt.show()