import pyshorteners
import pyperclip

def url_shortener(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)


url = input("Enter url: ")
print(f"The short url is: {url_shortener(url)}")
pyperclip.copy(url_shortener(url))