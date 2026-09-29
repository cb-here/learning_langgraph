from fastapi import Request

def get_chatbot(request: Request):
    return request.app.state.chatbot