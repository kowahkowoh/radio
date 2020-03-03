import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()

txtid = input('Masukan Link Live : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/"+slink)
print(socketstring)
botauthtoken2 = '1e6928bd8a017b4946242b398bbff2ad212c50a7'
mypesan = '{"event":"live_join","token":"'+botauthtoken2+'","appversion":"4.3.14","useragent":"Android","live_id":'+slink+',"type":"live_req"}'


def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":"halloooo semua , ucing dateng nih 😙"}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = [
         '😎', '😊', '😝', '🤭', '🙈', '😋', '😁']
        ya = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":"YA ' + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":" GAK ' + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":"Bisa jadi deh' + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":" Bodo amat lah terserah kamu aja' + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 'c' and psn[-1:] == '?':
            kambeng = random.choice(listjawaban)
            print(kambeng)
            ws.send(kambeng)
        ljoin = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":"Haloo kaka, ' + nick + ' , selamat datang jangan lupa tap love buat ucing 😘"}'
        lsjoin = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"dih kok kaka  ' + nick + ' jadi setan"}'
        llike = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"makasih taplovenya salam hangat dari ucing🤗"}'
        tidur = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"iya, ucing bobo manis dlu yah 😴"}'
        bangun = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"oke,  ' + nick + ' ,ucing dah bangun nih mau cuci muka abis itu nyapa🤤"}'
        ping = '{"appversion":"4.3.14","event":"live_message","token":"","useragent":"Android","message":" Eh,  ' + nick + ' ,ucing disini Kok, ngga akan hilang😍"}'
        rank = '{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"bentar ya  ' + nick + ' ucing liat ke atas dlu🥰"}'
        if evn == 'live_message' and (psn == '/status' or psn == '/durasi' or psn == '/info'):
            createdl = response2.json()['results'][0]['created']
            tanggal = datetime.today()
            cre = createdl[:-17]
            crea = createdl[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timehl2 = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"room ini sudah mengudara selama💕💫 ' + str(timehl2) + ' 💕💫"}')
        if evn == 'live_join':
            if status == 'bangun':
                ws.send(ljoin)
            if evn == 'live_shadowjoin':
                ws.send(lsjoin)
        if evn == 'live_like' and status == 'bangun':
            ws.send(llike)
        if evn == 'live_message' and psn == 'cing tidur' and status == 'bangun':
            status = 'tidur'
            ws.send(tidur)
        if evn == 'live_message' and psn == '_rank':
            headers3 = {'User-Agent': 'Mozilla/5.0'}
            response3 = requests.get('https://id-api.spooncast.net/lives/popular/', headers=headers3)
            ws.send(rank)
        if evn == 'live_message' and psn[:-3] == 'bro cek rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn[:-2] == '/rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn == '_cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = tag
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"nama' + nn + ' tanggal lahir akun-> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn[:4] == '/cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = psn[5:]
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.3.14","event":"live_message","token":" ","useragent":"Android","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn == 'cing bangun' and status == 'tidur':
            status = 'bangun'
            ws.send(bangun)
        if evn == 'live_message' and psn == 'cing':
            ws.send(ping)
        if evn == 'live_message':
            if psn == 'bro keluar' and uid == '210900010':
                ws.close()
def on_close(ws): #on close of the bot.
    print ("### closed ###")
    
def on_open(ws): #when the bot initially connects.
 print ("open")
 time.sleep(1)
 ws.send(mypesan)
 time.sleep(1)
 gblk = """Connected"""
 print(gblk)
 time.sleep(1)

if __name__ == "__main__":
 
 websocket.enableTrace(True)
 ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,                                           
                              on_message = on_message,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()