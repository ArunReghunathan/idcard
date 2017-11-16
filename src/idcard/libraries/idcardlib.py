import os

import pyqrcode

from django.contrib.staticfiles.templatetags.staticfiles import static

from reportlab.lib.pagesizes import portrait
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

from src.common.libraries.helper import upload_to_s3


def generate_qrcode(test='Arun Reghunathan', path='static/idCard/qrcodes/', scale=2):

    url = pyqrcode.create(test, error='L')
    test = test.replace("/", "_")
    with open(path + test + '.png', 'w') as fstream:
        url.png(fstream, scale=scale, module_color="#000", background=[255,255,255,255])

    return path + test + '.png'

def generate_idcard(paramObject, file_name="idcard", path="static/idCard/idcards/"):

    file_name = str(file_name) + ".pdf"
    height, width = A4

    #get files
    qrcode =  generate_qrcode(paramObject.qrCode)
    bg = static("idCard/bg.png")
    pic = static("idCard/my.jpg")
    frame = static("idCard/picframe.png")
    idcard = static("idCard/idcardframe.png")

    # get the fonts
    font_dirpath = static("idCard/fonts/")
    font_list = os.listdir(font_dirpath)
    for font in font_list:
        if ".ttf" in font:
            font_path = os.path.join(font_dirpath, font)
            font_name = os.path.splitext(font)[0]
            pdfmetrics.registerFont(TTFont(font_name, font_path))
    if paramObject.Language == "M":
        fontList = ["ML_TT_Thunchan_Bold", "Goodnewsj Roman", "Dyuthi-Regular" ]
    else:
        fontList = ["Dyuthi-Regular", "Dyuthi-Regular", "Dyuthi-Regular" ]

    #generate pdf
    pic = ImageReader(paramObject.pic)
    c = Canvas(path + file_name)
    c.setPageSize(portrait(A4))
    c.setLineWidth(.3)
    c.drawImage(image=bg, x=0, y=0, width=width, height=height, preserveAspectRatio=True)
    # c.drawImage(image=idcard, x=1, y=1, width=2.125*inch, height=3.370*inch, mask='auto')
    c.drawImage(image=pic, x=26, y=98.4, width=90, height=90, mask='auto')
    # c.drawImage(image=frame, x=25, y=97.4, width=100, height=100, mask='auto')
    c.drawImage(image=qrcode, x=110, y=2, width=43, height=43, mask='auto')
    c.drawImage(image=idcard, x=1, y=1, width=2.125*inch, height=3.370*inch, mask='auto')

    c.setFont(psfontname=fontList[0], size=18)
    c.setFillColor("#eeeeee")
    c.drawCentredString(x=80, y=205, text=paramObject.heading)
    c.setFont(psfontname=fontList[1], size=12)
    c.setFillColor("#555555")
    c.drawCentredString(x=75, y=82, text=paramObject.Name)
    c.setFont(psfontname=fontList[2], size=11)
    c.drawCentredString(x=75, y=68, text=paramObject.PhoneNumber)


    #card 2
    c.drawImage(image=idcard, x=1+2+2.125*inch, y=1, width=2.125*inch, height=3.370*inch, mask='auto')
    c.drawImage(image=pic, x=26+2+2.125*inch, y=98.4, width=90, height=90, mask='auto')
    # c.drawImage(image=frame, x=25+2+2.125*inch, y=97.4, width=100, height=100, mask='auto')
    c.drawImage(image=qrcode, x=110+2+2.125*inch, y=2, width=43, height=43, mask='auto')
    c.drawImage(image=idcard, x=1+2+2.125*inch, y=1, width=2.125*inch, height=3.370*inch, mask='auto')

    c.setFont(psfontname=fontList[0], size=18)
    c.setFillColor("#eeeeee")
    c.drawCentredString(x=80+2+2.15*inch, y=205, text=paramObject.heading)
    c.setFont(psfontname=fontList[1], size=12)
    c.setFillColor("#555555")
    c.drawCentredString(x=75+2+2.15*inch, y=82, text=paramObject.Name)
    c.setFont(psfontname=fontList[2], size=11)
    c.drawCentredString(x=75+2+2.15*inch, y=68, text=paramObject.PhoneNumber)

    #card 3

    c.drawImage(image=pic, x=26+2+2.125*inch+2+2.125*inch, y=98.4, width=90, height=90, mask='auto')
    # c.drawImage(image=frame, x=25+2+2.125*inch+2+2.125*inch, y=97.4, width=100, height=100, mask='auto')
    c.drawImage(image=qrcode, x=110+2+2.125*inch+2+2.125*inch, y=2, width=43, height=43, mask='auto')
    c.drawImage(image=idcard, x=1 + 2 + 2.125 * inch + 2 + 2.125 * inch, y=1, width=2.125 * inch, height=3.370 * inch,
                mask='auto')

    c.setFont(psfontname=fontList[0], size=18)
    c.setFillColor("#eeeeee")
    c.drawCentredString(x=80+2+2.15*inch+2+2.125*inch, y=205, text=paramObject.heading)
    c.setFont(psfontname=fontList[1], size=12)
    c.setFillColor("#555555")
    c.drawCentredString(x=75+2+2.15*inch+2+2.125*inch, y=82, text=paramObject.Name)
    c.setFont(psfontname=fontList[2], size=11)
    c.drawCentredString(x=75+2+2.15*inch+2+2.125*inch, y=68, text=paramObject.PhoneNumber)

    c.save()
    print "uploading to s3"
    os.remove(qrcode)
    return upload_to_s3("", path+file_name)
