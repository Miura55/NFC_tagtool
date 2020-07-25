import binascii
import nfc

def on_startup(target):
    print('-----------------Waiting for reading-----------------------')
    print('target:', target)
    return target

def on_connect(tag):
    for record in tag.ndef.records:
        print(record)
    return True

if __name__ == '__main__':
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={
            'on-startup':on_startup,
            'on-connect':on_connect
        })
