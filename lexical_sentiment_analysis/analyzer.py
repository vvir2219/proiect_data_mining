from enum import Enum

class Languages(Enum):
  English = 'AFINN-en-165.txt'
  Danish = 'AFINN-da-32.txt',
  Finnish = 'AFINN-fi-165.txt',
  French = 'AFINN-fr-165.txt',
  Polish = 'AFINN-pl-165.txt',
  Swedish = 'AFINN-sv-165.txt',
  Turkish = 'AFINN-tr-165.txt',



def analyzer(language_file=Languages.English):
  pass
