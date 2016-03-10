from unittest import TestCase
from xml.etree.ElementTree import Element

from mock import patch

from odatoo.record import Record
from odatoo.field import Field
from odatoo.errors import RecordValidationError


class TestRecord(TestCase):

    def setUp(self):
        self.data = Element('test_data')

    @patch('odatoo.record.Record._validate')
    def test_init_calls_create(self, mocked_validate):
        mocked_validate.return_value = None
        Record(self.data, id='test_id')
        Record._validate.assert_called_with(id='test_id')

    def test_field_returns_object_of_type_Field(self):
        record = Record(self.data, model='test')
        field = record.field(name='test_name')
        self.assertEqual(type(field), Field)

    def test_has_model_returns_None_if_kwargs_has_argument_model(self):
        record = Record(self.data, model='test')
        result = record._has_model(model='test_model', id=1)
        self.assertEqual(result, None)

    def test_has_model_raises_error_if_kwargs_has_no_argument_model(self):
        record = Record(self.data, model='test')
        with self.assertRaises(RecordValidationError):
            record._has_model(id=1)

    def test_validate_is_None_if_all_arguments_are_valid(self):
        record = Record(self.data, model='test')
        result = record._validate(model='test_model', id=1)
        self.assertTrue(result is None)

    def test_validate_raises_error_if_invalid_arguments(self):
        record = Record(self.data, model='test')
        with self.assertRaises(RecordValidationError):
            record._validate(model='test_model', invalid_arg=1)

    def test_validate_raises_error_if_no_argument_model(self):
        record = Record(self.data, model='test')
        with self.assertRaises(RecordValidationError):
            record._validate(id=1)
