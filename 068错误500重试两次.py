import urllib
import urllib.request

def downLoad(url, user_agent='wswp', num_retries=2):
    print('downloading:',url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers = headers)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('downloading error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return downLoad(url, user_agent, num_retries-1)
    return html
#downLoad('http://httpstat.us/500')
downLoad('https://www.meetup.com/')