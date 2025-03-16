# 
# deutsch.py                                                               
# 
# D. Clarke
# 
# Eine Sammlung von Scripts, um mir zu helfen, Deutsch zu lernen. 
# 
import xmltodict
from common import ARTIKELN, Nomen, Woerterbuch, Wort


def parseCard(back,front):
    pb = back.split()
    pf = front.split()
    # Ist es ein Nomen? Nomen haben immer ein Artikel.
    if len(pb)==2 and pb[0] in ARTIKELN:
        if '(' in back: 
            base   = pb[1].split('(')[0]
            endung = pb[1].split('(')[1][:-1]
            baseu  = pf[1].split('(')[0]
            return Nomen(base,pb[0],baseu,base+endung)
        return Nomen(pb[1],pb[0],pf[1])
    elif len(pb)==4: 
        if '(' in pb[1]: 
            return None 
        return Nomen(pb[1][:-1],pb[0],pf[1]), Nomen(pb[3],pb[2],pf[1])
    elif len(pb)==2: 
        return Wort(pb[0][:-1],pf[0]), Wort(pb[1],pf[0])
    elif len(pb)==1: 
        return Wort(pb[0][:-1],pf[0]) 
    else:
        return None 


with open('AnkiApp/Essen.xml') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


woerter = Woerterbuch()

for card in data_dict['deck']['cards']['card']:
    try:
        back  = card['rich-text'][0]['#text']
        front = card['rich-text'][1]['#text']
    except KeyError:
        continue

    wort = parseCard(back,front)
    if wort is not None:
        if type(wort)==tuple:
            for subwort in wort:
                woerter.append(subwort) 
        else:
            woerter.append(wort) 

woerter.dump()

#print(data_dict['deck']['@name'])