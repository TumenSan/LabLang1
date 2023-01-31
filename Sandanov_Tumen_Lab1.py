import requests
import os
from tqdm import tqdm

print('input url')
url = input()
#print(url.rfind('/'))
Slash = url.rfind('/') + 1
FileName = (url[Slash:len(url):1])

AtTheSameFile = 0
for root, dirs, files in os.walk("."):  
    for filenameFolder in files:
        print(filenameFolder)
        if FileName == filenameFolder:
            AtTheSameFile = 1
            break

response = requests.get(url)
if ((response.status_code == 200) & (AtTheSameFile == 0)):
    with open(FileName, 'wb') as f:
        f.write(response.content)
    with tqdm.wrapattr(open(os.devnull, "wb"), "write",
                   miniters=1, desc=FileName.split('/')[-1],
                   total=int(response.headers.get('content-length', 0))) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
        print('success')
else:
    print('error')
print('end')


#url = "http://craphound.com/images/1006884_2adf8fc7.jpg"




