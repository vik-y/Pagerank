from BeautifulSoup import BeautifulSoup
from multiprocessing import Pool
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
count =0
search_string = raw_input('Enter search string:')
web_address = raw_input('Enter web address')
while(count<1000):
    print count
    #I just look through the first 1000 results
    if(count==0):
        r = opener.open("http://www.google.com/search?q="+search_string);
    else:
        r = opener.open("http://www.google.com/search?q="+search_string+"&start="+str(count));

    html = r.read()

    html=BeautifulSoup(html);

    results = html.findAll('h3', {'class':'r'})
    #The class which contains the search result,

    for val in results:
        signal= 0
        try:
            #Getting the url out of the search results
            #print val.next.attrs[0][1].split('//')[1]+' Rank '+str(rank_count)
            zense = str(val.next.attrs[0][1].split('//')[1].split('/')[0])
            #print zense
            if(zense==web_address or zense==web_address[4:]):
                print 'Rank of "'+web_address+'" for search string "'+search_string+'" is '+str(rank_count)
                signal=1
            rank_count+=1

        except:
            error = 'error'

        if(signal==1):
            break
    if(signal==1):
        break
    count+=10
