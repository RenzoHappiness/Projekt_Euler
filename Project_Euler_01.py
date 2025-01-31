"""
Wenn wir alle natürlichen Zahlen unter 10 auflisten, die ein Vielfaches von 3 oder 5 sind, so erhalten wir 3, 5, 6 und 9. 
Die Summe dieser Vielfachen ist 23.

Finden Sie die Summe aller Vielfachen von 3 oder 5 unter 1000.
https://projecteuler.net/problem=1"""


sum = 0
vielfache = []
maxRange = 10

for i in range(maxRange):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        vielfache.append(i)
print(f'Die Vielfache von 3&5 unter {maxRange} sind: {vielfache}')
print(f'die Summe aller dieser gefundenen Vielfachen ist {sum}')