import requests

def httpRequest(method, url, **kwargs):
    try:
        kwargs.setdefault('allow_redirects', True)
        resp = requests.request(method, url, **kwargs)
        resp.raise_for_status()
        return resp
    except:
        return None


def httpGet(url, params=None, **kwargs):
    return httpRequest('get', url, params=params, **kwargs)

def httpHead(url, **kwargs):
    return httpRequest('HEAD', url, **kwargs)

def httpPost(url, data=None, json=None, **kwargs):
    return httpRequest('post', url, data=data, json=json, **kwargs)

def httpPut(url, data=None, **kwargs):
    return httpRequest('put', url, data=data, **kwargs)

def httpPatch(url, data=None, **kwargs):
    return httpRequest('patch', url,  data=data, **kwargs)

def httpDelete(url, **kwargs):
    return httpRequest('delete', url, **kwargs)
    
def httpOptions(url, **kwargs):
    return httpRequest('options', url, **kwargs)