def senha(senh, passw):
    if passw > senh:
        return
    print(passw)
    senha(senh, passw + 1)


senha(13, 1)
