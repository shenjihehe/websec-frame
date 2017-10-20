from urllib.parse import urlparse
import socket

def urlsplit(url):
    domain = url.split("?")[0]
    _url = url.split("?")[-1]
    pararm = {}
    for val in _url.split("&"):
        pararm[val.split("=")[0]] = val.split("=")[-1]

    #combine
    urls = []
    for val in pararm.values():
        new_url = domain + _url.replace(val,"my_Payload")
        urls.append(new_url)
    return urls

def gethostbyname(url):
    domain = urlparse(url)
    # domain.netloc
    if domain.netloc is None:
        return None
    ip = socket.gethostbyname(domain.netloc)
    return ip

