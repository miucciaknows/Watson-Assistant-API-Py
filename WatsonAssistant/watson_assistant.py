#Libraries that i need to do this api.
#I Was using this one for seeing logs, in case i have an error.
import logging

#Time to  manipulate time values
import time

#API and Json
from flask import Flask, request, jsonify

#From iBM's
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#A function that i need
from .helpers import get_response_text

#Files manipulation
import os

#Enviroments variables
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["apikey"]
url = os.environ["url"]
assistant_id = os.environ["enviroment_id"]

authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2023-05-25',
    authenticator=authenticator
)
assistant.set_service_url(url)

#Debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sessions = {}

def create_assistant_session():
    """This function will create a unique session_id to maintain the conversation between user and Watson Assistant."""
    try:
        session = assistant.create_session(
            assistant_id=assistant_id,
        ).get_result()
        session_id = session['session_id']
        sessions[session_id] = {}
        logger.debug(f"Your session has been created: {session_id}")
        return jsonify({'sessionId': session_id})
    except Exception as err:
        logger.exception('Error white creating the section')
        return jsonify({'error': 'Error white creating the session'}), 500

def ask_assistant_question():
    """This function will send your question to Watson Assistant."""
    question = request.json.get('question')
    session_id = request.json.get('sessionId')
    
    #Checking if question or session_id is not in request
    if not question or not session_id:
        return jsonify({'error': 'Question or provided id is not correct.'}), 400

    try:
        message_input = {
            'message_type': 'text',
            'text': question
        }

        response = assistant.message(
            assistant_id=assistant_id,
            session_id=session_id,
            input=message_input,
            context=sessions.get(session_id, {})
        ).get_result()

        #Getting the contet
        sessions[session_id] = response.get('context', {})  

        #Empty array to store the answers
        responses = []
        #Appeding the answers in the array
        responses.append(get_response_text(response)) 

        #max wait time, i set 7 seconds, you can set the time down or up.
        max_wait_time = 70000 
        start_time = time.time()
        elapsed_time = 0

        #Set this to control Assistant's time to get its answer.
        while elapsed_time < max_wait_time and len(response['output']['generic']) == 0:
            #little delay
            time.sleep(0.1)
            #Assistant message to user requirements
            response = assistant.message(
                assistant_id=assistant_id,
                session_id=session_id,
                input=message_input,
                context=sessions.get(session_id, {})
            ).get_result()

            #Controling the time to get the full answer
            elapsed_time = time.time() - start_time

            if len(response['output']['generic']) > 0:
                responses.append(get_response_text(response))  
        
        #Returning the answer 
        return jsonify({'responses': responses})
    except Exception as err:
        logger.exception('Error white sending the request back', exc_info=err)
        return jsonify({'error': 'Error white sending the request back'}), 500