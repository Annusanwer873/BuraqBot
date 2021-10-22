# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import json
from flask import make_response
from SendEmail.sendEmail import EmailSender
from email_templates import template_reader
from Webscrapping.webscrape_buraq import DataCollection
import os

IMG_FOLDER = os.path.join('static', 'images')
CSV_FOLDER = os.path.join('static', 'CSVs')
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER
app.config['CSV_FOLDER'] = CSV_FOLDER


@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    intent = result.get("intent").get('displayName')

    if (intent == 'Get Promotional Emails'):
        parameters = result.get("parameters")
        cust_name = parameters.get("name")
        cust_email = parameters.get("email")
        course_no = "1"
        course_name = 'DataScienceMasters'
        email_sender = EmailSender()
        template = template_reader.TemplateReader()
        email_message = template.read_course_template(course_name)
        email_sender.send_email_to_student(cust_email, email_message)

        fulfillmentText = "I have sent the brochure and a promocode valid for 10th June 2021. You can get 20% flat discount through this promocode. Enter 1 for main menu and 0 to exit the chat"

        return {
            "fulfillmentText": fulfillmentText
        }
    elif (intent == 'Contact Customer Support'):

        parameters = result.get("parameters")
        cust_name = parameters.get("name")
        cust_contactnumber = parameters.get("number")
        #converted_cust_num = str(cust_contactnumber)

        cust_email = 'affanaminn@gmail.com'

        email_sender = EmailSender()
        template = template_reader.TemplateReader()
        course_name = 'DS'
        email_message = template.read_course_template(course_name)
        #        email_sender.send_email_to_student(cust_email, email_message)
        email_sender.send_email_to_support(cust_name,cust_contactnumber,email_message )

        fulfillmentText = "Your Number and Name has been sent to the support team via email, you will be contacted shortly, Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"

        return {
            "fulfillmentText": fulfillmentText
        }

    elif (intent == 'abaya'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/abaya")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Men’s T-Shirts'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/men-Tshirt")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Full sleeves t shirts'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/fullsleevesmen-Tshirt")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Men’s formal shirts'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Mensformalshirts")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Men’s Kameez Shalwar'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Menskurta")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'BOTTOMS'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/bottom")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Loafers'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Loafers")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Formal Shoes'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/formal-shoes")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Boots'):
        str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/boots")

        fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
        return {
            "fulfillmentText": fulfillmentText}
    elif (intent == 'Lawn Collection'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/lawn-collection")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Embroidered Collection'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/EmbroideredCollection")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Winter Collection'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Wintercollection")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Pret Collection'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/PretCollection")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Western Style Kurti'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/WesternStyleKurti")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Bridals'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Bridals")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Face Care'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/facecare")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Face Cleansers'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/facecleansers")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Face Treatment'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/FaceTreatment")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Hair Care'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/haircare")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Bath & Shower'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Bath&Shower")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    elif (intent == 'Body'):
            str = "Please Proceed to our BuraqStore Recommendation engine through given link \n {link} \n Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            str2 = str.format(link="https://3da1-119-157-117-3.ngrok.io/Body")

            fulfillmentText = str2  # "You have selected , Enter 1 for main menu and 0 to exit the chat, Thanks. !!!"
            return {
                "fulfillmentText": fulfillmentText}
    else:
        return "nothing found"

@app.route('/',methods=['GET'])
def homePage():
	return render_template("index.html")


@app.route('/abaya', methods=("POST", "GET"))
def abaya():
    try:
        intent = 'abaya'
        search_string = 'ready-to-wear'
        cat = 'women'
        cat2 ='abaya'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/bottom', methods=("POST", "GET"))
def bottom():
    try:
        intent = 'BOTTOMS'
        search_string = 'bottoms'
        cat = 'women'
        cat2=''
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/men-Tshirt', methods=("POST", "GET"))
def mentshirt():
    try:
        intent = 'Men’s T-Shirts'
        search_string = 'western-wear'
        cat = 'men'
        cat2='mens-t-shirts'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/fullsleevesmen-Tshirt', methods=("POST", "GET"))
def fullsleevesmen():
    try:
        intent = 'Full sleeves t shirts'
        search_string = 'western-wear'
        cat = 'men'
        cat2='mens-t-shirts'
        cat3 ='full-sleeves-tees'

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Mensformalshirts', methods=("POST", "GET"))
def Mensformalshirts():
    try:
        intent = 'Men’s formal shirts'
        search_string = 'western-wear'
        cat = 'men'
        cat2='formal-shirts'
        cat3 =''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Menskurta', methods=("POST", "GET"))
def Menskurta():
    try:
        intent = 'Men’s Kameez Shalwar'
        search_string = 'eastern-wear'
        cat = 'men'
        cat2='kurta-shalwar-pajama'
        cat3 =''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Loafers', methods=("POST", "GET"))
def loafers():
    try:
        intent = 'Loafers'
        search_string = 'shoes'
        cat = 'men'
        cat2='mens'
        cat3 ='loafers'

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/formal-shoes', methods=("POST", "GET"))
def formalshoes():
    try:
        intent = 'Formal Shoes'
        search_string = 'shoes'
        cat = 'men'
        cat2='mens'
        cat3 ='formal-shoes'

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/boots', methods=("POST", "GET"))
def boots():
    try:
        intent = 'Boots'
        search_string = 'shoes'
        cat = 'men'
        cat2='mens'
        cat3 ='boots'

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat, cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/lawn-collection', methods=("POST", "GET"))
def lawncollection():
    try:
        intent = 'Lawn Collection'
        search_string = 'unstitched'
        cat = 'women'
        cat2 ='lawn-collection'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/EmbroideredCollection', methods=("POST", "GET"))
def Embroidered():
    try:
        intent = 'Embroidered Collection'
        search_string = 'unstitched'
        cat = 'women'
        cat2 ='embroidered'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Wintercollection', methods=("POST", "GET"))
def wintercollection():
    try:
        intent = 'Winter Collection'
        search_string = 'unstitched'
        cat = 'women'
        cat2 ='winter-collection'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/PretCollection', methods=("POST", "GET"))
def PretCollection():
    try:
        intent = 'Pret Collection'
        search_string = 'ready-to-wear'
        cat = 'women'
        cat2 ='pret-collection'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/WesternStyleKurti', methods=("POST", "GET"))
def WesternStyleKurti():
    try:
        intent = 'Western Style Kurti'
        search_string = 'ready-to-wear'
        cat = 'women'
        cat2 ='pret-collection'
        cat3='western-style-kurti'

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Bridals', methods=("POST", "GET"))
def Bridals():
    try:
        intent = 'Bridals'
        search_string = 'bridals'
        cat = 'women'
        cat2 =''
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/facecare', methods=("POST", "GET"))
def facecare():
    try:
        intent = 'Face Care'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='face-care'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/facecleansers', methods=("POST", "GET"))
def facecleansers():
    try:
        intent = 'Face Cleansers'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='face-cleansers'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/FaceTreatment', methods=("POST", "GET"))
def facetreatment():
    try:
        intent = 'Face Treatment'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='face-treatment'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/haircare', methods=("POST", "GET"))
def haircare():
    try:
        intent = 'Hair Care'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='hair-care'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Bath&Shower', methods=("POST", "GET"))
def bathshower():
    try:
        intent = 'Bath & Shower'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='bath-shower'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")

@app.route('/Body', methods=("POST", "GET"))
def body():
    try:
        intent = 'Body'
        search_string = 'cosmetics'
        cat = 'beauty'
        cat2 ='body'
        cat3=''

        data_scrapper_buraq = DataCollection()
        buraq_Scrapped = data_scrapper_buraq.bur_Scraped(intent, search_string, cat,cat2,cat3)

        download_path = data_scrapper_buraq.save_as_dataframe(buraq_Scrapped, fileName=search_string.replace("+", "_"))

        return render_template('review.html',
                               tables=[buraq_Scrapped.to_html(classes='data')],  # pass the df as html
                               titles=buraq_Scrapped.columns.values,  # pass headers of each cols
                               search_string=search_string,  # pass the search string
                               download_csv=download_path  # pass the download path for csv
                               )

    except Exception as e:
        print(e)
        return render_template("404.html")




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run()
