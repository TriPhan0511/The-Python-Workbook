from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# #
# Parsing HTML using BeautifulSoup
#

# Sample:
# We will use urllib to read the page and then use BeautifulSoup
# to extract the href attributes from the anchor (a) tags.

# The program prompts for a web address, then opens the web page, reads the data
# and passes the data to the BeautifulSoup parser, and then retrieves all of the
# anchor tags and prints out the href attribute for each tag.


# Get context (Ignore SSL certificate errors)
def get_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


# Get all specific tags within an url
def get_tags(url, tag_type='a'):
    # Ignore SSL certificate errors
    ctx = get_context()
    # Open the web page, read the data
    # and pass the data to the Beautiful parser
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the tags
    tags = soup(tag_type)

    return tags


# Get urls in anchor tags
def get_links(url):
    tags = get_tags(url, 'a')
    result = []
    for tag in tags:
        result.append(tag.get('href', None))
    return result

# Result:
# https://www.python.org/
# download.html
# https://docs.python.org/3.13/
# https://docs.python.org/3.12/
# #
# ...


# Pull out various parts of each tag
def pull_out_various_parts(url):
    tags = get_tags(url, 'a')
    for tag in tags:
        print(f"TAG: {tag}")
        print(f"URL: {tag.get('href', None)}")
        if len(tag.contents) > 0:
            print(f"Contents: {tag.contents[0]}")
        print(f"Attributes: {tag.attrs}")
        print('----------------------------------')

# Output:
# TAG: <a class="nav-logo" href="https://www.python.org/">
# <img alt="Logo" src="_static/py.svg"/>
# </a>
# URL: https://www.python.org/
# Contents:

# Attributes: {'href': 'https://www.python.org/', 'class': ['nav-logo']}
# class: ['nav-logo']
# ----------------------------------
# TAG: <a href="download.html">Download these documents</a>
# URL: download.html
# Contents: Download these documents
# Attributes: {'href': 'download.html'}
# ----------------------------------
# ...


def main():
    # url = input('Enter - ')
    url = 'https://docs.python.org'

    links = get_links(url)
    if len(links) > 0:
        for link in links:
            print(link)

    # pull_out_various_parts(url)


if __name__ == '__main__':
    main()
