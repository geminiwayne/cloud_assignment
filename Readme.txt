This system contains two parts: config.txt and crawling code
config.txt stores twitter application access
the format of config:
consumer_key
consumer_secret
access_token
access_secret
coordinates of city and
topic for historical_twitter
bounding of city
topic for new_twitter

crawling code:
twitter.py is main function to run this system.
filter.py is to filter duplicates by tweetid and identify gender by first name

And for this system,we creates many configs to use, though one config is better for distrited concept.