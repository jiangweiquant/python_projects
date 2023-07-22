import requests
# #登录

#会话
# url = 'https://passport.17k.com/ck/user/login'
# session = requests.session()
# data = {
#     "loginName": "18081208401",
#     "password": "fuspv4b2",
# }
# res = session.post(url=url,data=data)
# # print(res.cookies)#看cookies
#
# res1 = session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
# print(res1.json())


headers = {
    'Cookie':'GUID=af561d2c-729f-43e5-b816-556a12bff9e4; Hm_lvt_9793f42b498361373512340937deb2a0=1689593023; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F02%252F62%252F84%252F100608462.jpg-88x88%253Fv%253D1689594631000%26id%3D100608462%26nickname%3Djwhahaha%26e%3D1705147605%26s%3D06dd91c61811a2f6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100608462%22%2C%22%24device_id%22%3A%2218963978a0636-0cd3e7c7a55c2-7e565474-921600-18963978a07bb%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%22af561d2c-729f-43e5-b816-556a12bff9e4%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1689596239'
}
response = requests.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919',
                        headers=headers)
print(response.json())