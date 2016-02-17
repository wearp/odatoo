from xml.etree.ElementTree import SubElement

from field import Field
from errors import RecordValidationError


class Record(object):

    def __init__(self, data, **kwargs):
        self._validate(**kwargs)
        self._element = SubElement(data, 'record', **kwargs)

    @staticmethod
    def _has_model(**kwargs):
        if 'model' not in kwargs:
            raise RecordValidationError(
                    '**kwargs has no required key "model"')
        return None

    @staticmethod
    def _has_invalid(**kwargs):
        valid = ['model', 'id', 'context', 'forcecreate']
        invalid = set(kwargs.keys()) - set(valid)
        if invalid:
            raise RecordValidationError(
                    '**kwargs has arguments: %s' % invalid)
        return None

    def _validate(self, **kwargs):
        self._has_model(**kwargs)
        self._has_invalid(**kwargs)
        return None

    def field(self, **kwargs):
        return Field(self._element, **kwargs)

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

    @property
    def forcecreate(self):
        return self._element.attrib['forcecreate']

    @forcecreate.setter
    def context(self, value):
        self._element.attrib['forcecreate'] = value
