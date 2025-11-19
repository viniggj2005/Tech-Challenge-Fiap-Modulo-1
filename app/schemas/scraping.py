from pydantic import BaseModel


class ScrapedLinkAndCategory(BaseModel):
    link: str
    category: str
