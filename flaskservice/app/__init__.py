import config 
from flask_socketio import SocketIO

redis_uri = f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/0"

sio = SocketIO(message_queue=redis_uri, cors_allowed_origins="*")

def send_socket(event, namespace, room, message_key="default", message=""):
    ''' method for publishing messages using celery '''
    if namespace != 0:
        print(event,namespace,room,message_key,message)
        sio.emit(event, {f"{message_key}_msg":message}, namespace=namespace, room=room)
    else:
        print(message)