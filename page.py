from locators import Locators


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.text_box_xpath = Locators.text_box_xpath
        self.suggest_box_class_name = Locators.suggest_box_class_name
        self.button_xpath = Locators.button_xpath
        self.link_text = Locators.link_text
        self.pictures_xpath = Locators.pictures_xpath
        self.image_open_xpath = Locators.image_open_xpath
        self.image_check_xpath = Locators.image_check_xpath
        self.next_picture_button_xpath = Locators.next_picture_button_xpath
        self.previous_picture_button_xpath = Locators.previous_picture_button_xpath
        self.attribute = Locators.attribute

    def search_in_yandex(self, text):
        """
        find text box by xpath
        """
        self.driver.find_element_by_xpath(self.text_box_xpath).send_keys(text)

    def check_suggest(self):
        """
        find suggest by class name
        """
        self.driver.find_element_by_class_name(self.suggest_box_class_name)

    def click_on_search(self):
        """
        find button by xpath and click on it
        """
        self.driver.find_element_by_xpath(self.button_xpath).click()

    def check_link(self):
        """
        find link by link text
        """
        self.driver.find_element_by_partial_link_text(self.link_text)

    def click_on_pictures(self):
        """
        find pictures button by xpath
        """
        self.driver.find_element_by_xpath(self.pictures_xpath).click()

    def click_on_first_img(self):
        """
        find first image by xpath and click on it
        """
        self.driver.find_element_by_xpath(self.image_open_xpath).click()

    def check_img(self):
        """
        find img in open window
        """
        self.driver.find_element_by_xpath(self.image_check_xpath)

    def get_img_src(self):
        """
        find img in open window and get attribute src
        """
        self.driver.find_element_by_xpath(self.image_check_xpath).get_attribute(self.attribute)

    def next_image_button_click(self):
        """
        find next image button and click on it
        """
        self.driver.find_element_by_xpath(self.next_picture_button_xpath).click()

    def previous_picture_button_click(self):
        """
        find previous image button and click on it
        """
        self.driver.find_element_by_xpath(self.previous_picture_button_xpath).click()
