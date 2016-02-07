from unittest import TestCase
from xml.etree.ElementTree import Element

from mock import patch

from odatoo.field import Field


class TestField(TestCase):

    def setUp(self):
        self.record = Element('test_record')

    @patch('odatoo.field.Field._create')
    def test_init_calls_create(self, mocked_create):
        mocked_create.return_value = None
        Field(self.record, {'name': 'test'})
        Field._create.assert_called_with(self.record, {'name': 'test'})

    def test_creating_Field_when_value_is_in_attributes(self):
        field = Field(self.record, {'value': 'test_value'})
        self.assertEqual(field.value, 'test_value')

    def test_creating_Field_when_no_value_is_in_attributes(self):
        field = Field(self.record, {})
        self.assertEqual(field.value, None)

    def test_creating_Field_when_value_is_not_str_coverts_to_str(self):
        field = Field(self.record, {'value': 1})
        self.assertEqual(field.value, '1')
