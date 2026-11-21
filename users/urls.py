from django.urls import path
from users.apps import UsersConfig
# 30.2 импортируем контроллер списка платежей PaymentListAPIView
from users.views import UserUpdateAPIView, PaymentListAPIView

# 30.1 задаем пространство имен приложения users
app_name = UsersConfig.name

urlpatterns = [
    # 30.1 маршрут для получения и редактирования профиля любого пользователя по ID (GET, PUT, PATCH)
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    # 30.2 маршрут для получения списка платежей с поддержкой фильтрации и сортировки (GET)
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
]
