# файл для работы с созданными моделями
from django.contrib import admin
from .models import Post

admin.site.register(Post) # регистрация модели, чтобы можно было работать с ней в админке



