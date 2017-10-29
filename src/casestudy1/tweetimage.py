#tweettheimage
#!/usr/bin/env python
import picamera
from time import sleep

from twython import Twython

CONSUMER_KEY = APP_KEY = '****YOUR APP KEY FROM twitter ****'
CONSUMER_SECRET = APP_SECRET = '****YOUR APP SECRET **** '
ACCESS_TOKEN = OAUTH_TOKEN = '****YOUR OAUTH_TOKEN****'
ACCESS_TOKEN_SECRET = OAUTH_TOKEN_SECRET ='****YOUR OAUTH_TOKEN_SECRET ****'
#note the access premission for the APP should have Read, write, and direct messages 
#else auth errors would come. 

TAGS ="#iotgeeks #maxpi #iot #workshop #Paypal"

def tweetImage(imageLocation,TweetMessage):
        api = Twython(CONSUMER_KEY,CONSUMER_SECRET, OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
	takePic(imageLocation)
        photo = open(imageLocation, 'rb')
        response = api.upload_media(media=photo)
        api.update_status(status=str_join(TweetMessage,TAGS), media_ids=[response['media_id']])
	
	

def str_join(*args):
    return ''.join(map(str, args))

def takePic(imageLoc):
    camera = picamera.PiCamera()
    try:
        camera.start_preview()
        sleep(5)
        camera.capture(imageLoc)
        camera.stop_preview()
    finally:
        camera.close()


if __name__ == '__main__':
	tweetImage('./testImag.jpg','testing twitterImage')
