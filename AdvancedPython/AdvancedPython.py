# from collections import Counter
#
# mylist = [1,1,1,1,2,2,2,3,3,3,3,3,3,3]
# print(Counter(mylist))
#
# mylist = ['a','a',10,10]
# print(Counter(mylist))
# from Demos.win32cred_demo import pwd

# f = open("practice.txt","w+")
# f.write("This is a text string")
# f.close()
#
# import os
#
# print(os.getcwd())
# print(os.listdir('C:\\Users'))

# import shutil
# #
# # shutil.move('practice.txt','C:\\Users')

# import send2trash

# import datetime
# #
# # mytime = datetime.time()
# # print(mytime)
# #
# # today = datetime.date.today()
# # print(today)
# # print(today.ctime())
# #
# # from datetime import datetime
# # mydatetime = datetime(2020,10,3,14,20,1)
# # print(mydatetime)

# import math
# print(math.floor(4.222))
#
# print(round(3.5))
# print(math.pi)

# import requests
#
# result = requests.get("http://www.example.com")
#
# # print(result.text)
#
# import bs4
#
# soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup.select("title"))

# ###################### $$$ WEB SCARPING IMAGES $$$$ #######################

# import requests
# # import bs4
# #
# #
# # res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# #
# # soup = bs4.BeautifulSoup(res.text,'lxml')
# #
# # image_info = soup.select('.thumbimage')
# #
# # computer = image_info[0]
# #
# # print(computer['src'])
# #
# # image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")
# #
# # f = open("my_newFile_name.jpg",'wb')
# # f.write(image_link.content)
# # f.close()

# import requests
# import bs4
#
#
# base_url = "http://books.toscrape.com/catalogue/page-{}.html"
#
# res = requests.get(base_url.format(1))
#
# soup = bs4.BeautifulSoup(res.text,"lxml")
#
# # print(len(soup.select(".product_pod")))


import requests
import bs4

# res = requests.get("http://quotes.toscrape.com/")
# # print(res.text)
#
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# # print(soup.select(".author"))

# authors = set()
#
# for name in soup.select(".author"):
#     authors.add(name.text)
#
# print(authors)
#
# quotes = []
#
# for quote in soup.select(".text"):
#     quotes.append(quote.text)
#
# print(quotes)
#
# for item in soup.select(".tag-item"):
#     print(item.text)

url = "http://quotes.toscrape.com/page/"

# ###### EASY METHOD #################
# authors = []
#
# for page in range(1, 10):
#     page_url = url+str(page)
#     res = requests.get(page_url)
#     soup = bs4.BeautifulSoup(res.text,"lxml")
#
#     for name in soup.select(".author"):
#         authors.append(name.text)
#
# print(authors)

# ##################################### Dynamic Method ####################################
page_still_valid = True
authors = set()
page = 1

while page_still_valid:
    page_url = url+str(page)

    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break
    else:
        soup = bs4.BeautifulSoup(res.text,"lxml")

        for name in soup.select(".author"):
            authors.add(name.text)

        page = page + 1

print(authors)
























