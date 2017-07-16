#!/usr/bin/local/python3


from urllib import request
import urllib
from bs4 import BeautifulSoup
import os




def scrape (page_read):
    img_list = []
    img_count = 0
    soup = BeautifulSoup(page_read, 'html.parser')
    for img in soup.find_all('img'):
        img_list.append(img.get('src'))
        img_count += 1
        img


    if(img_count > 1):
        print("Found " + str(img_count) + " images.")
        save_imgs(img_list)
    if(img_count == 1):
        print("Found " +str(img_count) + " image.")
        save_imgs(img_list)

    elif(img_count < 1):
        print("No images found on this webpage.")



def save_imgs (img_list):
    os.mkdir('scraper_files', 0o777,)
    os.chdir('scraper_files')
    id = 1
    print("Scraping images", end='')
    for img in img_list:
        print(".", end='')
        name = "image_" + str(id)
        urllib.request.urlretrieve(img, name)
        id+=1
    print("[DONE]")




if __name__ == '__main__':
    go = True
    while go == True:
        try:
            page = input("Please provide the link to the webpage you would like to scrape ")
            if page[:6] != 'https//':
                page = 'https://' + page
            req = urllib.request.Request(page, headers)
            with urllib.request.urlopen(req) as opened_page:
                opened_page = opened_page.read()
            scrape(opened_page)
            go = False
        except(urllib.request.URLError) as e:
            print(e)
