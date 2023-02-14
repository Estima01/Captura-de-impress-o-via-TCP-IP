import socket
while True:
        
    ip = '127.0.0.2'
    port = 9100
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))

    s.listen(1)

    conn, addr = s.accept()

    print('Connected by', addr)

    print_signal= conn.recv(1024).decode("ISO-8859-1")

    for i in print_signal:
        with open("teste.txt", "a", encoding="utf-8") as myfile:
            
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

    with open("teste.txt", "r") as f:
        contents = f.read()

    contents = contents.replace("!{bE-MaB", "\n")

    with open("arquivo_limpo.txt", "w") as f:
        f.write(contents)

    #limpa arquivo
    with open("teste.txt", "w") as f:
        f.write('')
    conn.close()