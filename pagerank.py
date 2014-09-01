'''
Page Rank 
Author - Vikas Yadav
Helpes you to find your exact rank on Google based on your search string.
NOTE: Region Specific, results based on google.co.in region
'''
from BeautifulSoup import BeautifulSoup

import cookielib
import mechanize

#Brower Initialization Starts here

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False) 
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#Browser Initialization ends here

br.addheaders = [('User-agent', 'Firefox'), ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
#added headers to the request

'''
Note: All this could have been done by just using urllib2 and running that script will also reduce your memory requirements. 
I generally use mechanize library because it makes things easier in the long run.
-> Mechanize Library supports storage of cookies which you can send along with your headers
    Now when I talk about cookies - Yes we can maintain sessions :D that makes scraping easier than ever.
'''

rank_count = 1

search_string = raw_input("Enter the search string:\n") #The string which you want to search for
web_address = raw_input("Enter your web address (eg www.zense.co.in):\n") #Your website address

count = 0
while(count<1000):
    #I just look through the first 1000 results
    if(count==0):
        r = br.open("http://www.google.com/search?q="+search_string);
    else:
        r = br.open("http://www.google.com/search?q="+search_string+"&start="+str(count));

    html = r.read()
    
    html=BeautifulSoup(html);
    
    results = html.findAll('h3', {'class':'r'})
    #The class which contains the search result, 
    
    for val in results:
        signal= 0
        try:
            #Getting the url out of the search results
            print val.next.attrs[0][1].split('//')[1]+' Rank '+str(rank_count)
            zense = str(val.next.attrs[0][1].split('//')[1].split('/')[0])
            print zense
            if(zense==web_address or zense==web_address[4:]):
                print 'Rank of Zense is '+str(rank_count)
                signal=1
            rank_count+=1
           
        except:
            error = 'error'
        
        if(signal==1):
            break
    if(signal==1):
        break
    count+=10
    
'''
The code is not optimized, if you are willing to contribute or want to do the same thing with urllib2 then you are 
welcome, kindly do the same and send me a pull request. :) 
'''

    
    

        
    

    
    
