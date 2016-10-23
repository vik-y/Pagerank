'''
Page Rank 
Author - Vikas Yadav
Helps you to find your exact rank on Google based on your search string.
NOTE: Region Specific, results based on google.co.in region
'''
from BeautifulSoup import BeautifulSoup

import requests, re, threading, time, logging

#Browser Initialization ends here

logging.basicConfig(filename="example.log", format='%(levelname)s:%(message)s', level=logging.DEBUG)


rank_count = 1

search_string = raw_input("Enter the search string:\n") #The string which you want to search for
web_address = raw_input("Enter the url which you are looking for:\n") #Your website address

def search(query, website, count):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    if (count == 0):
        r = requests.get("http://encrypted.google.com/search?q=" + query, headers=headers);
    else:
        r = requests.get("http://encrypted.google.com/search?q=" + query + "&start=" + str(count), headers=headers);

    html = r.text
    #print html

    pattern = '<div class="g">(.*?)</div>'
    results = re.finditer(pattern, html)

    rank = count+1
    for result in results:
        temp = result.groups()[0]
        url = re.search("https?://(.*?)/", temp)

        if url:
            logging.debug(url.group(1))
            if url.group(1)==website:
                print "Website Found. Rank", rank
                break
        rank += 1

# TODO: Multithread it properly to prevent google captcha.
for i in range(0, 5):
    # Currently searching only 5 pages.
    t = threading.Thread(target=search, args=(search_string, web_address, i*10,))
    t.start()
    time.sleep(1)
    
