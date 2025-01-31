"""
Jeder neue Term in der Fibonacci-Reihe wird gebildet, indem die beiden vorherigen Zahlen addiert werden. 
Wenn man mit 1 und 2 beginnt, sind die ersten 10 Terme wie folgt:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Finden Sie die Summe aller geraden Terme der Fibonacci-Reihe, die jeweils 4 Millionen nicht überschreiten.

Notiz:
Fn = Fn-1 + Fn-2
F0 = 0 and F1 = 1. 

∑ F(n) -> Die Summe aller Fibonacci Integer
∀ F(n) ≤ 4.000.000 ->  Fibonacci Integer, die < or = 4 Millionen sind
F(n) ≡ 0 (mod 2) -> nbur gerade Fibonacci Integer werden entgegengenommen
= {result} -> Das berechnete Ergebnis wird eingesetzt

https://projekteuler.de/problems/2"""

maxRange = 4000000
def evenFibsum(limit):
    a, b = 1, 2  
    sumEven = 0 

    while a <= limit:
        if a % 2 == 0:  
            sumEven += a  
        a, b = b, a + b  
    return sumEven

result = evenFibsum(maxRange)
print(f"∑ F(n) für F(n) ≤ 4.000.000, wobei F(n) % 2 = 0 -> {result}")

