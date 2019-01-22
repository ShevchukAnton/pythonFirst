"""
Qxf2: Example script to run one test against the DuckduckGo browser app using Appium
The test will:
- launch the browser
- search for 'appium'
- save screenshot"""

import unittest

from appium import webdriver


class AndroidTests(unittest.TestCase):
    """Class to run tests against the Chess Free app"""

    def setUp(self):
        """Setup for the test"""

        # subprocess.call('adb devices')
        # subprocess.call('adb install -r ../Resources/Chess.apk')
        # d = uiautomator.Device('d575cc380904')
        # pprint(d.info)
        # d.press('home')  # looks like this doesn't work with virtual navigation bar
        # d.press('back')
        # d.screenshot("home.png")
        # d.open.notification()
        # d.screenshot("notifications.png")
        desired_caps = {'platformName': 'Android', 'platformVersion': '8.1', 'deviceName': 'vince',
                        'appPackage': 'com.duckduckgo.mobile.android', 'appActivity': 'com.duckduckgo.app.browser.BrowserActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    def test_single_player_mode(self):
        driver = self.driver
        element = self.driver.find_element_by_id('com.duckduckgo.mobile.android:id/omnibarTextInput')
        # element.click()
        element.send_keys('appium')
        driver.get_screenshot_as_file('duck.appium.png')
        driver.press_keycode(66)
        driver.wait_activity('com.duckduckgo.mobile.android:id/browserLayout', 5)
        element = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View/android.view.View/android.view.View[3]/android.view.View')
        assert element.is_displayed()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity = 2).run(suite)
