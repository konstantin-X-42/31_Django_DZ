from rest_framework import viewsets, generics
# 31 импортируем стандартный класс проверки авторизации
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
# 31 импортируем кастомный класс разрешений для проверки принадлежности к группе модераторов
from users.permissions import IsModer


class CourseViewSet(viewsets.ModelViewSet):
    # 30.1 указываем сериализатор для преобразования данных модели курса
    serializer_class = CourseSerializer
    # 30.1 определяем базовый набор объектов курсов из базы данных
    queryset = Course.objects.all()

    def get_permissions(self):
        # 31 запрещаем модераторам создание и удаление курсов через логическое отрицание ~IsModer
        if self.action in ('create', 'destroy'):
            self.permission_classes = [IsAuthenticated, ~IsModer]
        # 31 разрешаем просмотр и редактирование курсов авторизованным пользователям (включая модераторов)
        elif self.action in ('list', 'retrieve', 'update', 'partial_update'):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    # 30.1 указываем сериализатор для валидации и создания нового урока
    serializer_class = LessonSerializer
    # 31 запрещаем модераторам создавать новые уроки
    permission_classes = [IsAuthenticated, ~IsModer]


class LessonListAPIView(generics.ListAPIView):
    # 30.1 указываем сериализатор для отображения списка уроков
    serializer_class = LessonSerializer
    # 30.1 определяем набор всех объектов уроков для вывода списком
    queryset = Lesson.objects.all()
    # 31 разрешаем просмотр списка уроков авторизованным пользователям и модераторам
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    # 30.1 указываем сериализатор для детального просмотра одного урока
    serializer_class = LessonSerializer
    # 30.1 определяем набор объектов уроков для поиска по идентификатору
    queryset = Lesson.objects.all()
    # 31 разрешаем просмотр одного урока авторизованным пользователям и модераторам
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    # 30.1 указываем сериализатор для полного или частичного обновления урока
    serializer_class = LessonSerializer
    # 30.1 определяем набор объектов уроков для поиска редактируемой записи
    queryset = Lesson.objects.all()
    # 31 разрешаем редактирование уроков авторизованным пользователям и модераторам
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    # 30.1 определяем набор объектов уроков для поиска и удаления записи
    queryset = Lesson.objects.all()
    # 31 запрещаем модераторам удалять уроки
    permission_classes = [IsAuthenticated, ~IsModer]




#------30.2------


# from rest_framework import viewsets, generics
# from materials.models import Course, Lesson
# from materials.serializers import CourseSerializer, LessonSerializer
#
#
# class CourseViewSet(viewsets.ModelViewSet):
#     # 30.1 указываем сериализатор для преобразования данных модели курса
#     serializer_class = CourseSerializer
#     # 30.1 определяем базовый набор объектов курсов из базы данных
#     queryset = Course.objects.all()
#
#
# class LessonCreateAPIView(generics.CreateAPIView):
#     # 30.1 указываем сериализатор для валидации и создания нового урока
#     serializer_class = LessonSerializer
#
#
# class LessonListAPIView(generics.ListAPIView):
#     # 30.1 указываем сериализатор для отображения списка уроков
#     serializer_class = LessonSerializer
#     # 30.1 определяем набор всех объектов уроков для вывода списком
#     queryset = Lesson.objects.all()
#
#
# class LessonRetrieveAPIView(generics.RetrieveAPIView):
#     # 30.1 указываем сериализатор для детального просмотра одного урока
#     serializer_class = LessonSerializer
#     # 30.1 определяем набор объектов уроков для поиска по идентификатору
#     queryset = Lesson.objects.all()
#
#
# class LessonUpdateAPIView(generics.UpdateAPIView):
#     # 30.1 указываем сериализатор для полного или частичного обновления урока
#     serializer_class = LessonSerializer
#     # 30.1 определяем набор объектов уроков для поиска редактируемой записи
#     queryset = Lesson.objects.all()
#
#
# class LessonDestroyAPIView(generics.DestroyAPIView):
#     # 30.1 определяем набор объектов уроков для поиска и удаления записи
#     queryset = Lesson.objects.all()
