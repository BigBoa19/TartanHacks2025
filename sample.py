import random as rand
results = []
med = 60
temp = 30
while temp <= 90:
    price = abs(temp-med+ rand.random()*5)
    results.append(price)
    temp += 0.05
print(results)