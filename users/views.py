from rest_framework import generics
# 30.2 импортируем бэкенды для фильтрации по полям и сортировки результатов
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# 30.2 импортируем модель Payment и сериализатор PaymentSerializer
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    # 30.1 указываем сериализатор для просмотра и обновления профиля пользователя
    serializer_class = UserSerializer
    # 30.1 передаем набор всех пользователей для возможности редактирования любого профиля по ID
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    # 30.2 указываем сериализатор для отображения списка платежей
    serializer_class = PaymentSerializer
    # 30.2 передаем набор всех платежей из базы данных
    queryset = Payment.objects.all()
    # 30.2 подключаем бэкенды фильтрации и сортировки для данного эндпоинта
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 30.2 разрешаем фильтрацию по оплаченному курсу, уроку и способу оплаты
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    # 30.2 разрешаем сортировку по дате оплаты (по возрастанию и убыванию)
    ordering_fields = ('payment_date',)
