from lxml import etree

# 实例一个etree对象，将解析的内容加载到该对象中
tree = etree.XML('test.html')
# r = tree.xpath('/html/body/ul/li')
# r = tree.xpath('/html//li')
# r = tree.xpath('//li')
# r = tree.xpath('//div[@class="song"]')
# r = tree.xpath('//div[@class="song"]//text()')
r = tree.xpath('//img/@src')#提取属性值
print(r)