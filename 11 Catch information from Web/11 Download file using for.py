import requests

res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') #78981 Bytes
res.raise_for_status()
playFile = open('RomeoAndJuliet-3.txt','wb') # create a new file, will save in current cd, wb means binary string?>
#the reason we need binary is to save "unicode encoding" in this text
for chunk in res.iter_content(100000):      #chunk厚切, 一応10w Bytesをファイル容量とする
    playFile.write(chunk)   #Write returns a number, means how many bytes will write to file

playFile.close()

