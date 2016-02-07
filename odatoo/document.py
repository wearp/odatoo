from xml.etree.ElementTree import Element, SubElement

from record import Record


class Document(object):

    def __init__(self, update='1'):
        self.document = Element('openerp')
        self.data = SubElement(self.document, 'data', {'noupdate': update})

    def record(self, attributes):
        return Record(self.data, attributes)
