from unittest import TestCase

from document import Document
from record import Record


class TestDocument(TestCase):

    def setUp(self):
        self.document = Document()

    def test_record_returns_object_of_type_Record(self):
        record = self.document.record({})
        self.assertEqual(type(record), Record)
