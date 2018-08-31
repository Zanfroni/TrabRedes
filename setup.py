import server

#Configuracao do Servidor

#Deve ser executado antes de executar o Cliente, caso contrario, a conexao
#sera recusada

print('Digite 1 para TCP caso contrario, sera UDP')
choice = input()

#Inicializacao do Servidor

server.setup(choice)