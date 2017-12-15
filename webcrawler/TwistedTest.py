import requests
import datetime
import time
from scrapy.selector import Selector

import aiohttp
import asyncio
import async_timeout

url1 = "https://geizhals.de/?cat=acamobjo&xf=8219_Nikon+F"
url2 = "http://quotes.toscrape.com/page/1/"
url3 = "https://geizhals.de/nikon-af-p-dx-18-55mm-3-5-5-6g-schwarz-jaa827da-a1375460.html?hloc=at&hloc=de&hloc=pl&hloc=uk&hloc=eu"

def get_requests_time(url):
    start = datetime.datetime.now()
    response = requests.get(url)
    print(datetime.datetime.now() - start)
    return response

async def aio_fetch(session, url):
    start = datetime.datetime.now()
    #print(datetime.datetime.now())
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            result = await response.text()
            #print(datetime.datetime.now() - start)
            return result

async def get_aio_time(url, session):
    #async with aiohttp.ClientSession() as session:
    i = 0
    while(i < 1):
        html = await aio_fetch(session, url)
        i = i + 1
    response = html
    #print(type(response))
    #get_title_from_body(response)
    return response

def get_title_from_body(body):
    text = Selector(text=body).xpath('//title').extract()
    print(text)

def get_title(response):
    text = Selector(response=response).xpath('//title').extract()
    print(text)

session = aiohttp.ClientSession()
loop = asyncio.get_event_loop()
#loop.close()
i = 0
start = datetime.datetime.now()
while(i < 20):
    #print("Next cycle: " + str(datetime.datetime.now()))
    loop.run_until_complete(get_aio_time(url2, session)) 
    #time.sleep(7)
    i = i +1
print(datetime.datetime.now() - start)





import asyncio
import concurrent.futures
import requests

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                url2
            )
            for i in range(20)
        ]
        for response in await asyncio.gather(*futures):
            pass
            #get_title(response)

#start = datetime.datetime.now()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#print(datetime.datetime.now() - start)

