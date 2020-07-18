import nfc

def on_connect(tag):
    tag_type = tag.type
    version = {'Type1Tag': 0x12, 'Type2Tag': 0x12,
               'Type3Tag': 0x10, 'Type4Tag': 0x30}[tag_type]
    formatted = tag.format(version=version)
    if formatted:
        print('Formatted {}'.format(tag))
        if tag.ndef:
            print("  readable = %s" % ("no", "yes")[tag.ndef.is_readable])
            print("  writable = %s" % ("no", "yes")[tag.ndef.is_writeable])
            print("  capacity = %d byte" % tag.ndef.capacity)
            print("  message  = %d byte" % tag.ndef.length)
    elif formatted is None:
        print("Cannot formatted")
    else:
        print("Sorry, this tag is not abailable to format")
    return True

if __name__ == '__main__':
    print('------------Waiting for writing--------------')
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect':on_connect})
    print('------------      Finish       --------------')
