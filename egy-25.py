# -*- coding: utf-8 -*-
import eGy
from eGy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

print "Login eGy-NgapaK"

cl = LineClient(authToken='')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient(authToken='')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient(authToken='')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient(authToken='')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

ke = LineClient(authToken='')
ke.log("Auth Token : " + str(ke.authToken))
channel4 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel4.channelAccessToken))

kt = LineClient(authToken='')
kt.log("Auth Token : " + str(kt.authToken))
channel5 = LineChannel(kt)
kt.log("Channel Access Token : " + str(channel5.channelAccessToken))

ka = LineClient(authToken='')
ka.log("Auth Token : " + str(ka.authToken))
channel6 = LineChannel(ka)
ka.log("Channel Access Token : " + str(channel6.channelAccessToken))

kb = LineClient(authToken='')
kb.log("Auth Token : " + str(kb.authToken))
channel7 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel7.channelAccessToken))

ko = LineClient(authToken='')
ko.log("Auth Token : " + str(ko.authToken))
channel8 = LineChannel(ko)
ko.log("Channel Access Token : " + str(channel8.channelAccessToken))

ks = LineClient(authToken='')
ks.log("Auth Token : " + str(ks.authToken))
channel9 = LineChannel(ks)
ks.log("Channel Access Token : " + str(channel9.channelAccessToken))

ku = LineClient(authToken='')
ku.log("Auth Token : " + str(ku.authToken))
channel10 = LineChannel(ku)
ku.log("Channel Access Token : " + str(channel10.channelAccessToken))

kr = LineClient(authToken='')
kr.log("Auth Token : " + str(kr.authToken))
channel11 = LineChannel(kr)
kr.log("Channel Access Token : " + str(channel11.channelAccessToken))

kd = LineClient(authToken='')
kd.log("Auth Token : " + str(kd.authToken))
channel12 = LineChannel(kd)
kd.log("Channel Access Token : " + str(channel12.channelAccessToken))

kj = LineClient(authToken='')
kj.log("Auth Token : " + str(kj.authToken))
channel13 = LineChannel(kj)
kj.log("Channel Access Token : " + str(channel13.channelAccessToken))

km = LineClient(authToken='')
km.log("Auth Token : " + str(km.authToken))
channel14 = LineChannel(km)
km.log("Channel Access Token : " + str(channel14.channelAccessToken))

kv = LineClient(authToken='')
kv.log("Auth Token : " + str(kv.authToken))
channel15 = LineChannel(kv)
kv.log("Channel Access Token : " + str(channel15.channelAccessToken))

kh = LineClient(authToken='')
kh.log("Auth Token : " + str(kh.authToken))
channel16 = LineChannel(kh)
kh.log("Channel Access Token : " + str(channel16.channelAccessToken))

kn = LineClient(authToken='')
kn.log("Auth Token : " + str(kn.authToken))
channel17 = LineChannel(kn)
kn.log("Channel Access Token : " + str(channel17.channelAccessToken))

ky = LineClient(authToken='')
ky.log("Auth Token : " + str(ky.authToken))
channel18 = LineChannel(ky)
ky.log("Channel Access Token : " + str(channel18.channelAccessToken))

kp = LineClient(authToken='')
kp.log("Auth Token : " + str(kp.authToken))
channel19 = LineChannel(kp)
kp.log("Channel Access Token : " + str(channel19.channelAccessToken))

kx = LineClient(authToken='')
kx.log("Auth Token : " + str(kx.authToken))
channel20 = LineChannel(kx)
kx.log("Channel Access Token : " + str(channel20.channelAccessToken))

kf = LineClient(authToken='')
kf.log("Auth Token : " + str(kf.authToken))
channel21 = LineChannel(kf)
kf.log("Channel Access Token : " + str(channel21.channelAccessToken))

kg = LineClient(authToken='')
kg.log("Auth Token : " + str(kg.authToken))
channel22 = LineChannel(kg)
kg.log("Channel Access Token : " + str(channel22.channelAccessToken))

kq = LineClient(authToken='')
kq.log("Auth Token : " + str(kq.authToken))
channel23 = LineChannel(kq)
kq.log("Channel Access Token : " + str(channel23.channelAccessToken))

kw = LineClient(authToken='')
kw.log("Auth Token : " + str(kw.authToken))
channel24 = LineChannel(kw)
kw.log("Channel Access Token : " + str(channel24.channelAccessToken))

kz = LineClient(authToken='')
kz.log("Auth Token : " + str(kz.authToken))
channel25 = LineChannel(kz)
kz.log("Channel Access Token : " + str(channel25.channelAccessToken))

sw = LineClient(authToken='')
sw.log("Auth Token : " + str(sw.authToken))
channel26 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel26.channelAccessToken))

print "Mantaappp Login eGy-NgapaK Succsess"

poll = LinePoll(cl)
call = LineCall(cl)
creator = [""]
owner = [""]
admin = [""]
staff = [""]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ke.getProfile().mid
Emid = kt.getProfile().mid
Fmid = ka.getProfile().mid
Gmid = kb.getProfile().mid
Hmid = ko.getProfile().mid
Imid = ks.getProfile().mid
Jmid = ku.getProfile().mid
Kmid = kr.getProfile().mid
Lmid = kd.getProfile().mid
Mmid = kj.getProfile().mid
Nmid = km.getProfile().mid
Omid = kv.getProfile().mid
Pmid = kh.getProfile().mid
Qmid = kn.getProfile().mid
Rmid = ky.getProfile().mid
Smid = kp.getProfile().mid
Tmid = kx.getProfile().mid
Umid = kf.getProfile().mid
Vmid = kg.getProfile().mid
Wmid = kq.getProfile().mid
Xmid = kw.getProfile().mid
Ymid = kz.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,ke,kt,ka,kb,ko,ks,ku,kr,kd,kj,km,kv,kh,kn,kp,kx,kf,kg,kq,kw,kz]
ABC = [cl,ki,kk,kc,ke,kt,ka,kb,ko,ks,ku,kr,kd,kj,km,kv,kh,kn,kp,kx,kf,kg,kq,kw,kz]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Tmid,Umid,Vmid,Wmid,Xmid,Ymid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
#protectantijs = []
#ghost = []
autoleaveroom =[]
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = ke.getProfile().displayName
responsename5 = kt.getProfile().displayName
responsename6 = ka.getProfile().displayName
responsename7 = kb.getProfile().displayName
responsename8 = ko.getProfile().displayName
responsename9 = ks.getProfile().displayName
responsename10 = ku.getProfile().displayName
responsename11 = kr.getProfile().displayName
responsename12 = kd.getProfile().displayName
responsename13 = kj.getProfile().displayName
responsename14 = km.getProfile().displayName
responsename15 = kv.getProfile().displayName
responsename16 = kh.getProfile().displayName
responsename17 = kn.getProfile().displayName
responsename18 = ky.getProfile().displayName
responsename19 = kp.getProfile().displayName
responsename20 = kx.getProfile().displayName
responsename21 = kf.getProfile().displayName
responsename22 = kg.getProfile().displayName
responsename23 = kq.getProfile().displayName
responsename24 = kw.getProfile().displayName
responsename25 = kz.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"ɪɴɪ sɪᴅᴇʀ",
    "Respontag":"NO TAG DUDUL.... TIPUK PURON:...",
    "welcome":"Selamat datang & betah, ᴅᴀɴ ᴊᴀɴʟᴜᴘᴀ ᴄᴇᴋ ɴᴏᴛᴇ 😍😍😘😘💢💢👈",
    "comment":"Like like & like by ᴇɢʏ ɴɢᴀᴘᴀᴋ",
    "message":"Terimakasih sudah add saya ,, By: eGy Ngapakkkk..",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    #    cl.sendImageWithURL(msg.to,image)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        ki.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIdsx()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"┃🇮🇩┃ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n┃🇮🇩┃ Group : "+str(len(gid))+"\n┃🇮🇩┃ Teman : "+str(len(teman))+"\n┃🇮🇩┃ Expired : In "+hari+"\n┃🇮🇩┃ Version : eGy-NgapaK\n┃🇮🇩┃ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃🇮🇩┃ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n┣🌟🔵eGy ⁿᵍaᵖaᵏ🔵🌟\n╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eGy ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Me\n" + \
                  "┃💢┃ " + key + "Mid「@」\n" + \
                  "┃💢┃ " + key + "Info「@」\n" + \
                  "┃💢┃ " + key + "Nk「@」\n" + \
                  "┃💢┃ " + key + "Makasih「@」\n" + \
                  "┃💢┃ " + key + "Autolike on/off\n" + \
                  "┃💢┃ " + key + "Rakyat\n" + \
                  "┃💢┃ " + key + "Kuis\n" + \
                  "┃💢┃ " + key + "Status\n" + \
                  "┃💢┃ " + key + "About\n" + \
                  "┃💢┃ " + key + "Restart\n" + \
                  "┃💢┃ " + key + "Runtime\n" + \
                  "┃💢┃ " + key + "Creator\n" + \
                  "┃💢┃ " + key + "Bio\n" + \
                  "┃💢┃ " + key + "E/Sp\n" + \
                  "┃💢┃ " + key + "Sprespon\n" + \
                  "┃💢┃ " + key + "Sepii/Hmmm/Euy\n" + \
                  "┃💢┃ " + key + "Bro ,/Bro ,,\n" + \
                  "┃💢┃ " + key + "B,\n" + \
                  "┃💢┃ " + key + "R\n" + \
                  "┃💢┃ " + key + "M,\n" + \
                  "┃💢┃ " + key + "Leave「Namagrup」\n" + \
                  "┃💢┃ " + key + "Ginfo\n" + \
                  "┃💢┃ " + key + "Img:\n" + \
                  "┃💢┃ " + key + "Rem chat\n" + \
                  "┃💢┃ " + key + "Yank\n" + \
                  "┃💢┃ " + key + "Open\n" + \
                  "┃💢┃ " + key + "Close\n" + \
                  "┃💢┃ " + key + "Url grup\n" + \
                  "┃💢┃ " + key + "Gruplist\n" + \
                  "┃💢┃ " + key + "Infogrup「angka」\n" + \
                  "┃💢┃ " + key + "Infomem「angka」\n" + \
                  "┃💢┃ " + key + "Lurking「on/off」\n" + \
                  "┃💢┃ " + key + "Lurkers\n" + \
                  "┃💢┃ " + key + "Cek「on/off」\n" + \
                  "┃💢┃ " + key + "Updatefoto\n" + \
                  "┃💢┃ " + key + "Updategrup\n" + \
                  "┃💢┃ " + key + "Upbot\n" + \
                  "┃💢┃ " + key + "Broadcast:「Text」\n" + \
                  "┃💢┃ " + key + "Setkey「New Key」\n" + \
                  "┃💢┃ " + key + "Mykey\n" + \
                  "┃💢┃ " + key + "Resetkey\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "ID line:「Id Line nya」\n" + \
                  "┃💢┃ " + key + "Sholat:「Nama Kota」\n" + \
                  "┃💢┃ " + key + "Cuaca:「Nama Kota」\n" + \
                  "┃💢┃ " + key + "Lokasi:「Nama Kota」\n" + \
                  "┃💢┃ " + key + "Music:「Judul Lagu」\n" + \
                  "┃💢┃ " + key + "Lirik:「Judul Lagu」\n" + \
                  "┃💢┃ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "┃💢┃ " + key + "Ytmp4:「Judul Video」\n" + \
                  "┃💢┃ " + key + "Profileig:「Nama IG」\n" + \
                  "┃💢┃ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "┃💢┃ " + key + "Jumlah:「angka」\n" + \
                  "┃💢┃ " + key + "Sue「@」\n" + \
                  "┃💢┃ " + key + "Spc:「jumlahnya」\n" + \
                  "┃💢┃ " + key + "Spc\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Notag「on/off」\n" + \
                  "┃💢┃ " + key + "S p「on/off」\n" + \
                  "┃💢┃ " + key + "Prl「on/off」\n" + \
                  "┃💢┃ " + key + "Pin「on/off」\n" + \
                  "┃💢┃ " + key + "Pck「on/off」\n" + \
                  "┃💢┃ " + key + "Pcel「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Sticker「on/off」\n" + \
                  "┃💢┃ " + key + "Respon「on/off」\n" + \
                  "┃💢┃ " + key + "Absen\n" + \
                  "┃💢┃ " + key + "Contact「on/off」\n" + \
                  "┃💢┃ " + key + "Autojoin「on/off」\n" + \
                  "┃💢┃ " + key + "Autoadd「on/off」\n" + \
                  "┃💢┃ " + key + "Welcome「on/off」\n" + \
                  "┃💢┃ " + key + "Autoleave「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Admin:on\n" + \
                  "┃💢┃ " + key + "Admin:repeat\n" + \
                  "┃💢┃ " + key + "Staff:on\n" + \
                  "┃💢┃ " + key + "Staff:repeat\n" + \
                  "┃💢┃ " + key + "Bot:on\n" + \
                  "┃💢┃ " + key + "Bot:repeat\n" + \
                  "┃💢┃ " + key + "Adminadd「@」\n" + \
                  "┃💢┃ " + key + "Admindell「@」\n" + \
                  "┃💢┃ " + key + "Staffadd「@」\n" + \
                  "┃💢┃ " + key + "Staffdell「@」\n" + \
                  "┃💢┃ " + key + "Botadd「@」\n" + \
                  "┃💢┃ " + key + "Botdell「@」\n" + \
                  "┃💢┃ " + key + "Refresh\n" + \
                  "┃💢┃ " + key + "Listbot\n" + \
                  "┃💢┃ " + key + "Listadmin\n" + \
                  "┃💢┃ " + key + "Listprotect\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n┣━⏩eᵍʸ ⁿᵍaᵖaᵏ━⏩ \n╰━━━━━━━━━━━━━━━╯\n"+\
                  "──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Blc\n" + \
                  "┃💢┃ " + key + "Ban:on\n" + \
                  "┃💢┃ " + key + "Unban:on\n" + \
                  "┃💢┃ " + key + "Ban「@」\n" + \
                  "┃💢┃ " + key + "Unban「@」\n" + \
                  "┃💢┃ " + key + "Talkban「@」\n" + \
                  "┃💢┃ " + key + "Untalkban「@」\n" + \
                  "┃💢┃ " + key + "Talkban:on\n" + \
                  "┃💢┃ " + key + "Untalkban:on\n" + \
                  "┃💢┃ " + key + "Banlist\n" + \
                  "┃💢┃ " + key + "Talkbanlist\n" + \
                  "┃💢┃ " + key + "Clearban\n" + \
                  "┃💢┃ " + key + "Refresh\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Cek sider\n" + \
                  "┃💢┃ " + key + "Cek spam\n" + \
                  "┃💢┃ " + key + "Cek pesan \n" + \
                  "┃💢┃ " + key + "Cek respon \n" + \
                  "┃💢┃ " + key + "Cek welcome\n" + \
                  "┃💢┃ " + key + "Set sider:「Text」\n" + \
                  "┃💢┃ " + key + "Set spam:「Text」\n" + \
                  "┃💢┃ " + key + "Set pesan:「Text」\n" + \
                  "┃💢┃ " + key + "Set respon:「Text」\n" + \
                  "┃💢┃ " + key + "Set welcome:「Text」\n" + \
                  "┃💢┃ " + key + "Myn:「Nama」\n" + \
                  "┃💢┃ " + key + "B1:「Nama」\n" + \
                  "┃💢┃ " + key + "B2:「Nama」\n" + \
                  "┃💢┃ " + key + "B3:「Nama」\n" + \
                  "┃💢┃ " + key + "B4:「Nama」\n" + \
                  "┃💢┃ " + key + "B5:「Nama」\n" + \
                  "┃💢┃ " + key + "B6:「Nama」\n" + \
                  "┃💢┃ " + key + "B7:「Nama」\n" + \
                  "┃💢┃ " + key + "B8:「Nama」\n" + \
                  "┃💢┃ " + key + "B9:「Nama」\n" + \
                  "┃💢┃ " + key + "B10:「Nama」\n" + \
                  "┃💢┃ " + key + "B11:「Nama」\n" + \
                  "┃💢┃ " + key + "B12:「Nama」\n" + \
                  "┃💢┃ " + key + "B13:「Nama」\n" + \
                  "┃💢┃ " + key + "B14:「Nama」\n" + \
                  "┃💢┃ " + key + "B15:「Nama」\n" + \
                  "┃💢┃ " + key + "B16:「Nama」\n" + \
                  "┃💢┃ " + key + "B17:「Nama」\n" + \
                  "┃💢┃ " + key + "B18:「Nama」\n" + \
                  "┃💢┃ " + key + "B19:「Nama」\n" + \
                  "┃💢┃ " + key + "B20:「Nama」\n" + \
                  "┃💢┃ " + key + "B21:「Nama」\n" + \
                  "┃💢┃ " + key + "B22:「Nama」\n" + \
                  "┃💢┃ " + key + "B23:「Nama」\n" + \
                  "┃💢┃ " + key + "B24:「Nama」\n" + \
                  "┃💢┃ " + key + "B25:「Nama」\n" + \
                  "┃💢┃ " + key + "Swn:「Nama」\n" + \
                  "┃💢┃ " + key + "Bot1up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Bot2up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Bot3up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "┃💢┃ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n┣━⏩eᵍʸ ⁿᵍaᵖaᵏ━⏩\n╰━━━━━━━━━━━━━━━╯\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Blc\n" + \
                  "┃💢┃ " + key + "Ban:on\n" + \
                  "┃💢┃ " + key + "Unban:on\n" + \
                  "┃💢┃ " + key + "Ban「@」\n" + \
                  "┃💢┃ " + key + "Unban「@」\n" + \
                  "┃💢┃ " + key + "Talkban「@」\n" + \
                  "┃💢┃ " + key + "Untalkban「@」\n" + \
                  "┃💢┃ " + key + "Talkban:on\n" + \
                  "┃💢┃ " + key + "Untalkban:on\n" + \
                  "┃💢┃ " + key + "Banlist\n" + \
                  "┃💢┃ " + key + "Talkbanlist\n" + \
                  "┃💢┃ " + key + "Clearban\n" + \
                  "┃💢┃ " + key + "Refresh\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃💢┃ " + key + "Cek sider\n" + \
                  "┃💢┃ " + key + "Cek spam\n" + \
                  "┃💢┃ " + key + "Cek pesan \n" + \
                  "┃💢┃ " + key + "Cek respon \n" + \
                  "┃💢┃ " + key + "Cek welcome\n" + \
                  "┃💢┃ " + key + "Set sider:「Text」\n" + \
                  "┃💢┃ " + key + "Set spam:「Text」\n" + \
                  "┃💢┃ " + key + "Set pesan:「Text」\n" + \
                  "┃💢┃ " + key + "Set respon:「Text」\n" + \
                  "┃💢┃ " + key + "Set welcome:「Text」\n" + \
                  "┃💢┃ " + key + "Myn:「Nama」\n" + \
                  "┃💢┃ " + key + "B1:「Nama」\n" + \
                  "┃💢┃ " + key + "B2:「Nama」\n" + \
                  "┃💢┃ " + key + "B3:「Nama」\n" + \
                  "┃💢┃ " + key + "B4:「Nama」\n" + \
                  "┃💢┃ " + key + "B5:「Nama」\n" + \
                  "┃💢┃ " + key + "B6:「Nama」\n" + \
                  "┃💢┃ " + key + "B7:「Nama」\n" + \
                  "┃💢┃ " + key + "B8:「Nama」\n" + \
                  "┃💢┃ " + key + "B9:「Nama」\n" + \
                  "┃💢┃ " + key + "B10:「Nama」\n" + \
                  "┃💢┃ " + key + "B11:「Nama」\n" + \
                  "┃💢┃ " + key + "B12:「Nama」\n" + \
                  "┃💢┃ " + key + "B13:「Nama」\n" + \
                  "┃💢┃ " + key + "B14:「Nama」\n" + \
                  "┃💢┃ " + key + "B15:「Nama」\n" + \
                  "┃💢┃ " + key + "B16:「Nama」\n" + \
                  "┃💢┃ " + key + "B17:「Nama」\n" + \
                  "┃💢┃ " + key + "B18:「Nama」\n" + \
                  "┃💢┃ " + key + "B19:「Nama」\n" + \
                  "┃💢┃ " + key + "B20:「Nama」\n" + \
                  "┃💢┃ " + key + "Swn:「Nama」\n" + \
                  "┃💢┃ " + key + "Bot1up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Bot2up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Bot3up「Kirim fotonya」\n" + \
                  "┃💢┃ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "┃💢┃ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃💢┃ ┃┃ eᵍʸ┃💢┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n┣━⏩eᵍʸ ⁿᵍaᵖaᵏ━⏩\n╰━━━━━━━━━━━━━━━╯\n"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            cl.reissueGroupTicket(op.param1)
                                            X = cl.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kt.acceptGroupInvitation(op.param1)
                        ginfo = kt.getGroup(op.param1)
                        kt.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kt.leaveGroup(op.param1)
                    else:
                        kt.acceptGroupInvitation(op.param1)
                        ginfo = kt.getGroup(op.param1)
                        kt.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        ko.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ko.leaveGroup(op.param1)
                    else:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        ko.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                        ks.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ks.leaveGroup(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                        ks.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ku.acceptGroupInvitation(op.param1)
                        ginfo = ku.getGroup(op.param1)
                        ku.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ku.leaveGroup(op.param1)
                    else:
                        ku.acceptGroupInvitation(op.param1)
                        ginfo = ku.getGroup(op.param1)
                        ku.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Kmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kr.acceptGroupInvitation(op.param1)
                        ginfo = kr.getGroup(op.param1)
                        kr.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kr.leaveGroup(op.param1)
                    else:
                        kr.acceptGroupInvitation(op.param1)
                        ginfo = kr.getGroup(op.param1)
                        kr.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Lmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Mmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kj.acceptGroupInvitation(op.param1)
                        ginfo = kj.getGroup(op.param1)
                        kj.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kj.leaveGroup(op.param1)
                    else:
                        kj.acceptGroupInvitation(op.param1)
                        ginfo = kj.getGroup(op.param1)
                        kj.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Nmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Omid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kv.acceptGroupInvitation(op.param1)
                        ginfo = kv.getGroup(op.param1)
                        kv.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kv.leaveGroup(op.param1)
                    else:
                        kv.acceptGroupInvitation(op.param1)
                        ginfo = kv.getGroup(op.param1)
                        kv.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Pmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kh.leaveGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Qmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
                        kn.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kn.leaveGroup(op.param1)
                    else:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
                        kn.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Rmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ky.acceptGroupInvitation(op.param1)
                        ginfo = ky.getGroup(op.param1)
                        ky.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ky.leaveGroup(op.param1)
                    else:
                        ky.acceptGroupInvitation(op.param1)
                        ginfo = ky.getGroup(op.param1)
                        ky.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Smid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kp.acceptGroupInvitation(op.param1)
                        ginfo = kp.getGroup(op.param1)
                        kp.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kp.leaveGroup(op.param1)
                    else:
                        kp.acceptGroupInvitation(op.param1)
                        ginfo = kp.getGroup(op.param1)
                        kp.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Tmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kx.acceptGroupInvitation(op.param1)
                        ginfo = kx.getGroup(op.param1)
                        kx.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kx.leaveGroup(op.param1)
                    else:
                        kx.acceptGroupInvitation(op.param1)
                        ginfo = kx.getGroup(op.param1)
                        kx.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Umid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Vmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kg.leaveGroup(op.param1)
                    else:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Wmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kq.acceptGroupInvitation(op.param1)
                        ginfo = kq.getGroup(op.param1)
                        kq.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kq.leaveGroup(op.param1)
                    else:
                        kq.acceptGroupInvitation(op.param1)
                        ginfo = kq.getGroup(op.param1)
                        kq.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Xmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kw.acceptGroupInvitation(op.param1)
                        ginfo = kw.getGroup(op.param1)
                        kw.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kw.leaveGroup(op.param1)
                    else:
                        kw.acceptGroupInvitation(op.param1)
                        ginfo = kw.getGroup(op.param1)
                        kw.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Ymid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kz.acceptGroupInvitation(op.param1)
                        ginfo = kz.getGroup(op.param1)
                        kz.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kz.leaveGroup(op.param1)
                    else:
                        kz.acceptGroupInvitation(op.param1)
                        ginfo = kz.getGroup(op.param1)
                        kz.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                            kt.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ke.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                            kt.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kt.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kt.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kt.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kt.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kt.kickoutFromGroup(op.param1,[op.param2])
                                    kt.updateGroup(G)
                                    Ticket = kt.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kt.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kt.updateGroup(G)
                                    Ticket = kt.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        ka.inviteIntoGroup(op.param1,[op.param3])
                                        kt.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            kt.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kt.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kt.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kt.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ka.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.updateGroup(G)
                                    Ticket = ka.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ka.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ka.updateGroup(G)
                                    Ticket = ka.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                        kt.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ko.kickoutFromGroup(op.param1,[op.param2])
                                            ko.inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ko.kickoutFromGroup(op.param1,[op.param2])
                            ko.inviteIntoGroup(op.param1,[op.param3])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,[op.param3])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kb.updateGroup(G)
                                    Ticket = ka.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kr.kickoutFromGroup(op.param1,[op.param2])
                                        kr.inviteIntoGroup(op.param1,[op.param3])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                            kj.inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ku.kickoutFromGroup(op.param1,[op.param2])
                        ku.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ko.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ko.kickoutFromGroup(op.param1,[op.param2])
                                    ko.updateGroup(G)
                                    Ticket = ko.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ko.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ko.updateGroup(G)
                                    Ticket = ko.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kv.kickoutFromGroup(op.param1,[op.param2])
                                        kv.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kn.kickoutFromGroup(op.param1,[op.param2])
                        kn.inviteIntoGroup(op.param1,[op.param3])
                        ko.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ky.kickoutFromGroup(op.param1,[op.param2])
                            ky.inviteIntoGroup(op.param1,[op.param3])
                            ko.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kp.kickoutFromGroup(op.param1,[op.param2])
                                kp.inviteIntoGroup(op.param1,[op.param3])
                                ko.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ku.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ku.kickoutFromGroup(op.param1,[op.param2])
                                    ku.updateGroup(G)
                                    Ticket = ku.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ku.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ku.updateGroup(G)
                                    Ticket = kr.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ko.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ko.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kx.kickoutFromGroup(op.param1,[op.param2])
                        kx.inviteIntoGroup(op.param1,[op.param3])
                        ks.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            ks.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ks.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ku.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ku.kickoutFromGroup(op.param1,[op.param2])
                                    ku.updateGroup(G)
                                    Ticket = ku.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ku.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ku.updateGroup(G)
                                    Ticket = kr.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ks.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                            ks.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Kmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        kj.inviteIntoGroup(op.param1,[op.param3])
                        ku.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            km.inviteIntoGroup(op.param1,[op.param3])
                            ku.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kv.kickoutFromGroup(op.param1,[op.param2])
                                kv.inviteIntoGroup(op.param1,[op.param3])
                                ku.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kr.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr.updateGroup(G)
                                    Ticket = kr.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kr.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kr.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                        ku.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                            ku.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Lmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ky.kickoutFromGroup(op.param1,[op.param2])
                        ky.inviteIntoGroup(op.param1,[op.param3])
                        kr.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kp.kickoutFromGroup(op.param1,[op.param2])
                            kp.inviteIntoGroup(op.param1,[op.param3])
                            kr.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kx.kickoutFromGroup(op.param1,[op.param2])
                                kx.inviteIntoGroup(op.param1,[op.param3])
                                kr.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kd.updateGroup(G)
                                    Ticket = kj.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kr.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kr.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Mmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kt.kickoutFromGroup(op.param1,[op.param2])
                                kt.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kj.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kj.kickoutFromGroup(op.param1,[op.param2])
                                    kj.updateGroup(G)
                                    Ticket = kj.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kj.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kj.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kr.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                            kj.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Nmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kj.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ko.kickoutFromGroup(op.param1,[op.param2])
                            ko.inviteIntoGroup(op.param1,[op.param3])
                            kj.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,[op.param3])
                                kj.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    km.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    km.updateGroup(G)
                                    Ticket = kv.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ku.kickoutFromGroup(op.param1,[op.param2])
                                        ku.inviteIntoGroup(op.param1,[op.param3])
                                        kj.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kr.kickoutFromGroup(op.param1,[op.param2])
                                            kr.inviteIntoGroup(op.param1,[op.param3])
                                            kj.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Omid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kj.kickoutFromGroup(op.param1,[op.param2])
                            kj.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kv.kickoutFromGroup(op.param1,[op.param2])
                                kv.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                    kh.updateGroup(G)
                                    Ticket = kh.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kh.updateGroup(G)
                                    Ticket = kn.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ky.kickoutFromGroup(op.param1,[op.param2])
                                        ky.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kp.kickoutFromGroup(op.param1,[op.param2])
                                            kp.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Pmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kx.kickoutFromGroup(op.param1,[op.param2])
                        kx.inviteIntoGroup(op.param1,[op.param3])
                        kv.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kv.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kv.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kv.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kv.kickoutFromGroup(op.param1,[op.param2])
                                    kv.updateGroup(G)
                                    Ticket = kv.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kv.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kv.updateGroup(G)
                                    Ticket = kv.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kv.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kv.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Qmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                        kt.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kn.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kn.kickoutFromGroup(op.param1,[op.param2])
                                    kn.updateGroup(G)
                                    Ticket = kn.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kn.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kn.updateGroup(G)
                                    Ticket = kn.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ko.kickoutFromGroup(op.param1,[op.param2])
                                        ko.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                            ks.inviteIntoGroup(op.param1,[op.param3])
                                            kh.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Rmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ku.kickoutFromGroup(op.param1,[op.param2])
                        ku.inviteIntoGroup(op.param1,[op.param3])
                        kn.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr.kickoutFromGroup(op.param1,[op.param2])
                            kr.inviteIntoGroup(op.param1,[op.param3])
                            kn.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kn.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kp.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kp.kickoutFromGroup(op.param1,[op.param2])
                                    kp.updateGroup(G)
                                    Ticket = kp.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kp.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kp.updateGroup(G)
                                    Ticket = kp.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                        kj.inviteIntoGroup(op.param1,[op.param3])
                                        kn.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            km.kickoutFromGroup(op.param1,[op.param2])
                                            km.inviteIntoGroup(op.param1,[op.param3])
                                            kn.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Smid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                        kr.inviteIntoGroup(op.param1,[op.param3])
                        ky.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            ky.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kj.kickoutFromGroup(op.param1,[op.param2])
                                kj.inviteIntoGroup(op.param1,[op.param3])
                                ky.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ky.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ky.kickoutFromGroup(op.param1,[op.param2])
                                    ky.updateGroup(G)
                                    Ticket = ky.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ky.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ky.updateGroup(G)
                                    Ticket = ky.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ky.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                            kt.inviteIntoGroup(op.param1,[op.param3])
                                            ky.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Tmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kz.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kj.kickoutFromGroup(op.param1,[op.param2])
                            kj.inviteIntoGroup(op.param1,[op.param3])
                            kz.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.inviteIntoGroup(op.param1,[op.param3])
                                kz.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kz.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kz.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Umid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        kj.inviteIntoGroup(op.param1,[op.param3])
                        kx.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                            kf.inviteIntoGroup(op.param1,[op.param3])
                            kx.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kg.kickoutFromGroup(op.param1,[op.param2])
                                kg.inviteIntoGroup(op.param1,[op.param3])
                                kx.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kx.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kx.kickoutFromGroup(op.param1,[op.param2])
                                    kx.updateGroup(G)
                                    Ticket = kx.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kx.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kx.updateGroup(G)
                                    Ticket = kx.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kw.kickoutFromGroup(op.param1,[op.param2])
                                        kw.inviteIntoGroup(op.param1,[op.param3])
                                        kx.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                            kx.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Vmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kx.kickoutFromGroup(op.param1,[op.param2])
                        kx.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ky.kickoutFromGroup(op.param1,[op.param2])
                                ky.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kz.kickoutFromGroup(op.param1,[op.param2])
                                        kz.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kf.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Wmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                        kt.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kg.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Xmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kq.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kq.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kq.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kq.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kq.kickoutFromGroup(op.param1,[op.param2])
                                    kq.updateGroup(G)
                                    Ticket = kq.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kq.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kq.updateGroup(G)
                                    Ticket = kq.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kq.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kz.kickoutFromGroup(op.param1,[op.param2])
                                            kz.inviteIntoGroup(op.param1,[op.param3])
                                            kq.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Ymid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                        ko.inviteIntoGroup(op.param1,[op.param3])
                        kw.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ks.kickoutFromGroup(op.param1,[op.param2])
                            ks.inviteIntoGroup(op.param1,[op.param3])
                            kw.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ku.kickoutFromGroup(op.param1,[op.param2])
                                ku.inviteIntoGroup(op.param1,[op.param3])
                                kw.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kw.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kw.kickoutFromGroup(op.param1,[op.param2])
                                    kw.updateGroup(G)
                                    Ticket = kw.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kv.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ky.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kx.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kz.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kw.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kw.updateGroup(G)
                                    Ticket = kw.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kr.kickoutFromGroup(op.param1,[op.param2])
                                        kr.inviteIntoGroup(op.param1,[op.param3])
                                        kw.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kn.kickoutFromGroup(op.param1,[op.param2])
                                            kn.inviteIntoGroup(op.param1,[op.param3])
                                            kw.acceptGroupInvitation(op.param1)
                                        except:
                                            pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
              #     contact = cl.getContact(msg.from_)
               #    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                       #    ki.sendImageWithURL(msg.to,image)
                      #     ki.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002769","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n┃🇮🇩┃ STKID : " + msg.contentMetadata["STKID"] + "\n┃🇮🇩┃ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n┃🇮🇩┃ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["RAfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = ke.downloadObjectMsg(msg_id)
                     path5 = kt.downloadObjectMsg(msg_id)
                     path6 = ka.downloadObjectMsg(msg_id)
                     path7 = kb.downloadObjectMsg(msg_id)
                     path8 = ko.downloadObjectMsg(msg_id)
                     path9 = ks.downloadObjectMsg(msg_id)
                     path10 = ku.downloadObjectMsg(msg_id)
                     path11 = kr.downloadObjectMsg(msg_id)
                     path12 = kd.downloadObjectMsg(msg_id)
                     path13 = kj.downloadObjectMsg(msg_id)
                     path14 = km.downloadObjectMsg(msg_id)
                     path15 = kv.downloadObjectMsg(msg_id)
                     path16 = kh.downloadObjectMsg(msg_id)
                     path17 = kn.downloadObjectMsg(msg_id)
                     path18 = ky.downloadObjectMsg(msg_id)
                     path19 = kp.downloadObjectMsg(msg_id)
                     path20 = kx.downloadObjectMsg(msg_id)
                     path21 = kf.downloadObjectMsg(msg_id)
                     path22 = kg.downloadObjectMsg(msg_id)
                     path23 = kq.downloadObjectMsg(msg_id)
                     path24 = kw.downloadObjectMsg(msg_id)
                     path25 = kz.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path4)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kt.updateProfilePicture(path5)
                     kt.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ka.updateProfilePicture(path6)
                     ka.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path7)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ko.updateProfilePicture(path8)
                     ko.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ks.updateProfilePicture(path9)
                     ks.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ku.updateProfilePicture(path10)
                     ku.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kr.updateProfilePicture(path11)
                     kr.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path12)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kj.updateProfilePicture(path13)
                     kj.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     km.updateProfilePicture(path14)
                     km.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kv.updateProfilePicture(path15)
                     kv.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kh.updateProfilePicture(path16)
                     kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kn.updateProfilePicture(path17)
                     kn.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ky.updateProfilePicture(path18)
                     ky.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kp.updateProfilePicture(path19)
                     kp.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kx.updateProfilePicture(path20)
                     kx.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path21)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path22)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kq.updateProfilePicture(path23)
                     kq.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kw.updateProfilePicture(path24)
                     kw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kz.updateProfilePicture(path25)
                     kz.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                          #     ki.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")
                                k1.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")
                                k1.sendText(msg.to, "Selfbot diaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))
                               cl.sendMessage(msg.to, ("? https://line.me/ti/p/vFbarWjff3 ?"))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┃💢┃ eᵍʸ ┃💢┃ Protection\n\n"
                                if wait["sticker"] == True: md+="┃💢┃ Sticker「ON」\n"
                                else: md+="┃💢┃ Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃💢┃ Contact「ON」\n"
                                else: md+="┃💢┃ Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃💢┃ Talkban「ON」\n"
                                else: md+="┃💢┃ Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃💢┃ Notag「ON」\n"
                                else: md+="┃💢┃ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃💢┃ Respon「ON」"
                                else: md+="┃💢┃ Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="┃💢┃ Autojoin「ON」\n"
                                else: md+="┃💢┃ Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="┃💢┃ Autoadd「ON」\n"
                                else: md+="┃💢┃ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃💢┃ Welcome「ON」\n"
                                else: md+="┃💢┃ Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="┃💢┃ Autoleave「ON」\n"
                                else: md+="┃💢┃ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃💢┃ Protecturl「ON」\n"
                                else: md+="┃💢┃ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃💢┃ Protectjoin「ON」\n"
                                else: md+="┃💢┃ Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃💢┃ Protectkick「ON」\n"
                                else: md+="┃💢┃ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃💢┃ Protectcancel「ON」\n"
                                else: md+="┃💢┃ Protectcancel「OFF」\n"
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"Creator eGy Ngapakkk") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                          #     cl.sendText(msg.to,"ini contact boz/creator...")
                          #     ki.sendMessage1(msg)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                               ki.sendMessage(msg.to, msg._from)
               #                kk.sendMessage(msg.to, msg._from)
                #               kc.sendMessage(msg.to, msg._from)
                 #              ke.sendMessage(msg.to, msg._from)
                  #             kt.sendMessage(msg.to, msg._from)
                   #            ka.sendMessage(msg.to, msg._from)
                    #           kb.sendMessage(msg.to, msg._from)
                     #          ko.sendMessage(msg.to, msg._from)
                      #         ks.sendMessage(msg.to, msg._from)
                       #        ku.sendMessage(msg.to, msg._from)
                        #       kr.sendMessage(msg.to, msg._from)
                         #      kd.sendMessage(msg.to, msg._from)
                          #     kj.sendMessage(msg.to, msg._from)
                           #    km.sendMessage(msg.to, msg._from)
                             #  kv.sendMessage(msg.to, msg._from)
                            #   kh.sendMessage(msg.to, msg._from)
                           #    kn.sendMessage(msg.to, msg._from)
                          #     ky.sendMessage(msg.to, msg._from)
                         #      kp.sendMessage(msg.to, msg._from)
                        #       kx.sendMessage(msg.to, msg._from)
                            #   kn.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "┃🇮🇩┃ Nama : "+str(mi.displayName)+"\n┃🇮🇩┃ Mid : " +key1+"\n┃🇮🇩┃ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "rakyat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Kmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Lmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Mmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Nmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Omid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Pmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Qmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Rmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Smid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Tmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Umid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Vmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Wmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Xmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Ymid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)
                               cl.sendText(msg.to,"Kui kabeh muridku Coooyyyyy")

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "rem chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.sendText(msg.to,"Tunggu Sebentar Bozzz,,, gak sampe 5 hari ko bozzz...")
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kt.removeAllMessages(op.param2)
                                   ka.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   ko.removeAllMessages(op.param2)
                                   ks.removeAllMessages(op.param2)
                                   ku.removeAllMessages(op.param2)
                                   kr.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kv.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   kn.removeAllMessages(op.param2)
                                   ky.removeAllMessages(op.param2)
                                   kp.removeAllMessages(op.param2)
                                   kx.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kq.removeAllMessages(op.param2)
                                   kw.removeAllMessages(op.param2)
                                   kz.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"Rem Chat beresss bozzz...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu 2 menit bozzz...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Bot Mulai AwaL bozzzz...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "┃🇮🇩┃ ┃DPK┃ Family Grup Info\n\n┃🇮🇩┃ Nama Group : {}".format(G.name)+ "\n┃🇮🇩┃ ID Group : {}".format(G.id)+ "\n┃🇮🇩┃ Pembuat : {}".format(G.creator.displayName)+ "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))+ "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))+ "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)+ "\n┃🇮🇩┃ Group Qr : {}".format(gQr)+ "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "┃🇮🇩┃ ┃eGy┃ Family Grup Info\n"
                                ret_ += "\n┃🇮🇩┃ Nama Group : {}".format(G.name)
                                ret_ += "\n┃🇮🇩┃ ID Group : {}".format(G.id)
                                ret_ += "\n┃🇮🇩┃ Pembuat : {}".format(gCreator)
                                ret_ += "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┃🇮🇩┃ Group Qr : {}".format(gQr)
                                ret_ += "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "┃🇮🇩┃ "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"┃🇮🇩┃ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kt.leaveGroup(i)
                                    ka.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    ko.leaveGroup(i)
                                    ks.leaveGroup(i)
                                    ku.leaveGroup(i)
                                    kr.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    kj.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kv.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    kn.leaveGroup(i)
                                    ky.leaveGroup(i)
                                    kp.leaveGroup(i)
                                    kx.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kq.leaveGroup(i)
                                    kw.leaveGroup(i)
                                    kz.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Amid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Bmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["RAfoto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b3: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b4: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b5: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kt.getProfile()
                                profile.displayName = string
                                kt.updateProfile(profile)
                                kt.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b6: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b7: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b7: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ko.getProfile()
                                profile.displayName = string
                                ko.updateProfile(profile)
                                ko.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b9: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ks.getProfile()
                                profile.displayName = string
                                ks.updateProfile(profile)
                                ks.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b10: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ku.getProfile()
                                profile.displayName = string
                                ku.updateProfile(profile)
                                ku.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b11: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kr.getProfile()
                                profile.displayName = string
                                kr.updateProfile(profile)
                                kr.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b12: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b13: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kj.getProfile()
                                profile.displayName = string
                                kj.updateProfile(profile)
                                kj.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b14: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b15: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kv.getProfile()
                                profile.displayName = string
                                kv.updateProfile(profile)
                                kv.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b16: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b17: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kn.getProfile()
                                profile.displayName = string
                                kn.updateProfile(profile)
                                kn.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b18: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ky.getProfile()
                                profile.displayName = string
                                ky.updateProfile(profile)
                                ky.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b19: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kp.getProfile()
                                profile.displayName = string
                                kp.updateProfile(profile)
                                kp.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b20: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kx.getProfile()
                                profile.displayName = string
                                kx.updateProfile(profile)
                                kx.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b21: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b21: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b23: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kq.getProfile()
                                profile.displayName = string
                                kq.updateProfile(profile)
                                kq.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b24: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kw.getProfile()
                                profile.displayName = string
                                kw.updateProfile(profile)
                                kw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b25: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kz.getProfile()
                                profile.displayName = string
                                kz.updateProfile(profile)
                                kz.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("swn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif "Bio @" in msg.text:
                            _name = msg.text.replace("Getbio @","")
                            _nametarget = _name.rstrip(" ")
                            gs = cl.getGroup(msg.to)
                            for h in gs.members:
                              if _nametarget == h.displayName:
                                  cl.sendText(msg.to,"[Status]:\n" + h.statusMessage )
                              else:
                                pass

#===========BOT UPDATE============#
                        elif cmd == "hm" or text.lower() == 'sepii':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "euy":
                          if sender in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family bot\n\n"+ma+"\nTotal「%s」Family Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Family Saints" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family Protection\n\n┃🇮🇩┃ PROTECT URL :\n"+ma+"\n┃🇮🇩┃ PROTECT KICK :\n"+mb+"\n┃🇮🇩┃ PROTECT JOIN :\n"+md+"\n┃🇮🇩┃ PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "absen":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendText(msg.to,"hadir bozzz")
                                kk.sendText(msg.to,"aku yo hadir bozzz")
                                kc.sendText(msg.to,"inyong juga hadir")
                                ke.sendText(msg.to,"aku pie iki...")
                                kt.sendText(msg.to,"ojo pie-pie, rika lg apa..")
                                ka.sendText(msg.to,"lagi ngising broo..")
                                kb.sendText(msg.to,"sikaahhhh,. ngising jarree..")
                                ki.sendText(msg.to,"ehh.. loe loe pada ngomongin ap sh,,")
                                ks.sendText(msg.to,"ngomongi rondo bro..")
                                ku.sendText(msg.to,"nah ono sing ngmongi rondo kih,,, melu ehh..")
                                kr.sendText(msg.to,"bocah kue, angger krungu randa, y mesti nyambungan,,")
                                kd.sendText(msg.to,"aja kya kue isshhh broo,,,")
                                kj.sendText(msg.to,"kayong deweke ora doyan,,,")
                                km.sendText(msg.to,"randane ndi, randanee...")
                                kv.sendText(msg.to,"isshh,, kayong sangar kue, ujug ujug takon randa..")
                                kh.sendText(msg.to,"ws ws wiiissss, randa bae sh, ngmonge,,,")
                                kn.sendText(msg.to,"padahal, kae bocah, ora payu beeeh... hahaaa")
                                ky.sendText(msg.to,"husss,, ojo ngmong kya kui,,,")
                                kp.sendText(msg.to,"bozzz eGy mh ganteng ehh,,, payuan,,,")
                                kx.sendText(msg.to,"jangankan prawan,, randa bae nempel kabeh koh,,,")
                                ki.sendText(msg.to,"pisss bozz,, maaf bozzz,, ampuni kami bozzz,, kami khilap")
                                ko.sendText(msg.to,"Aku belum mandi")
                                ki.sendText(msg.to,"Tak tun tuang")
                                kk.sendText(msg.to,"Tak tun tuang")
                                ko.sendText(msg.to,"Tapi masih ganteng juga")
                                ke.sendText(msg.to,"Tak tun tuang")
                                kt.sendText(msg.to,"Tak tun tuang")
                                ko.sendText(msg.to,"apalagi kalau sudah mandi")
                                kb.sendText(msg.to,"Tak tun tuang")
                                ki.sendText(msg.to,"Pasti ganteng sekali")
                                ko.sendText(msg.to,"yiha")
                                ku.sendText(msg.to,"Kalau orang lain melihatku")
                                kr.sendText(msg.to,"Tak tun tuang")
                                kj.sendText(msg.to,"Badak aku taba bana")
                                kd.sendText(msg.to,"Tak tun tuang")
                                km.sendText(msg.to,"Tak tuntuang")
                                kv.sendText(msg.to,"Tapi kalau langsuang diidu")
                                kh.sendText(msg.to,"Tak tun tuang")
                                kn.sendText(msg.to,"Atagfirullah baunya")
                                ky.sendText(msg.to,"Males lanjutin ah")
                                kp.sendText(msg.to,"Sepi bat")
                                kx.sendText(msg.to,"Iya sepi udah udah")
                                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                                ki.sendText(msg.to,"Nah")
                                ki.sendText(msg.to,"Mending gua makan dulu")
                                ko.sendText(msg.to,"Siyap")
                                kc.sendText(msg.to,"Okeh")
                                ke.sendText(msg.to,"Katanya owner kita Jomblo ya")
                                kr.sendText(msg.to,"Iya emang")
                                kb.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                                kx.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
                                ko.sendText(msg.to,"Y udah lah.. moga cepet dapet yh...")
                                cl.sendText(msg.to,"iya Amin.. qu kojom dulu yh,, byeeee")
                                ki.sendText(msg.to,"Diiihhh,, dasaarrr duduuulllllll")
                                kw.sendText(msg.to,"aku jaga rumah ajh ahh,,, siapa tw ad berondong nungul... hhh")
                                cl.sendText(msg.to,"mantap ,,.")
                                kw.sendText(msg.to,"iya dong,, gue Gituloh,,, yg sllu setia di room ini hhaa,,,")

                        elif cmd == "yank":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendText(msg.to,"Aku belum mandi")
                                ki.sendText(msg.to,"Tak tun tuang")
                                kk.sendText(msg.to,"Tak tun tuang")
                                kc.sendText(msg.to,"Tapi masih ganteng juga")
                                ke.sendText(msg.to,"Tak tun tuang")
                                kt.sendText(msg.to,"Tak tun tuang")
                                ka.sendText(msg.to,"apalagi kalau sudah mandi")
                                kb.sendText(msg.to,"Tak tun tuang")
                                ki.sendText(msg.to,"Pasti ganteng sekali")
                                ks.sendText(msg.to,"yiha")
                                ku.sendText(msg.to,"Kalau orang lain melihatku")
                                kr.sendText(msg.to,"Tak tun tuang")
                                kj.sendText(msg.to,"Badak aku taba bana")
                                kd.sendText(msg.to,"Tak tun tuang")
                                km.sendText(msg.to,"Tak tuntuang")
                                kv.sendText(msg.to,"Tapi kalau langsuang diidu")
                                kh.sendText(msg.to,"Tak tun tuang")
                                kn.sendText(msg.to,"Atagfirullah baunya")
                                ky.sendText(msg.to,"Males lanjutin ah")
                                kp.sendText(msg.to,"Sepi bat")
                                kx.sendText(msg.to,"Iya sepi udah udah")
                                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                                ki.sendText(msg.to,"Nah")
                                ki.sendText(msg.to,"Mending gua makan dulu")
                                kk.sendText(msg.to,"Siyap")
                                kc.sendText(msg.to,"Okeh")
                                ke.sendText(msg.to,"Katanya owner kita Jomblo ya")
                                kr.sendText(msg.to,"Iya emang")
                                kb.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                                kx.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
                                ki.sendText(msg.to,"Y udah lah.. moga cepet dapet yh...")
                                cl.sendText(msg.to,"iya Amin.. qu kojom dulu yh,, byeeee")
                                ki.sendText(msg.to,"Diiihhh,, dasaarrr duduuulllllll")

                        elif cmd == "kuis":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendText(msg.to,"MULAIII")
                                ki.sendText(msg.to,"OK BOZZZ, SIAAPPP")
                                kk.sendText(msg.to,"OK, SEMUA UDH HADIR BOZZZ, KITA MULAI")
                                cl.sendText(msg.to,"OK ")
                                cl.sendText(msg.to,"HEWAN APA YANG KEPALANYA DI BELAKANG[...]")
                                kc.sendText(msg.to,"EEEH BUSETT,, MANA AD BOZ KEPALA DI BELAKANG")
                                ke.sendText(msg.to,"ADA PERTANYAAN BERARRTI AD JAWABAN, DUDUUULLL")
                                kc.sendText(msg.to,"SOKK JAJAL KOE JAWAB...")
                                ke.sendText(msg.to,"YOO SABAR OHH., LAGI TAK PIKIR-PIKIR  SUUW...")
                                kb.sendText(msg.to,"HEWAN YANG LAGI JALAN KEBELAKANG")
                                ki.sendText(msg.to,"HEWAN YANG KEPALANYA KETINGGALAN,,")
                                ks.sendText(msg.to,"EEHH BUSSEETTT KEPALA KETINGGALAN JARREEE...")
                                ku.sendText(msg.to,"HEWAN YANG LAGI TIDUR")
                                kr.sendText(msg.to,"HEWAN ULAR CABE")
                                cl.sendText(msg.to,"NAHHHH.. STOOPPP... ANDA BETUL. ULAR CABE")
                                cl.sendText(msg.to,"ok, lanjuttt... siaaaaapppp")
                                cl.sendText(msg.to,"APA KATA2 CWO, UNTUK MRLAMAR CWE[...]")
                                cl.sendText(msg.to,"GO, GO ,GOOOOOOOO......")
                                kd.sendText(msg.to," MAUKAH KAMU JDI TUNANGANKU")
                                km.sendText(msg.to,"MAUKAH KAMU JDI CALON ISTRIKU")
                                kv.sendText(msg.to,"TIBA SAATNYA AKU UNTUK MELAMAR KAMU")
                                cl.sendText(msg.to,"STOOPPPPP,,,,.")
                                cl.sendText(msg.to,"DONE.. [_TIBA SAATNYA AKU UNTUK MELAMAR KAMU_]")
                                cl.sendText(msg.to,"ok, kita njuuttt,,,")
                                cl.sendText(msg.to,"SEBUTKAN NAMA HEWAN,, YG DI AWALI DARI HURUF. [T]")
                                cl.sendText(msg.to,"GO, GO, GOOOOOOO...")
                                kn.sendText(msg.to,"TIKUS")
                                ky.sendText(msg.to,"TUPAY")
                                kp.sendText(msg.to,"TAWON")
                                kx.sendText(msg.to,"TENGU")
                                cl.sendText(msg.to,"OK DONE...... CUKUP.... HHAA")
                                cl.sendText(msg.to,"KITA LANJUT KE SOAL BERIKUT...")
                                cl.sendText(msg.to,"HEWAN APA SAJA YG HIDUP DI LAUTAN[...]")
                                cl.sendText(msg.to,"GO, GO, GOOOOOOO")
                                ki.sendText(msg.to,"IKAN, KURA-KURA, BUAYA")
                                kk.sendText(msg.to,"PUTRY DUYUNG, CUMI-CUMI, KODOK, AYAM KU JUGA DI LAUTAN, HHAA")
                                kc.sendText(msg.to,"SINGA LAUT, GAJAH LAUT, AYAM LAUT, KUCING LAUT... ")
                                ke.sendText(msg.to,"TIKUS LAUT, BADAK LAUT, KUDANIL, KUDA LAUT... ")
                                kr.sendText(msg.to,"BAH JAWABANE SERBA LAUT,, AKU YO BISO")
                                kr.sendText(msg.to,"BURUNG LAUT, KADAL LAUT, CACING LAUT, ULAR LAUT, BEBEK LAUT, ANJING LAUT, TENGO LAUT,")
                                kb.sendText(msg.to,"EHH BUSSEETT,, BANYAK BENER TUH,,, SUEEE,, AP ITU AD DI LAUTAN,, DUDUUULLLLL")
                                kx.sendText(msg.to,"HAHAHAAA NGAWUR KABEEEHHHH..")
                                ki.sendText(msg.to,"YG PASTI AKU BENER KAN,, HHAA")
                                cl.sendText(msg.to,"OK OK OK,,. AKU CUKUP SENANG, CUKUP KOPLAK JUGA,,,")
                                ki.sendText(msg.to,"IYA BOZZZ, SAMA AKU JUGA,,,. PADA KOPLAK,,.")
                                cl.sendText(msg.to,"OK OK DONE...")
                                cl.sendText(msg.to,"kita bahas, masalah hadiah,.. ok ok")
                                kr.sendText(msg.to,"ok bozzzz")
                                kr.sendText(msg.to,"kapan bozzz")
                                cl.sendText(msg.to,"ok hadianya nanti yh,, akhir bulan sajha,, biar sekalian tahun baruan ,, hh..,")
                                ki.sendText(msg.to,"diiihhh kooppllooookkkkk")
                                kh.sendText(msg.to,"Bozz dudulll,, lama bener,,")
                                ky.sendText(msg.to,"kuiss nya hari ini,, ko hadiah nya tahun depan,, kan Suueeee,")
                                kf.sendText(msg.to,"nah,, ad kuis gk ajak-2,, Sueeee")
                                kg.sendText(msg.to,"mana kuis mana,,,, Aiihhh bozzz payahhh")
                                kq.sendText(msg.to,"aihhh,, boozzz,, aku juga mw issshh, kuiss,")
                                kw.sendText(msg.to,"bozzz lagi bozz lagiii,, kuis nya")
                                kz.sendText(msg.to,"taw tuh,, bozz masa kita-2 gk di ajak,,")
                                cl.sendText(msg.to,"ok ok ok.,... nnti kita bikin kuis lg,, tpi hadir semua yh,,.,")
                                kf.sendText(msg.to,"ok ok bozzz,, siaapp,, kapan bozz")
                                cl.sendText(msg.to,"y nanti isshh,, bulan depan,, hhaa,, sabar yoo")
                                kf.sendText(msg.to,"ok bozzz,, saya tunggu bozzz")
                                kg.sendText(msg.to,"iy boss saya juga mw boss,,,")
                                kq.sendText(msg.to,"ok ok ok...,,")
                                kw.sendText(msg.to,"ok ok ok ok ok... siap hadirrr, kalo masalah kuis mah,,, hhaa")
                                kz.sendText(msg.to,"ok bozz,, y dh,, muanya,, saya pamit dulu yh,, mw anu dulu,, tanggung nih,. hehee,")
                                cl.sendText(msg.to,"ok ok semuanya,,, saya juga pamit dulu yh,,, rasanya ngantuk,, pengin bbuk,, habis kuis cape,, ketawa ketiwi,, hh,,")
                                ki.sendText(msg.to,"y dh,, aku juga pamit,, mw nguli,,,byeeee")
                                kh.sendText(msg.to,"aku juga")
                                kw.sendText(msg.to,"aku juga mw nguli udah jam nya,, ppaayyy semuanyaaaa,")

                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Amid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kt.acceptGroupInvitation(msg.to)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    ko.acceptGroupInvitation(msg.to)
                                    ks.acceptGroupInvitation(msg.to)
                                    ku.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "b,":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                         #       G = ki.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                          #      ginfo = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                        #        ki.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                       #         Ticket = ki.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kv.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kx.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kz.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kz.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kz.updateGroup(G)

                        elif cmd == "r":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                          #      G = ki.getGroup(msg.to)
                                ki.sendText(msg.to, "Assalamualaikum fams "+str(G.name))
                                kv.sendText(msg.to, "Assalamualaikum fams "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kt.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                ko.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                ku.leaveGroup(msg.to)
                                kr.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kv.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                kn.leaveGroup(msg.to)
                                ky.leaveGroup(msg.to)
                                kp.leaveGroup(msg.to)
                                kx.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kq.leaveGroup(msg.to)
                                kw.leaveGroup(msg.to)
                                kz.leaveGroup(msg.to)

                        elif cmd == "m,":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Assalamualaikum byee fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kt.leaveGroup(i)
                                        ka.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        ko.leaveGroup(i)
                                        ks.leaveGroup(i)
                                        ku.leaveGroup(i)
                                        kr.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        kj.leaveGroup(i)
                                        km.leaveGroup(i)
                                        kv.leaveGroup(i)
                                        kh.leaveGroup(i)
                                        kn.leaveGroup(i)
                                        ky.leaveGroup(i)
                                        kp.leaveGroup(i)
                                        kx.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kq.leaveGroup(i)
                                        kw.leaveGroup(i)
                                        kz.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "assist4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "assist5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kt.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kt.updateGroup(G)

                        elif cmd == "assist6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "assist7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "assist8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ko.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)

                        elif cmd == "assist9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ks.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ks.updateGroup(G)

                        elif cmd == "assist10":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ku.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ku.updateGroup(G)

                        elif cmd == "assist11":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kr.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kr.updateGroup(G)

                        elif cmd == "assist12":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "assist13":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kj.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kj.updateGroup(G)

                        elif cmd == "assist14":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = km.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)

                        elif cmd == "assist15":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kv.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kv.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kv.updateGroup(G)

                        elif cmd == "assist16":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)

                        elif cmd == "assist17":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kn.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kn.updateGroup(G)

                        elif cmd == "assist18":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ky.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ky.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ky.updateGroup(G)

                        elif cmd == "assist19":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kp.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kp.updateGroup(G)

                        elif cmd == "assist20":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kx.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kx.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kx.updateGroup(G)

                        elif cmd == "assist21":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kf.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)

                        elif cmd == "assist22":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)

                        elif cmd == "assist23":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kq.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kq.updateGroup(G)

                        elif cmd == "assist24":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kw.updateGroup(G)

                        elif cmd == "assist25":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kz.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kz.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kz.updateGroup(G)

                        elif cmd == "bro ,":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "bro ,,":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "┃eGy┃ ┃ngapak┃ Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "e" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "💢🌟🌟🌟💢..")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kt.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ka.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ko.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ks.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ku.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kr.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kd.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kj.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               km.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kv.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kh.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kn.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ky.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kp.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kx.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kf.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kg.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kq.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kw.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kz.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "cek on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  ki.sendMessage(msg.to, "Cek diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cek off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  ki.sendMessage(msg.to, "Cek dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0]
                                         ret_ += "\n┃🇮🇩┃ " + data[1]
                                         ret_ += "\n┃🇮🇩┃ " + data[2]
                                         ret_ += "\n┃🇮🇩┃ " + data[3]
                                         ret_ += "\n┃🇮🇩┃ " + data[4]
                                         ret_ += "\n┃🇮🇩┃ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n┃🇮🇩┃ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n┃🇮🇩┃ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n┃🇮🇩┃ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n┃🇮🇩┃ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n┃🇮🇩┃ Location : " + data[0]
                                    ret_ += "\n┃🇮🇩┃ Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik tidak ditemukan")

                        

                        elif cmd.startswith("img: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
                                    durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
                                    suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
                                    rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
                                    deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/resuls?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
                                    durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
                                    suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
                                    rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
                                    deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "┃🇮🇩┃ Link : " + "https://www.instagram.com/" + instagram
                                text = "┃🇮🇩┃ Name : "+namaIG+"\n┃🇮🇩┃ Username : "+usernameIG+"\n┃🇮🇩┃ Biography : "+bioIG+"\n┃🇮🇩┃ Follower : "+followerIG+"\n┃🇮🇩┃ Following : "+followIG+"\n┃🇮🇩┃ Post : "+mediaIG+"\n┃🇮🇩┃ Verified : "+verifIG+"\n┃🇮🇩┃ Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"┃🇮🇩┃ I N F O R M A S I ┃🇮🇩┃\n\n"+"┃🇮🇩┃ Date Of Birth : "+lahir+"\n┃🇮🇩┃ Age : "+usia+"\n┃🇮🇩┃ Ultah : "+ultah+"\n┃🇮🇩┃ Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spc: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spcall Diubah Menjadi " +strnum)
                                ki.sendText(msg.to,"Total Spcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("sue "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spc":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                group = ki.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Spc berhasil {} undangan Call Grup".format(str(wait["limit"])))
                                ki.sendMessage(msg.to, "Spc berhasil {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                        ki.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace("Welcome ",'')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Prl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace("Prl ",'')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pck ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pck ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pcel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pcel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "P cel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'S p ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace("S p ",'')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua pro sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua pro sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Makasih " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Admin:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Ora ono blc bozz")
                                    ki.sendMessage(msg.to,"Ora ono blc bozz")
                                    cl.sendMessage(msg.to,"By:eGy Ngapakkk")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)

#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
