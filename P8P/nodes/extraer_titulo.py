from bs4 import BeautifulSoup

def ejecutar(entrada):
    html = entrada.get('html')
    soup = BeautifulSoup(html, 'html.parser')
    titulo = soup.title.string if soup.title else ''
    return {'titulo': titulo}
