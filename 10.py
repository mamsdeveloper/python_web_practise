"""
11. Create a Python project to display and write the title and rating of Imdb top 250 movies in a csv file.


"""


from __future__ import annotations
import csv
import requests
from bs4 import BeautifulSoup


def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    titles = soup.find_all("td", attrs="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")
    return {
        title.a.text: float(rating.strong.text)
        for title, rating in zip(titles, ratings)
    }


def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    movies = get_imdb_top_250_movies()
    print("Movie Title and Rating:\n")
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Movie title", "IMDb rating"])
        for title, rating in movies.items():
            print(title, " ", rating)
            writer.writerow([title, rating])


if __name__ == "__main__":
    write_movies()
