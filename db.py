#''' # - Эта хрень нужна мне не удаляй *
from random import Random
import random
from config import settings
from firebase import Firebase
import os
keyfb=os.environ["KEY"]
chifrifb=os.environ["KEYCF"]
configfb = {
  "apiKey": keyfb,
  "authDomain": chifrifb+".firebaseapp.com",
  "databaseURL": "https://avroraacha.firebaseio.com/",
  "storageBucket": "avroraacha.appspot.com" 
}

firebase = Firebase (configfb)
db = firebase.database ()

def db_setchance (chance, guild_id):
    data = {"shans": chance}
    db.child ("timeout").child (guild_id).set (data)

def db_getchance (guild_id):
    all_users = db.child ("timeout").get ()

    for user in all_users.each ():
        kkey = user.key ()
        
        if str (kkey) == str (guild_id):    
            a = user.val ()
            return a ["shans"]
def onjn(guild2):
    data = {
        "shans": "20",
        "lang":"eng"
    }
    db.child("timeout").child(guild2.id).set(data)
    
def dbmcget():
    all_acc1 = db.child("accs").get()
    accs2=[]
    for user in all_acc1.each():
        accs2.append(user.key()+":"+user.val())
    rnd=random.choice(accs2)
    accitog=rnd.split(":")
    return [str(accitog[0]), str(accitog[1])]

def add_minecraft(email, passw):
  db.child("accs").child (email).set (passw)
  
"""
def adm_give(id):
  #give id of admin:
  adms = db.child("adms").get()
  for iamadmin in adms.each ():
      kkeyadm = iamadmin.key ()
        
      if str (kkeyadm) == str (id):    
          return True
      else:
          return False"""
         
''' # Смотри *

def db_setchance (a, b):
    pass

def db_getchance (a):
    return '20'

def onjn (a):
    pass

def dbmcget ():
    return ['ppap@ppap.ppap', 'ppap???']

def add_minecraft (a):
    pass

#'''# Смотри *
