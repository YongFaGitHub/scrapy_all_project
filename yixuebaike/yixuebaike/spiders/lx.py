from lxml import etree
import re
from bs4 import BeautifulSoup
import bs4
import requests
url = 'http://www.a-hospital.com/w/%E5%AD%90%E5%AE%AB%E9%A2%88%E5%B9%B3%E6%BB%91%E8%82%8C%E7%98%A4'
r = requests.get(url)
contents = r.content
detail_soup = BeautifulSoup(contents, 'lxml')
item = {}
def extract_article_parsed_content(content_html, publish_time=None, url=None, response=None):
    parsed_content = ''
    parsed_content_char_count = 0
    img_location = []
    img_location_count = 0
    parsed_content_main_body = ''
    authorized = ''
    download_img_flag = True
    url = url

    if content_html:
        soup = BeautifulSoup(content_html, 'lxml')
        """change ， 多个div处理"""
        for content in soup.find('body').contents:
            if not isinstance(content, (bs4.element.NavigableString)):
                news_content = content.contents
            if news_content:
                for one_row_content_item in news_content:
                    document_name = one_row_content_item.name
                    if document_name in ['div', 'p', 'font', 'span', 'td', 'b', 'img', 'center', 'tr', 'strong',
                                         'article', 'br', None] and document_name not in ['script']:
                        if document_name is None:
                            p_content = one_row_content_item.replace('\n', '').replace('\r', '')
                            # 判断有没有字，或许是空段落，
                            if p_content and type(one_row_content_item.string) != bs4.element.Comment:
                                parsed_content += '<p>{0}</p>'.format(p_content.encode('utf-8')).replace('<p> </p>', '')
                                parsed_content_char_count += len(p_content)
                                parsed_content_main_body += p_content.strip()
                        if document_name:
                            style_list = one_row_content_item.find_all('style')
                            for style_document in style_list:
                                style_document.decompose()
                        if one_row_content_item.find('script'):
                            pass
                        else:
                            p_content = one_row_content_item.get_text().replace('\n', '').replace('\r', '')
                            if p_content:
                                p_content = p_content.replace('\n', '').replace('\r', '')
                                parsed_content += '<p>{0}</p>'.format(p_content.encode('utf-8'))
                                parsed_content_char_count += len(p_content)
                                parsed_content_main_body += p_content.strip()

    return parsed_content, parsed_content_char_count, img_location, img_location_count, parsed_content_main_body, authorized, download_img_flag

storyline_html = detail_soup.find(id='bodyContent')
if storyline_html:
    results = extract_article_parsed_content(content_html=storyline_html.prettify().strip())
    item['storyline_html'] = results[0]
    item['storyline_text'] = results[4]
print(item['storyline_text'])