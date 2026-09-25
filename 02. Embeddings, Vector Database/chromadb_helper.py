import os
from typing import cast

import chromadb
from chromadb.api.types import Embeddable, EmbeddingFunction
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv
from file_helper import get_file_path

load_dotenv()
DB_PATH = get_file_path("chroma")


# Create a persistent client
client = chromadb.PersistentClient(path=DB_PATH)


def get_or_create_collection(
    name="default_name", model_name="text-embedding-3-small"
) -> chromadb.Collection:
    # Create OpenAI embedding function
    embedding_function = OpenAIEmbeddingFunction(
        model_name=model_name,
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Recreate the netflix_titles collection
    collection = client.get_or_create_collection(
        name=name,
        embedding_function=cast(EmbeddingFunction[Embeddable], embedding_function),
    )

    return collection
