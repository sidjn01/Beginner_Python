import webbrowser
#
# webbrowser.open("http://www.python.org/")
#
# help(webbrowser)
#
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9)

chrome = webbrowser.get(using='google-chrome')
chrome.open_new_tab("http://www.python.org/")