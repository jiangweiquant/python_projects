# leftTicketDTO.train_date: 2023-06-18
# leftTicketDTO.from_station: BJP
# leftTicketDTO.to_station: SHH
# purpose_codes: ADULT
#
#
# https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-06-18&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT
import requests
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2023-06-18&flag=N,N,Y'

response = requests.get(url=url, headers=header)
content = response.text

with open('ticker.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
print('保存成功！')

# url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2023-06-18&flag=N,N,Y'
