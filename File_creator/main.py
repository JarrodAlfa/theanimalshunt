print('[List of file types: ]')
print('|txt')
print('|php')
print('|html')
print('|css')
print('[---------------------]')

while True:
    _fileTypes = ['txt', 'php', 'html', 'css']
    _fileType = input("Enter file type: ")
    if any(ext in _fileType for ext in _fileTypes):
        break
    else:
        print("!!Invalid file type!!")

def _makeFile ():
    _fileName = input('Enter file name: ')
    _newFile = open(f'{_fileType}/{_fileName}' + f'.{_fileType}', 'w')

_makeFile()