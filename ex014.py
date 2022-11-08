import time
temp = float(input('Informe a temperatura em °C:'))
novo = (temp * 1.8)+32
print('Carregando')
time.sleep(2)
print('A temperatura de {:.1f}°C corresponde a {:.1f}°f'.format(temp, novo))
