#!/bin/env python3

def readconf(filename):
    """
    Cette fonction lit un fichier de configuration
    contenant des lignes de la forme variable=valeur.
    Le caractère # est la marque d'un début de commentaire.
    Il peut y avoir des lignes vides dans ce fichier.

    La fonction reçoit en paramètre le nom du fichier.
    Elle renvoie un dictionnaire dont les clés sont les variables
    définies dans le fichier, et les valeurs leurs valeurs.
    """
    il=1
    table = {}
    with open(filename, "r") as f:
      for line in f:
          line = line.strip()       
          if line=="": continue     
          if line[0]=="#": continue 
          if not "=" in line:       
              raise Exception(f"erreur de syntaxe en ligne {il}: {line}")
          l = line.split('=')
          table[l[0]] = l[1]
          il += 1
    return table

def read_from_keyboard():
    """
    Renvoie des entiers lus au clavier
    """
    l =[]
    print("entrer un entier par ligne, et autre chose pour finir")
    while True:
      c = input()
      try:
          l.append(int(c))
      except ValueError:
          break
    return l

def read_from_cmdline():
    """
    Renvoie des entiers lus sur la ligne de commande
    """
    import sys
    return sys.argv[1:]
        


def read_from_file(filename):
    """
    Renvoie des entiers lus dans le fichier dont le nom est contenu dans filename
    """
    l =[]
    ...
    return l

if __name__=="__main__":
  print("""
  ...
  """) 