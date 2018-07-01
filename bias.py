from google import google
from textblob import TextBlob
import texttable as tt
from time import sleep

def search(site, search):
    site = site
    search = search
    num_page = 3
    search_results = google.search("inurl:" + site + " intext:" + search, 3)
    search_results_list = []
    subjectivity_list = []
    polarity_list = []
    num = []
    number = 1

    for result in search_results:
        search_results = result.description
        search_results_list.append(search_results)

        analysis = TextBlob(search_results)
        subjectivity = analysis.sentiment.subjectivity
        subjectivity_list.append(subjectivity)
        polarity = analysis.sentiment.subjectivity
        polarity_list.append(polarity)
        number = number + 1
        num.append(number)
        sleep(5)

    tab = tt.Texttable()
    headings = ['Number','Results','Subjectivity', 'Polarity']
    tab.header(headings)

    for row in zip(num, search_results_list, subjectivity_list, polarity_list):
        tab.add_row(row)

    avg_subjectivity = (sum(subjectivity_list) / len(subjectivity_list))
    avg_polarity = (sum(polarity_list) / len(polarity_list))

    table = tab.draw()
    print site
    print search
    print table
    print (site + " average subjectivity: " + str(avg_subjectivity))
    print (site + " average polarity: " + str(avg_polarity))


search("newyorker", "trump")
sleep(10)
search("npr", "trump")
sleep(10)
search("cnn", "trump")
sleep(10)
search("foxnews", "trump")
sleep(10)
search("drudgereport", "trump")
sleep(10)
search("breitbart", "trump")
sleep(10)
