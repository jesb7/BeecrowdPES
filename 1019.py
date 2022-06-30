print("CONVERSOR DE TEMPO")
tempo = int(input(print( "insira o tempo em segundo")))
# convertendo o tempo em horas
horas = tempo // 3600
tempo = tempo - horas * 3600
#convertendo o que sobrou em minutos
min = tempo // 60
tempo = tempo - min*60
# o que sobrou sao os segundos
seg = tempo
print('{}:{}:{}'.format(horas, min, seg))
