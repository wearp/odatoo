import xml.dom.minidom as xmldom
from xml.etree.ElementTree import Element, SubElement, tostring

from record import Record


class Document(object):

    def __init__(self, update='1'):
        self.document = Element('openerp')
        self.data = SubElement(self.document, 'data', {'noupdate': update})

    def record(self, attributes):
        return Record(self.data, attributes)

    def write(self, file):
        pretty_xml = self._pretty_print()
        with open(file, 'wb') as f:
            f.write(pretty_xml)

    def _pretty_print(self):
        xml_string = tostring(self.document)
        xml_dom = xmldom.parseString(xml_string)
        return xml_dom.toprettyxml()
