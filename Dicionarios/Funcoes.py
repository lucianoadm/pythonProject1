def perguntar():
    resposta = input('O que deseja realizar?\n'
                     '<I> para Inserir usuário\n'
                     '<P> para Pesquisar usuario\n'
                     '<E> para excluir usuario\n'
                     '<L> para Listar usuário: ').upper()
    return resposta


def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                     input('Digite a última data de acesso: '),
                                                     input('Ditige a últma estação acessada: ').upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open('bd.txt', 'a') as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ':' + str(valor))


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print(f'Nome.............: {lista[0]}')
        print(f'Último acesso....: {lista[1]}')
        print(f'Última estação...: {lista[2]}')


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print('Objeto Eliminado!')


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Objeto.....')
        print('Login.....', chave)
        print('Dados.....', valor)
