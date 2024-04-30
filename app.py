# app.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from groq_operations import generate_answer

app = Flask(__name__)


@app.route('/sms',  methods=['POST'])
def chatgpt():

    incoming_que = request.values.get('Body', '').lower()
    print("Request: ", request.get_data())

    answer = generate_answer(incoming_que)

    print("Question: ", incoming_que)

    print("BOT Answer: ", answer)

    bot_resp = MessagingResponse()
    bot_resp.message(answer)

    return str(bot_resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
