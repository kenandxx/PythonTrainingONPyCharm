#!python3
# Webbrowser: within Python, open specific webpage
# Requests: download files and webpages from internet
# Beautiful Soup: analize HTML, it is the web basic format
# selenium: launch and control a web browser. it can fill forms and simulate as mouse to click in browser
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
# import webbrowser as wb
# wb.open(' http:// inventwithpython. com/')

import webbrowser, sys,pyperclip
if len(sys.argv)>1:
    # get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

# sys.argv is a virable saves file name and command line list, if this list is not only with file nmae,
# then len(sys.argv) will return >1
# sys.argv is a list of strings, [1:] cut off the first element, the string will save to varaible of address
# Todo: Get address from clipboard.
