from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
# consumer key, consumer secret, access token, access secret.
ckey = "ZdDX7WyetcKbVT8fTG7freOjh"
csecret = "Xg08qNlIEPOC5sDA44sthZP2BGjvxYqlI4rZ71vM95n2QICXKn"
atoken = "1262338809011802112-6BxKWDbhBE6BdBBJYZYEIk7PF1c6No"
asecret = "F2xhotwBwELmlThV5bPL1432DqOLakUHPVbDeWOkXgRrg"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence * 100 >= 80:
                output = open("twitter-out.txt", "a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cameroon"])
