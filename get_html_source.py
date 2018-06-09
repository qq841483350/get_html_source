#coding:utf8
#获取任意网页源代码包括http https  模块编写：李亚涛  个人微信号：liyatao01 有问题联系我  注意：如果没有安装 requests 模块请用命令 pip install requests安装后运行
import requests,re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers={"User-Agent":"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"}
def get_https_html(url):
    html1=requests.get(url,headers=headers,verify=False).content

    if 'gb2312' in html1 or 'GB2312' in html1:
        r=requests.get(url,headers=headers,verify=False)
        r.encoding='gb2312'
        html=r.text
        return html
    elif 'gbk' in html1 or 'GBK' in html1:
        r=requests.get(url,headers=headers,verify=False)
        r.encoding='gbk'
        html=r.text
        return html
    else:
        html=html1
        return html1
if __name__=="__main__":
    url="https://cs.focus.cn/zixun/shichang/2/"  #https
    # url="http://www.liyatao.com"                    #http
    get_https_html(url)
