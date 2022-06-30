from turtle import clear


print ("Calculo de media")
n1 = int (input(print(" Qual o valor da sua primeira nota?")))
n2 = int (input(print("qual o valor da sua segunda nota?")))
n3 = int (input(print("qual o valor da sua terceira nota?")))
n4 = int (input(print("qual o valor da sua quarta nota?")))
media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print ("Sua media:", media)
if media >= 7:
    print ("Aprovado")
elif media <= 5:
    print("Aluno reprovado")
else:
    print ('Aluno em exame')
