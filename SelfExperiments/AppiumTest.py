"""
Qxf2: Example script to run one test against the Chess Free app using Appium
The test will:
- launch the app
- click the 'PLAY!' button
"""

import subprocess
import unittest
from pprint import pprint

import uiautomator
from appium import webdriver


class ChessAndroidTests(unittest.TestCase):
    """Class to run tests against the Chess Free app"""

    def setUp(self):
        """Setup for the test"""

        subprocess.call('adb devices')
        # subprocess.call('adb install -r ../Resources/Chess.apk')
        d = uiautomator.Device('d575cc380904')
        pprint(d.info)
        d.press('home')  # looks like this doesn't work with virtual navigation bar
        d.press('back')
        d.screenshot("home.png")
        d.open.notification()
        d.screenshot("notifications.png")
        desired_caps = {'platformName': 'Android', 'platformVersion': '8.1', 'deviceName': 'vince',
                        'app': 'C:/Users/anton.shevchuk/PycharmProjects/pythonFirst/Resources/Chess.apk',
                        'appPackage': 'uk.co.aifactory.chessfree', 'appActivity': '.ChessFreeActivity'}
        # Returns abs path relative to this file and not cwd
        # Returns abs path relative to this file and not cwd
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
    #     "Tear down the test"
    #     self.driver.quit()

    def test_single_player_mode(self):
        """Test the Chess app launches correctly and click on Play button"""
        # element = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/ButtonPlay")
        driver = self.driver
        element = driver.open_notifications()
        # element.click()
        driver.lock()
        driver.unlock()
        print("These are settings:\n")
        pprint(driver.get_settings())
        driver.close_app()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
