import requests, random, datetime, sys, time, argparse, os , colorama ,pickle
from Banners import banner1an, banner2an, banner3, banner4
from fake_useragent import UserAgent
from ServesSMS import *
from Message import *
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

oso = os.name
user_war = 15
_phones = []
user_instruct = '0'
version = '12.1'


def instruction():
	global user_instruct
	user_instruct += '5'





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
	if user_input == str(1):
	    print('Тут ваня умник не до делал')
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
	if user_input == str(1):
	    print('Тут ваня умник не до делал')
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
	topic = input('\n\n        Введите тему сообщенипя спама! \n\n        [\033[32m>>\033[33m]')
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
	phone_number = input('\n        Введите номер для поиска информации ! \n\n        [\033[32m>>\033[33m] ')
	num_kol = len(phone_number)

	try:
		if num_kol == 11:
			print('        \nПожалуйста подождите [\033[32m3 сек.\033[33m]!')
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
			print('    [\033[31mx\033[33m] Введите Российский номер из 11 символов ! ')
	except:
		print('    [\033[31mx\033[33m] Введите Российский номер из 11 символов ! ')