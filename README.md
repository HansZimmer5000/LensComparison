# LensComparison

## Overview
This project is about comparing DSLR Lenses from every brand and hopefully from every timeline.
With all necessary data without the price.

Just saw that there are complete databases for all lenses. 
For example the one from [Photographylife](https://photographylife.com/lenses).

So I guess from now on its just about practice.
Maybe I will find something new to add in my database.

### Attributes of each Lens
Each Entry has:

Entry                 Description of data (example)
1. Full Lens Name-----"Nikon 8-15mm 1:3.5-4.5E ED AF-S VR"
2. Focal Length Start--8mm
3. Focal Length End---15mm
4. Apeture Start-------3.5
5. Apeture End--------4.5
6. Filtersize------------77mm 
7. Magnification------1:4
8. Minimal Focus------0.2m
9. Mount--------------Nikon F
10. Sensor--------------APS-C /Kleinbild
11. Weight-------------350g
12. Size-----------------141x66mm (Diagram x Length) 



## Task List
- [ ] \(Must-Have)----(Never done) Create UML graphs and keep them updated
- [x] \(Must-Have)----Complete README file
- [x] \(Must-Have)----Got all necessary data from the most lenses
- [x] \(Must-Have)----Made a nice GUI for filtering and comparing the lenses (perhaps something like on "geizhals.de") 
- [x] \(Must-Have)----RawData will be shown in the Result Table, if they match the selected / active filters.
- [ ] \(Should-Have)--Create or find Key, so Data about the same lens comes together and so doesn`t creates multiple entries.
- [ ] \(Should-Have)--Got all necessary data from all lenses
- [ ] \(Should-Have)--Data of Autofocus (AF,AF-S,MF) (Not finished yet)
- [x] \(Should-Have)--Data of Vibration Reduction
- [x] \(Should-Have)--Data of Brand
- [ ] \(Should-Have)--A Sheet with a Table where you can compare (from the ResultTable) selected lenses.
- [ ] \(NiceTo-Have)--Move from Excel to a real database (e.g. Wide-Column?)
- [ ] \(NiceTo-Have)--Complete standalone program.
- [ ] \(NiceTo-Have)--When Selecting a certain mount, show also the lenses compatible with an adapter.
- [ ] \(NiceTo-Have)--Sheet with a Table with alle the lenses someone ownes, to see how much you can do with them and if you really need a new lens.
- [ ] \(NiceTo-Have)--Not only Nikon F Lenses and Nikon F compatible lenses, but all Lenses every made.

## Motivation
I really enjoy comparing all the lenses out there.
But on "geizhals.de" you just can compare all lenses which are in stock at the moment.
So all of the good old glas and perhaps one or the other pearl is missing in that list.
I didn`t find such a list, so here I will build my own. 

Also I want to practice how to document a project well so everybody could understand it.

## Code Example
Example from Webcrawler/StartCrawling.py (total file except Comments and Imports):
```
def start_spider_within_python():
    custom_settings = {
        `DOWNLOAD_DELAY`: 7,
	`RANDOMIZE_DOWNLOAD_DELAY`: False, #from 0.5*DELAY till 1.5*DELAY
	`COOKIES_ENABLED`: False
    }
```
`DOWNLOAD_DELAY` was set to 7 (seconds). Faster will lead to a ban from Geizhals.de
The other two settings were set to perhaps avoid a ban.
```
    process = CrawlerProcess(custom_settings)
    process.crawl(LensSpider)
    process.start() 
```
I use `scrapy.crawler.CrawlerProcess` to set the settings and set our Spider class (LensSpider).
We start the crawling with `process.start()`
```
if __name__ == "__main__":
	RawData.clean_rawdata_file_and_write_titles()
	start_spider_within_python()
```
So, if its not imported first it will wipe out any data in the WebCrawler/rawData.csv and then start the crawling which will fill the file.

## Installation
1. To see or edit the UML diagrams go to [draw.io](https://draw.io).
2. To see or edit the Excel sheet, you will need Microsoft Excel, I use Office 365.
3. Python is used in Version 3.6.1
4. Run the WebCrawler with `python StartCrawling.py` in the WebCrawler directory, but beware! WebCrawler/RawData.csv will be wiped clean of data! (see the Code Example).

Following modules are imported overall:
```
from scrapy.crawler import CrawlerProcess
from glob import glob
import unittest
import scrapy
import os
```

## Tests
To run all the python Tests at once run the "testall.py" file with `python testall.py` in the WebCrawler directory.
Testclasses contains:
-   setUp
-   tearDown
-   The test functions with one Assertion each
-   Sample Data is from the file "GhExamples.py"
-   uses the built-in python unittests 

Following Code is from "GhAdapterTestsuite.py":
```
    def test_pos_get_all_attributes_with_everything1(self):
```
Functions start with "test" (unittests module requires it) then "pos" as a positive test.
"get_all_attributes" the actually function which is being tested and "with_everything1", info about the input data.
In this case has the input all necessary Info and because there are several like that, its uses the first variation of the that kind of data.
```        
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
```
Set the input for the upcoming function call.
```
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)
```
Actually do the call.
```
        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1,result_dict)
```
Assert.

## Contributers
If you want to join write me a message on Github.