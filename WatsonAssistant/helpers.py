def get_response_text(result):
    response_text = []
    if 'output' in result and 'generic' in result['output']:
        for response in result['output']['generic']:
            if response['response_type'] == 'text':
                response_text.append(response['text'])
    return response_text

