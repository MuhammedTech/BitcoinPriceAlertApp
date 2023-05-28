from bs4 import BeautifulSoup
import requests
import smtplib
import time



price = 0


def get_price():
    global price
    url = ('https://www.google.com/search?sxsrf=ALeKk00s9WPCj3j86zdRDrWQWgp_2aKsMQ%3A1585686671872&source=hp&ei=j6iDXpb2MvXY9AOdt4zwAg&q=bitcoin+price&oq=bitcoin&gs_lcp=CgZwc3ktYWIQAxgAMgoIABDLARBGEIICMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgcIIxDqAhAnOgIIADoECCMQJzoHCAAQRhCCAlDHG1iSTGCPVWgHcAB4AIABoAKIAZQOkgEGMy4xMC4xmAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab')
    headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    div = soup.find_all('div',{'class':'dDoNo vk_bk gsrt'})[0].find('span').text.strip()
    price = div
    while True:
          if price < str(5.000):
             time.sleep(60 * 120) #it will check for bitcoin price every 2 hours
             print(price)
             send_email()
             break


def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alimbetov.mo@gmail.com','password')
    subject = 'Bitcoin gone down'
    body = price
    msg = f"Subject:{subject}\n\nCurrent bitcoin price is: ${body}"
    server.sendmail('alimbetov.mo@gmail.com','alimbetov.mu@gmail.com',msg)
    print('Message has been sent')
    server.quit()


get_price()
