import nfc
import binascii
import ndef

def on_connect(tag):
    old_record = tag.ndef.records
    uri, title = 'http://nfcpy.org', 'nfcpy project'
    new_record = [ndef.SmartposterRecord(uri, title)]
    if old_record == new_record:
        print("already written")
    else:
        tag.ndef.records = new_record
        print("Complete!")
    return True

if __name__ == '__main__':
    print('------------Waiting for writing--------------')
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect':on_connect})
    print('------------      Finish       --------------')
