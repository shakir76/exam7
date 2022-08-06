from django.urls import path

from webapp.views import IndexPollView, PollView, CreatePoll, UpdatePoll, DeletePoll, CreateChoice, UpdateChoice

urlpatterns = [
    path('', IndexPollView.as_view(), name="index_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="view_poll"),
    path('poll/create/', CreatePoll.as_view(), name="create_poll"),
    path('poll/update/<int:pk>/', UpdatePoll.as_view(), name="update_poll"),
    path('poll/delete/<int:pk>/', DeletePoll.as_view(), name="delete_poll"),
    path('poll/<int:pk>/choice/add/', CreateChoice.as_view(), name="add_choice"),
    path('poll/<int:pk>/choice/update', UpdateChoice.as_view(), name="update_choice"),
    path('poll/<int:pk>/choice/delete', DeletePoll.as_view(), name="delete_choice")
]
