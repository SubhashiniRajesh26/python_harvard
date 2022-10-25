def main():
    string = input("Enter the filename with extension: ")
    string = string.lower().strip()
    MIMEtype(string)


def MIMEtype(filename):
    
    if '.' not in filename:
        print('application / octet-stream')
        return
    else:
        ext = filename.split('.')[1]
        if  ext == 'gif' or ext == 'jpeg' or ext == 'png':
            print('image /',ext)
        elif ext == 'jpg':
            print('image / jpeg')
        elif ext == 'txt':
            print('text / plain')
        elif ext == 'pdf' or ext == 'zip':
            print('application /',ext)
        else:
            print('application / octet-stream')

main()

