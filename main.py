pessoas = []

class Agenda:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def armazena_pessoa(self):
        """Armazena a pessoa na agenda."""
        pessoas.append([self.__nome,self.__idade,self.__altura])

    def checa_remocao(self):
        """Verifica se é este o que deverá ser removido da agenda."""
        global remover
        if self.__nome == remove:
            return f'Pessoa Removida:{self.__nome.title()}'

    def busca_pessoa(self):
        """Busca na agenda se existe determinada pessoa"""
        if self.__nome == busca:
            return f'Pessoa:{self.__nome.ljust(30).title()} Idade:{self.__idade} Altura:{self.__altura}'

    def ret_pessoa(self):
        """Retorna todos os dados de determinadas pessoas"""
        return f'Pessoa:{self.__nome.ljust(30).title()} Idade:{self.__idade} Altura:{self.__altura}'


while True:
    print("MENU DE OPÇÕES:\nDigite 'a' para armazenar nova pessoa.\nDigite 'r' para remover pessoa.\nDigite 'b' para buscar pessoa.\nDigite 't' para imprimir os dados de todos que estão na agenda.\nDigite 'i' para imprimir a pessoa de uma determinada posição.\nDigite 's' para sair.\n")
    menu = input('Digite uma opção do menu:')
    if menu == 'a':
        name = input('Digite o seu nome: ')
        if name == '':
            while name == '':
                name = input('Tente novamente!\nDigite o nome: ')
        age = None
        while age is None:
            try:
                age = int(input('Digite a idade:'))
            except (ValueError,EOFError):
                print('Entrada não reconhecida. Tente novamente!')
        high = None
        while high is None:
            try:
                high = int(input('Digite a altura em cm: '))
            except ValueError:
                print('Entrada não reconhecida. Tente Novamente!')
        pessoa = Agenda(name, age, high)
        Agenda.armazena_pessoa(pessoa)
    elif menu == 'r':
        remover = False
        if not pessoas:
            print('Não existe pessoa alguma na agenda agenda, portanto não é possível remover ninguém.')
        else:
            remove = input('Digite o nome da pessoa que deseja remover: ')
            if remove == '':
                while remove == '':
                    remove = input('Tente novamente!\nDigite o nome da pessoa que deseja remover: ')
            for p in pessoas:
                p1 = Agenda(*p)
                if Agenda.checa_remocao(p1) is not None:
                    print(Agenda.checa_remocao(p1))
                    remover = True
                if remover:
                    pessoas.remove(p)
            if not remover:
                print('Pessoa não encontrada na agenda!')
    elif menu == 'b':
        encontrado = False
        busca = input('Digite o nome de quem deseja buscar: ')
        if busca == '':
            while busca == '':
                busca = input('Entrada não reconhecida. Tente novamente!\nDigite o nome de quem deseja buscar: ')
        for p in pessoas:
            p1 = Agenda(*p)
            if Agenda.busca_pessoa(p1) is not None:
                print(Agenda.busca_pessoa(p1))
                encontrado = True
        if not encontrado:
            print('Nome não encontrado na agenda')
    elif menu == 't':
        for p in pessoas:
            p1 = Agenda(*p)
            print(Agenda.ret_pessoa(p1))
    elif menu == 'i':
        posi = None
        while posi is None:
            try:
                posi = int(input('Digite uma posição numérica:'))
            except ValueError:
                print('Entrada não númerica. Tente novamente!')
        if posi>len(pessoas) or posi<0:
            print('Posição não existente na agenda!')
        else:
            for indice,p in enumerate(pessoas):
                if indice == posi:
                    p1 = Agenda(*p)
                    print(Agenda.ret_pessoa(p1))
    elif menu == 's':
        exit(1)
    else:
        print('Comando não reconhecido. Tente novamente!')