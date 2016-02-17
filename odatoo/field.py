from xml.etree.ElementTree import SubElement

from errors import FieldValidationError


class Field(object):

    def __init__(self, record, **kwargs):
        self._validate(**kwargs)

        if 'value' in kwargs:
            value = str(kwargs['value'])
            del kwargs['value']
        else:
            value = None

        self._element = SubElement(record, 'field', kwargs)
        self.value = value

    @staticmethod
    def _has_name(**kwargs):
        if 'name' not in kwargs:
            raise FieldValidationError(
                    '**kwargs has no required key "name"')
        return None

    @staticmethod
    def _has_invalid(**kwargs):
        valid = ['value', 'name', 'search', 'ref', 'type', 'eval']
        invalid = set(kwargs.keys()) - set(valid)
        if invalid:
            raise FieldValidationError(
                    '**kwargs has arguments: %s' % invalid)
        return None

    def _validate(self, **kwargs):
        self._has_name(**kwargs)
        self._has_invalid(**kwargs)
        return None

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
