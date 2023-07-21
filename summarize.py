from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import SimpleSequentialChain
from langchain.text_splitter import TokenTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Summarize:
  def __init__(_self,  openai_api_key, gpt_model_name = "gpt-3.5-turbo-0613", transcription_temperature=0):

    _self.llm = ChatOpenAI(
      model_name = gpt_model_name,
      temperature=transcription_temperature,
      openai_api_key=openai_api_key
    )

  def predict(_self, document):
    max_tokens:int = 400 # 分割長

    text_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=0)

    promptSubject = PromptTemplate(input_variables=["text"], template="""
Write a concise summary of the following:

{text}

CONCISE SUMMARY IN JAPANESE:""")

    summary_chain = load_summarize_chain(_self.llm, chain_type="stuff", prompt = promptSubject)

    summarize_result = summary_chain.run(text_splitter.create_documents([document]))

    return summarize_result