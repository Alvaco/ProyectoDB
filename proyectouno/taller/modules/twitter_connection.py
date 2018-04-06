import tweepy

def conectarTwitter():
    consumer_key="wONCt0gIskBoToWRaAYTa3EpQ"
    consumer_secret="03aeo9EwnaTxoF4zfoLN8phyoW75RwKMnmv3nwge5QKW3ePShj"
    access_token="976638170388488194-qLECTKYA5hq7n1nHLN3zUjUJ6lUG0Dz"
    access_token_secret = "CNNoe9bHnewbyMFdw26NwatVoTMQeHYq2krNirCyhadKe"

    auth = tweepy.OAuthHandler(consumer_key= consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def getUserTweets(user, api):
    userTweets = []

    api.create_friendship(user)

    tweets = api.user_timeline(screen_name=user, count=10, include_rts=False)

    for tweet in tweets:
        jsonTweet = tweet._json
        userTweets.append(jsonTweet['text'])

    return userTweets


def getTweetsFiltro(api, word):
    tweetsMatch = []
    tweets = api.home_timeline(count=100)

    for tweet in tweets:
        jsonTweet = tweet._json
        userTweet = jsonTweet['user']['screen_name']
        textTweet = jsonTweet['text']

        if word.lower() in textTweet.lower():
            tweetMatch = {'user': userTweet, 'tweet': textTweet}
            tweetsMatch.append(tweetMatch)

    return tweetsMatch

def unfollowUser(api, user):
    api.destroy_friendship(screen_name=user)