#!/usr/bin/env python
secret=1337
guess=0
i=0
while guess!=secret:
	guess=input("Raten sie: ")
	if guess < secret:
		print("Zu klein")
	if guess > secret:
		print("Zu gross")
	i = i + 1
print "Super, Sie haben es in", i, "Versuchen geschaft"
