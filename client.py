import socket

#Executado no mesmo computador, logo, deve-se manter estes parametros
#Para Lab. Redes, o host foi alterado para estabelecer comunicacao entre dois
#computadores.

#Para estabelecer entre dois computadores diferentes, deve-se alterar
#o localhost para o IP do computador que esta atuando como servidor. O IP de
#ambos deve ser o mesmo (neste caso, escolheu-se 50007).
host = 'localhost'
ip = 50007

def setup(choice, bArray):
    
    if choice == '1':   
        print('TCP CONNECTION!')
        
        #Inicia Socket
        print('Establishing connection with server...')
        sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Confirma conexao
        sockobj.connect((host,ip))
        
        #Envia o texto para o servidor
        signal = bytes(bArray, 'utf-8')
        sockobj.send(signal)
            
        #Recebe de volta o texto do servidor
        data = sockobj.recv(50000)
        print('Client received:', data)
        
        #Fecha o Socket
        sockobj.close()
    
    else:
        
        #Inicia Socket
        print('UDP CONNECTION!')
        print('Sending archive to server...')
        sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_addr = (host,ip)
        
        #Envia texto para o Servidor
        signal = bytes(bArray, 'utf-8')
        sockobj.sendto(signal,server_addr)
        
        #Recebe texto do Servidor
        data = sockobj.recvfrom(50000)
        print('Client received from Server:', data)
        
        #Fecha o Socket
        sockobj.close()