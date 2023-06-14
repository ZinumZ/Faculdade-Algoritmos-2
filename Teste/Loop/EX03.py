#c) Faça um programa que imprime os primeiros 10 números da sequência de Fibonacci.

num1 = 0
num2 = 1

i = 0
print("Sequência de Fibonacci:")

for i in range(10):
    print(num1)
    proximo_num = num1 + num2
    num1 = num2
    num2 = proximo_num
    i = i + 1
