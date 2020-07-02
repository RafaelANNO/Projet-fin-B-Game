from flask import Flask, render_template, request
from flask_socketio import SocketIO
from methods_bot import chatBot_lemma, chatBot_arrCleaner, chatBot_findIdResponse, chatBot_selectRandomResponse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat1')
def chat1():
    return render_template('chatPage1.html')

@app.route('/chat2')
def chat2():
    return render_template('chatPage2.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    socketio.emit('my response', json, callback=messageReceived)

@app.route('/api/ringBot', methods=['GET'])
def api_msg():
    if 'msg' in request.args:
        print(request)
        message = str(request.args['msg'])
        #print('1- ' + message)
        arr_message = chatBot_lemma(message)
        #print('2- ' + str(arr_message))
        arr_message = chatBot_arrCleaner(arr_message)
        #print('3- ' + str(arr_message))
        id = chatBot_findIdResponse(arr_message, 3, 1)
        #print('4- ' + str(id))
        reponse = chatBot_selectRandomResponse(id)
        #print('5- ' + reponse)
        return reponse
    else:
        return "Pas de message entrant."


if __name__ == '__main__':
    socketio.run(app, debug=True)
    app.run(debug=True, host='0.0.0.0')