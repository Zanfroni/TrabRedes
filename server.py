import socket

#Executado no mesmo computador, logo, deve-se manter estes parametros
#Para Lab. Redes, o host foi alterado para estabelecer comunicacao entre dois
#computadores.

#Se manter como host sem nenhum IP, a biblioteca automaticamente considera
#o IP do PC que está executando o script como IP padrao. O IP de
#ambos deve ser o mesmo (neste caso, escolheu-se 50007).
host = ''
ip = 50007

def setup(choice):
    
    if choice == '1':
        #Inicializa Servidor
        print('TCP CONNECTION!')
        print('Awaiting connection from Client...')
        sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockobj.bind((host,ip))
        #Aguarda conexao do cliente (limite maximo settado para apenas um)
        sockobj.listen(1)
        
        while True:
            #Recebe conexao do Cliente
            connection, address = sockobj.accept()
            print('Server established connection with: ', address)
            
            while True:
                #Recebe texto do Cliente
                data = connection.recv(50000)
                print('Server received:', data)
                
                if not data: break
            
                #Manda texto de volta para o Cliente            
                connection.send(data)
                
            #Fecha a conexao
            connection.close()
        
        #Fecha o Socket
        sockobj.close()
    
    else:
        #Inicializa Servidor
        print('UDP CONNECTION!')
        sockobj= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockobj.bind((host, ip))
        
        while True:
            #Recebe texto do Cliente
            data, addr = sockobj.recvfrom(50000)
            if not data: break
        
            print('Server received from Client:', data)
            
            #Manda texto de volta para o Cliente 
            sockobj.sendto(data, addr)

        #Fecha o Socket
        sockobj.close()