# premium_max_width = "?w=900"
# width = "?w="
# height = "&h="
# dpr = "&dpr=" # 1, 1.5, 2, 3, ...

# auto_format = "&auto=format" # to detect which format does suits best for the browser
# force_format = "&fm=png" # png, jpg, webp, avif
# fit = "&fit=crop"
# quality = "&q=100"

# blend = "" # &blend=ff0000     Overlay color on the image.
# blend_mode = "" # &blend=000000&blend-mode=overlay     normal, multiply, screen, overlay, etc.
# saturation = "" # &sat=-50   -100 to 100
# exposure = "" # exp      -100 to 100
# blend_alpha= "" # &blend=000000&blend-alpha=0.3      0 to 1
# blur = "" # &blur=20       0 to 100
# sharp = ""   # &sharp=25     -100 to 100
# invert = "" # invert      true or false



# # st.image(f"{premium_domain_url}1676478746990-4ef5c8ef234a{premium_max_width}")
# # st.image(f"{premium_domain_url}1676478746990-4ef5c8ef234a")
# # st.image(f"{premium_domain_url}1676478746990-4ef5c8ef234a{premium_max_width}{force_format}{fit}{quality}")
# # st.image(f"{free_domain_url}1525310072745-f49212b5ac6d{width}{dpr}{force_format}{fit}{quality}")
# # st.image(f"{free_domain_url}1525310072745-f49212b5ac6d?auto=format&fit=crop&w=800&h=600&crop=faces&dpr=2&blur=90&sat=-30")
# # st.image(f"{free_domain_url}1525310072745-f49212b5ac6c?auto=format&fit=crop&w=800&h=600&dpr=2&fm=webp")

##########################################################################################
import streamlit as st
import subprocess
import os
from bs4 import BeautifulSoup
from typing import List
import random


BASE_SEARCH_URL = "https://unsplash.com/s/photos/"
BASE_FREE_URL = "https://images.unsplash.com/"
BASE_PREMIUM_URL = "https://plus.unsplash.com/"
FILE_NAME = "temp.html"


def extract_img_id(urls: List[str]) -> List[str]:
    """Extract image id from url."""
    extracted = []
    for i in urls:
        extracted.append(i.split("?")[0].split("unsplash.com/")[1])
    return extracted

def random_emoji_returner():
    """Returns a emoji radomly."""
    emojis = ["😀","😁","😂","🤣","😃","😄","😅","😆","😗","🥰","😘",
              "😍","😎","😋","😊","😉","😙","😚","🙂","🤗","🤩","🤔",
              "😮","😣","😏","🙄","😶","😑","😐","🤐","😯","😪","😫",
              "😛","😜","😲","🤪","😳","😠","🤓","🤡","🤭","🧐","😇",
              "🥳","🥺","🤫","🎈","🎄","✨","🎃","❤","🧡","💛","💚"]
    return random.choice(emojis)

def img_extracter():
    """Extract image from FILE_NAME and show in page."""
    with open(FILE_NAME, "r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, "html.parser")
        images = soup.find_all("img")
         
        image_urls = [img["src"] for img in images if "unsplash.com" in img["src"]] # type: ignore
        # print(image_urls)
        
        extracted_img_id = extract_img_id(image_urls) # type: ignore
        
        col1 = st.empty()
        col2 = st.empty()
        col1, col2 = st.columns(2)
        # col size ~344
        
        def print_img(url):
            if url.startswith("premium"):
                st.image(f"{BASE_PREMIUM_URL}{url}?w=350&q=60")
                st.link_button(f"Download {random_emoji_returner()}", f"{BASE_PREMIUM_URL}{url}?w=900&q=100&dpr=1&fm=png")
                
            else:
                st.image(f"{BASE_FREE_URL}{url}?w=350&q=60")
                st.link_button(f"Download {random_emoji_returner()}", f"{BASE_FREE_URL}{url}?w=auto&q=100&dpr=1&fm=png")

        for i, url in enumerate(extracted_img_id):
            if i % 2 == 0:
                with col1:
                    print_img(url)
            else:
                with col2:
                    print_img(url)

with st.form("my_form"):
    """Form for searching"""
    search = st.text_input("Search", placeholder="Search photos", label_visibility="collapsed")
    submitted = st.form_submit_button('Search')

if search or submitted:
    
    with st.spinner(":) Scrapping..."):
        # scrap_web(BASE_SEARCH_URL, search)
        
        result = subprocess.run(
            ["python", "webscrapper.py", search],
            capture_output=True,
            text=True
        )
        # result1 = subprocess.run(
        #     ["python", "--version"],
        #     capture_output=True,
        #     text=True
        # )

        # Show output and errors from the subprocess for debugging
        # st.subheader("Scraper Output")
        # st.code(result.stdout + result.stderr)
        # st.code(result1.stdout + result1.stderr)
                
        if os.path.exists(FILE_NAME):
            # with open(FILE_NAME, "r", encoding="utf-8") as f:
            #     st.html(f.read())

            img_extracter()
            
        else:
            st.error("Scraping failed or file not found.")
        
        # st.write(f"Showing results for: [{BASE_SEARCH_URL}{search}]({BASE_SEARCH_URL}{search})")

