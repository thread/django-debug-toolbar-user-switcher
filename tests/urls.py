import debug_toolbar
from django.urls import include, path

app_name = 'test'

urlpatterns = (
    path('__debug__', include(debug_toolbar.urls)),
)
