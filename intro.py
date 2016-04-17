print('Ciao, Djangogirls!')
if 3>2:
    print('5 è maggiore di 2')
else:
    print('5 è maggiore di 2')
nome = 'Sonia'
if nome == 'Ola':
    print('Ciao Ola!')
elif nome== 'Sonia':
    print('Ciao Sonia!')
else:
    print('Ciao anonimo')
volume=57
if volume<20:
    print('piuttosto basso.')
elif 20<=volume<=40:
    print('Adatto per musica di sottofondo')
elif 40<=volume<=60:
    print('Perfetto, posso apprezzare ogni dettaglio')
elif 60<=volume<=80:
    print('Ideale per le feste')
elif 80<=volume<=100:
    print('Un po\' altino!')
else:
    print('Oddio, le mie orecchie')
def ciao():
    print('Ciao!')
    print('Come stai?')
ciao()
def ciao (nome):
    if nome=='Ola':
        print('Ciao Ola')
    elif nome =='Sonia':
        print('Ciao Sonia')
    else:
        print('Ciao anonimo')
ciao('Serena')
def ciao(nome):
    print('Ciao ' + nome + '!')
ragazze = ['Rachel','Monica','Phoebe','Tu']
for nome in ragazze:
    ciao(nome)
    print('Prossima ragazza')
for i in range(1,6):
    print(i)
