from bs4 import BeautifulSoup


def get_films(filename: str) -> list[dict]:
    films = []
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    divs = soup.find_all("li", {"class": "gallerySection__item"})
    for div in divs:
        film = {"title": div.find("div", {"class": "nbl-broadPosterBlock__title"}).text,
                "extra": div.find("div", {"class": "nbl-broadPosterBlock__extra"}).text,
                "details": div.find("div", {"class": "nbl-broadPosterBlock__details"}).text}
        films.append(film)

    return films
