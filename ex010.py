real = float(input('Quanto dinheiro voçê tem na carteira? R$'))
dolar = real / 3.27
euro = real / 4.30
print('com R${:.2f} voçê pode comprar US${:.2f}'.format(real, dolar))
print('com R${:.2f} voçê pode comprar €{:.2f}'.format(real, euro))