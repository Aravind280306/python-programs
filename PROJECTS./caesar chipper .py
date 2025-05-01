symbols='ABCDEFGHJKLMNOPQRSTUVWXYZ'
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response=input('>').lower()
    if response.startswith('e'):
        mode='encrypt'
        break
    elif response.startswith('d'):
        mode='decrypt'
        break
    print("Please Enter e or d")
while True :
    maxkey=len(symbols)-1
    print('please enter the key to use ( 0 to {}) :'.format(maxkey))
    response=input('>').upper()
    if not response.isdecimal():
        continue
    elif 0<= int(response)<len(symbols):
        key=int(response)
        break
print("enter the message to format {}".format(mode))
message=input('>')
message=message.upper()
translated=''
for symbol in  message:
    if symbol in symbols:
        num=symbols.find(symbol)
        if mode=='encrypt':
            num=num+key
        elif mode=='decrypt':
            num=num-key
        if num>=len(symbols):
            num=num-len(symbols)
        elif num<0:
            num=num+len(symbols)
        translated=translated+symbols[num]
    else:
        translated=translated+symbol
print(translated)
