# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models import Student
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client


def insert_course():
    new_user_1 = User.objects.create(
                            username='user_1')

    new_user_2 = User.objects.create(
                            username='user_2')

    new_user_3 = User.objects.create(
                            username='user_3')

    new_course_1 = Course.objects.create(
                            name='Python/Django',
                            short_description='Практический курс',
                            description='Практический курс по изучению современного языка программирования Python и фреимворка Django.')

    new_course_2 = Course.objects.create(
                            name='JavaScript',
                            short_description='Базовый JavaScript',
                            description='Базовый JavaScript, клиентский JavaScript, работа с HTML5, написание плагинов jQuery, использование шаблонов, введение в Backbone JS.')

    new_course_3 = Course.objects.create(
                            name='Web-дизайн',
                            short_description='Освоите Photoshop и Illustrator.',
                            description='Освоите на профессиональному уровне работу с такими программами, как Photoshop и Illustrator.')

    new_coach_1 = Coach.objects.create(
                            user=new_user_1,
	                        date_of_birth='1985-11-26',
	                        gender='M',
	                        phone='(050) 847-73-37',
	                        address='ул. Садовая, дом 75, квартира 156',
	                        skype='user_1',
	                        description='Руководитель группы разработки веб-проектов')


  

# Create your tests here.
class CoursesListTest(TestCase):
    def test_new_course(self):
        insert_course()
        self.assertEqual(Course.objects.all().count(), 3)

    def test_page_c(self):
        client = Client()
        insert_course()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PYTHON/DJANGO')
        self.assertTemplateUsed(response, 'index.html')

class CoursesDetailTest(TestCase):
    def test_detail_page_c(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        insert_course()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Практический курс')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_link_student(self):
        client = Client()
        response = client.get('/students/', {'course_id': 1})
        self.assertEqual(response.status_code, 200)

    def test_coach(self):
        client = Client()
        insert_course()
        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
