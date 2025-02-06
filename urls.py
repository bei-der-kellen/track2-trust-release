from django.urls import path
from pages.checked_documents import checked_documents_view

urlpatterns = [
    # ... other URL patterns ...
    path('checked-documents/', checked_documents_view, name='checked_documents'),
] 