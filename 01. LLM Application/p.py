from typing import cast

from openai import OpenAI
from openai.types.responses import ResponseInputParam

from settings import OPENAI_MODEL1

client = OpenAI()


response = client.responses.create(
    model=OPENAI_MODEL1,
    input=cast(
        ResponseInputParam,
        [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "What teams are playing in this image?",
                    },
                    {
                        "type": "input_image",
                        "image_url": "https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg",
                    },
                ],
            }
        ],
    ),
)

print(response.output_text)
