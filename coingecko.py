from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq







url ='https://www.tradingview.com/markets/cryptocurrencies/prices-all/'

#get the html code
uClient = uReq(url)
page_html = uClient.read()
uClient.close
print(">Page Grabed")


#parse it
page_soup = soup(page_html,"html.parser")
print(">>Page Parsed")

html_table = page_soup.findAll("table")#table of crypto

crypto_table = html_table[0]
crypto_info = crypto_table.findAll("tr")

csvfile = "crypto.csv"
try:
    fil = open(csvfile,"w")
    header = "name,marketcap,price,pricechange\n"
    fil.write(header)

    for i in range(1,len(crypto_info)):
        crypto_name = crypto_info[i].findAll("a",{'class':'tv-screener__symbol'})[0].text
        crypto_mrktcap = crypto_info[i].findAll("td",{'class':'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big'})[0].text
        crypto_price = float(crypto_info[i].findAll("td",{'class':'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big'})[2].text) 
        crypto_prcChange =float(crypto_info[i].findAll("td")[-1].text.replace('%',''))

        info = f"{crypto_name},{crypto_mrktcap},{crypto_price},{crypto_prcChange}\n"
    
        fil.write(info)

    print(">>>Finished")
except Exception as e :
    print(e)
finally:
    fil.close()


