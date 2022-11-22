import requests,os
url='https://graph.facebook.com/{}/picture?type=large'
for i in range(4,20):
    result=requests.get(url.format(i))
    #folders don't get created by themselves so would have to make a new folder manually
    if "fb_pictures" not in os.listdir():
        os.mkdir('fb_pictures')
    with open("fb_pictures/{}_img".format(i),'wb') as file:
        file.write(result.content)  