import logging
import time
from flask import jsonify
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from helpers import get_response_text

from flask import Flask, request, jsonify

authenticator = IAMAuthenticator('')
assistant = AssistantV2(
    version='2023-05-25',
    authenticator=authenticator
)
assistant.set_service_url('')

#Debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sessions = {}

def create_assistant_session():
    try:
        session = assistant.create_session(
            assistant_id=''
        ).get_result()
        session_id = session['session_id']
        sessions[session_id] = {}
        logger.debug(f"Your session has been created: {session_id}")
        return jsonify({'sessionId': session_id})
    except Exception as err:
        logger.exception('Error white creating the section')
        return jsonify({'error': 'Error white creating the session'}), 500

def ask_assistant_question():
    question = request.json.get('question')
    session_id = request.json.get('sessionId')

    if not question or not session_id:
        return jsonify({'error': 'Question or provided id is not correct.'}), 400

    try:
        message_input = {
            'message_type': 'text',
            'text': question
        }

        response = assistant.message(
            assistant_id='',
            session_id=session_id,
            input=message_input,
            context=sessions.get(session_id, {})
        ).get_result()

        sessions[session_id] = response.get('context', {})  

        responses = []
        responses.append(get_response_text(response)) 

        max_wait_time = 70000 
        start_time = time.time()
        elapsed_time = 0

        while elapsed_time < max_wait_time and len(response['output']['generic']) == 0:
            

            time.sleep(0.1)

           
            response = assistant.message(
                assistant_id='',
                session_id=session_id,
                input=message_input,
                context=sessions.get(session_id, {})
            ).get_result()

            elapsed_time = time.time() - start_time

            if len(response['output']['generic']) > 0:
                responses.append(get_response_text(response))  

        return jsonify({'responses': responses})
    except Exception as err:
        logger.exception('Error white sending the request back', exc_info=err)
        return jsonify({'error': 'Error white sending the request back'}), 500