# -*- coding:utf-8 -*- 
from django.test import LiveServerTestCase
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
# import time;
import unittest;
# from distutils.dist import warnings
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox();
        self.browser.implicitly_wait(1);
    def tearDown(self):
        self.browser.refresh();
        self.browser.quit();
    def check_for_row_in_lists_table(self,row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
#         time.sleep(10)
        self.check_for_row_in_lists_table('1:Buy peacock feathers')
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
#         time.sleep(10)
        self.check_for_row_in_lists_table('1:Buy peacock feathers')
#         time.sleep(10)
        self.check_for_row_in_lists_table('2:Use peacock feathers to make a fly')
    
    
# 模拟一个新人登录
        self.browser.quit()
        self.browser=webdriver.Firefox()
        
        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
#唯一的URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)  
if __name__=='__main__':
    unittest.main(warnings='ignore')