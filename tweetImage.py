import twint
import requests
import shutil
import pathlib
import argparse
import math
import progressbar


def downloadImages(args, listURL, count, path = ''):
	if not path:
		pathlib.Path('images').mkdir(parents = True, exist_ok = True)
		path = 'images'
	with progressbar.ProgressBar(widgets =[progressbar.Bar()] ,max_value = args.number - 1) as bar:
		for saved, tweet in enumerate(listURL):
			if saved == count:
				return
			bar.update(saved)
			for imageURL in tweet:
				r = requests.get(imageURL, stream = True)
				with open (path +'/'+ imageURL.split('/')[4], 'wb') as image: #split to save image with twitter hashed name
					shutil.copyfileobj(r.raw, image)
				del r

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str, help = "Username to download from" )
parser.add_argument("-n", "--number", type=int, default = 3200, help = "Max number of tweets to save, up to 3200, each tweet may contain multiple images")
parser.add_argument("-p", "--path", type=str, default = '', help = "Path to save images at")
args = parser.parse_args()


##Configuring twint to scrap what we want
c = twint.Config()
c.Username = args.username
c.Limit = math.ceil(args.number/20)*20
c.Store_object = True
c.Media = True
c.Hide_output = True
c.Retries_count = 15

##scrap the user favourites
print("Scrapping tweets...")
twint.run.Favorites(c)

#store the image url of each tweet into a list if theres an image
imagesURL = [i.photos for i in twint.output.tweets_list if i.photos]
print("DOWNLOADING IMAGES!!")
downloadImages(args, imagesURL, args.number, args.path)


