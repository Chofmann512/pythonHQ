from PIL import Image
import pytesseract
import pyautogui, os
import pycurl
import certifi
from StringIO import StringIO
import time

count=0
start_time = time.time()
Ans1=0
Ans2=0
Ans3=0

###QUESTION
im = pyautogui.screenshot(region=(720,215, 475, 150))
im.save('test1.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = Image.open('test1.jpg')

questionText = pytesseract.image_to_string(img)
print("Question:")
print(questionText)
###ANSWER1
im = pyautogui.screenshot(region=(760,440, 390, 60))
im.save('test2.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = Image.open('test2.jpg')

answer1Text = pytesseract.image_to_string(img)

###ANSWER2
im = pyautogui.screenshot(region=(760,540, 390, 60))
im.save('test3.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = Image.open('test3.jpg')

answer2Text = pytesseract.image_to_string(img)

###ANSWER3
im = pyautogui.screenshot(region=(760,640, 390, 60))
im.save('test4.jpg')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

img = Image.open('test4.jpg')

answer3Text = pytesseract.image_to_string(img)


questionText = questionText.replace(" ","+")

answer1Text=answer1Text.strip('\n')
answer1Text=answer1Text.strip('\t')
answer1Text= answer1Text.replace('\n','')
answer1Text= answer1Text.replace('\t','')
answer1Text= answer1Text.replace(' ','')
answer1Text = answer1Text.encode('ascii')
answer1Text = answer1Text.lower()

answer2Text=answer2Text.strip('\n')
answer2Text=answer2Text.strip('\t')
answer2Text= answer2Text.replace('\n','')
answer2Text= answer2Text.replace('\t','')
answer2Text= answer2Text.replace(' ','')
answer2Text = answer2Text.encode('ascii')
answer2Text = answer2Text.lower()

answer3Text=answer3Text.strip('\n')
answer3Text=answer3Text.strip('\t')
answer3Text= answer3Text.replace('\n','')
answer3Text= answer3Text.replace('\t','')
answer3Text= answer3Text.replace(' ','')
answer3Text = answer3Text.encode('ascii')
answer3Text = answer3Text.lower()

print("Answer1:")
print(answer1Text)
print("Answer2:")
print(answer2Text)
print("Answer3:")
print(answer3Text)
    
###Websearch
url = "https://www.google.com/search?q="+questionText
url=url.strip('\n')
url=url.strip('\t')
url= url.replace('\n','+')
url= url.replace('\t','')
url = url.encode('ascii')

#url = (c for c in url if 0 < ord(c) < 127)
#''.join(url)


print(url)

def pageForward(url,answer1Text,answer2Text,answer3Text,Ans1,Ans2,Ans3,count,urlAdd):
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, urlAdd)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()

    content= content.strip('\n')
    content= content.strip('\t')
    content= content.replace('\n','')
    content= content.replace('\t','')
    content= content.replace(' ','')
    try:
        content= content.encode('ascii')
    except UnicodeDecodeError:
        pass

        
    content= content.lower()

    ##print content

    ##Answer Solver


    content = str(content)
    Ans1 = Ans1+content.count(answer1Text)
    Ans2 = Ans2+content.count(answer2Text)
    Ans3 = Ans3+content.count(answer3Text)
    print (Ans1)
    print (Ans2)
    print (Ans3)
    count = count+1
    if(count<5):
        if(count==1):
            urlAdd = url+"&ei=Gs9PW9ryL426tQXh6IfYCA&start=10&sa=N&biw=1280&bih=649"
        if(count==2):
            urlAdd = url+"&ei=tc9PW4X2FpKjjwSG_aTAAg&start=20&sa=N&biw=1280&bih=649"
        if(count==3):
            urlAdd = url+"&ei=KNBPW_65PMPGjwTbyZ6QDQ&start=30&sa=N&biw=1280&bih=649"
        if(count==4):
            urlAdd = url+"&ei=lNBPW8PWDsLysQWD6Z7gBw&start=40&sa=N&biw=1280&bih=649"

        
        pageForward(url,answer1Text,answer2Text,answer3Text,Ans1,Ans2,Ans3,count,urlAdd)
    
urlAdd = url        
pageForward(url,answer1Text,answer2Text,answer3Text,Ans1,Ans2,Ans3,count,urlAdd)


print(time.time()-start_time)
