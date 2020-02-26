import twint
import requests
import shutil

def downloadImages(listURL, path):
	for tweet in listURL:
		for imageURL in tweet:
			r = requests.get(imageURL, stream = True)
			with open (imageURL.split('/')[4], 'wb') as image: #split to save image with twitter hashed name
				shutil.copyfileobj(r.raw, image)
			del r

##Configuring twint to scrap what we want
c = twint.Config()
c.Username = "twitter"
c.Limit = 20
c.Store_object = True
c.Media = True

##scrap the user favourites
twint.run.Favorites(c)

#store the image url of each tweet into a list if theres an image
imagesURL = [i.photos for i in twint.output.tweets_list if i.photos]

print("DOWNLOADING IMAGES!!")
downloadImages(imagesURL, 'path')


