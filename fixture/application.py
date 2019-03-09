from selenium import webdriver
from fixture.session import SessionHelper



class Application:


    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif  browser == "chrome":
            self.wd = webdriver.Chrome()
        elif  browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized Browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.base_url=base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def return_to_home_page(self):
        wd = self.wd
        if not len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()

    def open_group_page_by_id(self, id):
        wd = self.wd
        if not wd.current_url.endswith("/?group=%s" % id):
            wd.get(self.base_url + "?group=%s" % id)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False