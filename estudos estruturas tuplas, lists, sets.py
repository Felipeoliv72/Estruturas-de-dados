from array import array

def pegaDadosPessoa():
    return 'Felipe' , 28

nome , idade = pegaDadosPessoa()
print(nome)
print(idade)

sucos = [('Laranja', 1, 15.99), ('Uva', 2, 12.99), ('Acerola', 3, 9.99), ('Maracujá', 4, 14.99)]

for suco, num, preco in sucos:
    print(f'{num} - {suco} - R$ {preco}')
selecao = input('Digite o numero do suco desejado:')
quantidade = input('Digite a quantidade desejada:')

lista = [1, 2, 3, 4, 5, 'Amarelo', 'Azul', 'Verde', 'Vermelho', 'Preto']
lista.clear()
print(lista)

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

lista = [Carro]
carro1 = lista[0]()
lista.append(carro1)
lista[1].acelerar()
lista[1].acelerar()
lista[1].acelerar()
print(lista[1].velocidade)

emails = {"joao@example.com", "maria@example.com"}
novo_email = "joao@example.com"

if novo_email in emails:
    print("O email já existe no dicionário.")
else:
    emails.add(novo_email)

#resolvendo dados duplicados em listas facilmente com set
emails_list = ["joao@example.com", "maria@example.com", "joao@example.com"]
print(set(emails_list))#apenas para mostrar os dados sem duplicidade
emails_set = set(emails_list)# cria uma nova variável com os dados sem duplicidade
emails_list = list(emails_set)#a lista original é atualizada com os dados sem duplicidade
print(emails_list)

