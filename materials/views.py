from rest_framework import viewsets, generics
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    # 30.1 указываем сериализатор для преобразования данных модели курса
    serializer_class = CourseSerializer
    # 30.1 определяем базовый набор объектов курсов из базы данных
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    # 30.1 указываем сериализатор для валидации и создания нового урока
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    # 30.1 указываем сериализатор для отображения списка уроков
    serializer_class = LessonSerializer
    # 30.1 определяем набор всех объектов уроков для вывода списком
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    # 30.1 указываем сериализатор для детального просмотра одного урока
    serializer_class = LessonSerializer
    # 30.1 определяем набор объектов уроков для поиска по идентификатору
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    # 30.1 указываем сериализатор для полного или частичного обновления урока
    serializer_class = LessonSerializer
    # 30.1 определяем набор объектов уроков для поиска редактируемой записи
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    # 30.1 определяем набор объектов уроков для поиска и удаления записи
    queryset = Lesson.objects.all()
