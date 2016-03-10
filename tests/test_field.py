from unittest import TestCase
from xml.etree.ElementTree import Element

from mock import patch

from odatoo.field import Field
from odatoo.errors import FieldValidationError


class TestField(TestCase):

    def setUp(self):
        self.record = Element('test_record')

    @patch('odatoo.field.Field._validate')
    def test_init_calls_validate(self, mocked_validate):
        mocked_validate.return_value = None
        Field(self.record, name='test')
        Field._validate.assert_called_with(name='test')

    def test_creating_Field_when_value_is_in_attributes(self):
        field = Field(self.record, name='test_name', value='test_value')
        self.assertEqual(field.value, 'test_value')

    def test_creating_Field_when_no_value_is_in_attributes(self):
        field = Field(self.record, name='test_name')
        self.assertEqual(field.value, None)

    def test_creating_Field_when_value_is_not_str_coverts_to_str(self):
        field = Field(self.record, name='test_name', value=1)
        self.assertEqual(field.value, '1')

    def test_has_name_returns_None_if_kwargs_has_argument_name(self):
        field = Field(self.record, name='test')
        result = field._has_name(name='test')
        self.assertEqual(result, None)

    def test_has_name_raises_error_if_kwargs_has_no_argument_name(self):
        field = Field(self.record, name='test')
        with self.assertRaises(FieldValidationError):
            field._has_name(id=1)

    def test_validate_is_None_if_all_arguments_are_valid(self):
        field = Field(self.record, name='test')
        result = field._validate(name='test')
        self.assertTrue(result is None)

    def test_validate_raises_error_if_invalid_arguments(self):
        field = Field(self.record, name='test')
        with self.assertRaises(FieldValidationError):
            field._validate(name='test_model', invalid_arg=1)

    def test_validate_raises_error_if_no_argument_model(self):
        field = Field(self.record, name='test')
        with self.assertRaises(FieldValidationError):
            field._validate(id=1)
