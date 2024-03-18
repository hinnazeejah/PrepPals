from openai import OpenAI
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv()
os.environ["TOKENIZERS_PARALLELISM"] = "false"

openai_client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def get_embedding(sentence):
    return model.encode(sentence)


def get_cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))


def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    
    return [para for para in paragraphs if len(para) > 40]


def get_most_relevant_embeddings(embeddings, query_embedding):
    similarities = []
    for e in embeddings:
        sim = get_cosine_similarity(query_embedding, embeddings[e])
        similarities.append((sim, e))


    similarities.sort(reverse=True, key=lambda x: x[0])


    return similarities[:10]


def query_model(website_data, resume_data):

    context = f"""\n\nHere is some information about me:
    {resume_data}


    Here is the website of the company that I am interviewing with:
    {website_data}
    """

    prompt = f"""You are an expert at preparing for interviews at Big Tech companies. I am a Cybersecurity student that is preparing for interviews. Given the information about the company that I am interviewing with below, generate an agenda for a 30 minute interview with the company. 

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
