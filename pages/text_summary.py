import streamlit as st
from summarize import Summarize
from get_html import get_html
from extract_html import extract_html

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  summary_temperature= st.slider('要約のtemperature', 0.0, 2.0, 0.0,step=0.1)

with st.form("シンプルに要約してもらう"):
  webpage_url = st.text_area(label="ウェブページのURL")
  submitted = st.form_submit_button("要約する")

  document = st.text_area(label="記事")

  pushed = st.form_submit_button("button")


if pushed:
  if not webpage_url:
    st.warning('文章を入力してください', icon='⚠')
  st.write(get_html(webpage_url))

if submitted:
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API keyを入力してください', icon='⚠')
  if not webpage_url:
    st.warning('文章を入力してください', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    summarize = Summarize(openai_api_key, transcription_temperature = summary_temperature)

    output = summarize.predict(document)
    st.write(output)

