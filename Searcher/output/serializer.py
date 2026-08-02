import sys, os, json
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import NewsItem
from Searcher.processing.scorer import score_articles

def sorted_articles(articles: list) -> list:
    return sorted(articles, key=lambda article: article.score, reverse=True)

def _get_target_path(filename: str) -> Path:
    main_folder = Path(__file__).resolve().parents[2]

    target_directory = main_folder / "data"

    target_directory.mkdir(parents= True, exist_ok= True)

    return target_directory / filename

def save_best(articles: list, filename: str="articles.json", max: int = 5):
    top_articles = articles[:max]

    serialized_articles = []

    for item in top_articles:
        if hasattr(item, "model_dump"):
            serialized_articles.append(item.model_dump())
        elif hasattr(item, "dict"):
            serialized_articles.append(item.dict())
        else:
            serialized_articles.append(vars(item))

    file_path = _get_target_path(filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_articles, f, indent=4, ensure_ascii=False, default=str)
        print(f"Successfully serialized and saved 5 articles to: {file_path}")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")



if __name__ == '__main__':

    data = sorted_articles(score_articles())
    save_best(data)

    '''
    i = 1
    data = sorted_articles(scored_articles())

    for article in data:
        print(i)
        print(f"title: {article.title} \nscore: {article.score}")
        i += 1
        
    '''
    