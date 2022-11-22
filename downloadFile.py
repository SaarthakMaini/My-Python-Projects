# In order to download the file I have to make a request
url='https://www.africau.edu/images/default/sample.pdf'
#import requests module
import requests,math,time,tqdm
chunk_size=256
r=requests.get(url,stream=True)
size=int(r.headers['Content-Length'])
n=math.ceil(size/chunk_size)
print(r) # Returns the 200 and 404 response
print(r.content)
with open("file.pdf","wb") as file:
    for chunk in tqdm.tqdm(r.iter_content(chunk_size=chunk_size),total=n):
        time.sleep(1)
        file.write(chunk)


        
#Gives contents of the pdf in binary format,pdf is a binary file
#To decode into human readable format, use the decode function, use the decode function, cannot decode byte data but can do html pages

#If I want to download the file I should be worried about the length of my document
#Can't download large files in 1 go, maybe 256 bytes in 1 go
#Can also download csv files in a similar fashion
#To make it more pretty I can add some animations

a={3,4,22,78}
for i in tqdm.tqdm(a):
    time.sleep(1)