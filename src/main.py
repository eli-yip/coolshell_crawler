import requests
from bs4 import BeautifulSoup


def get_data(page_url: str):

    response = requests.get(page_url, timeout=1000)
    soup = BeautifulSoup(response.text, 'html.parser')

    h2_tags = soup.find_all('h2', {'class': 'entry-title'})
    links_result = [tag.find('a')['href'] for tag in h2_tags]

    return links_result


def write_to_file(artical_urls: list):
    with open('links.txt', 'a', encoding='utf-8') as file:
        for link in artical_urls:
            file.write(f'{link}\n')


if __name__ == '__main__':
    url = 'https://coolshell.cn/'
    # links = get_data(url)
    # print("Get data from page: ", url)
    # write_to_file(links)
    for page_num in range(2, 75):
        url = f'https://coolshell.cn/page/{page_num}'
        links = get_data(url)
        print("Get data from page: ", url)
        write_to_file(links)
