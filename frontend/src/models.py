from pydantic import BaseModel

class MyBaseModel2(BaseModel):
    """
    A simple Pydantic model with two fields.

    Attributes:
        c (int): An integer value.
        d (str): A string value.
    """
    c: int
    d: str
