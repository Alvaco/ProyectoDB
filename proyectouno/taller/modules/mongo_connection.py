from pymongo import MongoClient
import taller.modules.twitter_connection as tc

def dbConection():

    client = MongoClient('localhost', 27017)

    dbmongo = client['prueba_mongo']

    return dbmongo



def agregateUserTweets(dbmongo, api, user):
    tweets_por_usuario = dbmongo['tweets_por_usuario']
    tweets = tc.getUserTweets(user,api)
    try:
        cursor = tweets_por_usuario.find({'user': user})
        t = cursor[0]
        print("Actualizando tweetsen base de datos de usuario: " + user)
        tweets_por_usuario.update_one({'user': user}, {"$set": {'tweets': tweets}})

    except IndexError:
        print("Agregando usuario y actualizando tweets en base de datos de: " + user)
        dic = {'user': user, 'tweets': tweets}
        tweets_por_usuario.insert_one(dic)


    return tweets_por_usuario


def agregateFilterTweets(dbmongo,api,word):
    tweets_filtrados_col = dbmongo['tweets_filtrados']

    tweets_filtrados = tc.getTweetsFiltro(api,word)

    try:
        cursor = tweets_filtrados_col.find({'word':word})
        t = cursor[0]
        print('Actualizando tweet fitrados de palabra: ' + word)
        tweets_filtrados_col.update_one({'word': word}, {"$set": {'tweets_filtrados': tweets_filtrados}})

    except:
        print("Agregando palabra y actualizando tweets filtrados en base de datos de: " + word)
        dic = {'word': word, 'tweets_filtrados': tweets_filtrados}
        tweets_filtrados_col.insert_one(dic)

    return tweets_filtrados_col

def imprimirCol(coleccion):
    c = coleccion.find({})
    for d in c:
        print(d)

def getUserTweets(dbmongo, user):
    tweets_por_usuario = dbmongo['tweets_por_usuario']
    cursor = tweets_por_usuario.find({'user':user})
    tweets = []
    for doc in cursor:
        tweets = doc
    return tweets['tweets']

def getFilterTweets(dbmongo, word):
    tweetsFiltrados = dbmongo['tweets_filtrados']
    cursor = tweetsFiltrados.find({'word': word})
    tweets = []
    for doc in cursor:
        tweets = doc
    return tweets['tweets_filtrados']

def removeAllUserTweets(dbmongo):
    tweets_por_usuario = dbmongo['tweets_por_usuario']
    tweets_por_usuario.delete_many({})

def removeAllFilterTweets(dbmongo):
    tweets_filtrados_col = dbmongo['tweets_filtrados']
    tweets_filtrados_col.delete_many({})

def unfollowUser(dbmongo, api, user):
    tweets_por_usuario = dbmongo['tweets_por_usuario']
    tweets_por_usuario.delete_many({'user':user})
    tc.unfollowUser(api,user)