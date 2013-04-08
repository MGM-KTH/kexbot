import urllib, urllib2

try:
    import json
except:
    import simplejson as json


API_URL = 'http://conceptnet5.media.mit.edu/data/5.1/'

def lookup(word, absolute=False, limit=None):
    if word==None:
        print "a term must be specified"
        return "{}"
    if not limit == None:
        limit = "?limit="+str(limit)
    else:
        limit = ""
    if absolute:
        url = API_URL + word + limit
    else:
        url = API_URL + "c/en/" + word + limit
    return _get_json(url)

def search(absolute=False, rel=None, start=None, end=None, limit=None):

    if rel == None and start == None and end == None:
        print "atleast one argument must be specified"
        return "{}"

    if not rel == None:
        if not absolute:
            print rel
            rel = "/r/"+rel
        rel = "rel="+rel
    else:
        rel = ""

    if not start == None:
        if not absolute:
            start = "/c/en/"+start
        start = "start="+start
    else:
        start = ""

    if not end == None:
        if not absolute:
            end = "/c/en/"+end
        end = "end="+end
    else:
        end = ""

    if not limit == None:
        limit = "limit="+str(limit)
    else:
        limit = ""

    url = API_URL + "search?"+"&".join([rel,start,end,limit])
    return _get_json(url)

def assoc(absolute=False, word=None, filt=None, limit=None):
    if word == None:
        print "Word needs to be defined."
        return "{}"

    if not absolute:
        word = "/c/en/"+word

    if not filt == None:
        if not absolute:
            filt = "/c/en/"+filt
        filt = "filter=" + filt
    else:
        filt = ""

    if not limit == None:
        limit = "limit=" + str(limit)
    else:
        limit = ""

    url = API_URL + "assoc" + word + "?"+"&".join([filt,limit])
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
