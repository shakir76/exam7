from django.urls import path

from webapp.views import IndexPollView, PollView, CreatePoll, UpdatePoll, DeletePoll

urlpatterns = [
    path('', IndexPollView.as_view(), name="index_poll"),
    path('product/<int:pk>/', PollView.as_view(), name="view_poll"),
    path('product/create/', CreatePoll.as_view(), name="create_poll"),
    path('product/update/<int:pk>/', UpdatePoll.as_view(), name="update_poll"),
    path('product/delete/<int:pk>/', DeletePoll.as_view(), name="delete_poll"),
    path('product/<int:pk>/add/cart', CreatePoll.as_view(), name="create_poll"),
]
