import binascii
import nfc

def on_connect(tag):
    for record in tag.ndef.records:
        print(record)    
    return True

if __name__ == '__main__':
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect':on_connect})
