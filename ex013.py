salario = float(input('Qual o salário do funcionario? R$'))
porcento = float(input('Qual a porcentagen:'))
novo = salario + (salario * porcento / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, porcento, novo))