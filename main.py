from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import ast
import selenium
from subprocess import Popen, PIPE









class Snap:
	def __init__(self):
		# "appPackage": "com.snapchat.android",
		#    "appActivity": "com.snapchat.android.LandingPageActivity",
		

		
		self.count = 0
		self.users = []
		self.desired_caps = {
		   "deviceName": "emulator-5554",
		   "platformName": "Android"
		}
		   # 'MobileCapabilityType.NEW_COMMAND_TIMEOUT': '300'



		try:
			self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
		except:
			self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
		self.actions = TouchAction(self.driver)
		self.wait = WebDriverWait(self.driver, 100)
		if self.driver.is_locked():
			self.unlock()
	
	def open(self):
		print(self.driver.current_activity)
		if self.driver.current_activity == "com.snap.identity.loginsignup.ui.LoginSignupActivity":
			return
		elif self.driver.current_activity != '.LandingPageActivity':
			self.driver.swipe(700, 1200, 700, 800)
			self.driver.find_elements(By.XPATH, '//android.widget.TextView[@content-desc="Snapchat"]')[0].click()
		

	def unlock(self):
		self.driver.find_elements(By.ID, 'com.android.systemui:id/kg_alternative_password')[0].click()
		self.driver.find_elements(By.ID, 'com.android.systemui:id/passwordEntry')[0].send_keys("phone pin")
		self.driver.press_keycode(66)
		time.sleep(2)
		
	def login(self): #tofix: empty login fields before sending keys
		print("logging in")
		try:
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/login_button_horizontal')[0].click()
			time.sleep(2)
		except Exception as ex:
			print(ex)
			try:
				self.driver.find_elements(By.ID, 'com.snapchat.android:id/account_login_button')[0].click()
			except:
				pass
		# self.#(//android.view.View[@content-desc="New Chat"])[1]/javaClass[2]
		else:
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/username_or_email_field')[0].send_keys(self.user)
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/password_field')[0].send_keys(self.password) #below are permissions that are accepted
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout')[0].click()
			self.wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout')))       
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout')[0].click()
			time.sleep(5)
			try:
				self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]')[0].click()
				time.sleep(3)
				self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]')[0].click()
				time.sleep(3)
				self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]')[0].click()
			except:#no allow persmissions popped up
				pass 
	
	def import_snaps(self, xpath): # import a snap into memories needed only to post on story 
			self.driver.find_elements(By.XPATH, xpath)[0].click()
			TouchAction(self.driver).tap(None, 1354, 92, 1).perform()
			TouchAction(self.driver).tap(None, 310, 1710, 1).perform()
			time.sleep(2)
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView')[0].click()
			time.sleep(2)
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView')[0].click()
			self.driver.back()
			self.driver.back() 
	
	def accept_adds(self): 
		contin = True 
		try: #we are not in home
			try:
				self.count = self.driver.find_elements(By.ID, 'com.snapchat.android:id/circular_notification_count').text
			except:
				pass
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/hova_header_add_friend_icon')[0].click()
		except Exception as ex:
			self.driver.back()
			time.sleep(2)
			try:
				self.count = self.driver.find_elements(By.ID, 'com.snapchat.android:id/circular_notification_count').text
			except:
				self.count = 0
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/hova_header_add_friend_icon')[0].click()
			time.sleep(2)
		else:
			pass
		try:
			view_more = self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.view.View')
			self.count = int(str(view_more.text).split(' ')[1]) + 5
			view_more[0].click()
		except:
			try:
				view_more = self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.view.View/javaClass')
				self.count = int(str(view_more.text).split(' ')[1]) + 5
				view_more[0].click()
			except:
				print('you dont have any new adds!')
				contin = False
			
		l = 2

		while contin:
			try:
				xpath1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[' + str(l) + ']/android.view.View/android.view.View[3]'
				add = self.driver.find_elements(By.XPATH, xpath1)[0].click()
				try:
					textbox = self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')

				except:
					pass
				else:
					if self.driver.is_keyboard_shown():
						self.driver.back()
						self.driver.back()
					else:
						self.driver.back()
				try:
					self.driver.find_elements(By.ID, 'com.snapchat.android:id/lenses_camera_lens_button_view')
				except:
					pass
				else:
					if self.driver.is_keyboard_shown():
						self.driver.back()
						self.driver.back()
					else:
						self.driver.back()
				# try:
				# 	xpath2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[' + str(l) + ']/android.view.View/android.view.View[2]'
				# 	if self.driver.find_elements(By.XPATH, xpath2):
				# 		add[0].click()
				# except  Exception as es: #cant find cancel button so its not a add request
				# 	print(es)
				# 	print('not a damn request')
				# 	pass
				l += 1
				time.sleep(2)
				if l == int(self.count):
					break

			except Exception as ex:

				self.driver.swipe(700, 2000, 700, 1200)
				time.sleep(1)
				try:
					self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
				except:
					pass
				else:
					self.driver.back()
					self.driver.back()
				try:
					view_more = self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]/android.view.View')[0].click()
				except:
					self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[9]/android.view.View')[0].click()
		self.driver.back()

	def checkuser(self, username, xpath): #checks if username exists in users and returns message to be sent

		message = ''
		for j in range(len(self.users)):
			if username == self.users[j]['user']:

				if self.users[j]['messages'] == 1:
					if  self.messages["message2"]['type'] == 'TEXT':
						message = self.messages["message2"]['message']
					elif self.messages["message2"]['type'] == ('IMAGE' or 'VID'):

						self.send_snaps(username, xpath, self.messages['message2']['message'], self.messages['message2']['type'], self.messages['message2']['src'])

						message = 'SNAP_SENT'
						pass
					self.users[j]['messages'] = 2
					break
					
				elif self.users[j]['messages'] == 2:
					# message = self.messages[2]
					if  self.messages["message3"]['type'] == 'TEXT':
						message = self.messages["message3"]['message']
					elif self.messages["message3"]['type'] == ('IMAGE'or'VID'):
						
						self.send_snaps(username, xpath, self.messages['message3']['message'], self.messages['message3']['type'], self.messages['message3']['src'])
						message = 'SNAP_SENT'
					# self.users[j]['messages'] = 2
					self.users[j]['messages'] = 3
					break
				elif self.users[j]['messages'] == 3:
					if  self.messages["message4"]['type'] == 'TEXT':
						message = self.messages["message4"]['message']
					elif self.messages["message4"]['type'] == ('IMAGE'or'VID'):
						self.send_snaps(username, xpath, self.messages['message4']['message'], self.messages['message4']['type'], self.messages['message4']['src'])
						message = 'SNAP_SENT'
					# self.users[j]['messages'] = 2
					self.users[j]['messages'] = 4
					break
				elif self.users[j]['messages'] == 4:
					message = 'chat_finished'
					break
		if message == '':
			message = 'not_found'
		print('message is :' + message)
		return message

	def checkmsgs(self): #tofix: should be opened from any page answer messages basicly
		# shielf.driver.swipe(250, 1500, 700, 1500)
		self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View[1]')[0].click()
		time.sleep(2)
		try:
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/exit_location_access_title')
			self.driver.find_elements(By.ID, 'com.snapchat.android:id/not_now_location_access')[0].click()
			
		except: #we are not in the snap map which is good
			pass
		file = 'path/to/users.txt'
		probe = open(file, 'r', encoding='utf-8')
		dirty = probe.readlines()
		probe.close()
		try:
			for i in dirty:
				self.users.append(ast.literal_eval(i.replace('\n', '')))
		except:
			print(i)
		probe.close()
		# print(self.users)
		i = 1
		m = 1
		g = 1
		swipes = 0
		second_swipes = False	
		while True:
			p1 = False
			p2 = False
			p3 = False
			p4 = False 
			try:#say hi
				# snapbtn = self.driver.find_elements(By.XPATH, '(//android.view.View[@content-desc="Say hi!"])[1]/android.view.View[2]')
				xpath1 = '(//android.view.View[@content-desc="Say hi!"])[' + str(i) +  ']/'
				chat = self.driver.find_elements(By.XPATH, xpath1 + 'javaClass[2]')
				username = self.driver.find_elements(By.ID, xpath1 + 'javaClass[1]').text
				profile = xpath1 + 'android.view.View[1]'
				swipes = 0
				message = self.checkuser(username, profile)
				if message == 'not_found':
					print('user not found in users')
					self.users.append({'user': username, 'messages': 1})
					textbox = self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
					if self.messages["message1"]['type'] == 'TEXT':
						message = self.messages["message1"]['message']
						textbox.clear()		
						textbox[0].send_keys(message)
						time.sleep(2)
						self.driver.press_keycode(66)
					else:
						self.send_snaps(username, profile, self.messages["message1"]['message'], self.messages["message1"]['type'], self.messages["message1"]['src'])
				
				self.driver.back()
				self.driver.back()
				
			except selenium.common.exceptions.NoSuchElementException as ex:
				p1 = True


			try: #NEW CHAT
				xpath2 = '(//android.view.View[@content-desc="New Chat"])[' + str(i)  + ']/'
				chat = self.driver.find_elements(By.XPATH, xpath2 + 'javaClass[2]')
				username = self.driver.find_elements(By.XPATH, xpath2 + 'javaClass[1]').text
				profile2 = xpath2 + 'android.view.View[1]'
				message = self.checkuser(username, profile2)
				if message == 'not_found':
					print('user not found in users')
					self.users.append({'user': username, 'messages': 1})
					if self.messages["message1"]['type'] == 'TEXT':
						message = self.messages["message1"]['message']
					else:
						self.send_snaps(username, profile2, self.messages["message1"]['message'], self.messages["message1"]['type'], self.messages["message1"]['src'])
				
				if message == 'chat_finished': 
					i += 1 
					pass
				elif message == 'SNAP_SENT':
					self.driver.back()
					self.driver.back()
				else:
					swipes = 0
					print('sending : ' + str(message))
					chat[0].click()
					textbox = self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
					textbox.clear()
					textbox[0].send_keys(message)
					time.sleep(2)
					self.driver.press_keycode(66)
					self.driver.back()
					self.driver.back()
				
			except selenium.common.exceptions.NoSuchElementException as ex:
				p2 = True
				

			try:#new snap t
				xpath3 = '(//android.view.View[@content-desc="New Snap"])[' + str(m) + ']/'
				chat = self.driver.find_elements(By.XPATH, xpath3 + 'javaClass[2]')
				username = self.driver.find_elements(By.XPATH, xpath3 + 'javaClass[1]').text
				profile3 = xpath3 + 'android.view.View[1]'
				message = self.checkuser(username, profile3)
				if message == 'not_found':
					print('user not found in users')
					self.users.append({'user': username, 'messages': 1})
					if self.messages["message1"]['type'] == 'TEXT':
						message = self.messages["message1"]['message']
					else:
						self.send_snaps(username, profile3, self.messages["message1"]['message'], self.messages["message1"]['type'], self.messages["message1"]['src'])

				if message == 'chat_finished': 
					m += 1 
					pass
				elif message == 'SNAP_SENT':
					pass
				else:
					
					swipes = 0
					chat[0].click()
					# self.driver.back()
					self.driver.find_elements(By.XPATH, '//android.widget.FrameLayout[@content-desc="opera_content_index:-1"]/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout')[0].click()
					textbox = self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
					textbox.clear()
					textbox[0].send_keys(message)
					time.sleep(2)
					self.driver.press_keycode(66)
					# self.driver.back()
					self.driver.back()
				
			except selenium.common.exceptions.NoSuchElementException as ex:
				p3 = True
				# print('new Snaps not found ')
				
			try:#RECIEVED
				xpath4 = '(//android.view.View[@content-desc="Received"])[' + str(g)  + ']/'
				chat = self.driver.find_elements(By.XPATH, xpath4 + 'javaClass[2]')
				username = self.driver.find_elements(By.XPATH,  xpath4 + 'javaClass[1]').text
				profile4 = xpath4 + 'android.view.View[1]'
				message = self.checkuser(username, profile4)
				if message == 'not_found':
					print('user not found in users')
					self.users.append({'user': username, 'messages': 1})
					if self.messages["message1"]['type'] == 'TEXT':
						message = self.messages["message1"]['message']
					else:
						self.send_snaps(username, profile4, self.messages["message1"]['message'], self.messages["message1"]['type'], self.messages["message1"]['src'])

				if message == 'chat_finished': 
					m += 1 
					pass
				elif message == 'SNAP_SENT':
					pass
					# self.driver.back()
					# self.driver.back()
				else:
					swipes = 0
					chat[0].click()
					# self.driver.back()
					self.driver.find_elements(By.XPATH, '//android.widget.FrameLayout[@content-desc="opera_content_index:-1"]/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout')[0].click()
					textbox = self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
					textbox.clear()
					textbox[0].send_keys(message)
					time.sleep(2)
					self.driver.press_keycode(66)
					# self.driver.back()
					self.driver.back()
				
				
			except selenium.common.exceptions.NoSuchElementException as ex:
				p4 = True
				# print('new chats not found ')


				
			try: #if chats ended refresh
				self.driver.find_elements(By.ID, 'com.snapchat.android:id/item')
				self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View[1]')[0].click()

			except:
				pass
				# refresh



			if (p1 and p2 and p3 and p4):
				i = 1
				m = 1
				g = 1

				
				
				try:
					self.driver.find_elements(By.ID, 'com.snapchat.android:id/chat_input_text_field')
				except:
					pass
				else:
					if self.driver.is_keyboard_shown():
						self.driver.back()
						self.driver.back()
					else:
						self.driver.back()
						
				try:
					self.driver.swipe(700, 2000, 700, 1200)
					swipes += 1
				except:
					self.driver.swipe(700, 2000, 700, 1200)
					swipes += 1
				if int(swipes) == 14:
					self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View[1]')[0].click()
					second_swipes = True
					swipes = 0
				if second_swipes == True and swipes == 3:
					break


		wprobe = open(file, 'w', encoding='utf-8')	
		for p in self.users:
			wprobe.write(str(p) + '\n')
		wprobe.close()	

	def send_snaps(self, username, xpath, stext, SnapState, Link, ): #add snaps to  #fix image moving images should be in sdcard downloads 
		chat = self.driver.find_elements(By.XPATH, xpath)				
		self.actions.long_press(chat).perform()
		self.actions.tap(None, 300, 1352, 1).perform()
		username11 = self.driver.find_elements(By.ID, 'com.snapchat.android:id/profile_header_secondary_text').text
		user11 = username11.split(' ')[0]
		# try: #wer not in homepage
		# 	self.driver.find_elements(By.ID, 'com.snapchat.android:id/lenses_camera_lens_button_view')
		# except:
		# 	try:
		# 		self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.View')[0].click()
		# 	except:#wer not in snap 
		# 		pass 

		self.driver.press_keycode(3)
		time.sleep(2)
		self.driver.swipe(700, 1200, 700, 500)
		app = self.driver.find_elements(By.XPATH, '(//android.widget.TextView[@content-desc="Camera"])[2]')
		app[0].click()

		
		time.sleep(1)
		self.driver.find_elements(By.ID, 'com.snapchat.kit.creativesample:id/image_preview')[0].click()
		time.sleep(1)
		if SnapState == 'IMAGE':
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]')[0].click()
			text = self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText')
			text[0].send_keys(Link)
			
		else:
			self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]')[0].click()
			time.sleep(1)
			text = self.driver.find_elements(By.XPATH, 'get.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText')
			text[0].send_keys(Link)
		self.driver.find_elements(By.ID, 'android:id/button1')[0].click()
		while True:
			try:
				time.sleep(1) #check if download finished
				self.driver.find_elements(By.ID, 'android:id/button1')[0].click()
			except:
				pass
			else:
				break
		self.driver.find_elements(By.ID, 'com.snapchat.kit.creativesample:id/share_button')[0].click()
		while True:
			try:
				time.sleep(1)
				self.driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ImageView')[0].click()
			except: 
				pass
			else:
				break
		time.sleep(2)
		self.driver.find_elements(By.ID, 'com.snapchat.android:id/caption_edit_text_view')[0].send_keys(stext)
		self.driver.back()
		time.sleep(1)
		self.driver.find_elements(By.ID, 'com.snapchat.android:id/send_btn')[0].click()
		time.sleep(1)
		self.driver.find_elements(By.ID, 'com.snapchat.android:id/send_to_search_text')[0].send_keys(user11)

		usr = self.driver.find_elements_by_xpath('//android.view.View[@content-desc="' + str(username) + '"]')[0].click()
		self.driver.find_elements(By.ID, 'com.snapchat.android:id/send_to_bottom_panel_send_button')[0].click()














# p1 = Snap()
# # p1.send_snaps('username', 'pass', 'IMAGE', 'https://i.imgur.com/Evmqvp2.jpeg')
# p1.open()
# p1.login()

try:
	# p1.accept_adds()
	p1.checkmsgs()
except Exception as ex:
	print(ex)
	f = open('path/to/users.txt', 'a+', encoding='utf-8')
	f.write(str(p1.users) + '\n')
	f.close()