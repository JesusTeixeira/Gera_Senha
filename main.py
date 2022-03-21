import random

lista = ['Luiz Otávio', 'Maria' , 'Pedro', 'Oliveira', 'Faria', 'Luiz', 'Ot\u00e1vio']
#sorteio = random.choice(lista)
#sorteio2 = random.choices(lista, k=2)
embaralha = random.sample(lista, 2)
random.shuffle(lista)

    
#print(sorteio)
#print(sorteio2)
print(lista)

'''
for i in range(50):
    sem_repeticao = random.sample(lista, 2)
    print(sem_repeticao)
    '''