import eventlet
eventlet.monkey_patch()

from flask_socketio import SocketIO, emit, join_room
from flask import Flask
import config

app = Flask('socket-io-app')
app.config.from_object(config)

msg_queue = f"redis://{app.config['REDIS_HOST']}:{app.config['REDIS_PORT']}/0"
sio = SocketIO(app, message_queue=msg_queue, path='socket.io', cors_allowed_origins='*', manage_session=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello world!!"

@sio.on('connect')
def socket_connect():
    print('its connected')
    emit('msg', {'data': 'Connected'})

def join_room_xplan(data):
    print(f"============================{data}")
    print(f"============================{type(data)}")

    if (type(data) is not int) and  (data is None or 'room_id' not in data):
        app.logger.info(f'data: {data}')
        raise Exception('room_id is required')
        #room_id = 14
    else:
        print(f'====================={type(data)}')
        room_id = int(data) if type(data) is int else  int(data['room_id'])
    print("u have joined room --- ", room_id)
    #room = 14
    #print(f'\n\n\njoin room {room}\n\n\n')
    join_room(int(room_id))
    emit('room_id', {'id': room_id})


@sio.on('join_room', namespace='/xtest')
def join_the_room_xpnp(data=None):
    #room = str(uuid.uuid1())
    join_room_xplan(data)