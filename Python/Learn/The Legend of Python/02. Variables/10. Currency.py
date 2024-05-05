pesos = int(input('Enter amount in pesos:  '))
soles = int(input('Enter amount in soles:  '))
reais = int(input('Enter amount is reais:  '))

USD = (pesos * 0.058) +  (soles * 0.27) + (reais * 0.19)

print(USD)