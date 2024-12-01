import qrcode
import PIL

img = qrcode.make(r'''
BEGIN:VCARD
VERSION:3.0
N:last;first;;
FN:FN
ORG:Organiztion
# TEL;TYPE=Work:011 555-1212
TEL;TYPE=mobile:404 562-9651
# ADR;TYPE=Work,PREF:;;100 Waters Edge;Baytown;LA;30314;USA
# LABEL;TYPE=Work,PREF:100 Waters Edge\nBaytown\, LA 30314\nUSA
EMAIL;TYPE=Work:example@gmail.com
END:VCARD
''')
type(img)
img.save("v3_qrcode/qr_output/qrcode_contact.png")
img