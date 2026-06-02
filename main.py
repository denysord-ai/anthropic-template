from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Write a short sentence about a unicorn.",
        }
    ],
    model="claude-opus-4-8",
)
print(message.content)
print(message.usage)
