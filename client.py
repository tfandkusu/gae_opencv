import requests

with open('src.jpg','rb') as f:
    data = f.read()
    res = requests.post("https://ip-dot-jjsonplaceholder.appspot.com/binarize", data=data)
    if res.status_code == 200:
        with open('bin.png','wb') as f:
            f.write(res.content)
    else:
        print("Server error : %d" % res.status_code)
