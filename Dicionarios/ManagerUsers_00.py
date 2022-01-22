usuarios = {}
opcao = input('O que deseja realizar? '  # opçao perguntar
              '<i> para Inserir um usuário'
              '<P> para Pesquisar um usuário'
              '<E> para excluir um usuário'
              '<L> para Listar um usuário: ').upper()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':  # opção inserir
        chave = input('Digite o login: ').upper()
        nome = input('Digite o nome: ').upper()
        data = input('Digite a última data de acesso: ')
        estacao = input('Digite a última estação acessada: ').upper()
        usuarios = input('O que deseja realizar?: ').upper()
        usuarios[chave] = [nome, data, estacao]
    opcao = input('O que deseja realizar? '  # opçao perguntar
                  '<i> para Inserir um usuário'
                  '<P> para Pesquisar um usuário'
                  '<E> para excluir um usuário'
                  '<L> para Listar um usuário: ').upper()