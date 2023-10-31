# pythonRetrieveInternalSiteLinks
## 🔎HTML Finder

### Description

HTML Finder is a Python script that crawls websites and saves internal links ending with .html to an Excel file with multiple sheets.  

### Requirements

- Python 3.x
- Required libraries:
  - BeautifulSoup
  - openpyxl
  - requests
  
### Use

1- Clone this repository to your local machine:  
```git clone https://github.com/AlbiaqueMonica/pythonRetrieveInternalSiteLinks.git```

2- Change to the project directory:   
```cd pythonRetrieveInternalSiteLinks```

3- Install the required libraries:  
```pip install beautifulsoup4 requests openpyxl```

or  

```pip install -r requirements.txt```

#### Running the Script

To execute the script, open a terminal or command prompt and navigate to the script's directory.     
There are two ways to run the script:  
👌 Passing the URLs of the sites to check as an argument.  
👌 Passing a text file containing the list of sites as an argument.  
 
- Crawling Websites with Base URLs    
Provide base URLs directly as arguments to the script.  
This will crawl the specified websites and create separate sheets in the Excel file for each site:   
```python HTML_finder.py https://example.com https://anotherexample.com```    

- Using a Sites File     
Specify a text file containing a list of websites to crawl using the --sites_file option.
Make sure to format your sites file with one URL per line.    
```python HTML_finder.py --sites_file sites.txt```

#### Example Sites File

Included in this directory is an example sites file named "sites.txt." You can use this file as a template for creating your own sites list. Simply edit "sites.txt" to add your desired website URLs, with one URL per line.

#### Output  
The script will create an Excel file named "Results.xlsx" in the same directory, which will contain the collected data from the websites.  


