from django.test import TestCase
from datetime import date
from .models import Person

class PersonModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.person = Person.objects.create(
            ClientOwner="3434454556",
            FirstName="Volodymyr",
            LastName="Kolomiiets",
            Patronym="Mikolevich",
            OtherInfo="is and will be happy",
            BirthDate="1988-10-26",
            ClientContact="380954350854",
        )
    
    def test_fields(self):
        self.assertIsInstance(self.person.ClientOwner, str)
        self.assertIsInstance(self.person.FirstName, str)
        self.assertIsInstance(self.person.LastName, str)
        self.assertIsInstance(self.person.Patronym, str)
        self.assertIsInstance(self.person.OtherInfo, str)
        self.assertEqual(self.person.ClientContact, "380954350854")
    
    def test_timestamps(self):
        print(type(self.person.BirthDate), '--------------')
        self.assertIsInstance(self.person.BirthDate, str)
        