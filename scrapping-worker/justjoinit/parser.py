from AdvancedHTMLParser import IndexedAdvancedHTMLParser,AdvancedTag

'''
Tu narazie nic nie ma. Trzeba przeiterować elementy HTML ofert i powyciągać z nich inforamcje.
Niektóre informacje takie jak wymagane doświadczenie nie są w nich zawarte, ale można je zdobyć poprzez filtry.
'''

parser = IndexedAdvancedHTMLParser()
parser.parseFile("offers.xml")
for i in parser.getElementsByTagName("offers")[0].childNodes:
    i: AdvancedTag # dla podpowiedzi w ide
    print(i.getAttribute("data-index"))