resposta= 'S'
s=0
count=0
maior=menor=0
while resposta == 'S':
    n=int(input('Digite um número: '))
    resposta=str(input('Quer continuar digitando? [S/N]: ')).upper().strip()[0]
    s=s+n
    count+=1
    media=s/count
    if count==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        elif n<menor:
            menor=n
print('Você digitou {} números. A média entre os valores digitados é igual a {:.2f}.'.format(count, media))
print('O maior número digitado é {} e o menor {}.'.format(maior, menor))
