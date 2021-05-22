#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies
import os
import pandas as pd
import requests
import pymongo
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


#Splinter Set Up
executable_path = ChromeDriverManager().install()
executable_path
browser = Browser('chrome', executable_path=executable_path, headless=False)


# # NASA Mars News Scraping

# In[3]:


#Set up for NASA Mars News Scraping
mars_news_url = "https://redplanetscience.com/"
browser.visit(mars_news_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


#NASA Mars News Scraping for Latest News Title and Paragraph Text
mars_news_title = soup.find('div', class_='content_title').text
mars_news_paragraph = soup.find('div', class_='article_teaser_body').text


# In[5]:


#Display scraped Title & Paragraph Text
print(f'The Latest NASA Mars News Title: {mars_news_title}')
print(f'The Latests NASA Mars News Paragraph Text: {mars_news_paragraph}')


# # Featured Mars Image Scraping

# In[6]:


#Set up for JPL Featured Mars Image Scraping
jpl_url = "https://spaceimages-mars.com/"
browser.visit(jpl_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


#Use Splinter to find the Image URL for the current Featured Mars Image
image_url = soup.find('img', class_='headerimage fade-in')['src']
featured_image_url = f'{jpl_url}{image_url}'
print(featured_image_url)


# # Mars Facts Scraping

# In[8]:


#Set up for Mars Facts Scraping
facts_url = 'https://galaxyfacts-mars.com/'
facts_table = pd.read_html(facts_url)
facts_table


# In[9]:


mars_facts = facts_table[0]
mars_facts


# In[10]:


mars_facts = mars_facts.rename(columns=mars_facts.loc[0]).drop(mars_facts.index[0])
mars_facts


# In[11]:


mars_facts = mars_facts.rename(columns={'Mars - Earth Comparison': ''})
mars_facts


# In[12]:


mars_facts_table = mars_facts[['', 'Mars', 'Earth']].reset_index(drop=True)
mars_facts_table = mars_facts_table.set_index('')
mars_facts_table


# In[13]:


#Convert the formated DataFrame to a HTML table string
mars_facts_html_table = mars_facts_table.to_html(classes = 'table table-striped')
mars_facts_html_table = mars_facts_html_table.replace('\n', ' ')
print(mars_facts_html_table)


# # Mars Hemisphere Images Scraping

# In[14]:


#Scrape Cerberus Hemisphere
hemispheres_url = 'https://marshemispheres.com/'
browser.visit(hemispheres_url)
browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere1_title = soup.find('h2', class_='title').text
hemisphere1_img = soup.find('img', class_='wide-image')['src']
hemisphere1_img_url = f'{hemispheres_url}{hemisphere1_img}'
print(hemisphere1_title)
print(hemisphere1_img_url)


# In[15]:


#Scrape Schiaparelli Hemisphere
hemispheres_url = 'https://marshemispheres.com/'
browser.visit(hemispheres_url)
browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere2_title = soup.find('h2', class_='title').text
hemisphere2_img = soup.find('img', class_='wide-image')['src']
hemisphere2_img_url = f'{hemispheres_url}{hemisphere2_img}'
print(hemisphere2_title)
print(hemisphere2_img_url)


# In[16]:


#Scrape Syrtis Major Hemisphere
hemispheres_url = 'https://marshemispheres.com/'
browser.visit(hemispheres_url)
browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere3_title = soup.find('h2', class_='title').text
hemisphere3_img = soup.find('img', class_='wide-image')['src']
hemisphere3_img_url = f'{hemispheres_url}{hemisphere3_img}'
print(hemisphere3_title)
print(hemisphere3_img_url)


# In[17]:


#Scrape Syrtis Major Hemisphere
hemispheres_url = 'https://marshemispheres.com/'
browser.visit(hemispheres_url)
browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere4_title = soup.find('h2', class_='title').text
hemisphere4_img = soup.find('img', class_='wide-image')['src']
hemisphere4_img_url = f'{hemispheres_url}{hemisphere4_img}'
print(hemisphere4_title)
print(hemisphere4_img_url)


# In[20]:


#Create a Dictionary of the Hemisphere Titles & Images
hemisphere_image_urls = [
    {"title1": hemisphere1_title, "img_url1": hemisphere1_img_url},
    {"title2": hemisphere2_title, "img_url2": hemisphere2_img_url},
    {"title3": hemisphere3_title, "img_url3": hemisphere3_img_url},
    {"title4": hemisphere4_title, "img_url4": hemisphere4_img_url}]

hemisphere_image_urls


# In[21]:


#Close Browser
browser.quit()


# In[ ]:




