####################
#imports
import json
import spacy
nlp = spacy.load("fr_core_news_sm")
import random

####################
#globals
with open('data.json') as json_file:
    globalData = json.load(json_file)

globalTags = []
for item in globalData['intents']:
    for string in item['tags']:
        if string not in globalTags:
            globalTags.append(string)

####################
#methods
def chatBot_lemma(str_in):
    text = nlp(str_in)

    arr_out = []
    for word in text:
        arr_out.append(word.lemma_)

    return arr_out

def chatBot_arrCleaner(arr_in):
    arr_out = []
    for str in arr_in:
        if str in globalTags:
            arr_out.append(str)

    return arr_out

def chatBot_findIdResponse(arr_in, security):
    accuracy = {}
    for item in globalData['intents']:
        count = 0 
        for string in arr_in:
            if string in item['tags']:
                count += 1
        accuracy[item['id']] = count
    
    id = 0
    for item in accuracy:
        if accuracy[item] > accuracy[id]:
            if accuracy[item] >= security:
                id = item
    
    return id

def chatBot_selectRandomResponse(id_in):
    for item in globalData['intents']:
        if str(item['id']) == str(id_in):
            return random.choice(item['reponse'])
    return 'invalid id'


#print(chatBot_lemma('bonjour je fais des tests'))
#print(chatBot_arrCleaner(['bonjour', 'comment', 'aller', 'tu']))
#print(chatBot_findIdResponse(['salut', 'comment', 'aller', 'tu'], 3))
#print(chatBot_selectRandomResponse(2))


########################################
########################################
########################################
def ia_test_printData():
    for item in globalData['intents']:
        print('id: ' + str(item['id']))

        print('reponse: ')
        for string in item['reponse']:
            print('     ' + string)

        print('tags: ')
        for string in item['tags']:
            print('     ' + string)
        print('')

def ia_test_recu():
    return " - recu"
