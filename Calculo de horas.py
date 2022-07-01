Linha = input().split()
hi, mi, hf, mf = Linha

hi = int(Linha[0])
mi = int(Linha[1])
hf = int(Linha[2])
mf = int(Linha[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        mj = mf - mi
    if mi > mf:
        hj = h - 1
        mj = (60 - mi) + mf
    if mi == mf:
        mj = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        mj = mf - mi
    if mi > mf:
        hj = h - 1
        mj = (60 - mi) + mf
    if mi == mf:
        mj = 0
if hi == hf:
    if mi < mf:
        mj = mf - mi
        hj = 0
    if mi > mf:
        mj = (60 - mi) + mf
        hj   = 23
    if mi == mf:
        hj = 24
        mj = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hj, mj))