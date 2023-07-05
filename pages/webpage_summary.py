import streamlit as st
from summarize import Summarize
from get_html import get_html

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  summary_temperature= st.slider('要約のtemperature', 0.0, 2.0, 0.0,step=0.1)

with st.form("シンプルに要約してもらう"):
  webpage_url = st.text_area(label="ウェブページのURL")
  submitted = st.form_submit_button("要約する")

  # document = st.text_area(label="記事")

if submitted:
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API keyを入力してください', icon='⚠')
  if not webpage_url:
    st.warning('文章を入力してください', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    summarize = Summarize(openai_api_key, transcription_temperature = summary_temperature)

    output = summarize.predict(get_html(webpage_url))
    print(output)
    st.write(output)

