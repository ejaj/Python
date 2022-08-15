from urllib.request import urlopen
from xml.etree.ElementTree import parse, iterparse, Element, tostring
from collections import Counter

# u = urlopen('http://planet.python.org/rss20.xml')
# doc = parse(u)
#
# for item in doc.iterfind('channel/item'):
#     title = item.findtext('title')
#     date = item.findtext('puDate')
#     link = item.findtext('link')
#
#     print(title)
#     print(date)
#     print(link)
#     print()


# # Parsing Huge XML Files Incrementally
# def parse_and_remove(filename, path):
#     path_parts = path.split('/')
#     doc = iterparse(filename, ('start', 'end'))
#     # Skip the root element
#     next(doc)
#     tag_stack = []
#     elem_stack = []
#     for event, elem in doc:
#         if event == 'start':
#             tag_stack.append(elem.tag)
#             elem_stack.append(elem)
#         elif event == 'end':
#             if tag_stack == path_parts:
#                 yield elem
#                 elem_stack[-2].remove(elem)
#             try:
#                 tag_stack.pop()
#                 elem_stack.pop()
#             except IndexError:
#                 pass

# potholes_by_zip = Counter()
#
# doc = parse('../data/potholes.xml')
#
# for pothole in doc.iterfind('row/row'):
#     potholes_by_zip[pothole.findtext('zip')] += 1
# for zipcode, num in potholes_by_zip.most_common():
#     print(zipcode, num)

# data = iterparse('../data/potholes.xml', ('start', 'end'))
# print(data)

# def dict_to_xml(tag, d):
#     elem = Element(tag)
#     for key, val in d.items():
#         child = Element(key)
#         child.text = str(val)
#         elem.append(child)
#     return elem
#
#
# s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
# e = dict_to_xml('stock', s)
# print(e)
# print(tostring(e))
# e.set('_id', '1234')
# print(tostring(e))

# def dict_to_xml_str(tag, d):
#     '''
#     Turn a simple dict of key/value pairs into XML
#     '''
#     parts = ['<{}>'.format(tag)]
#     for key, val in d.items():
#         parts.append('<{0}>{1}</{0}>'.format(key, val))
#     parts.append('</{}>'.format(tag))
#     return ''.join(parts)
#
#
# d = {'name': '<spam>'}
# print(dict_to_xml_str('item', d))
# e = dict_to_xml_str('item', d)
# print(tostring(e))
doc = parse('../data/pred.xml')
root = doc.getroot()
print(root)
root.remove(root.find('sri'))
root.remove(root.find('cr'))
print(root.getchildren().index(root.find('nm')))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)
doc.write('newpred.xml', xml_declaration=True)
