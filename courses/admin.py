from django.contrib import admin
from courses.models import Course, Lesson

admin.site.register(Course)
admin.site.register(Lesson)
'''
class LessonAdmin(admin.ModelAdmin):
	list_display = ['subject', 'course', 'order']
admin.site.register(Lesson, LessonAdmin)
'''
