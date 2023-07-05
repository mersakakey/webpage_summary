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
    max_tokens:int = 400 # 分割長

    text_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=0)

    promptSubject = PromptTemplate(input_variables=["text"], template="""
#命令書
あなたはプロの編集者です。以下の制約条件に従って、入力する文章を要約してください。

#制約条件
・日本語で出力する。
・箇条書きで出力する。
・重要なキーワードを取りこぼさない。
・文章の意味を変更しない。
・架空の表現や言葉を使用しない。
・文章中の数値には変更を加えない。

#入力する文章
"{text}"

#出力形式
要約した文章:
""")

    summary_chain = load_summarize_chain(_self.llm, chain_type="map_reduce", map_prompt = promptSubject)

    summarize_result = summary_chain.run(text_splitter.create_documents([document]))

    return summarize_result