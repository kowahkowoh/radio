import requests,os,time,json,sys
import string,random
from time import sleep,time
API_BASE_URL = "https://id-api.spooncast.net"
API_BASE_TAG = 'https://id-api.spooncast.net/search/user/?q='
API_LIVES = '/lives/'
API_CAST = '/casts/'
API_USER = '/users/'
API_QUERY = '/search/user/?q='
API_LOGIN = '/signin/'
API_VOICETYPE = '/impression/'
API_VOICEPROFILE = '/voice_like/'
API_FOLLOW = '/follow/'
API_FANBOARD = '/fanmessages/'
API_IDCHANGE = 'username/'
API_JOIN = '/join/'
API_LIKE = '/like/'
API_PLAY = '/play/'
API_BLOCK = '/block/'
API_COMMENTCAST = '/tcomments/'
API_REPORT = '/report/'
API_LEAVE = '/leave/'
API_UNBLOCK = '/unblock/'
start_time = time()
user_token_list = open('Tokennya.txt', 'r').read().splitlines()
UAInput = open('UALIST.txt','r').read().splitlines()
DBKomentarFB = open('listkomentarfb.txt','r').read().splitlines()
DBKomentarCAST = open('listkomentarcast.txt','r').read().splitlines()
headerbasic = {'content-type':'application/json','connection':'keep-alive','user-agent':str(UAInput)}
paramex = {'cv':'heimdallr'}
###############################
def main():
 print("""
 
  Asisten pribadi 
  spoon radio Indonesia
  menu fitur:
 1. Bot taplove + listener
 2. Bot taplove
 3. Bot Listener
 4. Cek Token
 5. Cek akun
 6. Tambah Followers
 7. Ganti id
 8. Ganti id acak
 9. Taplove cast
 10. Listener cast
 11. Coment cast
 12. Report akun
 13. Report room
 14. Report cast
 15. kick MJ DJ  & Listener (harus jadi mj)
 16. Kick Global
 17. Like voice akun
 18. Ganti voice 
 19. save foto live
 20. tarik bot
 
 """)
 menu = input("Silahkan Pilih Menu : ")
 if menu == '1':
  bomtaplop()
 if menu == '2':
  bomhitrun()
 if menu == '3':
  bomlisterner()
 if menu == '4':
  cekakunmu()
 if menu == '5':
  cekid()
 if menu == '6':
  suntikfollower()
 if menu == '7':
  gantiid()
 if menu == '8':
  randomID()
 if menu == '9':
  bomcast()
 if menu == '10':
  bomlistenercast()
 if menu == '11':
  spamkomentarcast()
 if menu == '12':
  reportprofil()
 if menu == '13':
  reportlive()
 if menu == '14':
  reportcast()
 if menu == '15':
  kickuser()
 if menu == '16':
  globalkicker()
 if menu == '17':
  lvp()
 if menu == '18':
  rvt()
 if menu == '19':
  malinglive()
 if menu == '20':
  tarikbot()
 if menu == 'd':
  spamfanboard()
 if menu == 'a':
  malingprofil()
 if menu == 'b':
  malingcast()
 if menu == 'c':
  unblockbot() 
 elif menu == 'q':
  print("Perintah Salah!")
  main()
 else:
  print("Perintah salah balik ke menu")
  main()
###############################
def cekakunmu():
 print('''
 [ Cek Akun Profil mu ]
 
 Penjelasan :
 Fitur ini untuk cek detail akun kamu
 
 Silahkan login akun spoon mu
 ''')
 nomerhp = input("Masukan Nomer Hp : ")
 password = input("Masukan Password : ")
 print('Sedang Login')
 sleep(1)
 authjson = {'sns_type':'phone','sns_id':nomerhp,'password':password}
 login = requests.post(API_BASE_URL+API_LOGIN,json=authjson)
 respon_data = login.json()
 for i in respon_data['results']:
  idnya = i['id']
  tagnya = i['tag']
  nicknya = i['nickname']
  tokennya = i['token']
  budgetnya = i['budget']['total_exchange_spoon']
  aktif = i['is_active']
  lahir = i['date_joined']
  print ('\nNama :\n', nicknya,
  '\nUser Tag :\n',tagnya,
  '\nID Spoon :\n', idnya,
  '\nToken :\n', tokennya,
  '\nTotal Koin :\n',budgetnya,
  '\nTanggal Lahir Akun\n',lahir)
 else:
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
#################################  
def cekid():
 print('''
 [ Cek ID User Lain]
 
 Penjelasan :
 Fitur ini untuk Cek akun user lain.
 
 ''')
 print("Gunakan id spoon tanpa @\nContoh : officialdev")
 katakunci = input("Masukan ID Spoon nya : ")
 requestID = requests.get(API_BASE_TAG+katakunci)
 respon_data = requestID.json()
 for i in respon_data['results']:
  taguser = i['tag']
  nickuser = i['nickname']
  followers = i['follower_count']
  print(
 'Nama Spoon :',nickuser,
 '\nID Spoon :',taguser,
 '\nFollowers :',followers)
 else:
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
#################################
def rvt():
 vtlistid = '''
 [ Rate Voice Type ]
 
 Penjelasan :
 Fitur ini untuk memberi nilai Voice Type
 pada akun Spoon.
 Tutorial :
 1. Masukan ID User yang mau di kasih Voice Type
 2. Masukan Angka Voice Type (cek list di bawah)
 3. Masukan Jumlah Vote
 
 [1] Manis 
 [2] Seksi
 [3] Ramah
 [4] Hangat
 [6] Halus
 [7] Bersahabat
 [8] Kuat
 [9] Lucu
 [10] Keras
 [11] Imut
 [12] Serak
 [13] Romantis
 [14] Seram
 
 '''
 print(vtlistid)
 txtid = input("Masukan ID User : ")
 txtVT = input("Masukan Nilai VT : ")
 jml = int(input('Jumlah Rate : '))
 print('Proces >>> ')
 requestID = requests.get(API_BASE_TAG+txtid)
 respon_data = requestID.json()
 for i in respon_data['results']:
  idnya = i['id']
 sleep(1)
 for i in range(0, jml):
 		pesan = {"new_impression_ids":txtVT}
 		headers = {'Authorization': 'Token ' + str(user_token_list[i]),
 		'content-type':'application/json',
 		'connection':'keep-alive',
 		'user-agent':str(UAInput[i])}
 		with requests.Session() as c:
 			r = c.post(API_BASE_URL + API_USER + str(idnya) + API_VOICETYPE, headers = headers,params=paramex,json=pesan)
 			myprint('\rProses Vote Ke : ',i+1)
 else:
   kembalikemenu()
####################################
def lvp():
 print('''
 [ Like Voice Profil ]
 
 Penjelasan :
 Fitur ini untuk menambah jumlah like
 pada Voice Profil kita.
 Tutorial :
 1. Buat dulu Voice Profil nya
 2. Masukan ID Spoon nya (tanpa tanda @)
 3. Masukan Jumlah Like (Max sesuai jumlah bot)
 ''')
 txtid = input("Masukan ID User : ")
 jml = int(input("Masukan Jumlah Like : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_TAG+txtid)
 respon_data = requestID.json()
 for i in respon_data['results']:
  taguser = i['id']
  
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_USER+str(taguser)+API_VOICEPROFILE,headers=headers,params=paramex)
    myprint('\rProses Bot Ke : ',i+1)
 else:
  kembalikemenu()
##########################
def spamkomentarcast():
 sleep(1)
 print('''
 [ Spoon Spammer Komentar CAST ]
 
 Penjelasan :
 Fitur ini untuk meramaikan komentar CAST
 Tutorial :
 1. Masukan Link CAST
 2. Masukan Jumlah Komentar
 *Catatan :
 Untuk memasukan pesan sendiri sesuai keinginan
 pada file listkomentarcast.txt edit dengan text editor
 isi sesuai komentar yang di inginkan.
 ''')
 txtid = input("Masukan Link CAST : ")
 respone = requests.get(txtid)
 url = respone.url
 shortcast = url[34:-58]
 jml = int(input("Masukan Jumlah Komentar : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_URL+API_CAST+shortcast)
 respon_data = requestID.json()
 for i in respon_data['results']:
  namac = i['title']
  authc = i['author']['nickname']
 for i in range(0,jml):
   isikomentar = {"contents":str(DBKomentarCAST[i])}
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rspamfb = c.post(API_BASE_URL + API_CAST + shortcast + API_COMMENTCAST,headers=headers,json=isikomentar,params=paramex)
    myprint('\rProses Bot Ke : ',str(DBKomentarCAST[i+1]))
 else:
  kembalikemenu()
def spamfanboard():
 sleep(1)
 print('''
 [ Spoon Spammer Fanboard ]
 
 Penjelasan :
 Fitur ini untuk meramaikan Fanboard
 pada profil Spoon.
 Tutorial :
 1. Masukan ID Spoon (tanpa tanda @)
 2. Masukan Jumlah Fanboard
 *Catatan :
 Untuk memasukan pesan sendiri sesuai keinginan
 pada file listkomentarfb.txt edit dengan text editor
 isi sesuai komentar yang di inginkan.
 ''')
 txtid = input("Masukan ID User : ")
 jml = int(input("Masukan Jumlah Fanboard : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_TAG+txtid)
 respon_data = requestID.json()
 for i in respon_data['results']:
  taguser = i['id']
  
 for i in range(0,jml):
   isikomentar = {"contents":str(DBKomentarFB[i])}
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_USER+str(taguser)+API_FOLLOW,headers=headers,params=paramex)
    rspamfb = c.post(API_BASE_URL + API_USER + str(taguser) + API_FANBOARD,headers=headers,json=isikomentar,params=paramex)
    myprint('\rProses Bot Ke : ',str(DBKomentarFB[i+1]))
 else:
  kembalikemenu()
def suntikfollower():
 sleep(1)
 print('''
 [ Spoon Auto Followers ]
 
 Penjelasan :
 Fitur ini untuk menambah followers Spoon
 Tutorial :
 1. Masukan ID Spoon (tanpa tanda @)
 2. Masukan Jumlah Followers
 *Catatan :
 Jumlah followers maximal dari jumlah bot.
 ''')
 txtid = input("Masukan ID User : ")
 jml = int(input("Masukan Jumlah Followers : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_TAG+txtid)
 respon_data = requestID.json()
 for i in respon_data['results']:
  taguser = i['id']
  
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_USER+str(taguser)+API_FOLLOW,headers=headers,params=paramex)
    sleep(1)
    myprint('\rProses Followers Ke : ',i+1)
 else:
  kembalikemenu()
def gantiid():
 sleep(1)
 print('''
 [ Spoon ID Changer ]
 
 Penjelasan :
 Fitur ini untuk merubah ID yang terbatas pada Spoon.
 Tutorial :
 1. Login ID Spoon (gunakan nomer hp)
 2. Masukan ID yang baru (Maks 20 Karakter)
 ''')
 nomerhp = input("Masukan Nomor HP : ")
 passwordhp = input("Masukan Password : ")
 sleep(1)
 print('Sedang Login >>>')
 auth = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
 r = requests.post(API_BASE_URL + API_LOGIN , json=auth)
 respon_data = r.json()
 for i in respon_data['results']:
  taguser = i['id']
  tokennyaa = i['token']
  idbaru = input('Masukan ID yang baru : ')
  inputidbaru = {'username':idbaru}
  iddump = json.dumps(inputidbaru)
  headers = {'Authorization':'Token ' + tokennyaa,
  'content-type':'application/json',
  'user-agent':'STEALG'}
  rid = requests.post(API_BASE_URL + API_USER + API_IDCHANGE,headers=headers,params=paramex,json=inputidbaru)
  print('Success ! ID Telah di ganti ke ' + str(idbaru))
  print('Silahkan Cek ID Spoon kamu..')
   # myprint('\rProses Followers Ke : ',i+1)
 else:
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def randomID():
 sleep(1)
 print('''
 [ Spoon Random ID Changer ]
 
 Penjelasan :
 Fitur ini untuk merubah ID yang terbatas pada Spoon.
 Tutorial :
 1. Login ID Spoon (gunakan nomer hp)
 2. Masukan ID yang baru (Maks 20 Karakter)
 ''')
 nomerhp = input("Masukan Nomor HP : ")
 passwordhp = input("Masukan Password : ")
 sleep(1)
 print('Sedang Login >>>')
 auth = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
 r = requests.post(API_BASE_URL + API_LOGIN , json=auth)
 respon_data = r.json()
 for i in respon_data['results']:
  taguser = i['id']
  tokennyaa = i['token']
  tagged = i['tag']
  #idbaru = input('Masukan ID yang baru : ')
  inputidbaru = {'username':id_generator()}
  headers = {'Authorization':'Token ' + tokennyaa,
  'content-type':'application/json',
  'user-agent':'STEALG'}
  rid = requests.post(API_BASE_URL + API_USER + API_IDCHANGE,headers=headers,params=paramex,json=inputidbaru)
  sleep(1)
  print('Success ! ID Telah di ganti ke ' + str(tagged))
  print('Silahkan Cek ID Spoon kamu..')
   # myprint('\rProses Followers Ke : ',i+1)
 else:
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
def bomlisterner():
 sleep(1)
 print('''
 [ Spoon Bot Listener ]
 
 Penjelasan :
 Fitur ini untuk menambah bot sebagai listener
 pada LIVE.
 Tutorial :
 1. Masukan Link LIVE (sharelink dari apk spoon)
 2. Masukan Jumlah Listener
 3. Masukan Jeda Waktu
 *Catatan :
 Jumlah listener maximal dari jumlah bot.
 ''')
 inputlink = input("Masukan Link LIVE : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-59]
 ress = requests.get( API_BASE_URL + API_LIVES + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Listener : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Listener Ke : ',i+1)
 else:
  kembalikemenu()
def bomtaplop():
 sleep(1)
 print('''
 [ Spoon Bot Taplove ]
 
 Penjelasan :
 Fitur ini untuk menambah bot sebagai listener
 pada LIVE.
 Tutorial :
 1. Masukan Link LIVE (sharelink dari apk spoon)
 2. Masukan Jumlah Taplove
 3. Masukan Jeda Waktu
 *Catatan :
 Jumlah listener maximal dari jumlah bot.
 ''')
 inputlink = input("Masukan Link LIVE : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-59]
 ress = requests.get( API_BASE_URL + API_LIVES + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Taplove : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
    rlvp2 = c.post( API_BASE_URL + API_LIVES + shortlink + API_LIKE , headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Taplove Ke : ',i+1)
 else:
  kembalikemenu()
def bomhitrun():
 sleep(1)
 print('''
 [ Spoon Bot Hit & Run ]
 
 Penjelasan :
 Fitur ini untuk menambah bot sebagai listener
 pada LIVE.
 Tutorial :
 1. Masukan Link LIVE (sharelink dari apk spoon)
 2. Masukan Jumlah Hit & Run
 3. Masukan Jeda Waktu
 *Catatan :
 Jumlah listener maximal dari jumlah bot.
 ''')
 inputlink = input("Masukan Link LIVE : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-59]
 ress = requests.get( API_BASE_URL + API_LIVES + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Hit & Run : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex)
    rlvp2 = c.post( API_BASE_URL + API_LIVES + shortlink + API_LIKE, headers=headers,params=paramex)
    rlvp3 = c.post( API_BASE_URL + API_LIVES + shortlink + API_LEAVE, headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Hit & Run Ke : ',i+1)
 else:
  kembalikemenu()
def bomcast():
 sleep(1)
 print('''
 [ Spoon Bot CAST ]
 
 Penjelasan :
 Fitur ini untuk menambah bot sebagai listener
 pada LIVE.
 Tutorial :
 1. Masukan Link CAST (sharelink dari apk spoon)
 2. Masukan Jumlah Taplove
 3. Masukan Jeda Waktu
 *Catatan :
 Jumlah listener maximal dari jumlah bot.
 ''')
 inputlink = input("Masukan Link CAST : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-58]
 ress = requests.get( API_BASE_URL + API_CAST + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Taplove : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama CAST :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_CAST+shortlink+API_LIKE,headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Taplove Ke : ',i+1)
 else:
  kembalikemenu()
def bomspamcast():
 sleep(1)
 
def bomlistenercast():
 sleep(1)
 print('''
 [ Spoon Bot Listener CAST ]
 
 Penjelasan :
 Fitur ini untuk menambah bot sebagai listener
 pada LIVE.
 Tutorial :
 1. Masukan Link CAST (sharelink dari apk spoon)
 2. Masukan Jumlah Listener
 3. Masukan Jeda Waktu
 *Catatan :
 Jumlah listener maximal dari jumlah bot.
 ''')
 inputlink = input("Masukan Link CAST : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-58]
 ress = requests.get( API_BASE_URL + API_CAST + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Listener : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama CAST :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_CAST+shortlink+API_PLAY,headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Listener Ke : ',i+1)
 else:
  kembalikemenu()
def reportprofil():
 sleep(1)
 print('''
 [ Spoon Report Profil ]
 
 Penjelasan :
 Fitur ini untuk me-report akun Spoon
 Tutorial :
 1. Masukan ID Spoon (tanpa tanda @)
 2. Masukan tipe report
 [1] Dewasa atau Cabul
 [2] Peniruan dan Pembajakan
 [3] Bullying atau Unsur Kebencian
 *Catatan :
 Report yang pasti adalah dengan memberi bukti
 berupa Screenshot / Record Video yg di lampirkan
 ke email helpid@mykoon.com
 ''')
 txtid = input("Masukan ID User : ")
 jml = int(input("Masukan Jumlah Report : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_TAG+txtid)
 respon_data = requestID.json()
 for i in respon_data['results']:
  taguser = i['id']
  nick = i['nickname']
  basereport = int(input("Masukan Tipe Report : "))
  tipereport = {'report_type':basereport}
  print('Nama Profil : ',nick)
  sleep(1)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_USER+str(taguser)+API_REPORT,headers=headers,params=paramex,json=tipereport)
    myprint('\rProses Report Ke : ',i+1)
 else:
  kembalikemenu()
def reportlive():
 sleep(1)
 print('''
 [ Spoon Report LIVE ]
 
 Penjelasan :
 Fitur ini untuk me-report LIVE Spoon
 Tutorial :
 1. Masukan ID Spoon (tanpa tanda @)
 2. Masukan tipe report
 [1] Dewasa atau Cabul
 [2] Peniruan dan Pembajakan
 [3] Bullying atau Unsur Kebencian
 [4] Bunuh diri dan Melukai diri
 *Catatan :
 Report yang pasti adalah dengan memberi bukti
 berupa Screenshot / Record Video yg di lampirkan
 ke email helpid@mykoon.com
 ''')
 txtid = input("Masukan Link LIVE : ")
 respone = requests.get(txtid)
 url = respone.url
 shortlink = url[34:-59]
 jml = int(input("Masukan Jumlah Report : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_URL + API_LIVES + shortlink)
 respon_data = requestID.json()
 for i in respon_data['results']:
  titleroom = i['title']
  basereport = int(input("Masukan Tipe Report : "))
  tipereport = {'report_type':basereport}
  print('Nama LIVE : ',titleroom)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_LIVES+shortlink+API_JOIN,headers=headers,params=paramex,json=tipereport)
    rlvp2 = c.post(API_BASE_URL + API_LIVES + shortlink + API_REPORT,headers=headers,params=paramex,json=tipereport)
    myprint('\rProses Report Ke : ',i+1)
 else:
  kembalikemenu()
def reportcast():
 sleep(1)
 print('''
 [ Spoon Report CAST ]
 
 Penjelasan :
 Fitur ini untuk me-report LIVE Spoon
 Tutorial :
 1. Masukan ID Spoon (tanpa tanda @)
 2. Masukan tipe report
 [1] Dewasa atau Cabul
 [2] Peniruan dan Pembajakan
 [3] Bullying atau Unsur Kebencian
 *Catatan :
 Report yang pasti adalah dengan memberi bukti
 berupa Screenshot / Record Video yg di lampirkan
 ke email helpid@mykoon.com
 ''')
 txtid = input("Masukan Link CAST : ")
 respone = requests.get(txtid)
 url = respone.url
 shortlink = url[34:-58]
 jml = int(input("Masukan Jumlah Report : "))
 sleep(1)
 print("Proses >>>")
 requestID = requests.get(API_BASE_URL + API_CAST + shortlink)
 respon_data = requestID.json()
 for i in respon_data['results']:
  titleroom = i['title']
  basereport = int(input("Masukan Tipe Report : "))
  tipereport = {'report_type':basereport}
  print('Nama CAST : ',titleroom)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_CAST+shortlink+API_REPORT,headers=headers,params=paramex,json=tipereport)
    myprint('\rProses Report Ke : ',i+1)
 else:
  kembalikemenu()
def kickuser():
 sleep(1)
 print('''
 [ Spoon Kick User ]
 
 Penjelasan :
 Fitur ini untuk Kick user dalam room
 bahkan ketika user tersebut tidak dalam room
 atau pun untuk kick manajer yang lain.
 Tutorial :
 1. Masukan Link LIVE
 2. Login Akun yang sedang jadi MJ
 3. Masukan ID Spoon yang mau di kick (tanpa tanda @)
 *Cataran :
 Anda harus menjadi MJ pada Room.
 ''')
 txtid = input("Masukan Link LIVE : ")
 respone = requests.get(txtid)
 url = respone.url
 shortlive = url[34:-59]
 print("Silahkan Login terlebih dahulu ..")
 nomerhp = input("Masukan Nomer HP : ")
 passwordhp = input("Masukan Password : ")
 print("Sedang login ...")
 authid = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
 r1 = requests.get(API_BASE_URL + API_LIVES + shortlive)
 r2 = requests.post(API_BASE_URL + API_LOGIN , json=authid)
 d1 = r1.json()
 d2 = r2.json()
 definisilive = d1['results']
 definisiakun = d2['results']
 for i in definisiakun:
  hasiltoken = i['token']
  headers = {'Authorization':'Token ' + hasiltoken,
  'content-type':'application/json'
  }
 idkorban = input("Masukan ID Korban : ")
 r3 = requests.get( API_BASE_TAG + idkorban)
 data3 = r3.json()
 results_data = data3['results']
 for k in results_data:
  iduser = k['id']
  nickn = k['nickname']
  korbankick = {'block_user_id':str(iduser)}
  rlvp = requests.post(API_BASE_URL + API_LIVES + shortlive + API_BLOCK,headers=headers,json=korbankick,params=paramex)
  print(nickn," Telah di Kick dari room ")
 else:
  kembalikemenu()
def globalkicker():
 sleep(1)
 print('''
 [ Spoon Global Kicker ]
 
 Penjelasan :
 Fitur ini untuk Kick user dalam room
 bahkan ketika user tersebut tidak dalam room
 atau pun untuk kick manajer yang lain.
 Tutorial :
 1. Masukan Link LIVE
 2. Login Akun yang sedang jadi MJ
 3. Masukan ID Spoon yang mau di kick (tanpa tanda @)
 *Cataran :
 Anda harus menjadi MJ pada Room.
 ''')
 txtid = input("Masukan Link LIVE : ")
 respone = requests.get(txtid)
 url = respone.url
 shortlive = url[34:-59]
 print("Silahkan Login terlebih dahulu ..")
 nomerhp = input("Masukan Nomer HP : ")
 passwordhp = input("Masukan Password : ")
 print("Sedang login ...")
 authid = {'sns_type':'phone','sns_id':nomerhp,'password':passwordhp}
 r1 = requests.get(API_BASE_URL + API_LIVES + shortlive)
 r2 = requests.post(API_BASE_URL + API_LOGIN , json=authid)
 d1 = r1.json()
 d2 = r2.json()
 definisilive = d1['results']
 definisiakun = d2['results']
 for i in definisiakun:
  hasiltoken = i['token']
  headers = {'Authorization':'Token ' + hasiltoken,
  'content-type':'application/json'
  }
 idkorban = input("Masukan Kata Kunci : ")
 r3 = requests.get( API_BASE_TAG + idkorban)
 data3 = r3.json()
 results_data = data3['results']
 for i in range(len(results_data)):
  korbankick = {'block_user_id':results_data[i]['id']}
  rlvp = requests.post(API_BASE_URL + API_LIVES + shortlive + API_BLOCK,headers=headers,json=korbankick,params=paramex)
 #  print(nickn," Telah di Kick dari room ")
  sys.stdout.write("\rUser Yang Telah di Kick : " + results_data[i]['nickname'])
 else:
  kembalikemenu()
def malingprofil():
 sleep(1)
 print('''
 [ Spoon Profil Stealer ]
 
 Penjelasan :
 Fitur ini untuk mengambil foto profil user lain.
 Tutorial :
 1. Masukan ID Spoon yang mau di ambil
 
 ''')
 print("Gunakan id spoon tanpa @\nContoh : officialdev")
 katakunci = input("Masukan ID Spoon nya : ")
 requestID = requests.get(API_BASE_TAG+katakunci)
 respon_data = requestID.json()
 for i in respon_data['results']:
  nicku = i['nickname']
  imgkey = i['profile_url']
  print(
  'Nama User : ',nicku,
  '\nLink Foto Profil :',imgkey)
  print("Silahkan Copy Link Profil ke Browser")
 else:
  sleep(1)
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
def malinglive():
 sleep(1)
 print('''
 [ Spoon LIVE Background Stealer ]
 
 Penjelasan :
 Fitur ini untuk mengambil foto background LIVE user lain.
 Tutorial :
 1. Masukan Link LIVE yang mau di ambil backgroundnya.
 
 ''')
 katakunci = input("Masukan Link LIVE nya : ")
 respone = requests.get(katakunci)
 url = respone.url
 shortlink = url[34:-59]
 requestID = requests.get(API_BASE_URL+API_LIVES+shortlink)
 respon_data = requestID.json()
 for i in respon_data['results']:
  nicku = i['title']
  imgkey = i['img_url']
  print(
  'Nama Room : ',nicku,
  '\nLink Foto :',imgkey)
  print("Silahkan Copy Link Profil ke Browser")
 else:
  sleep(1)
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
def malingcast():
 sleep(1)
 print('''
 [ Spoon CAST Cover Stealer ]
 
 Penjelasan :
 Fitur ini untuk mengambil foto cover CAST user lain.
 Tutorial :
 1. Masukan Link CAST yang mau di ambil backgroundnya.
 
 ''')
 katakunci = input("Masukan Link CAST nya : ")
 respone = requests.get(katakunci)
 url = respone.url
 shortlink = url[34:-58]
 requestID = requests.get(API_BASE_URL+API_CAST+shortlink)
 respon_data = requestID.json()
 for i in respon_data['results']:
  nicku = i['title']
  imgkey = i['img_url']
  print(
  'Nama Cast : ',nicku,
  '\nLink Foto :',imgkey)
  print("Silahkan Copy Link Profil ke Browser")
 else:
  sleep(1)
  backhome = input("Kembali ke menu utama ? (Ketik Y) : ")
  if backhome == 'y':
   sleep(2)
   main()
#################### UPDATED ##########################
def unblockbot():
 print('''
 [ Spoon Unblock Bot ]
 
 Penjelasan :
 Fitur ini untuk unblock akun yang live nya
 tidak bisa di masukin bot.
 
 Tutorial :
 1. Masukan ID yang mau di Unblock
 ''')
 txtid = input("Masukan ID Spoon : ")
 requestQuery = requests.get(API_BASE_URL + API_QUERY + txtid)
 respone_data = requestQuery.json()
 for i in respone_data['results']:
  iduser = i['id']
 for i in range(0,len(user_token_list)):
  headers = {'Authorization': 'Token ' + str(user_token_list[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
  with requests.Session() as c:
   r = c.post(API_BASE_URL + API_USER + str(iduser) + API_UNBLOCK , headers=headers , params = paramex)
   myprint('\rProses Unblock Ke : ',i+1)
 else:
  kembalikemenu()
def tarikbot():
 sleep(1)
 print('''
 [ Spoon Bot Leave ]
 
 Penjelasan :
 Fitur ini untuk menarik Bot dari LIVE
 pada LIVE.
 Tutorial :
 1. Masukan Link LIVE (sharelink dari apk spoon)
 2. Masukan Jumlah Listener yang mau di tarik
 3. Masukan Jeda Waktu
 ''')
 inputlink = input("Masukan Link LIVE : ")
 respone = requests.get(inputlink)
 url = respone.url
 shortlink = url[34:-59]
 ress = requests.get( API_BASE_URL + API_LIVES + shortlink )
 respon_live = ress.json()
 for i in respon_live['results']:
  titlelive = i['title']
  authlive = i['author']['nickname']
  jml = int(input("Masukan Jumlah Listener : "))
  dly = int(input("Masukan Jeda : "))
  print('Proses >>>')
  sleep(1)
  print(
  '\x1b[1;31;40m' + ' Nama Room :' + '\x1b[0m'+' '+titlelive,
  '\n','\x1b[1;32;40m'+'Penyiar : '+'\x1b[0m'+authlive)
 for i in range(0,jml):
   headers = {'Authorization': 'Token ' + str(user_token_list[i]),
    'content-type':'application/json',
    'connection':'keep-alive',
    'user-agent':str(UAInput[i])}
   with requests.Session() as c:
    rlvp = c.post(API_BASE_URL+API_LIVES+shortlink+API_LEAVE,headers=headers,params=paramex)
    sleep(dly)
    myprint('\rProses Tarik Ke : ',i+1)
 else:
  kembalikemenu()
def servergagal():
 print("Server Status : Gagal | Silahkan ulangi kembali nanti..")
 sleep(1)
 main()
def servergagal2():
 print("Server Status : Gagal | Silahkan ulangi kembali nanti..")
 sleep(1)
# main() 
def myprint(x,i):
 sys.stdout.write(str(x) + str(i) + ' | Sudah Terkirim') 
 sleep(1)
def kembalikemenu():
 sleep(1)
 os.system('clear')
 for i in range(0,3):
  total = i+1
  sys.stdout.write('\rKembali Ke Menu Setelah : '+ str(total))
  sleep(1)
 os.system('clear')
 main()
###########
main()