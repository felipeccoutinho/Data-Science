
#acertou 13 numeros, 20,00
#acertou 12 numeros, 8,00
#acertou 11 numeros, 4,00

#Quantidade de números	Valor em R$
#15 números	2,00
#16 números	32,00
#17 números	272,00
#18 números	1.632,00

'''Caixa realizou nesta quinta-feira (7/7/2017) o concurso da Lotofácil da Independência.
As 15 dezenas sorteadas foram: 02-03-04-05-06-09-12-16-17-18-20-21-22-24-25.
Houve 15 apostas ganhadoras, e cada uma levou R$ 5.905.591.

Dos 15 ganhadores, 8 são de São Paulo, 3 da Bahia, 1 do Espírito Santo,
1 do Piauí, 1 do Rio de Janeiro e 1 do Distrito Federal.

Outras 3.369 pessoas acertaram 14 números. Cada uma levou R$ 2.165,59.

=================================================================================
Dez apostas acertaram os 15 números do concurso 1.408 da Lotofácil da Independência,7/7/2016
cujo sorteio foi realizado na noite desta terça-feira (6) no Terminal Rodoviário do Tietê,
em São Paulo (SP), e ganharam R$ 8.227.506,94 cada uma. 14 - 1600

Veja os números sorteados: 01 - 03 - 05 - 08 - 10 - 11 - 12 - 13 - 14 - 19 - 21 - 22 - 23 - 24 - 25.

Nove cidades de cinco estados tiveram apostas que vão levar o prêmio máximo: Astolfo Dutra (MG),
Campo Grande (MS), Palmeira do Índios (AL), Piracicaba (SP), Ponta Grossa (PR), Ponte Nova (MG),
São José dos Pinhais (PR), São Paulo (duas apostas) e Várzea Paulista (SP).
'''

#valor do jogo 2.00   total do bolao 40.00o
# os jogos de 21 a 23 sao bolao


print('==================LOTOFACIL======================')
print('GANHE ACERTANDO 11,12,13,14 e 15 NUMEROS')
n1=int(input('Digite o primeiro numero do sorteio '))
n2=int(input('Digite o segundo numero do sorteio '))
n3=int(input('Digite o terceiro numero do sorteio '))
n4=int(input('Digite o quarto numero do sorteio '))
n5=int(input('Digite o quinto numero do sorteio '))
n6=int(input('Digite o sexto numero do sorteio '))
n7=int(input('Digite o setimo numero do sorteio '))
n8=int(input('Digite o oitavo numero do sorteio '))
n9=int(input('Digite o nono numero do sorteio '))
n10=int(input('Digite o decimo numero do sorteio '))
n11=int(input('Digite o decimo primeiro numero do sorteio '))
n12=int(input('Digite o decimo segundo numero do sorteio '))
n13=int(input('Digite o decimo terceiro numero do sorteio '))
n14=int(input('Digite o decimo quarto numero do sorteio '))
n15=int(input('Digite o decimo quinto numero do sorteio '))
print(""
      "")
print("=================VALORES POR FAIXA DE ACERTO=====================")
print(""
      "")

resultado=set([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15])

acertou11=float(input('Digite o valor para quem acertou 11 numeros R$  '))
acertou12=float(input('Digite o valor para quem acertou 12 numeros R$  '))
acertou13=float(input('Digite o valor para quem acertou 13 numeros R$  '))
acertou14=float(input('Digite o valor para quem acertou 14 numeros R$  '))
acertou15=float(input('Digite o valor para quem acertou 15 numeros R$  '))
print(""
      "")
print("=========================RESULTADO===============================")
print(""
      "")

#meu bolão

jogo1=set([1,2,3,5,7,9,10,11,12,14,15,17,18,19,21])
jogo2=set([1,2,3,5,8,9,10,13,16,17,18,22,23,24,25])
jogo3=set([1,2,4,5,7,9,10,11,13,14,15,18,20,22,25])
jogo4=set([1,2,5,6,7,8,11,12,14,15,19,21,23,24,25])
jogo5=set([1,3,6,7,9,10,11,13,15,16,18,20,22,23,24])
jogo6=set([1,3,4,5,6,11,12,13,15,17,19,20,22,24,25])
jogo7=set([1,3,5,7,8,10,11,14,15,17,19,20,21,22,23])
jogo8=set([1,4,6,7,8,12,13,15,17,18,19,22,23,24,25])
jogo9=set([1,5,7,8,9,10,11,14,15,18,20,21,23,24,25])
jogo10=set([2,3,4,5,7,10,11,13,16,17,18,20,21,22,24])
jogo11=set([2,3,5,6,8,9,12,13,15,16,18,20,21,22,25])
jogo12=set([2,3,6,7,9,10,13,14,15,17,18,22,23,24,25])
jogo13=set([2,4,5,6,9,10,11,12,14,16,19,20,21,22,25])
jogo14=set([2,4,6,7,8,10,11,13,14,16,17,19,20,23,24])
jogo15=set([2,5,8,9,10,12,13,15,16,17,18,21,22,24,25])
jogo16=set([2,5,6,7,8,11,13,15,16,17,20,21,23,24,25])
jogo17=set([2,6,7,9,11,12,14,15,16,18,19,20,22,23,25])
jogo18=set([3,4,7,9,10,11,12,14,16,17,19,20,22,23,24])
jogo19=set([4,5,6,9,10,12,13,15,16,18,20,21,22,23,24])
jogo20=set([5,6,8,9,11,12,14,15,17,18,19,22,23,24,25])

#bolão1painho
jogo21=set([1,2,3,5,7,10,11,13,14,16,19,20,23,24,25])
jogo22=set([1,2,3,4,8,11,13,15,16,19,20,21,23,24,25])
jogo23=set([1,2,3,6,7,10,11,16,17,18,20,22,23,24,25])
jogo24=set([2,4,5,6,7,8,10,13,14,16,17,18,19,23,24])
jogo25=set([2,3,6,9,10,11,12,15,16,18,19,20,23,24,25])
jogo26=set([2,5,6,7,8,10,12,13,17,18,19,20,21,23,24])
jogo27=set([3,4,5,9,11,12,15,18,19,20,21,22,23,24,25])
jogo28=set([3,6,7,9,10,12,13,14,17,18,19,20,22,24,25])
jogo29=set([3,5,6,9,12,13,14,15,16,17,19,21,22,23,24])



jogo30=set([1,2,5,6,7,8,11,12,14,15,19,21,23,24,25])
jogo31=set([1,3,6,7,9,10,11,13,15,16,18,20,22,23,24])
jogo32=set([1,3,4,5,6,11,12,13,15,17,19,20,22,24,25])
jogo33=set([1,3,5,7,8,10,11,14,15,17,19,20,21,22,23])
jogo34=set([1,4,6,7,8,12,13,15,17,18,19,22,23,24,25])
jogo35=set([1,5,7,8,9,10,11,14,15,18,20,21,23,24,25])
jogo36=set([2,3,4,5,7,10,11,13,16,17,18,20,21,22,24])
jogo37=set([2,3,5,6,8,9,12,13,15,16,18,20,21,22,25])
jogo38=set([2,3,6,7,9,10,13,14,15,17,18,22,23,24,25])
jogo39=set([2,4,5,6,9,10,11,12,14,16,19,20,21,22,25])
jogo40=set([2,4,6,7,8,10,11,13,14,16,17,19,20,23,24])
jogo41=set([2,5,8,9,10,12,13,15,16,17,18,21,22,24,25])
jogo42=set([2,5,6,7,8,11,13,15,16,17,20,21,23,24,25])
jogo43=set([2,6,7,9,11,12,14,15,16,18,19,20,22,23,25])
jogo44=set([3,4,7,9,10,11,12,14,16,17,19,20,22,23,24])
jogo45=set([4,5,6,9,10,12,13,15,16,18,20,21,22,23,24])
jogo46=set([5,6,8,9,11,12,14,15,17,18,19,22,23,24,25])

if resultado==jogo1:
    print('O jogo 01 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo1))==14:
    print('O jogo 01 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo1))==13:
    print('O jogo 01 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo1))==12:
    print('O jogo 01 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo1))==11:
    print('O jogo 01 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 01 nao ganhou nada')

if resultado==jogo2:
    print('O jogo 02 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ ')
elif len(resultado.intersection(jogo2))==14:
    print('O jogo 02 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo2))==13:
    print('O jogo 02 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo2))==12:
    print('O jogo 02 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo2))==11:
    print('O jogo 02 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 02 nao ganhou nada')

if resultado == jogo3:
    print('O jogo 03 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo3))==14:
    print('O jogo 03 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo3))==13:
    print('O jogo 03 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo3))==12:
    print('O jogo 03 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo3))==11:
    print('O jogo 03 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 03 nao ganhou nada')

if resultado == jogo4:
    print('O jogo 04 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo4))==14:
    print('O jogo 04 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo4))==13:
    print('O jogo 04 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo4))==12:
    print('O jogo 04 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo4))==11:
    print('O jogo 04 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 04 nao ganhou nada')

if resultado == jogo5:
    print('O jogo 05 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo5))==14:
    print('O jogo 05 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo5))==13:
    print('O jogo 05 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo5))==12:
    print('O jogo 05 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo5))==11:
    print('O jogo 05 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 05 nao ganhou nada')

if resultado == jogo6:
    print('O jogo 06 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo6))==14:
    print('O jogo 06 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo6))==13:
    print('O jogo 06 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo6))==12:
    print('O jogo 06 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo6))==11:
    print('O jogo 06 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 06 nao ganhou nada')

if resultado == jogo7:
    print('O jogo 07 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo7))==14:
    print('O jogo 07 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo7))==13:
    print('O jogo 07 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo7))==12:
    print('O jogo 07 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo7))==11:
    print('O jogo 07 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 07 nao ganhou nada')

if resultado == jogo8:
    print('O jogo 08 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo8))==14:
    print('O jogo 08 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo8))==13:
    print('O jogo 08 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo8))==12:
    print('O jogo 08 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo8))==11:
    print('O jogo 08 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 08 nao ganhou nada')


if resultado == jogo9:
    print('O jogo 09 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo9))==14:
    print('O jogo 09 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo9))==13:
    print('O jogo 09 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo9))==12:
    print('O jogo 09 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo9))==11:
    print('O jogo 09 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 09 nao ganhou nada')


if resultado == jogo10:
    print('O jogo 10 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo10))==14:
    print('O jogo 10 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo10))==13:
    print('O jogo 10 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo10))==12:
    print('O jogo 10 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo10))==11:
    print('O jogo 10 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 10 nao ganhou nada')



if resultado == jogo11:
    print('O jogo 11 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo11))==14:
    print('O jogo 11 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo11))==13:
    print('O jogo 11 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo11))==12:
    print('O jogo 11 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo11))==11:
    print('O jogo 11 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 11 nao ganhou nada')

if resultado == jogo12:
    print('O jogo 12 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo12))==14:
    print('O jogo 12 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo12))==13:
    print('O jogo 12 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo12))==12:
    print('O jogo 12 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo12))==11:
    print('O jogo 12 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 12 nao ganhou nada')

if resultado == jogo13:
    print('O jogo 13 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo13))==14:
    print('O jogo 13 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo13))==13:
    print('O jogo 13 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo13))==12:
    print('O jogo 13 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo13))==11:
    print('O jogo 13 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 13 nao ganhou nada')

if resultado == jogo14:
    print('O jogo 14 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo14))==14:
    print('O jogo 14 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo14))==13:
    print('O jogo 14 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo14))==12:
    print('O jogo 14 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo14))==11:
    print('O jogo 14 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 14 nao ganhou nada')

if resultado == jogo15:
    print('O jogo 15 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo15))==14:
    print('O jogo 15 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo15))==13:
    print('O jogo 15 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo15))==12:
    print('O jogo 15 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo15))==11:
    print('O jogo 15 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 15 nao ganhou nada')

if resultado == jogo16:
    print('O jogo 16 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo16))==14:
    print('O jogo 16 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo16))==13:
    print('O jogo 16 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo16))==12:
    print('O jogo 16 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo16))==11:
    print('O jogo 16 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 16 nao ganhou nada')

if resultado == jogo17:
    print('O jogo 17 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo17))==14:
    print('O jogo 17 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo17))==13:
    print('O jogo 17 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo17))==12:
    print('O jogo 17 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo17))==11:
    print('O jogo 17 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 17 nao ganhou nada')

if resultado == jogo18:
    print('O jogo 18 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo18))==14:
    print('O jogo 18 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo18))==13:
    print('O jogo 18 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo18))==12:
    print('O jogo 18 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo18))==11:
    print('O jogo 18 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 18 nao ganhou nada')


if resultado == jogo19:
    print('O jogo 19 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo19))==14:
    print('O jogo 19 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo19))==13:
    print('O jogo 19 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo19))==12:
    print('O jogo 19 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo19))==11:
    print('O jogo 19 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 19 nao ganhou nada')


if resultado == jogo20:
    print('O jogo 20 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo20))==14:
    print('O jogo 20 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo20))==13:
    print('O jogo 20 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo20))==12:
    print('O jogo 20 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo20))==11:
    print('O jogo 20 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 20 nao ganhou nada')

if resultado == jogo21:
    print('O jogo 21 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo21))==14:
    print('O jogo 21 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo21))==13:
    print('O jogo 21 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo21))==12:
    print('O jogo 21 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo21))==11:
    print('O jogo 21 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 21 nao ganhou nada')

if resultado == jogo22:
    print('O jogo 22 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo22)) == 14:
    print('O jogo 22 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo22)) == 13:
    print('O jogo 22 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo22)) == 12:
    print('O jogo 22 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo22)) == 11:
    print('O jogo 22 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 22 nao ganhou nada')

if resultado == jogo23:
    print('O jogo 23 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo23)) == 14:
    print('O jogo 23 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo23)) == 13:
    print('O jogo 23 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo23)) == 12:
    print('O jogo 23 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo23)) == 11:
    print('O jogo 23 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 23 nao ganhou nada')

if resultado == jogo24:
    print('O jogo 24 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo24)) == 14:
    print('O jogo 24 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo24)) == 13:
    print('O jogo 24 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo24)) == 12:
    print('O jogo 24 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo24)) == 11:
    print('O jogo 24 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 24 nao ganhou nada')

if resultado == jogo25:
    print('O jogo 25 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo25)) == 14:
    print('O jogo 25 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo25)) == 13:
    print('O jogo 25 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo25)) == 12:
    print('O jogo 25 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo25)) == 11:
    print('O jogo 25 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 25 nao ganhou nada')

if resultado == jogo26:
    print('O jogo 26 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo26)) == 14:
    print('O jogo 26 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo26)) == 13:
    print('O jogo 26 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo26)) == 12:
    print('O jogo 26 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo26)) == 11:
    print('O jogo 26 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 26 nao ganhou nada')


if resultado == jogo27:
    print('O jogo 27 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo27)) == 14:
    print('O jogo 27 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo27)) == 13:
    print('O jogo 27 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo27)) == 12:
    print('O jogo 27 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo27)) == 11:
    print('O jogo 27 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 27 nao ganhou nada')



if resultado == jogo28:
    print('O jogo 28 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo28)) == 14:
    print('O jogo 28 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo28)) == 13:
    print('O jogo 28 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo28)) == 12:
    print('O jogo 28 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo28)) == 11:
    print('O jogo 28 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 28 nao ganhou nada')


if resultado == jogo29:
    print('O jogo 29 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo29)) == 14:
    print('O jogo 29 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo29)) == 13:
    print('O jogo 29 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo29)) == 12:
    print('O jogo 29 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo29)) == 11:
    print('O jogo 29 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 29 nao ganhou nada')


if resultado == jogo30:
    print('O jogo 30 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo30)) == 14:
    print('O jogo 30 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo30)) == 13:
    print('O jogo 30 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo30)) == 12:
    print('O jogo 30 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo30)) == 11:
    print('O jogo 30 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 30 nao ganhou nada')



if resultado == jogo31:
    print('O jogo 31 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo31)) == 14:
    print('O jogo 31 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo31)) == 13:
    print('O jogo 31 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo31)) == 12:
    print('O jogo 31 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo31)) == 11:
    print('O jogo 31 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 31 nao ganhou nada')



if resultado == jogo32:
    print('O jogo 32 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo32)) == 14:
    print('O jogo 32 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo32)) == 13:
    print('O jogo 32 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo32)) == 12:
    print('O jogo 32 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo32)) == 11:
    print('O jogo 32 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 32 nao ganhou nada')



if resultado == jogo33:
    print('O jogo 33 acertou os 15 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou15))
elif len(resultado.intersection(jogo33)) == 14:
    print('O jogo 33 acertou os 14 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou14))
elif len(resultado.intersection(jogo33)) == 13:
    print('O jogo 33 acertou os 13 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou13))
elif len(resultado.intersection(jogo33)) == 12:
    print('O jogo 33 acertou os 12 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou12))
elif len(resultado.intersection(jogo33)) == 11:
    print('O jogo 33 acertou os 11 numeros sorteados da lotofacil')
    print('voce ganhou o valor de R$ {}'.format(acertou11))
else:
    print('O jogo 33 nao ganhou nada')

