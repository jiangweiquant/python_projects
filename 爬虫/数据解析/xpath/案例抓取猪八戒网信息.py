import requests
from lxml import etree
url = 'https://www.zbj.com/search/service/?l=0&kw=saas&r=2&lr=3418'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url=url,headers=headers)
content = response.text
# print(content)
# #数据解析xpath
tree = etree.HTML(content)
divs = tree.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')
# print(len(divs))
for div in divs:
    # price = div.xpath('.//div[@class="price"]/span/text()')
    title = div.xpath('.//a[@target="_blank"]/text()')
#     # shop_name = div.xpath('.//div[@class="shop-info text-overflow-line" ]/text()')
    print(title)



# <a data-linkid="sp-pc-search pg-qyfw-se list-0-2-9790925" href="https://shop.zbj.com/9790925/sid-1466291.html" data-href="https://shop.zbj.com/9790925/sid-1466291.html?pdcode=2&amp;pos=1&amp;ym=1&amp;pst=searchf-list-service-2021-1-1&amp;xdverid=1446513398484303872&amp;fr=tgt" target="_blank" class="serve-name text-overflow-line-two oneline hasad">校园车工业物联网关边缘计算传感器java后端开发saas定制</a>
#
# < a
# data - linkid = "sp-pc-search pg-qyfw-se list-1-2-34161750"
# href = "https://shop.zbj.com/34161750/sid-1920598.html"
# data - href = "https://shop.zbj.com/34161750/sid-1920598.html?pdcode=17&amp;pos=2&amp;ym=1&amp;pst=searchf-list-service-2021-1-2&amp;version=1"
# target = "_blank"


# class ="serve-name text-overflow-line-two oneline" > 进销存oa系统crm企业管理软件开发 < hl > SaaS < /hl > 办公erp < /a >
#
# < a
# data - linkid = "sp-pc-search pg-qyfw-se list-3-2-7074595"
# href = "https://shop.zbj.com/7074595/sid-1911024.html"
# data - href = "https://shop.zbj.com/7074595/sid-1911024.html?pdcode=17&amp;pos=4&amp;ym=1&amp;pst=searchf-list-service-2021-1-4&amp;version=1"
# target = "_blank"
#
#
# class ="serve-name text-overflow-line-two oneline" > 软件开发网站定制OA系统CRM系统 < hl > SaaS < /hl > 平台ERP系统 < /a >


