# 
# statistics.py                                                               
# 
# D. Clarke
# 
# 

from common import Woerterbuch

woerterbuch=Woerterbuch()
woerterbuch.load('GRANDDICTIONARY.json')

print('Number of words:',len(woerterbuch))