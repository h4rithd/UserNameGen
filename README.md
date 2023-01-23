# UserNameGen
This is used to generate list of usernames for some formats

----
```bash

┌──(h4rithd🦠kali)-[~/UserNameGen]
└─$ python usernamegen.py -h              
usage: python3 usernamegen.py -f [usernames.txt] 

-------------------------------------------------------------
---------------- | Username Generator |----------------------
-------------------------------------------------------------
     _____             _____               _____
    |  |  |___ ___ ___|   | |___ _____ ___|   __|___ ___
    |  |  |_ -| -_|  _| | | | .'|     | -_|  |  | -_|   |
    |_____|___|___|_| |_|___|__,|_|_|_|___|_____|___|_|_|   
                                        by h4rith.com
-------------------------------------------------------------

[!] Required arguments:
  -o , --output     Output file name.

[!] Optional arguments:
  -f , --file       File that contain FirstName LastName.
  -u , --username   Single username as "FirstName LastName".

------------------ Script from h4rithd.com ------------------
```
----
```
┌──(h4rithd🦠kali)-[~/UserNameGen]
└─$ cat usernames.txt 
Angoose Garden
James Migel
```
----
```
┌──(h4rithd🦠kali)-[~/UserNameGen]
└─$ python -u "Angoose Garden" -o output.txt
angoosegarden
gardenangoose
angoose.garden
a.garden
angoose.g
g.angoose
garden.a
AngooseGarden
GardenAngoose
Angoose.Garden
A.Garden
Angoose.G
G.Angoose
Garden.A


┌──(h4rithd🦠kali)-[~/UserNameGen]
└─$ python -f usernames.txt -o output.txt
angoosegarden
gardenangoose
angoose.garden
a.garden
angoose.g
g.angoose
garden.a
AngooseGarden
GardenAngoose
Angoose.Garden
A.Garden
Angoose.G
G.Angoose
Garden.A
jamesmigel
migeljames
james.migel
j.migel
james.m
m.james
migel.j
JamesMigel
MigelJames
James.Migel
J.Migel
James.M
M.James
Migel.J

```
