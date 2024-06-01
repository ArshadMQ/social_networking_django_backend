from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('search/', views.UserSearchView.as_view(), name='user-search'),
    path('friend-request/', views.SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/<int:pk>/', views.ManageFriendRequestView.as_view(), name='manage-friend-request'),
    path('friends/', views.ListFriendsView.as_view(), name='list-friends'),
    path('pending-requests/', views.ListPendingRequestsView.as_view(), name='list-pending-requests'),
]
