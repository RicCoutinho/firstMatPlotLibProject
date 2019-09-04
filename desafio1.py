import matplotlib.pyplot as plt

qtd = int(input('Enter the population on earth: \n'))

plt.ylabel('Population in billions')
def_x = ['Before Thanos' , 'After Thanos']
def_y = [(qtd), (qtd / 2)]
plt.bar(def_x, def_y)
plt.title('Finger Snap')

plt.show()
