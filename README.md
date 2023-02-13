# Captura-de-impress-o-via-TCP-IP
Um filtro de rede na qual capta o arquivo enviado para a impressora via TCP/IP e escreve em TXT, para testes de impressão sem precisar ter uma impressora
<br>
<h2>Como configurar</h2>
Para você capturar o que esta sendo enviado para impressão e não tem a impressora especifica (nesse caso da imagem, é de uma impressora não-fical), você deverar criar uma impressora com drivers genericos e criar uma porta TCP/IP. No código é criada uma faixa 127.0.0.2 e a porta é de acordo com a que o sistema seleciona, sendo informado na tela antes de concluir a criação da porta.

Em seguida, no sistema de impressão do seu aplicativo que deseja capturar, selecione a impressora criada.

Após isso, antes de enviar para impressão o conteudo em seu sistema, aplicativo, deve rodar o algoritmo para que ele fique escutando a porta, e em seguida enviar para impressão.

Neste caso, ele faz um filtro dos comandos que, na impressora, seriam de espaçamento, podendo variar de sistema pra sistema.
E por fim ele salva em um TXT.
<br>
![image](https://user-images.githubusercontent.com/62814826/218541494-07b19f26-936f-4d2f-af0f-dc3a4fdb21e0.png)
