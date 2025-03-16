# 
# common.py                                                               
# 
# D. Clarke
# 

from latqcdtools.interfaces.interfaces import readJSON
import latqcdtools.base.logger as logger

ARTIKELN = ['der','die','das']


class Wort():
    wort    =None
    englisch=None
    def __init__(self,wort,englisch):
        self.wort=wort
        self.englisch=englisch


class Nomen(Wort):
    artikel =None
    plural  =None

    def __init__(self,wort,artikel,englisch,plural=None):
 
        self.wort=wort
        self.artikel=artikel
        self.englisch=englisch
        if not artikel in ARTIKELN:
            logger.TBRaise(self.artikel,'ist kein Artikel.')

        # Rules for plurals that work 100% of the time
        if plural is None:

            if artikel=='die' and wort.endswith('e'):
                self.plural=wort+'n'
            elif artikel=='die' and wort.endswith('el'):
                self.plural=wort+'n'
            elif artikel=='die' and wort.endswith('ei'):
                self.plural=wort+'n'
            elif artikel=='die' and wort.endswith('in'):
                self.plural=wort+'nen'

            elif artikel=='der' and wort.endswith('ant'):
                self.plural=wort+'en'
            elif artikel=='der' and wort.endswith('ast'):
                self.plural=wort+'en'
            elif artikel=='der' and wort.endswith('e'):
                self.plural=wort+'n'
            elif artikel=='der' and wort.endswith('el'):
                self.plural=wort
            elif artikel=='der' and wort.endswith('en'):
                self.plural=wort
            elif artikel=='der' and wort.endswith('er'):
                self.plural=wort
            elif artikel=='der' and wort.endswith('ist'):
                self.plural=wort+'en'
            elif artikel=='der' and wort.endswith('opf'):
                self.plural=wort[:-3]+'öpfe'
            elif artikel=='der' and wort.endswith('oph'):
                self.plural=wort+'en'

            # Inherited from words
            elif wort.endswith('fett'):
                self.plural=wort+'e'
            elif wort.endswith('fisch'):
                self.plural=wort+'e'
            elif wort.endswith('fleisch'):
                self.plural=wort+'e'
            elif wort.endswith('form'):
                self.plural=wort+'en'
            elif wort.endswith('frucht'):
                self.plural=wort[:-4]+'üchte'
            elif wort.endswith('gerät'):
                self.plural=wort+'e'
            elif wort.endswith('holz'):
                self.plural=wort[:-4]+'hölzer'
            elif wort.endswith('kohl'):
                self.plural=wort+'e'
            elif wort.endswith('nuss'):
                self.plural=wort[:-4]+'nüsse'
            elif wort.endswith('papier'):
                self.plural=wort+'e'
            elif wort.endswith('schrank'):
                self.plural=wort[:-7]+'schränke'

            # Endings with unambiguous gender 
            elif wort.endswith('chen'):
                self.plural=wort
            elif wort.endswith('heit'):
                self.plural=wort+'en'
            elif wort.endswith('keit'):
                self.plural=wort+'en'
            elif wort.endswith('lein'):
                self.plural=wort
            elif wort.endswith('ling'):
                self.plural=wort+'e'
            elif wort.endswith('tät'):
                self.plural=wort+'en'
            elif wort.endswith('ung'):
                self.plural=wort+'en'

            # Endings that pluralize the same way regardless of gender
            elif wort.endswith('nis'):
                self.plural=wort+'se'

        else:
            self.plural=plural

    def __str__(self):
        return f'{self.artikel} {self.wort} : the {self.englisch}'


class Woerterbuch(list):

    def dump(self,fname='Woerterbuch.json'):
        outfile = open(fname,'w')
        outfile.write('{\n')
        for i,wort in enumerate(self):
            if type(wort)==Nomen:
                outfile.write('"'+wort.wort+'": {\n')
                outfile.write('  "wortart": "Nomen",\n')
                outfile.write('  "artikel": "'+wort.artikel+'",\n')
                outfile.write('  "plural": "'+str(wort.plural)+'",\n')
                outfile.write('  "uebersetzung": "'+wort.englisch+'"\n')
                if i==len(self)-1:
                    outfile.write('  }\n')
                else:
                    outfile.write('  },\n')
        outfile.write('}')
        outfile.close()

    def empty(self):
        self = []

    def load(self,fname='Woerterbuch.json'):
        self.empty()
        wb = readJSON(fname)
        for key in wb:
            wort = wb[key]
            if wort['wortart']=='Nomen':
                self.append(Nomen(key,wort['artikel'],wort['uebersetzung']))