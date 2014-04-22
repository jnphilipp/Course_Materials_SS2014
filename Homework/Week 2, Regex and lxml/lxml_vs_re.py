import re
from lxml import etree
from timeit import timeit
from tkinter.filedialog import askopenfilename
source = askopenfilename(title = 'Where is your xml source file?')
def re_test(xml):
    result = []
    lem_re = re.compile(r'lem="(.*?)"')
    for line in xml:
        lemma = re.search(lem_re, line).group(1)
        result.append(lemma)
    return result
def lxml_test(xml):
    result = []
    for w in xml.xpath('//w'):
        result.append(w.get('lem'))
    return result
with open(source, encoding = 'utf-8') as file:
    xml = etree.fromstring(file.read(), parser = etree.HTMLParser())
with open(source, encoding = 'utf-8') as file:
    lines = file.readlines()
print('Regex takes', str(timeit('re_test(lines)', 'from __main__ import re_test, lines', number = 10)), 'seconds')
print('lxml takes', str(timeit('lxml_test(xml)', 'from __main__ import lxml_test, xml', number = 10)), 'seconds')
re_list = re_test(lines)
lxml_list = lxml_test(xml)
print('re_list == lxml_list?', str(re_list == lxml_list))
