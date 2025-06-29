from dataclasses import dataclass, field

@dataclass
class Config:
    max_wait_time: int = 10
    url: str = 'https://quotes.toscrape.com/search.aspx'
    