# Captura de impressão via TCP/IP

<p>Um filtro de rede na qual capta o arquivo enviado para a impressora via TCP/IP e escreve em TXT, para testes de impressão sem precisar ter uma impressora
</p>
<h2>Como configurar</h2>
<p>O sistema de captura de impressão via TCP/IP consiste em ficar escutando uma determinada faixa e porta, na qual quando é enviado uma comanda de impressão, ela captura e printa na tela, não precisando assim de uma impressora fisica de fato para testar o envio da mesma.
</p>
<p>Para utilizar, basta indicar seu prefixo e porta que se comunica, como na imagem ilustrada. Caso os campos estejam vazios, sera sinalizado no campo "Estado:" que não foi preenchido devidamente. Caso preencha corretamente ele irá conectar e ficar escutando a faixa até uma impressão ser enviada.
</p>
<p>Após ele ter capturado e mostrado ele ira desconectar, para escutar novamente basta clicar em "Conectar" novamente que ele ira estabelecer a conexão novamente.</p>

![image](https://user-images.githubusercontent.com/62814826/221083313-77a83e85-6e68-4c65-b41c-f6f2e1d19dad.png)

<h2>Bibliotecas usadas</h2>

<strong>PySimpleGUIWx</strong>
pip install PySimpleGUIWx

<strong>Socket</strong>
pip install socket
pip install pysocket

<strong>Time</strong>
