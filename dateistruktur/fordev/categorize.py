user=str(input("Bitte Nummer eingeben: "))
categorie=user[0:2]
schooltype=user[2:3]
if schooltype=="1":
	schooltype="Grundschule"
elif schooltype=="2":
	schooltype="Mittelschule"
elif schooltype=="3":
	schooltype="Gymnasium"
id=user[3:10]
print "Kategorie:", categorie
print "Schultyp:", schooltype 
print "Identifizierungsnummer:",id
