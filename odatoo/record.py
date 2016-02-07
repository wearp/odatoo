from xml.etree.ElementTree import SubElement

from field import Field


class Record(object):

    def __init__(self, data, attributes):
        self._create(data, attributes)

    def _create(self, data, attributes):
        self._element = SubElement(data, 'record', attributes)

    def field(self, attributes):
        return Field(self._element, attributes)

    @property
    def model(self):
        return self._element.attrib['model']

    @model.setter
    def model(self, value):
        self._element.attrib['model'] = value

    @property
    def id(self):
        return self._element.attrib['id']

    @id.setter
    def id(self, value):
        self._element.attrib['id'] = value

    @property
    def context(self):
        return self._element.attrib['context']

    @context.setter
    def context(self, value):
        self._element.attrib['context'] = value
