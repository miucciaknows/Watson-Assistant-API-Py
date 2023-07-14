from flask import Flask, request, jsonify
from .WatsonAssistant.watson_assistant import create_assistant_session, ask_assistant_question

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/session', methods=['GET'])
def create_session_route():
    return create_assistant_session()

@app.route('/ask', methods=['POST'])
def ask_question_route():
    return ask_assistant_question()

if __name__ == '__main__':
    app.run(port=3000)