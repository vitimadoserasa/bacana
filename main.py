import requests
from bs4 import BeautifulSoup

def fetch_ad_data(ad_tag_url):
    response = requests.get(ad_tag_url, timeout=10)
    if response.status_code != 200:
        return {"error": "Erro ao buscar a tag do anúncio."}

    soup = BeautifulSoup(response.text, 'html.parser')
    img_url = soup.find("img")["src"] if soup.find("img") else "Imagem não encontrada"
    ad_url = soup.find("a")["href"] if soup.find("a") else "Anunciante não encontrado"

    return {"image_url": img_url, "ad_url": ad_url}

if __name__ == "__main__":
    url = "https://exemplo.com/adtag"
    print(fetch_ad_data(url))
