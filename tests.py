# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from page import Page
import HtmlTestRunner
import logging

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=u'testlogs.log')


class TensorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_yandex(self):
        driver = self.driver
        driver.implicitly_wait(3)
        logging.info(u'set wait time 3 sec')
        try:
            driver.get("https://www.yandex.ru/")
            logging.info(u'go to yandex.ru')
        except:
            logging.error(u'cannot go to yandex.ru')
        try:
            assert "Яндекс" in driver.title
            logging.info(u'it is yandex.ru')
        except:
            logging.error(u'it is not yandex.ru')
        try:
            search = Page(driver)
        except:
            logging.error(u'cannot create object of class')
        try:
            search.search_in_yandex('Тензор')
            logging.info(u'input text')
        except:
            logging.error(u"cannot input Тензор")
        try:
            search.check_suggest()
            logging.info(u'suggest is find')
        except:
            logging.error(u'suggest not find')
        try:
            search.click_on_search()
            logging.info(u'click is success')
        except:
            logging.error(u'cannot find button')
        try:
            search.check_link()
            logging.info(u'link is here')
        except:
            logging.error(u'cannot find link')
        assert "No results found." not in driver.page_source

    def test_picture_in_yandex(self):
        driver = self.driver
        driver.implicitly_wait(3)
        logging.info(u'set wait time 3 sec')
        try:
            driver.get("https://www.yandex.ru/")
            logging.info(u'go to yandex.ru')
        except:
            logging.error(u'cannot go to yandex.ru')
        try:
            assert "Яндекс" in driver.title
            logging.info(u'it is yandex.ru')
        except:
            logging.error(u'it is not yandex.ru')
        pick_test = Page(driver)
        try:
            pick_test.click_on_pictures()
            logging.info(u'click on pictures')
        except:
            logging.error(u'cannot click on pictures')
        try:
            assert 'https://yandex.ru/images/' in driver.current_url
            logging.info(u'it is yandex/images')
        except:
            logging.error(u'it is not yandex/images')
        try:
            pick_test.click_on_first_img()
            logging.info(u'first img is found')
        except:
            logging.error(u'first img is not found')
        try:
            pick_test.check_img()
            logging.info(u'image is open')
        except:
            logging.error(u'image is not open')
        try:
            src = pick_test.get_img_src()
            logging.info(u'get argument scr')
        except:
            logging.error(u'cannot get argument scr')
        try:
             pick_test.next_image_button_click()
             logging.info(u'get next img')
        except:
            logging.error(u'cannot get next img')
        try:
            src1 = pick_test.get_img_src()
            logging.info(u'get argument src')
        except:
            logging.error(u'cannot get argument scr')
        if (src == src1):
            logging.info(u'image arnt different')
        else:
            logging.error(u'image are different')
        try:
            pick_test.previous_picture_button_click()
            logging.info(u'click on prev button')
        except:
            logging.error(u'cannot click on prev button')
        try:
            src2 = pick_test.get_img_src()
            logging.info(u'get attribute scr')
        except:
            logging.error(u'cannot get attribute scr')
        if (src1 != src2):
            logging.error(u'image are different')
        else:
            logging.error(u'image arnt different')
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='R:/temzortest/reports'))
