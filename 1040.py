print ("Calculo de media")
n1 = float (input(print(" Qual o valor da sua primeira nota?")))
n2 = float (input(print("qual o valor da sua segunda nota?")))
n3 = float (input(print("qual o valor da sua terceira nota?")))
n4 = float (input(print("qual o valor da sua quarta nota?")))
media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print ("Sua media:", media)
if media >= 7:
    print ("Aprovado")
elif media <= 5:
    print("Aluno reprovado")
else:
    print ('Aluno em exame')
    ne = float (input(print("qual o valor da nota do seu exame final?")))
    mediaf = ne*media/2
    if mediaf >= 5:
     print ("aluno aprovado")
     print("media final igual: ", mediaf)
    else:
     print ("Aluno reprovado")
     print("media final igual: ", mediaf)
