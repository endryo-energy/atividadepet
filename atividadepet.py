#Grupo: Endryo, Amanda, Matheus yuri
class Animal:
    def __init__(self, nome, idade, especie):
        self._nome = nome
        self._idade = idade
        self._especie = especie

    def calcular_preco_servico(self):
        pass


class Cachorro(Animal):
    def calcular_preco_servico(self):
        return 50


class Gato(Animal):
    def calcular_preco_servico(self):
        return 40


class Passaro(Animal):
    def calcular_preco_servico(self):
        return 30



animais = []


def cadastrar_animal():
    nome = input("Digite o nome do animal: ")
    idade = input("Digite a idade do animal: ")
    especie = input("Digite a espécie do animal (cachorro, gato, passaro): ").lower()

    if especie == "cachorro":
        animal = Cachorro(nome, idade, especie)
    elif especie == "gato":
        animal = Gato(nome, idade, especie)
    elif especie == "passaro":
        animal = Passaro(nome, idade, especie)
    else:
        print("Espécie inválida! Tente novamente.")
        return

    animais.append(animal)
    print(f"{nome} cadastrado com sucesso!")


def consultar_animal():
    nome = input("Digite o nome do animal que deseja consultar: ")
    for animal in animais:
        if animal._nome == nome:
            print(f"Nome: {animal._nome}, Idade: {animal._idade}, Espécie: {animal._especie}")
            return
    print("Animal não encontrado!")


def calcular_preco_servico():
    nome = input("Digite o nome do animal para calcular o preço do serviço: ")
    for animal in animais:
        if animal._nome == nome:
            preco = animal.calcular_preco_servico()
            print(f"O preço do serviço para {animal._nome} é R${preco:.2f}")
            return
    print("Animal não encontrado!")


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar animal")
        print("2. Consultar animal")
        print("3. Calcular preço de serviço")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_animal()
        elif opcao == '2':
            consultar_animal()
        elif opcao == '3':
            calcular_preco_servico()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")



menu()