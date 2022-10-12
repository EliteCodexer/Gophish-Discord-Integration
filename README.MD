# Integração Gophish com Discord
Script para coletar eventos de uma campanha do Gophish via webhook e encaminhar os dados para um canal de chat do Discord.

Ao executar o script, ele irá abrir um listener http na porta 5000 que servirá como um webhook para o Gophish, quando o Gophish enviar dados para a url *http://127.0.0.1:5000/webhook* irá ativar a função que irá adequar os dados para o formato aceito e irá fazer o encaminhamento para o webhook do Discord

## Requisitos
- Python 3
- Blibliotecas necessárias:
```bash
pip3 install requirements.txt
```


## How to Use
- Instalar todas as dependências do script com o comando acima.
- Criar um webhook em seu canal do discord e colocar na variavel *webhook_discord* na linha 6 do script.
- Executar o script e criar um webhook no Gophish e adicionar a url do Script nele.
![](/images/img3.png)

![](/images/img1.png)

Os alertas devem começar a chegar no Discord:
![](/images/img2.png)
