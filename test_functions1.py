# -*- coding: utf-8 -*-
def saludar_es():
  print "Hola"
def saludar_en():
  print "Hi"
def saludar_fr():
  print "Salut"

def saludar(lang):
  lang_func = {"es": saludar_es, "en": saludar_en, "fr": saludar_fr}
  return lang_func[lang]

f = saludar("es")()
