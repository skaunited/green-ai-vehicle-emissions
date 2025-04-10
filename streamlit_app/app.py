import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")
ademe_page = st.Page("ademe.py", title="ADEME Data", icon="🗃")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, ademe_page])

# Run the selected page
pg.run()