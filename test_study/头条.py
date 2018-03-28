# coding=utf-8
from selenium import webdriver
import requests


class Toutiao:

    def __init__(self, page=1):
        # self.dr = webdriver.PhantomJS(executable_path='D:/phantomjs.exe')
        self.dr = webdriver.PhantomJS()
        self.dr.get(
            'http://toutiao.io/search?utf8=%E2%9C%93&page={}&q=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95'.format( page ) )
        # self.dr.get('http://www.baidu.com')
        # print self.dr.page_source

    def print_content(self):
        elements = self.dr.find_elements_by_xpath( "//h3[@class='title']/a" )
        # print elements
        result = [{'title': i.get_attribute('title'), 'link': i.get_attribute('href')} for i in elements]
        self.dr.quit()
        return result

    @staticmethod
    def http_jump(url):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        }
        res = requests.get(url, headers=headers, allow_redirects=False )
        try:
            Location = res.headers['Location']
            return Location
        except:
            return url

if __name__ == '__main__':
    toutiao = Toutiao()
    print toutiao.http_jump('https://toutiao.io/k/tzx7lm')
    result = []
    for i in range(1, 20):
        result.append(Toutiao(i).print_content())
    print result
    for i in range(0, len(result)):
        for j in range(0, len(result[i])):
            print result[i][j]['title'].replace(u'- 开发者头条', '' )
            print toutiao.http_jump(result[i][j]['link'])
            print '\n'
            # //a/@title
            # //*[@id="main"]/div/div[1]/div[1]/div[2]/h3/a
