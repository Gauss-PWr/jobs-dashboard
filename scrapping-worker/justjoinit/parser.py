from AdvancedHTMLParser import IndexedAdvancedHTMLParser,AdvancedTag

'''
Tu narazie nic nie ma. Trzeba przeiterować HTMLe ofert i powyciągać z nich inforamcje.
'''

parser = IndexedAdvancedHTMLParser()
parser.parseFile("./offers/test.html")
# for i in parser.getElementsByTagName("html")[0].childNodes:
#     i: AdvancedTag # dla podpowiedzi w ide
#     print(i.getAttribute("data-index"))