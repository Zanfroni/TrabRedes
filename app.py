import client

#Configuracao do Cliente

print('Digite 1 para TCP caso contrario, sera UDP')
choice = input()

#Leitura do arquivo de texto

with open ('test.txt') as f:
    
    bArray = ''
    
    for line in f:
        bArray += line

#Inicializacao do Cliente (Requer Servidor inicializado)
        
client.setup(choice, bArray)