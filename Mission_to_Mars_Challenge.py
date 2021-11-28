#!/usr/bin/env python
# coding: utf-8

# In[316]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[317]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[318]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[19]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[20]:


slide_elem.find('div', class_='content_title')


# In[21]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[22]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[23]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[24]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[25]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[26]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[27]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[29]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[30]:


df.to_html()


# In[31]:


browser.quit()


# **Challenge**
# 

# In[869]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
import os
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[870]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[324]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[325]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[326]:


slide_elem.find('div', class_='content_title')


# In[327]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[328]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[329]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[330]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[331]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[332]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[333]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[334]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[335]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[336]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[871]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[872]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[873]:


anchors = img_soup.find_all('a', 'itemLink')


anchors


# In[874]:


pages =  browser.find_by_tag('h3')[0], browser.find_by_tag('h3')[1], browser.find_by_tag('h3')[2], browser.find_by_tag('h3')[3]
type(pages)


# In[875]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []



# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    browser.find_by_tag('h3')[i].click()
    hemispheres = {}
    
    hemi = browser.html
    hemi_soup = soup(hemi, 'html.parser')

    links = hemi_soup.find('a', text='Sample').get('href')
    title = hemi_soup.find('h2', class_='title').text

    hemispheres['title'] = title
    hemispheres['img_url'] = url + links

    hemisphere_image_urls.append(hemispheres)
    
    browser.back()



# In[876]:


hemispheres


# In[877]:


hemisphere_image_urls


# In[867]:


# 5. Quit the browser
browser.quit()


# In[ ]:




