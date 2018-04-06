import taller.modules.twitter_connection as t
import taller.modules.mongo_connection as mgdb

db = mgdb.dbConection()
api = t.conectarTwitter()

def getUserTweets(user):
    collection = mgdb.agregateUserTweets(db, api, user)
    mgdb.imprimirCol(collection)
    return mgdb.getUserTweets(db,user)

def getFilterTweets(word):
    collection = mgdb.agregateFilterTweets(db, api, word)
    mgdb.imprimirCol(collection)
    return mgdb.getFilterTweets(db, word)

def deleteAllUserTweets():
    mgdb.removeAllUserTweets(db)

def deleteAllFilterTweets():
    mgdb.removeAllFilterTweets(db)

def unfollowUser(user):
    mgdb.unfollowUser(db,api,user)