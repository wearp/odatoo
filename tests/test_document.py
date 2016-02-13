import os

from xml.etree.ElementTree import ElementTree
from unittest import TestCase


from odatoo.odatoo.document import Document
from odatoo.odatoo.record import Record


class TestDocument(TestCase):

    def setUp(self):
        self.document = Document()

    def tearDown(self):
        try:
            os.remove("test.xml")
        except OSError:
            pass

    def test_record_returns_object_of_type_Record(self):
        record = self.document.record({})
        self.assertEqual(type(record), Record)

    def test_write_creates_file_and_writes_document(self):
        self.document.write("test.xml")
        tree = ElementTree()
        tree.parse("test.xml")
        root = tree.getroot()
        data = root.find("data")
        self.assertEqual(root.tag, "openerp")
        self.assertEqual(data.tag, "data")

    def test_pretty_print_return_string(self):
        xml = ('<?xml version="1.0" ?>\n<openerp>\n'
               '\t<data noupdate="1"/>\n</openerp>\n')
        pretty_string = self.document._pretty_print()
        self.assertEqual(pretty_string, xml)
