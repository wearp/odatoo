from xml.etree.ElementTree import SubElement


class Field(object):

    def __init__(self, record, attributes):
        self._create(record, attributes)

    def _create(self, record, attributes):
        if 'value' in attributes:
            value = str(attributes['value'])
            del attributes['value']
        else:
            value = None

        self._element = SubElement(record, 'field', attributes)
        self.value = value

    @property
    def value(self):
        return self._element.text

    @value.setter
    def value(self, value):
        self._element.text = value

    @property
    def name(self):
        return self._element.attrib['name']

    @name.setter
    def name(self, value):
        self._element.attrib['name'] = value

    @property
    def ref(self):
        return self._element.attrib['ref']

    @ref.setter
    def ref(self, value):
        self._element.attrib['ref'] = value

    @property
    def eval(self):
        return self._element.attrib['eval']

    @eval.setter
    def eval(self, value):
        self._element.attrib['eval'] = value
