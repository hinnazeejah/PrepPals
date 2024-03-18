# from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os
import numpy as np
from dotenv import load_dotenv

# Load a Hugging Face model
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Specify the model name you want to use

load_dotenv()
os.environ["TOKENIZERS_PARALLELISM"] = "false"

openai_client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def get_embedding(sentence):
    return model.encode(sentence)


def get_cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))


# Function to split the text into paragraphs
def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    # Filter out any empty paragraphs or ones that are too short to be meaningful
    return [para for para in paragraphs if len(para) > 40]


def get_most_relevant_embeddings(embeddings, query_embedding):
    similarities = []
    for e in embeddings:
        sim = get_cosine_similarity(query_embedding, embeddings[e])
        similarities.append((sim, e))

    # Sort by similarity in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Get top 10 similarities
    return similarities[:10]


def query_model(website_data, resume_data):

    # website_embeddings = {}
    # for k in website_paragraphs:
    #     website_embeddings[k] = get_embedding(k)

    # resume_embeddings = {}
    # for k in resume_paragraphs:
    #     resume_embeddings[k] = get_embedding(k)

    # q_embedding = get_embedding("values principles products services team about")

    # relevant_website_embeddings = get_most_relevant_embeddings(website_embeddings, q_embedding)
    # relevant_resume_embeddings = get_most_relevant_embeddings(resume_embeddings, q_embedding)

    context = f"""\n\nHere is some information about me:
    {resume_data}


    Here is the website of the company that I am interviewing with:
    {website_data}
    """

    prompt = f"""You are an expert at preparing for interviews at Big Tech companies. I am a Computer Science student that is preparing for interviews. Given the information about the company that I am interviewing with below, generate an agenda for a 30 minute interview with the company. 

    For each section of the agenda, include specific topics to discuss based on my resume and the company's website. 
             
    {context}
    """

    print("PROMPT", prompt)

    res = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": prompt},
        ]
    )

    print(res.choices[0].message.content)

    return res.choices[0].message.content
