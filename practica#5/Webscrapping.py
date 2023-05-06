from bs4 import BeautifulSoup
from io import open
import requests


url = requests.get('https://dble.bn-ent.net/en/')
#Mostramos si logramos conectar con la página
def show_status(url):
    if url.status_code == 200:
        print('La página está funcionando correctamente.')
    else:
        print('Error.')
show_status(url)

#Obtenemos todos los links

def get_links(url):
    fo = open("data.txt", "a")
    soup = BeautifulSoup(url.content, 'html.parser')
    links_list = soup.find_all('a')
    for link in links_list:
        if 'href' in link.attrs:
            links = str(link.attrs['href'])
        if r'.com' in links:
            fo.write(f"\n [+] {links} \n" )
    fo.close()
get_links(url)

print("El scrapping se ha realizado, links obtenidos")

