from django.contrib import admin
from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 30.1 настраиваем отображение списка курсов в административной панели
    list_display = ('id', 'title')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    # 30.1 настраиваем отображение списка уроков с привязкой к курсу в административной панели
    list_display = ('id', 'title', 'course')
