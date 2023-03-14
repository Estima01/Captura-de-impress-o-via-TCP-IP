import PySimpleGUIWx as sg
import socket
import time
import bluetooth

# Layout
layout = [
    [sg.Text('Captura Impressão TCP/IP')],
    [sg.Text('IP:'), sg.InputText('')],
    [sg.Text('Porta:'), sg.InputText('')],
    [sg.Button('Conectar'),
     sg.Button('Sair'),
     sg.Text('Estado: '), sg.Text('Desconectado', key='estado', size=(10, 2))],
     [sg.Text('Captura Impressão Bluetooth'), sg.Button('Conectar Bluetooth')],
     [sg.Multiline(size=(34, 22), key='output')]
]

# Janela
janela = sg.Window('Captura Impressão TCP/IP').layout(layout)

# Ler os eventos
while True:
    eventos, valores = janela.Read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Conectar':
        
        if valores[0] == '' or valores[1] == '':
            janela.FindElement('estado').Update('Preencha os campos')
            time.sleep(2)
            janela.FindElement('estado').Update('Desconectado')
            continue
        
        janela.FindElement('estado').Update('Conectando...')
        time.sleep(2)
        janela.FindElement('estado').Update('Conectado')


        ip = valores[0]
        port = int(valores[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))

        s.listen(1)

        conn, addr = s.accept()

        
        print_signal= conn.recv(1073741824).decode("ISO-8859-1")
        for i in print_signal:
            with open("limpador.txt", "a") as myfile:
                
                if i == '\x00':
                    myfile.write('')
                elif i == '\x01':
                    myfile.write('')
                elif i == '\x02':
                    myfile.write('')
                elif i == '\x03':
                    myfile.write('')
                elif i == '\x00':
                    myfile.write('')
                elif i == '\x01':
                    myfile.write('')
                elif i == '\x02':
                    myfile.write('')
                elif i == '\x03':
                    myfile.write('')
                elif i == '\x04':
                    myfile.write('')
                elif i == '\x05':
                    myfile.write('')
                elif i == '\x06':
                    myfile.write('')
                elif i == '\x07':
                    myfile.write('')
                elif i == '\x08':
                    myfile.write('')
                elif i == '\x09':
                    myfile.write('')
                elif i == '\x0a':
                    myfile.write('')
                elif i == '\x0b':
                    myfile.write('')
                elif i == '\x0c':
                    myfile.write('')
                elif i == '\x0d':
                    myfile.write('')
                elif i == '\x0e':
                    myfile.write('')
                elif i == '\x0f':
                    myfile.write('')
                elif i == '\x10':
                    myfile.write('')
                elif i == '\x11':
                    myfile.write('')
                elif i == '\x12':
                    myfile.write('')
                elif i == '\x13':
                    myfile.write('')
                elif i == '\x14':
                    myfile.write('')
                elif i == '\x15':
                    myfile.write('')
                elif i == '\x16':
                    myfile.write('')
                elif i == '\x17':
                    myfile.write('')
                elif i == '\x18':
                    myfile.write('')
                elif i == '\x19':
                    myfile.write('')
                elif i == '\x1a':
                    myfile.write('')
                elif i == '\x1b':
                    myfile.write('')
                elif i == '\x1c':
                    myfile.write('')
                elif i == '\x1d':
                    myfile.write('')
                elif i == '\x1e':
                    myfile.write('')
                elif i == '\x1f':
                    myfile.write('')
                elif i == '\x7f':
                    myfile.write('')
                elif i == '\x80':
                    myfile.write('')
                elif i == '\x81':
                    myfile.write('')
                elif i == '\x82':
                    myfile.write('')
                elif i == '\x83':
                    myfile.write('')
                elif i == '\x84':
                    myfile.write('')
                elif i == '\x85':
                    myfile.write('')
                elif i == '\x86':
                    myfile.write('')
                elif i == '\x87':
                    myfile.write('')
                elif i == '\x88':
                    myfile.write('')
                elif i == '\x89':
                    myfile.write('')
                elif i == '\x8a':
                    myfile.write('')
                elif i == '\x8b':
                    myfile.write('')
                elif i == '\x8c':
                    myfile.write('')
                elif i == '\x8d':
                    myfile.write('')
                elif i == '\x8e':
                    myfile.write('')
                else:
                    myfile.write(i)
                myfile.close()


        with open("limpador.txt", "r") as f:
            contents = f.read()

        contents = contents.replace("!{bE-MaB", "\n")

        with open("arquivo_limpo.txt", "w") as f:
            f.write(contents)
            
        with open("limpador.txt", "w") as f:
            f.write('')

        #mostra o arquivo limpo
        with open("arquivo_limpo.txt", "r") as f:
            contents = f.read()
            janela.FindElement('output').Update(contents)

        conn.close()
        janela.FindElement('estado').Update('Desconectado')
    if eventos == 'Conectar Bluetooth':
        
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        uuid = "00001101-0000-1000-8000-00805F9B34FB" # UUID padrão para porta serial Bluetooth

        bluetooth.advertise_service(server_sock, "TestServer",
                            service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

        janela.FindElement('estado').Update('Aguardando conexão Bluetooth...')
        conn, addr = server_sock.accept()
        janela.FindElement('estado').Update('Conectado Bluetooth')
        
        data = conn.recv(1073741824).decode("ISO-8859-1")
        
        for i in data:
            with open("limpador.txt", "a", encoding="utf-8") as myfile:
                
                if i == '\x00':
                    myfile.write('')
                elif i == '\x01':
                    myfile.write('')
                elif i == '\x02':
                    myfile.write('')
                elif i == '\x03':
                    myfile.write('')
                elif i == '\x00':
                    myfile.write('')
                elif i == '\x01':
                    myfile.write('')
                elif i == '\x02':
                    myfile.write('')
                elif i == '\x03':
                    myfile.write('')
                elif i == '\x04':
                    myfile.write('')
                elif i == '\x05':
                    myfile.write('')
                elif i == '\x06':
                    myfile.write('')
                elif i == '\x07':
                    myfile.write('')
                elif i == '\x08':
                    myfile.write('')
                elif i == '\x09':
                    myfile.write('')
                elif i == '\x0a':
                    myfile.write('')
                elif i == '\x0b':
                    myfile.write('')
                elif i == '\x0c':
                    myfile.write('')
                elif i == '\x0d':
                    myfile.write('')
                elif i == '\x0e':
                    myfile.write('')
                elif i == '\x0f':
                    myfile.write('')
                elif i == '\x10':
                    myfile.write('')
                elif i == '\x11':
                    myfile.write('')
                elif i == '\x12':
                    myfile.write('')
                elif i == '\x13':
                    myfile.write('')
                elif i == '\x14':
                    myfile.write('')
                elif i == '\x15':
                    myfile.write('')
                elif i == '\x16':
                    myfile.write('')
                elif i == '\x17':
                    myfile.write('')
                elif i == '\x18':
                    myfile.write('')
                elif i == '\x19':
                    myfile.write('')
                elif i == '\x1a':
                    myfile.write('')
                elif i == '\x1b':
                    myfile.write('')
                elif i == '\x1c':
                    myfile.write('')
                elif i == '\x1d':
                    myfile.write('')
                elif i == '\x1e':
                    myfile.write('')
                elif i == '\x1f':
                    myfile.write('')
                elif i == '\x7f':
                    myfile.write('')
                elif i == '\x80':
                    myfile.write('')
                else :
                    myfile.write(i)
                myfile.close()

        with open("limpador.txt", "r") as f:
            contents = f.read()

        contents = contents.replace("!{bE-MaB", "\n")

        with open("arquivo_limpo.txt", "w") as f:
            f.write(contents)

        with open("limpador.txt", "w") as f:
            f.write('')

        #mostra o arquivo limpo
        with open("arquivo_limpo.txt", "r") as f:
            contents = f.read()
            janela.FindElement('output').Update(contents)

        conn.close()
        janela.FindElement('estado').Update('Desconectado')
        server_sock.close()
server_sock.close()




janela.Close()
