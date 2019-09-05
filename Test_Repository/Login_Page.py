from  ZBase_Framework.Utilities.UIObjects  import Utilities as uiobject

Userxpath = "XPATH=//input[contains(@id,'txtUserID')]"
passxpath = "XPATH=/html[1]/body[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
login_button = "Xpath=//input[@id='btnLogin']"
logout = "Xpath=//a[@id='Header1__HeaderMenu1_btnLogout']"
wf_inbox = "Xpath=//a[contains(text(),'APInvoices(7)')]"
verify_wfinbox_folder = "XPATH=//td[contains(text(),'APInvoices')]"

class Loginpage(uiobject):


    def __init__(self,name = "vinay"):
        self.Name = name



    def browser_launch(self,browser =''):
        uiobject.browserlaunch(self,browser)

    def browser_url(self,url=''):
        uiobject.Openurl(self,url)

    def userid(self,loc = '',username =''):
        val = uiobject.WebLocator_get_element(self,Userxpath)
        val.clear()
        val.send_keys(username)

    def password(self,loc = '',password = ''):
        passw = uiobject.WebLocator_get_element(self,passxpath)
        passw.clear()
        passw.send_keys(password)

    def click_login(self):
        Click = uiobject.WebLocator_get_element(self,login_button)
        Click.click()

    def click_logout(self):
        Click = uiobject.WebLocator_get_element(self,logout)
        Click.click()

    def click_wfinbox(self):
        wfin = uiobject.WebLocator_get_element(self,wf_inbox)
        #weinbox_verify = uiobject.initialwebdriver(verify_wfinbox_folder)
        verifytext = wfin.text
        veri = str(verifytext).split('(')
        #print(verifytext)
        if veri[0] == "APInvoices":
            wfin.click()
        else:
            print("failed to find ap invoice folder to click")
