from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import os
IMG_FOLDER = os.path.join('static', 'images')
CSV_FOLDER = os.path.join('static', 'CSVs')

buraq_Scrapped=""

class CleanCache:

    def __init__(self, directory=None):
        self.clean_path = directory
        # only proceed if directory is not empty
        if os.listdir(self.clean_path) != list():
            # iterate over the files and remove each file
            files = os.listdir(self.clean_path)
            for fileName in files:
                print(fileName)
                os.remove(os.path.join(self.clean_path, fileName))
        print("cleaned!")

class DataCollection:
    def __init__(self):
        self.data = {
		"Name": list(),
		"Price": list(),
        "Link-For-Product": list(),
        }

    def get_final_data(self, commentbox=None):

         ### Link Of-Product Tags
       try:

            productlist = commentbox.find_all('li',{"class": "item"})
            for item in productlist:
                for link in item.find_all('a',{"class": "product-link"}):
                    self.data["Link-For-Product"].append(link['href'])

       except:
             self.data["Link-For-Product"].append('none')

       try:

            for item in productlist:
                for name in item.find_all('a',{"class": "product-link"}):
                    self.data["Name"].append(name['title'])

       except:
            self.data["Name"].append('none')

       try:
            hh=[]
            for item in productlist:
             for link2 in item.find_all('span', {"class": "price"}):
                 hh.append(link2.get_text().strip())

            for i, j in enumerate(hh):
                front, mid, end = j.partition(' ')
                self.data["Price"].append(front)

       except:
             self.data["Price"].append('0')


    def get_main_HTML(self, base_URL=None, cat = None , search_string=None,cat2= None,cat3=None):
        search_url = f"{base_URL}/product-category/{cat}/{search_string}/{cat2}/{cat3}"
        r= requests.get(search_url)
        return soup(r.content,'lxml')

    def get_data_dict(self):
        return self.data

    def save_as_dataframe(self, dataframe, fileName=None):
        csv_path = os.path.join(CSV_FOLDER, fileName)
        fileExtension = '.csv'
        final_path = f"{csv_path}{fileExtension}"
        # clean previous files -
        CleanCache(directory=CSV_FOLDER)
        # save new csv to the csv folder
        dataframe.to_csv(final_path, index=None)
        print("File saved successfully!!")
        return final_path
    


    def bur_Scraped(self,intent,search_string,cat,cat2,cat3):
        
        base_URL = 'https://buraqstore.com'
        search_string = search_string.replace(" ", "-")
        print('processing, Please wait')
        get_data = DataCollection()
        buraq_HTML = get_data.get_main_HTML(base_URL,cat,search_string,cat2,cat3)

        get_data.get_final_data(buraq_HTML)

        buraq_Scrapped = pd.DataFrame(get_data.get_data_dict())

        buraq_Scrapped = buraq_Scrapped.head(15)
        #print(buraq_Scrapped)

        # def fun(path):
        #     # returns the final component of a url
        #     f_url = os.path.basename(path)
        #
        #     # convert the url into link
        #     return '<a href="{}">{}</a>'.format(path, f_url)
        #
        # yayvo_Scrappeds = buraq_Scrapped.style.format({"Link-For-Product": fun})
        # print(yayvo_Scrappeds)

        return buraq_Scrapped
    
