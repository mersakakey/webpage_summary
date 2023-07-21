import streamlit as st
from summarize import Summarize
from url_to_text_data import url_to_text_data

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')
  summary_temperature= st.slider('要約のtemperature', 0.0, 2.0, 0.2,step=0.1)
  gpt_model_name = st.radio(label='モデル',
                 options=('gpt-3.5-turbo-0613', 'gpt-4-0613'),
                 index=1,
                 horizontal=True,
)

with st.form("シンプルに要約してもらう"):
  webpage_url = st.text_area(label="ウェブページのURL")
  submitted = st.form_submit_button("要約する")

if submitted:
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API keyを入力してください', icon='⚠')
  if not webpage_url:
    st.warning('URLを入力してください', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    summarize = Summarize(openai_api_key, gpt_model_name = gpt_model_name, transcription_temperature = summary_temperature)

    output = summarize.predict(url_to_text_data(webpage_url))
    print(output)
    st.write(output)

