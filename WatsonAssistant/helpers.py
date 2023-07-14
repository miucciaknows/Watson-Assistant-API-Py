def get_response_text(result):
    """
    Get the result of Watson Assistant and make a verification to return the answer"""
    response_text = []
    if 'output' in result and 'generic' in result['output']:
        for response in result['output']['generic']:
            if response['response_type'] == 'text':
                response_text.append(response['text'])
    return response_text

