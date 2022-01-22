from MeusTestes.FuncoesInventario import *
materiais = {}
opcao = escolher()
while opcao == 'I' or opcao == 'R' or opcao == 'L':
    if opcao == 'I':
        inserir(materiais)
    if opcao == 'R':
        resumir(materiais, input('Digite o serial do elemento que deseja resumir: '))
    if opcao == 'L':
        listar(materiais)
    opcao = escolher()
