"""
dumpimages.py
Downloads all the images on the supplied URL, and saves them to /test/

Usage:
python dumpimages.py http://example.com/
"""

from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys

def main(url):
    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url))
    parsed = list(urlparse.urlparse(url))
    
    for image in soup.findAll("img"):
        print "Image: %(src)s" % image
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join("/test/", filename)
        urlretrieve(urlparse.urlunparse(parsed), outpath)

if __name__ == "__main__":
    url = sys.argv[-1]
    if not url.lower().startswith("http"):
        print "usage: python dumpimages.py http://example.com"
        sys.exit(-1)
    main(url)
