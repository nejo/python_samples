# -*- coding: utf-8 -*-
import sqlite3
import hashlib # usamos hashlib ya que md5 nos dice q está DEPRECATED
# investigarcomo pasar los warnings a un fichero en vez de que salgan por consola

try:
  conn = sqlite3.connect("mibasededatos")
except:
  print "No se ha podido conectar con la base de datos :S"
  exit()

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, nombre TEXT, password INTEGER)")
conn.commit()


while True:
  print '''
  1. Dar de alta usuario
  2. Dar de baja usuario
  3. Autenticar usuario
  4. Salir
  
  Tell me what to do baby: ''',

  a = raw_input()
  if a == "4":
    # salir
    exit()
  elif a == "1":
    # crear usuario
    user = ""
    while user == "":
      print "Introduce un nombre de usuario: "
      user = raw_input()
    
    password = ""
    while password == "":
      print "Introduce una contraseña: "
      password = raw_input()
    
    password = hashlib.md5(password).hexdigest()
    cur.execute("SELECT id FROM user WHERE nombre = '"+user+"' AND password = '"+password+"' LIMIT 1")
    
    res = cur.fetchone()
    
    if res != None:
      print "Sorry bro, este usuario ya existe :("
      print "Try again later"
    else:
      cur.execute("INSERT INTO user (nombre, password) VALUES ('"+user+"', '"+password+"')")
      conn.commit()
    
  elif a == "2":
    # eliminar usuario
    user = ""
    while user == "":
      print "Dime el nombre del usuario a eliminar: "
      user = raw_input()
    
    cur.execute("DELETE FROM user WHERE nombre = '"+user)
    conn.commit()
    
  elif a == "3":
    # autenticarse
    user = ""
    while user == "":
      print "Introduce un nombre de usuario: "
      user = raw_input()
    
    password = ""
    while password == "":
      print "Introduce una contraseña: "
      password = raw_input()
    
    password = hashlib.md5(password).hexdigest()
    cur.execute("SELECT id FROM user WHERE nombre = '"+user+"' AND password = '"+password+"' LIMIT 1")
    
    try:
      res = cur.fetchone()
      print "¡¡¡ Te has autenticado correctamente ;). Tu usuario es el número "+str(res[0])+" !!!"
    except:
      print "Este usuario no existe"
    
  print ""