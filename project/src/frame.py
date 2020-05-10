from bs4 import BeautifulSoup
import re
import requests
url='https://news.163.com'
news=[]
def get_html_text(url):
    try:
        r=requests.get(url)
        if r.status_code==200:
            r.encoding=r.apparent_encoding
            return r.text
    except requests.exceptions.RequestException:
        return None
def get_urls(url):
    extracted_urls = []
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    def has_no_class(tag):
        return not tag.has_attr('class') and not tag.has_attr('em')
    news_links = soup.find_all(has_no_class, href=re.compile("https://news.163.com/20"))
    for each in news_links:
        single_link=each.get('href')
        len_=len(single_link)
        if str(single_link)[:4] == 'http':
            extracted_urls.append(single_link)
            print(len_,single_link)
    print('end')
    #for i in news_links:
    #    print(i)
    #return news_links
    return extracted_urls
def get_page(link):
    #post_text=''
    soup = BeautifulSoup(get_html_text(link), 'html.parser')
    post_title=soup.title.text
    print(post_title)
    post_text = soup.find(attrs={"class": "post_text"})
    if post_text == None:
        print('post_text没有匹配成功')
        print('匹配另一个模式endText')
        post_text = soup.find(attrs={"class": "endText"})
    # for i in news_links:
    #     # print(i.text)
    #     news.append(i.text)
    #     #print(news)
    return (post_text)

    #send redis / MQ

def content_parse(post_text):
    text = post_text.text
    text = text.replace('\n', '')
    text = text.split('(function ()')[0]
    print(text)
    return text
    #send MySQL / MongoDB

if __name__ == "__main__":
    print('running as main function')
    #print(url)
    news_links=get_urls(url)
    news_contents=[]
    for i in range(len(news_links)):
        print(news_links[i])
        post_text=get_page(news_links[i])
        content=content_parse(post_text)
        print(content)
        news_contents.append(content)
    #for i in news:
    #    print(i)

else:
    print('called by others')