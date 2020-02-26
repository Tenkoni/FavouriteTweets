import twint

##Configuring twint to scrap what we want
c = twint.Config()
c.Username = "twitter"
c.Limit = 20
c.Store_object = True
c.Media = True

##scrap the user favourites
twint.run.Favorites(c)

#store the image url of each tweet into a list
imagesURL = [i.photos for i in twint.output.tweets_list]

