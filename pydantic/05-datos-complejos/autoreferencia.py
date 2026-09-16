from pydantic import BaseModel

class Comment(BaseModel):
    text: str
    author: str
    replies: list[Comment] = []

comment = Comment(
    text="Great article!",
    author="Alice",
    replies=[
        Comment(text="Thanks!", author="Bob")
    ]
)
