# Ai-moslima-chatbot
from flask import Flask, render_template, request, jsonify
from qa_data import qa_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question', '').lower()
    for vraag, antwoord in qa_data.items():
        if vraag in user_question:
            return jsonify({'answer': antwoord})
    return jsonify({'answer': 'Geen antwoord gevonden. We verwijzen je graag naar een studente van kennis, in shaa Allah.'})

if __name__ == '__main__':
    app.run(debug=True)

    qa_data = {
    "moet ik de khimar dragen": "Ja. Surah An-Nur (24:31): 'En laat haar hun khimar over hun boezem trekken.' Tafsir Ibn Kathir bevestigt dit als verplicht.",
    "wat is het verschil tussen fard en sunnah": "Fard is verplicht, niet doen is zonde. Sunnah is aanbevolen. Bron: Usul al-Fiqh.",
    "mag ik bidden met nagellak": "Alleen als het waterdoorlatend is. Anders is wudu ongeldig. Bron: Dar al-Ifta & Ibn Uthaymeen.",
    "mag ik koran lezen tijdens menstruatie": "Meeste madhhabs: niet aanraken mushaf, wel via telefoon. Bron: Mālik's Muwatta.",
    "wanneer is het gebedstijd": "Gebruik apps zoals Muslim Pro. Gebedstijden volgen zonstanden. Bron: Sahih Muslim.",
    "moet gebed in arabisch": "Ja, verplichte gebeden in het Arabisch. Dua mag in eigen taal. Bron: Umdat as-Salik.",
    "wat is halal kleding voor vrouwen": "Los, bedekkend, niet doorschijnend. Gezicht en handen mogen zichtbaar. Surah Al-Ahzab 33:59.",
    "mag ik als vrouw alleen reizen": "Zonder mahram niet toegestaan bij meeste madhhabs. Sommige geleerden maken uitzondering bij veiligheid. Sahih Bukhari 3006.",
    "hoe begin ik met islam leren": "Begin met tawheed, wudu, salāh. Gebruik betrouwbare bronnen zoals IslamQA, SeekersGuidance.",
    "mag ik vasten met borstvoeding": "Ja, tenzij schadelijk voor jou of baby. Dan mag je het inhalen. Bron: Sahih Muslim."
}
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <title>AI Chatbot voor Moslima’s</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <div class="chat-container">
    <h1>🤍 AI Chat voor Moslima’s 🤍</h1>
    <div id="chat-box"></div>
    <input type="text" id="user-input" placeholder="Stel je vraag..." />
    <button onclick="sendQuestion()">Verstuur</button>
  </div>

  <script>
    async function sendQuestion() {
      const input = document.getElementById("user-input").value;
      const chatBox = document.getElementById("chat-box");

      chatBox.innerHTML += `<p><strong>Jij:</strong> ${input}</p>`;
      document.getElementById("user-input").value = "";

      const response = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: input })
      });

      const data = await response.json();
      chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  </script>
</body>
</html>
body {
  background-color: #ffe6f0;
  font-family: 'Arial', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.chat-container {
  background-color: white;
  border: 3px solid #ff80ab;
  border-radius: 15px;
  padding: 20px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 0 15px #ffb6c1;
}
h1 {
  text-align: center;
  color: #ff3399;
  margin-bottom: 20px;
}
#chat-box {
  height: 300px;
  overflow-y: auto;
  border: 2px solid #ffcce0;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #fff5f9;
  color: #333;
  font-size: 15px;
}
#user-input {
  width: 70%;
  padding: 10px;
  border: 1px solid #ff99cc;
  border-radius: 8px;
}
button {
  width: 25%;
  padding: 10px;
  background-color: #ff66a3;
  border: none;
  color: white;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
}
button:hover {
  background-color: #ff3385;
}
