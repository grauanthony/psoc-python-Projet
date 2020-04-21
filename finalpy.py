import time
import serial
import mysql.connector

# Connection à la BDD
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "ecluse",
  database = "nom-BDD (à fixer) "
)

# lecture données Psoc# Boucle infinie:
  while 1:
    serial_line = ser.readline()
    print(serial_line)

    # stockage données Psoc
    mycursor = mydb.cursor()
    sql = "INSERT INTO table (name, address) VALUES (%s, %s)"#
    A completer
    val = ("XXX", "XXXX")
    mycursor.execute(sql, val)

    mydb.commit()

    time.sleep(1)

    # ferme port
    ser.close()

if (serial_line == 0):

    #stockage en bdd# et changement depuis la dernière lecture
    mycursor = mydb.cursor()
    sql = "INSERT INTO table (name, address) VALUES (%s, %s)"
    val = ("XXX", "XXXX")
    mycursor.execute(sql, val)

    mydb.commit()

# alerte site(donnée modifiée, fail)
if (test - en - cours == 1)

  if (durée < durée min et changement depuis la dernière lecture)

    # stockage en bdd# et changement depuis la dernière lecture
    mycursor = mydb.cursor()
    sql = "INSERT INTO table (name, address) VALUES (%s, %s)"
    val = ("XXX", "XXXX")
    mycursor.execute(sql, val)

    mydb.commit()





                                                                    # alerte site(donnée modifiée, fail)

elif (durée > durée max et pas de changement depuis la dernière lecture)             # stockage en bdd
                                                                                        # alerte site(donnée modifiée, fail)



else                                        # stockage en bdd
                                            # comparaison avec scénario
                                            # alerte site(donnée modifiée, pass / fail)
                                            # changement trame attendue # changement durée min
                                            # changement durée max
                                            # raz timer


etape = etape + 1

if(etape > etapemax)                    # alerte site(donnée modifiée, pass)


test - en - cours = 0                   # lecture fichier ordres Web


if(ordre):                              # raz fichier ordres
                                        # construction code à transmettre au Psoc
                                        # transmission code
                                        # définition durée min
                                        # définition durée max
                                        # définition trame attendue
                                        # définition etapemax

starttime=time.time()                   # lancement timer de 4s
while True:
    print ("tick")
    time.sleep(4.0)


                            # etape = 1
test - en - cours = 1

# lancement timer de 4s
import time
starttime=time.time()
while True:
  print ("tick")
  time.sleep(4.0)





#Partie envoie des données
#ouvre le fichier data.txt, ou afficher les données contenus
filename = "data.txt"
for line in open(filename, 'r'):
    print(line)


# on envoie la variable "line" par le port serie USB0 du raspberry au psoc
ser = serial.Serial("/dev/ttyUSB0", 9600)  # open serial port
ser.write(line.encode())
s = ser.read(3)
print(s)
