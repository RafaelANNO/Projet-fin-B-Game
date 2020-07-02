####################
#imports
import json
import spacy

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
    for string in item['tags++']:
        if string not in globalTags:
            globalTags.append(string)

####################
#methods
def chatBot_lemma(str_in):
    nlp = spacy.load("fr_core_news_sm")
    text = ''
    text = nlp(str_in)

    arr_out = []
    for word in text:
        #try:
        arr_out.append(word.lemma_)
        #except:
        #    pass

    return arr_out

def chatBot_arrCleaner(arr_in):
    arr_out = []
    for str in arr_in:
        if str in globalTags:
            arr_out.append(str)

    return arr_out

def chatBot_findIdResponse(arr_in, occ_security, pp_security):
    occ_accuracy = {}
    pp_accuracy = {}
    for item in globalData['intents']:
        occ_count = 0 
        pp_count = 0
        for string in arr_in:
            if string in item['tags']:
                occ_count += 1
            if string in item['tags++']:
                pp_count += 1
        occ_accuracy[item['id']] = occ_count
        pp_accuracy[item['id']] = pp_count
    
    id = 0
    for item in occ_accuracy:
        if occ_accuracy[item] > occ_accuracy[id]:
            if occ_accuracy[item] >= occ_security:
                if pp_accuracy[item] >= pp_security:
                    id = item
    
    return id

def chatBot_selectRandomResponse(id_in):
    for item in globalData['intents']:
        if str(item['id']) == str(id_in):
            return random.choice(item['reponse'])
    return 'invalid id'


#print(chatBot_lemma('bonjour je fais des tests'))
#print(chatBot_arrCleaner(['bonjour', 'comment', 'aller', 'tu']))
#print(chatBot_findIdResponse(['salut', 'comment', 'aller', 'tu'], 3, 1))
#print(chatBot_findIdResponse(['comment', 'aller', 'tu'], 3, 1))
#print(chatBot_selectRandomResponse(2))
