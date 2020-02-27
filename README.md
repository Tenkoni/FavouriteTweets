# FavouriteTweets

A script to download a user's liked images from Twitter.

## Installation

Install the dependencies with [pip](https://pip.pypa.io/en/stable/).

```bash
pip install twint
```
```bash
pip install requests
```
```bash
pip install progressbar
```
Clone the repository to your directory.
```bash
git clone https://github.com/Tenkoni/FavouriteTweets.git
```


## Usage
``` 
python3 tweetImage.py username [-h] [-n NUMBER] [-p PATH]
``` 
``` 
positional arguments:
  username              Username to download from

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Max number of tweets to save, up to 3200, each tweet
                        may contain multiple images
  -p PATH, --path PATH  Path to save images at

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)