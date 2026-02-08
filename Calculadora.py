num1= float(input("Digite seu primeiro número: "))

num2 = float(input("Digite seu segundo número: "))

print("Escolha sua opção: 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão")
opcao = int(input("Digite sua opcão: "))



if opcao == 1:
  print(num1 + num2)
elif opcao == 2:
  print(num1 + num2)
elif opcao == 3:
  print(num1 * num2)
elif opcao == 4 and num2 != 0:
  print(num1/num2)
elif opcao == 4 and num2 == 0:
  print("Erro. Não dá pra dividir por zero")
else:
  print(f"{opcao} não é válido")


