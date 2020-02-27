import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest_post(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_use_website(self):
        # วันนี้ เอ็มมีปัญหาเกี่ยวกับการบวก ลบ คูณ หาร เลขมากๆ
        # เขาได้ไปเจอเว็บไซต์เว็บหนึ่ง มันมีการรับข้อมูลเเบบ POST
        self.browser.get(self.live_server_url + "/post")

        # สุดยอดไปเลย เว็บนี้มันเป็นเว็บเครื่องคิดเลข เพราะชื่อเเท็บมันคือ Calculator
        self.assertIn('Calculator', self.browser.title)

        # เเละเขาได้เห็นหัวข้อของเว็บไซต์เป็น Calculator
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator POST', header_text)

        # เขาได้รู้ว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ด้านหลังก็มี ข้อความว่า Result ด้วย มันเอาไว้บอกผลลัพธ์ สินะ ; เขาพูดกับตัวเอง
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Result', result_text)

        self.fail('Finish the test!')

    def test_user_can_plus_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองบวกเลขดู
        self.browser.get(self.live_server_url + "/post")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 112 ลงไป
        inputbox_x.send_keys('112')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 888 ลงไป
        inputbox_y.send_keys('888')

        # จากนั้นเขาก็กดปุ่ม +
        plus_button = self.browser.find_element_by_name('plus')
        plus_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 1000 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('1000', result_text)

        self.fail('Finish the test!')

    def test_user_can_sub_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองลบเลขดู
        self.browser.get(self.live_server_url + "/post")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 123 ลงไป
        inputbox_x.send_keys('123')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 23 ลงไป
        inputbox_y.send_keys('23')

        # จากนั้นเขาก็กดปุ่ม -
        sub_button = self.browser.find_element_by_name('sub')
        sub_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 100 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('100', result_text)

        self.fail('Finish the test!')

    def test_user_can_multi_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองคูณเลขดู
        self.browser.get(self.live_server_url + "/post")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 25 ลงไป
        inputbox_x.send_keys('25')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 25 ลงไป
        inputbox_y.send_keys('25')

        # จากนั้นเขาก็กดปุ่ม *
        multi_button = self.browser.find_element_by_name('multi')
        multi_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 625 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('625', result_text)

        self.fail('Finish the test!')

    def test_user_can_div_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองหารเลขดู
        self.browser.get(self.live_server_url + "/post")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 900 ลงไป
        inputbox_x.send_keys('900')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 45 ลงไป
        inputbox_y.send_keys('45')

        # จากนั้นเขาก็กดปุ่ม /
        div_button = self.browser.find_element_by_name('div')
        div_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 20 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('20', result_text)

        self.fail('Finish the test!')


class NewVisitorTest_get(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_use_website(self):
        # วันนี้ เอ็มมีปัญหาเกี่ยวกับการบวก ลบ คูณ หาร เลขมากๆ
        # เขาได้ไปเจอเว็บไซต์เว็บหนึ่ง มันมีการรับข้อมูลเเบบ GET
        self.browser.get(self.live_server_url + "/get")

        # สุดยอดไปเลย เว็บนี้มันเป็นเว็บเครื่องคิดเลข เพราะชื่อเเท็บมันคือ Calculator
        self.assertIn('Calculator', self.browser.title)

        # เเละเขาได้เห็นหัวข้อของเว็บไซต์เป็น Calculator
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator GET', header_text)

        # เขาได้รู้ว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ด้านหลังก็มี ข้อความว่า Result ด้วย มันเอาไว้บอกผลลัพธ์ สินะ ; เขาพูดกับตัวเอง
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Result', result_text)

        self.fail('Finish the test!')

    def test_user_can_plus_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองบวกเลขดู
        self.browser.get(self.live_server_url + "/get")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 112 ลงไป
        inputbox_x.send_keys('112')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 888 ลงไป
        inputbox_y.send_keys('888')

        # จากนั้นเขาก็กดปุ่ม +
        plus_button = self.browser.find_element_by_name('plus')
        plus_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 1000 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('1000', result_text)

        self.fail('Finish the test!')

    def test_user_can_sub_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองลบเลขดู
        self.browser.get(self.live_server_url + "/get")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 123 ลงไป
        inputbox_x.send_keys('123')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 23 ลงไป
        inputbox_y.send_keys('23')

        # จากนั้นเขาก็กดปุ่ม -
        sub_button = self.browser.find_element_by_name('sub')
        sub_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 100 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('100', result_text)

        self.fail('Finish the test!')

    def test_user_can_multi_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองคูณเลขดู
        self.browser.get(self.live_server_url + "/get")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 25 ลงไป
        inputbox_x.send_keys('25')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 25 ลงไป
        inputbox_y.send_keys('25')

        # จากนั้นเขาก็กดปุ่ม *
        multi_button = self.browser.find_element_by_name('multi')
        multi_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 625 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('625', result_text)

        self.fail('Finish the test!')

    def test_user_can_div_number(self):
        # จากนั้นเขาก็เขาไปที่เว็บเดิม เพื่อที่จะลองหารเลขดู
        self.browser.get(self.live_server_url + "/get")

        # เขาเห็นว่า เว็บนี้มีช่องใส่ตัวเลข 2 ช่อง
        inputbox_x = self.browser.find_element_by_id('id_x')
        inputbox_y = self.browser.find_element_by_id('id_y')

        # ในช่อง X มี hint text คือ Enter your first number
        # มันเเปลว่าใส่เลขจำนวนเเรกของคุณ
        self.assertEqual(
            inputbox_x.get_attribute('placeholder'),
            'Enter your first number'
        )

        # ช่อง X เขาใส่เลข 900 ลงไป
        inputbox_x.send_keys('900')

        # ในช่อง Y มี hint text คือ Enter your second number
        # มันเเปลว่าใส่เลขจำนวนที่สองของคุณ
        self.assertEqual(
            inputbox_y.get_attribute('placeholder'),
            'Enter your second number'
        )

        # ช่อง Y เขาใส่เลข 45 ลงไป
        inputbox_y.send_keys('45')

        # จากนั้นเขาก็กดปุ่ม /
        div_button = self.browser.find_element_by_name('div')
        div_button.send_keys(Keys.ENTER)
        time.sleep(1)

        # ว้าว เว็บนี้คำนวณได้ผลลัพธ์ 20 ตามเฉลยเลย
        result_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('20', result_text)

        self.fail('Finish the test!')