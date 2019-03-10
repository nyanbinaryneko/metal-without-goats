# Metal without Goats: A dataviz and Twitter bot project
## About
### Twitter bot
The goal of this project is to create realistic band names not containing the word "goat", as a Metal Archives style entry.

### Dataviz
Metal Archives has a lot of information about a lot of bands. It is probably the most comprehensive source
of metal information on the internet. using [this scraper](https://github.com/alikoneko/metal-scraper), I was able to get
a decently sized scrape of MA back in September. 

#### Goals for Dataviz:
1. find connection between location and genre
2. connections between name, lyrical themes, and genre.


# Quick Start:

1. run `pipenv install`
2. `python cli.py -i ./json/fixed_bands.json -m create`


