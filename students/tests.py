# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from students.models import Student
from courses.models import Course


def insert_student():
    new_student = Student.objects.create(
                            name='Test',
                            surname='Test',
                            date_of_birth='1987-02-02',
                            email='test@test.com',
                            phone='099-999-99-99',
                            address='ул. Пушкина, д. 57, кв. 137',
                            skype='test',
                            )
    return new_student
# Create your tests here.
class StudentsListTest(TestCase):
    def test_new_student(self):
        insert_student()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_page_s(self):
        client = Client()
        insert_student()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ул. Пушкина, д. 57, кв. 137')

class StudentsDetailTest(TestCase):
    def test_detail_page_s(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
        insert_student()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test@test.com')
