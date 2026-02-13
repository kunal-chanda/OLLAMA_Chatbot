from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

#Indexing Part - fetching transcript, splitting, creating vector store
yt_api = YouTubeTranscriptApi()
video_id = "jG4Vs81kMlc"
transcript = yt_api.fetch(video_id)

transcript_text = " ".join(t.text for t in transcript)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_text(transcript_text)

"""
need to uncomment this line to use openai embeddings
"""
embeddings = OpenAIEmbeddings(model="text-embedding-3-small") 

vector_store = FAISS.from_texts(chunks,embeddings)

#Retrieval Part - creating retriever from vector store
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

#Augmentation Part - creating prompt template
prompt = PromptTemplate(template="""You are a helpful assistant.
                        Answer the question based on the following context. If the context
                        is insufficient then directly say I dont know: 
                        {context} 
                        Question: {question}""", input_variables=["context", "question"])  

question="How to use GitHub in daily usecases?"
context = retriever.invoke(question)
context = "".join([doc.page_content for doc in context])
final_prompt = prompt.invoke({"context":context, "question":question})

#Generation Part - using LLM to generate answer based on the final prompt
"""
need to uncomment this line to use openai LLM
"""
llm = ChatOpenAI(model="gpt-5-nano", temperature=0.72)
response = llm.invoke(final_prompt)
print(response.content)
