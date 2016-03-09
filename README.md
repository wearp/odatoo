# odatoo
_Generate Odoo XML data files, effortlessly, in python._


For times when you need to create _a lot_ of data (i.e. for demonstration or test purposes), and you can't be bothered.

## Install

```
pip install odatoo
```

## Create a document
```python
>>> from odatoo.document import Document
>>> doc = Document()
```

## Create a record and fields
```python
>>> record = doc.record(model="openacademy.course", id="course0")
>>> # add a fields to the record
>>> record.field(name="name", value="Course 0")
>>> record.field(name="description", value="Course 0's description")
>>> # add another record
>>> another_record = doc.record(model="openacademy.course", id="course1")
>>> ...
```

## Write document to a file
```python
>>> doc.write("demo.xml")
```

## Output XML data file
```xml
<?xml version="1.0" ?>
<openerp>
  <data noupdate="1">
    <record id="course0" model="openacademy.course">
      <field name="name">Course 0</field>
      <field name="description">Course 0's description</field>
    </record>
    <record id="course1" model="openacademy.course">
      ...
    </record>
  </data>
</openerp>
```
