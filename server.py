from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Список для хранения подключенных пользователей
users = {}

@app.route('/')
def index():
    # Рендерим HTML-страницу
    return render_template('index.html')


# Обработка нового подключения клиента
@socketio.on('connect')
def handle_connect():
    print(f'Пользователь подключен!')


# Обработка отключения клиента
@socketio.on('disconnect')
def handle_disconnect():
    print(f'Пользователь отключен!')


# Обработка сообщений от клиента
@socketio.on('send_message')
def handle_message(data):
    sender = data['sender']
    message = data['message']

    print(f'Сообщение от {sender}: {message}')

    # Отправляем сообщение всем подключенным пользователям
    emit('receive_message', {'sender': sender, 'message': message}, broadcast=True)


# Запуск сервера
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)
