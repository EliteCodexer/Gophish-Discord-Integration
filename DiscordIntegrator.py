from flask import Flask, request, abort
import json,requests

#webhook do canal do discord
webhook_discord = ''


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def get_webhook():
    if request.method == 'POST':
        resposta_gophish = request.json
        mensagem = generate_msg(resposta_gophish)

        #enviar mensagem para o discord
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        resposta_discord = requests.post(webhook_discord, data=mensagem, headers=headers)
        
        #se precisar debugar resposta http do discord
        #print(resposta_discord.status_code)
        return 'success', 200
    else:
            abort(400)

#função para adequar informações do Gophish ao formato aceito pelo Discord            
def generate_msg(msg):
    #corpo do alerta no formato aceito pelo discord
    payload_discord = {
            "embeds": [
            {
                "title": "Gophish Alert - Campanha {}".format(msg["campaign_id"]),
                "color": "3731970",
                "fields": [
                {
                    "name": "email",
                    "value": "{}".format(msg["email"]),
                    "inline": True
                },
                {
                    "name": "time",
                    "value": "{}".format(msg["time"]),
                    "inline": True
                },
                {
                "name": "message",
                "value": "{}".format(msg["message"]),
                "inline": True
                }]}]}

    #Tratamento para o campo "Value", o Discord não aceita campos vazios.
    if  msg["details"]:
        payload_discord["embeds"][0]["fields"].append({
        "name": "details",
        "value": "{}".format(msg["details"]),
        "inline": True
        })
    else:
        payload_discord["embeds"][0]["fields"].append({
        "name": "details",
        "value": "N/A",
        "inline": True
        })

    return json.dumps(payload_discord)       


if __name__ == '__main__':
	app.run()
