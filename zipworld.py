import zipfile
import time

folderpath = input("path to the file")
zipf = zipfile.ZipFile(folderpath)
global result 
result = 0
global tried 
tried = 0
c = 0
if not zipf:
    print("zipped file is not passowrd protected")
else :
    starttime = time.time()
    wordlistfile=open("wordlist.txt","r",errors="ignore")
    body = wordlistfile.read().lower()
    words = body.split("\n")
    for i in range(len(words)):
        word=words[i]
        password=word.encode("utf8").strip()
        c=c+1
        print("trying to decode password")
        try:
            with zipfile.ZipFile(folderpath,'r')as zf:
                zf.extractall(pwd=password)
                print("success the passsword is"+word)
                endtime=time.time()
                result = 1

            break 
        except:
            pass
    if(result == 0):
        print("sorry, password not found. password is not of 4 characters")  
    else:
        duration=endtime-starttime
        print("success password found after trying '+str(c)+' combinations in '+str(duration)+'seconds")          