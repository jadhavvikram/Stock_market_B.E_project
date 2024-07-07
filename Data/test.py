import base64
import io
import urllib
import requests
import PIL
import PIL.Image
from matplotlib import pylab
from pylab import *
from textblob import TextBlob
from bs4 import BeautifulSoup

def news_fetch():
    search = "RELIANCE"
    def percentage(part, whole):
        return 100 * float(part) / float(whole)

    url = 'https://www.bing.com/news/search?q=' + search + '&qs=n&form=NWRFSH'

    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    page = requests.get(url, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    noOfSearch = len(soup.findAll('a', {'class': 'title'}))
    if noOfSearch > 10:
        noOfSearch = 10
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    news_dir = {}

    for x in range(noOfSearch):
        print(len(soup.findAll('a', {'class': 'title'})))
        title = soup.findAll('a', {'class': 'title'})[x]
        analysis = TextBlob(title.text)
        source = soup.findAll('div', {'class': 'source'})[x]
        news_dir[title.text] = source.text
        news_url = soup.findAll('a', href=True)[x]

        polarity += analysis.sentiment.polarity

        if analysis.sentiment.polarity == 0.000:
            neutral += 1

        elif analysis.sentiment.polarity < 0.000:
            negative += 1

        elif analysis.sentiment.polarity > 0.000:
            positive += 1

    positive = percentage(positive, noOfSearch)
    negative = percentage(negative, noOfSearch)
    neutral = percentage(neutral, noOfSearch)

    if polarity == 0:
        news_feedback = 'Hold'
    elif polarity < 0.000:
        news_feedback = 'Sell'
    elif polarity > 0.000:
        news_feedback = 'Buy'

    labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]',
                'Neutral [' + str(neutral) + '%]']
    sizes = [positive, negative, neutral]
    colors = ['lightblue', 'red', '#ffc107c2']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best", prop={'size': 6})
    plt.title('Latest News Analysis ')
    plt.axis('equal')
    plt.tight_layout()
    buffer_a = io.BytesIO()
    canvas_a = pylab.get_current_fig_manager().canvas
    canvas_a.draw()
    pil_image_a = PIL.Image.frombytes("RGB", canvas_a.get_width_height(), canvas_a.tostring_rgb())
    pil_image_a.save(buffer_a, "PNG")
    buffer_a.seek(0)
    string_a = base64.b64encode(buffer_a.read())
    news_feed = 'data:image/png;base64,' + urllib.parse.quote(string_a)
    pylab.close()

    return news_feed, news_dir, news_feedback, news_url

news = news_fetch()
print(news[3])
