import requests
import streamlit as st

api_key = '9b1ca740ac5544d498ab57dcc8555a90'

def get_news_articles(query):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&from=2024-11-02&sortBy=publishedAt&apiKey={api_key}"
    request = requests.get(url)
    content = request.json()
    for article in content['articles']:
        st.subheader(f"[{article['title']}]({article['url']})")
        st.image(article['urlToImage'])
        st.write(f"**By: {article['author']}**")
        st.write(article['description'])

st.title('News Aggregator')

with st.form('user_search_form'):
    search_query = st.text_input('Input your search query here', placeholder="e.g. Bitcoin")
    submit = st.form_submit_button()
    
    if submit:
        get_news_articles(search_query)
    




