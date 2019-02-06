from selenium import webdriver

chrome_path = 'C://Users/young/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

browser.get('http://localhost:8000')
assert 'Django' in browser.title
# browser.quit()    
