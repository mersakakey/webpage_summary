from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import SimpleSequentialChain
from langchain.text_splitter import TokenTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Summarize:
  def __init__(_self,  openai_api_key, transcription_temperature=0):

    _self.llm = OpenAI(
      temperature=transcription_temperature,
      openai_api_key=openai_api_key
    )

  def predict(_self, document):
    max_tokens:int = 40

    text_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=20)

    summary_chain = load_summarize_chain(_self.llm, chain_type="map_reduce")

    promptSubject = PromptTemplate(input_variables=["text"], template="""以下の文章について、簡潔に要約してください:

"{text}"
""")
    chainSubject = LLMChain(llm=_self.llm, prompt=promptSubject)

    overall_chain_map_reduce = SimpleSequentialChain(chains=[summary_chain, chainSubject])
    subject = overall_chain_map_reduce.run(text_splitter.create_documents([document]))

    return subject