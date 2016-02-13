from unittest import TestCase
from xml.etree.ElementTree import Element

from mock import patch

from odatoo.odatoo.record import Record
from odatoo.odatoo.field import Field


class TestRecord(TestCase):

    def setUp(self):
        self.data = Element('test_data')

    @patch('odatoo.odatoo.record.Record._create')
    def test_init_calls_create(self, mocked_create):
        mocked_create.return_value = None
        Record(self.data, {'id': 'test_id'})
        Record._create.assert_called_with(self.data, {'id': 'test_id'})

    def test_field_returns_object_of_type_Field(self):
        record = Record(self.data, {})
        field = record.field({})
        self.assertEqual(type(field), Field)
