cook_county_address_scraper
=======================

Scrapes the Cook County Property Tax Info portal's Address Results page and dumps data in a more useful format. Give it a CSV file with three columns (but don't name them): street number, street direction, street name (street name can include the suffix, i.e. "ave"). The address results page gives you a list of all the PINs (Property Index Numbers) at that address. Use the cook_county_pin_scraper to scrape the PIN pages. 

Setup and Running
-----------------

```python
# Install scrapy (preferably in a virtual environment)
mkvirtualenv --no-site-packages cook_county_address_scraper
pip install scrapy
# Clone the git repo
git clone git@github.com:stevevance/cook_county_address_scraper.git
# Update the list of addresses you want to scrape by changing the file on line 13 in cook_county_address_scraper/spiders/dmoz.py
# Run the scraper
cd cook_county_address_scraper
scrapy crawl propertyaddress -o addresses.json -t jsonlines -L INFO
# The output will be in addresses.json
```
You can set the crawl rate in cook_county_address_scraper/settings.py: DOWNLOAD_DELAY = 0.05 (in ms/milliseconds)