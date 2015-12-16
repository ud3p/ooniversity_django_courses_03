# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.test import Client


def insert_course():
    new_course = Course.objects.create(
                            name='Python/Django',
                            short_description='Практический курс по изучению современного языка программирования Python и фреимворка Django.')
    return new_course

# Create your tests here.
class CoursesListTest(TestCase):
    def test_new_course(self):
        insert_course()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_page_c(self):
        client = Client()
        insert_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PYTHON/DJANGO')

class CoursesDetailTest(TestCase):
    def test_detail_page_c(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        insert_course()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python/Django')

    def test_link_student(self):
        client = Client()
        response = client.get('/students/', {'course_id': 1})
        self.assertEqual(response.status_code, 200)
