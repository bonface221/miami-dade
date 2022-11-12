# Tried scraping using BeautifulSoup and Requests but they were not able to do scrape well 
# Though they were able to login and send requests
# This file is not to be used ...!!!!!!!!!!!!!

import requests
from bs4 import BeautifulSoup as bs


loginurl = 'https://www2.miami-dadeclerk.com/PremierServices/login.aspx'

account_url = 'https://www2.miami-dadeclerk.com/PremierServices/accountmanager.aspx'

official_record_url = 'https://onlineservices.miami-dadeclerk.com/officialrecords/StandardSearch.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0',
    'Connection': 'keep-alive'
}


loginPayload = {
    'username': 'hirolex',
    'password': 'hirolex231',
    'ctl00$cphPage$btnLogin': 'Login'
}
loginPayload2 = {
    'ctl00$cphPage$txtUserName': 'hirolex',
    'ctl00$cphPage$txtPassword': 'hirolex231',
    'ctl00$cphPage$btnLogin': 'Login',
    'ctl00$cphPage$registrationEmail': ''}

official_record_payload = {
    '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$btnNameSearch',
    'ctl00$ContentPlaceHolder1$hfTab': '',
    'ctl00$ContentPlaceHolder1$pfirst_party': '',
    'ctl00$ContentPlaceHolder1$prec_date_from': '11/01/2022',
    'ctl00$ContentPlaceHolder1$prec_date_to': '11/03/2022',
    'ctl00$ContentPlaceHolder1$pdoc_type': 'LIS',
    'ctl00$ContentPlaceHolder1$pcfn_year': '',
    'ctl00$ContentPlaceHolder1$pcfn_seq': '',
    'ctl00$ContentPlaceHolder1$prec_book': '',
    'ctl00$ContentPlaceHolder1$prec_page': '',
    'ctl00$ContentPlaceHolder1$prec_booktype': 'O',
    'ctl00$ContentPlaceHolder1$pplat_book': '',
    'ctl00$ContentPlaceHolder1$pplat_page': '',
    'ctl00$ContentPlaceHolder1$pblock_no': '',
    'ctl00$ContentPlaceHolder1$party_name': ''
}


def scrapper():
    with requests.Session() as s:
        r = s.get(loginurl, headers=headers)
        soup = bs(r.content, 'html.parser')

        loginPayload2['__VIEWSTATE'] = soup.find(
            'input', attrs={'id': '__VIEWSTATE'})['value']
        loginPayload2['__VIEWSTATEGENERATOR'] = soup.find(
            'input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
        loginPayload2['__EVENTVALIDATION'] = soup.find(
            'input', attrs={'id': '__EVENTVALIDATION'})['value']

        s.post(loginurl,data=loginPayload2,headers=headers)

        # debugger
        print('''
        successfully logged in
        ```````````````
        ```````````````
        ``````````````
        ```````````````
        `````````````
        ''')

        # r2= s.get(official_record_url,headers=headers)
        # soup2 = bs(r2.content,'html.parser')

       
        # official_record_payload['__EVENTARGUMENT'] = soup2.find(
        #     'input', attrs={'id': '__EVENTARGUMENT'})['value']
        # official_record_payload['__VIEWSTATE'] = soup2.find(
        #     'input', attrs={'id': '__VIEWSTATE'})['value']
        # official_record_payload['__VIEWSTATEGENERATOR'] = soup2.find(
        #     'input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
        # official_record_payload['__EVENTVALIDATION'] = soup.find(
        #     'input', attrs={'id': '__EVENTVALIDATION'})['value']

        # print(official_record_payload2)
        
        # r3 = s.get(account_url, headers=headers)
        # soup3 = bs(r3.content,'html.parser')
        # print(soup3.prettify())

        # print(official_record_payload)
        
        r3 = s.post(official_record_url,
                    data=official_record_payload, headers=headers)
        soup3 = bs(r3.content,'html.parser')
        print(soup3.prettify())
        




