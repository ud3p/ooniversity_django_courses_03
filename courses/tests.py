# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.test import Client
import os.path

def test_insert_course():
    new_student = Course.objects.create(
                            name='Python/Django',
                            short_description='Практический курс по изучению современного языка программирования Python и фреимворка Django.')
    return new_student
# Create your tests here.
class CoursesListTest(TestCase):
    def test_new_course(self):
        test_insert_course()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_page_c(self):
        client = Client()
        test_insert_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PYTHON/DJANGO')

class CoursesDetailTest(TestCase):
    def test_detail_page_c(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        test_insert_course()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python/Django')
