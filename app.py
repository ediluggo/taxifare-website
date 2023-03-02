import streamlit as st
import pandas as pd
import numpy as np



if st.button('Clic to be surprised'):
# print is visible in the server output, not in the page
    video_file = open('dancing-mushroom.mov', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write('🍄 This is a magic mushroom 🍄')
