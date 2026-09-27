import itertools
import os

from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()


def get_pinecone_client():
    # Initialize the Pinecone client with your API key
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    return pc


def get_index(name="datacamp-index"):
    pc = get_pinecone_client()
    index = pc.Index(name)
    return index


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))
