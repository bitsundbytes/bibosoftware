#import der module
import gettext
import os
import sqlite3
#installation der uebersetzung
lang = os.environ.get("LANGUAGE", "de_DE")
trans = gettext.translation("install", "../locale", [lang])
trans.install()
#begruessung
print _("Hello, I am the installscript for the Bibosoftware of the Bits und Bytes Computer-AG of the Bischoefliches Maria-Montessori-Schulzentrums Leipzig.")
print _("Should you find an Issue please don't keep it report it on https://github.com/bitsundbytes/bibosoftware/issues. Thanks.")
print _("First I have to ask you a few questions. If you don't know what they mean press enter.")
#oeffnen der datenbank
connection = sqlite3.connect("../db/daten.sqlite")
#initialisiere cursor
cursor=connection.cursor()
#erstellen der leeren tabellen
print _("Creating Table Media")
cursor.execute("""CREATE TABLE IF NOT EXISTS media (
    ID INTEGER PRIMARY KEY, signatur INTEGER,
    systematik VARCHAR, autor VARCHAR, mediatypID INTEGER)""")
print _("Creating Table User")