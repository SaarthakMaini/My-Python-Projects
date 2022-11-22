import selenium
from webdriver_manager.chrome import ChromeDriverManager
# webdriver : tells the chrome tab to do operation on,chrome object to access web browser
#selenium is a framework
print(selenium.__file__)
chrome=selenium.webdriver.Chrome(ChromeDriverManager().install())# parameter : path from where web driver should be accessed
# chrome.get('https://web.whatsapp.com')
#Whatever you want to do in browser would be done by script
#Opposite of the above is the functionality of the request module