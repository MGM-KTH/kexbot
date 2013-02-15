import urllib, urllib2

try:
    import json
except:
    import simplejson as json


API_URL = 'http://conceptnet5.media.mit.edu/data/5.1/'

def lookup(type, language, key, limit):
    url = API_URL + type + '/' + language + '/' + key + '?limit=5'
    return _get_json(url)

def search(query):
    return _get_json("search?"+query)

def assoc(word, filter, limit):
    url = API_URL + "c/en/" + word + "?filter=" + filter + "&limit=" + limit
    return _get_json(url)

'''
def old_get_json(*url_parts):
    url = API_URL + '/'.join(urllib2.quote(p) for p in url_parts) + '?limit=5'
    return json.loads(_get_url(url))
'''

def _get_json(url):
    print url
    conn = urllib2.urlopen(url)
    return json.loads(conn.read())
