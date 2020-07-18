
import requests as rq
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # get html
    url = "https://pokemondb.net/pokedex/all"
    page = rq.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find(id="pokedex")
    trs = table.find_all('tr')
    for res in trs:
        pokemons = res.find('a', class_="ent-name")
        pokemons_muted = res.find('small', class_="text-muted")
        tipos = res.find_all("td", class_="cell-icon")
        id_ = res.find("span", class_="infocard-cell-data")
        mega_name = ""
        if pokemons_muted:
            mega_name = pokemons_muted.text
        if pokemons:
            for tipo in tipos:
                print(
                    f"{id_.text} - Name: {pokemons.text} {mega_name} Type: {tipo.text}")

"""
Output:
001 - Name: Bulbasaur  Type: Grass Poison
002 - Name: Ivysaur  Type: Grass Poison
003 - Name: Venusaur  Type: Grass Poison
003 - Name: Venusaur Mega Venusaur Type: Grass Poison
004 - Name: Charmander  Type: Fire
"""
