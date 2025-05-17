# import streamlit as st


# """
# https://media.istockphoto.com/id/2163598703/photo/close-up-of-a-beautiful-pink-chrysanthemum-flower-in-the-garden.webp?a=1&b=1&s=612x612&w=0&k=20&c=HNrL3JaJzxMYViGWRAfxnR5kh7QpPxrr97cYLMS8sI8=
# https://media.istockphoto.com/id/2163598703/photo/close-up-of-a-beautiful-pink-chrysanthemum-flower-in-the-garden.jpg?s=2048x2048&w=is&k=20&c=Z8E-GU7GOf_OSHJNWvHM6ZPByX2AMrrnMdMzuKFh1LA=
# """

# premium_domain_url = "https://plus.unsplash.com/premium_photo-"
# free_domain_url = "https://images.unsplash.com/photo-"

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


# # https://images.unsplash.com/file-1715714098234-25b8b4e9d8faimage?w=416&dpr=2&auto=format&fit=crop&q=60

# free_domain_url = "https://images.unsplash.com/"
# link = st.text_input("Enter the url from unsplash")

# is_premium = False if link.strip().split(".unsplash.com")[0] == "https://images" else True
# # print(is_premium)

# img_id = link.strip().split("?")[0].split(".unsplash.com/")[1]
# # print(img_id)

# st.image(f"{free_domain_url}{img_id}")

# """
# https://images.unsplash.com/photo-1682695797221-8164ff1fafc9
# https://images.unsplash.com/photo-1682695797221-8164ff1fafc9

# https://images.unsplash.com/file-1715714098234-25b8b4e9d8faimage

# https://unsplash.com/photos/pink-petaled-flower-YdAqiUkUoWA
# https://unsplash.com/photos/podium-display-design-with-paper-art-pastel-color-flower-abstract-background-3d-rendering-X3J8H6Svi_s
# https://unsplash.com/photos/sakura-tree-in-bloom-7NBO76G5JsE
# https://unsplash.com/photos/a-bouquet-of-flowers-sitting-on-top-of-a-wooden-table-ElxBX6bsAgQ
# https://unsplash.com/photos/a-bunch-of-flowers-that-are-in-a-vase-yurVcRioP8o

# https://images.unsplash.com/photo-1474112704314-8162b7749a90
# """


##########################################################################################

import streamlit as st
from playwright.sync_api import sync_playwright


BASE_SEARCH_URL = "https://unsplash.com/s/photos/flower"

search = st.text_input("", placeholder="Search Photos")

if search:
    
    with sync_playwright() as pr:
        browser = pr.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{BASE_SEARCH_URL}{search}")
        page.wait_for_selector("figure")
        content = page.content()
        browser.close()
    
    st.write(f"{BASE_SEARCH_URL}{search}")
    st.write(content)
