from Searcher.processing.scorer import fetch_data, score_articles
from Searcher.output.serializer import sorted_articles, save_best


def run_pipeline_1(query: str):
    data = fetch_data(query)
    data = score_articles(data)
    data = sorted_articles(data)
    save_best(data)

if __name__ == "__main__":
    run_pipeline_1()