from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path, getcwd



class TestHemsida(TestCase):

    # inställningar för hur testerna körs
    stangintebrowsern = True  # om True så hålls webbläsaren öppen efter testerna är klara, annars stängs den
    gomfonstret = True  # visar webbläsaren medan testerna körs

    # setUpClass körs INNAN FÖRSTA testet
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.stangintebrowsern:
            chr_options.add_experimental_option("detach", True)

        if cls.gomfonstret:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass körs EFTER SISTA testet
    @classmethod
    def tearDownClass(cls):
        pass  # gör ingenting

    # setUp körs INNAN VARJE TEST
    def setUp(self):
        pass  # gör ingenting

    # tearDown körs EFTER VARJE TEST
    def tearDown(self):
        self.browser.get('about:blank')  # gå till en tom sida för att undvika att tidigare test påverkar senare

#ändrinf
    # HÄR BÖRJAR TESTERNA
    def testPageText(self):
        self.browser.get(path.join(path.dirname(getcwd()), "JITS-pizzeria", 'index.html'))
        self.assertIn("Välkommen", self.browser.page_source)

    def testPageNumber(self):
        self.browser.get(path.join(path.dirname(getcwd()), "JITS-pizzeria", 'index.html'))
        self.assertIn("018-123456", self.browser.page_source)




# denna bit finns här så att testerna körs om filen körs som vanligt python-program
if __name__ == '__main__':
    main(verbosity=2)
