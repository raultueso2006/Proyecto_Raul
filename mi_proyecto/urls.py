from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # 👈 Vistas de autenticación
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 Apps personalizadas
    path('', include('recomendador.urls')),
    path('', include('usuarios.urls')),
    path('', include('catalogo.urls')),

    # 👇 Logout incorporado de Django
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

# 👇 Esto sirve para mostrar las imágenes subidas en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)