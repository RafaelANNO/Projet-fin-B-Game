#pip3 install flask

import flask
from flask import request, jsonify
from methods_bot import chatBot_lemma, chatBot_arrCleaner, chatBot_findIdResponse, chatBot_selectRandomResponse

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Bienvenue chez Ring Bot</h1>
<p>Ici vous pouvez posez toutes vos questions a notre ami les films du seigneur des anneaux.</p>'''

@app.route('/api/v1/ringBot', methods=['GET'])
def api_msg():
    if 'msg' in request.args:
        message = str(request.args['msg'])
        #print('1- ' + message)
        arr_message = chatBot_lemma(message)
        #print('2- ' + str(arr_message))
        arr_message = chatBot_arrCleaner(arr_message)
        #print('3- ' + str(arr_message))
        id = chatBot_findIdResponse(arr_message, 3)
        #print('4- ' + str(id))
        reponse = chatBot_selectRandomResponse(id)
        #print('5- ' + reponse)
        return reponse
    else:
        return "Pas de message entrant."

#app.run(host='192.168.43.145')
app.run()