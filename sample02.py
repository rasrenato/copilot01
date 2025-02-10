# crie um código python para calcular a média de 3 notas de um aluno
# e informar se ele foi aprovado ou reprovado.
# A média para aprovação é 7.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")  # se a média for menor que 7
