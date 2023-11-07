from django.test import TestCase
from django.contrib.auth.models import User
from contactform.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Name Surname",
            email="example@gmail.com",
            subject="Feedback",
            message=" I am very happy"
        )

    def test_contact_model(self):
        contact_from_db = Contact.objects.get(id=self.contact.id)
        self.assertEqual(contact_from_db.name, "Name Surname")
        self.assertEqual(contact_from_db.email, "example@gmail.com")
        self.assertEqual(contact_from_db.subject, "Feedback")
        self.assertEqual(contact_from_db.message, " I am very happy")

    def tearDown(self):
        self.contact.delete()