from unittest import TestCase

from odatoo.document import Document
from odatoo.record import Record


class TestDocument(TestCase):

    def setUp(self):
        self.document = Document()

    def test_record_returns_object_of_type_Record(self):
        record = self.document.record({})
        self.assertEqual(type(record), Record)
