#tweettheimage
#!/usr/bin/env python
from time import sleep
import urllib
from twython import Twython
#we are using IP Webcam application to now tweet. 
IPADDRESS ="192.168.43.1"

TAGS =" #maxpi #iot #workshop "

CONSUMER_KEY = APP_KEY = 'H3HOtnu4wdQtVeV36BtA2QoMI'
CONSUMER_SECRET = APP_SECRET = 't5AcaVOE1ZtgHXBeGPC1YJupUAjLgd08k41VC4wjVJh1XggH3A'
ACCESS_TOKEN = OAUTH_TOKEN = '924094561521057792-homc7Ugyrd1QuPLE5kfx9x2trtbZxMT'
ACCESS_TOKEN_SECRET = OAUTH_TOKEN_SECRET ='CxpEDA9rlQrXAflmfVqORTDF91fZgxwxDjwEaWqUb8dvA'
#note the access premission for the APP should have Read, write, and direct messages 
#else auth errors would come. 


def tweetImage(imageLocation,TweetMessage):
        api = Twython(CONSUMER_KEY,CONSUMER_SECRET, OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
        takePic(imageLocation)
        photo = open(imageLocation, 'rb')
        response = api.upload_media(media=photo)
        api.update_status(status=str_join(TweetMessage,TAGS), media_ids=[response['media_id']])
	
	

def str_join(*args):
    return ''.join(map(str, args))

def takePic(imageLoc):
	return LoadImagefromIPCam(IPADDRESS,imageLoc)
	
def LoadImagefromIPCam(IPaddress, imageLocation ):
		address =str_join("http://",IPaddress)
		address = str_join(address,":8080/photo.jpg")
		print(address)
		urllib.urlretrieve(address,imageLocation)


if __name__ == '__main__':
	tweetImage('./testImage.jpg','testing twitterImage')
