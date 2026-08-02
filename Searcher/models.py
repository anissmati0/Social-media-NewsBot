from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class NewsItem:
    title: str
    source: str
    url: str
    published_at: datetime
    summary: Optional[str] = None
    thumbnail: Optional[str] = None
    score: float = 0.0
    category: str = "Uncategorized"
    
