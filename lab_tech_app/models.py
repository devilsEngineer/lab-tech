from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields

class Test(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.StringField(required=True)
    
class Patient(Document):
    pid = fields.StringField(required=True)
    name = fields.StringField(required=True)
    phone = fields.StringField(required=True)
    dob = fields.DateField(required=True)
    tests = fields.ListField(fields.EmbeddedDocumentField(Test))

