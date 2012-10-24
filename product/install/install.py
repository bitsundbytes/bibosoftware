#import der module
import gettext
import os
#installation der uebersetzung
lang = os.environ.get("LANGUAGE", "de_DE")
trans = gettext.translation("install", "../locale", [lang])
trans.install()
#begruessung
print _("Hello, I am the installscript for the Bibosoftware of the Bits und Bytes Computer-AG of the Bischoefliches Maria-Montessori-Schulzentrums Leipzig.")
print _("Should you find an Issue please don't keep it report it on https://github.com/bitsundbytes/bibosoftware/issues. Thanks.")
print _("First I have to ask you a few questions. If you don't know what they mean press enter.")
#print _("")
#print _("")
#print _("")