from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
movie_title = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_text = [movie.getText() for movie in movie_title]
movies = movie_text[::-1]
with open("./assets/movies/movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")
