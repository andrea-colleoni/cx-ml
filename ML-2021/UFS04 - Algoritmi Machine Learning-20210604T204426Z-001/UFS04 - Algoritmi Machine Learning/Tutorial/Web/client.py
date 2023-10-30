import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen('http://www.libero.it')
html = response.read()

print(html)