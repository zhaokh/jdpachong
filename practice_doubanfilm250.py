import requests,sys
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250'

def download_page(url):
    # 伪造谷歌浏览器  防止服务器通过校验请求的U-A来识别爬虫，最简单的反爬虫机制
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers = headers).content
    return data

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    movie_list_soup = soup.find_all('ol' , class_ = 'grid_view')
    movie_name_list = []
    movie_list_bs = BeautifulSoup(str(movie_list_soup[0]),'html.parser')
    movie_list_li = movie_list_bs.find_all('li');
    for movie_li in movie_list_li:
        detail = movie_li.find('div',attrs={'class':'hd'})
        movie_name = detail.find('span',class_="title").text
        movie_name_list.append(movie_name+"\n")
        # sys.stdout.write(movie_name+"\n")
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


def main():
    url = DOWNLOAD_URL
    with open('movies.txt', 'a', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.writelines(movies)


if __name__ == '__main__':
    main()