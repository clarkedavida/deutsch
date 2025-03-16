# 
# testYourGerman.py                                                               
# 
# D. Clarke
#
 
from common import Woerterbuch

woerter = Woerterbuch()

woerter.load('GRANDDICTIONARY.json')

for wort in woerter:
    print(wort)
    exit()
