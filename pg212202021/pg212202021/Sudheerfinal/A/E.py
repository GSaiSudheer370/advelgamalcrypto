try:
    path = input(r'Enter path of Image : ')
    key = int(input('Enter Key for encryption of Image : '))	
    print('The path of file : ', path)
    print('Key for encryption : ', key)	
    fin = open(path, 'rb')	
    image = fin.read()
    fin.close()	
    image = bytearray(image)
    
    for i, values in enumerate(image):
        image[i] = values ^ key
        if(i<10):
            print(i,' = ',values)
            
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('Encryption Done...')
except Exception:
    print('Error caught : ', Exception.__name__)

