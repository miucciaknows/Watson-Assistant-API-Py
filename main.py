#Setting the requirements
from flask import Flask, request, jsonify
from .WatsonAssistant.watson_assistant import create_assistant_session, ask_assistant_question

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/session', methods=['GET'])
def create_session_route():
    """This function call the function that in watson_assistant.py to create a session_id.
     return the session_id """
    return create_assistant_session()

@app.route('/ask', methods=['POST'])
def ask_question_route():
    """This function call the function that is watson_assistant.py to send ask WA a question."""
    return ask_assistant_question()

if __name__ == '__main__':
    app.run(port=3000)