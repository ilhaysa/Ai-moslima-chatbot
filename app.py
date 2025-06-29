from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Moslima Chatbot draait!"

@app.route('/chat', methods=['POST'])
def chat():
    vraag = request.json.get("message", "")
    
    # Simpele logica (hier kun je AI aan koppelen)
    antwoorden = {
        "wat is de hijab?": "De hijab is de islamitische hoofddoek die moslima’s dragen als vorm van gehoorzaamheid aan Allah.",
        "wie is Allah?": "Allah is de Enige God in de islam, de Schepper van alles dat bestaat.",
        "wat is halal?": "Halal betekent toegestaan volgens de islamitische wetten.",
    }

    antwoord = antwoorden.get(vraag.lower(), "Sorry zuster, ik weet daar nog geen antwoord op.")
    return jsonify({"response": antwoord})

if __name__ == '__main__':
    app.run(debug=True)
