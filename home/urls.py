from django.urls import path
from home import views
from home.views import TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView, UserTransactionListView

urlpatterns = [
    path('about/',views.about, name="home-about" ),
    path('',TransactionListView.as_view(), name="home-home" ),
    path('user/<str:username>', UserTransactionListView.as_view(), name='user-transactions'),
    path('transaction/<int:pk>/',TransactionDetailView.as_view(), name="transaction-detail" ),
    path('transaction/new/',TransactionCreateView.as_view(), name="transaction-create" ),
    path('transaction/<int:pk>/update/',TransactionUpdateView.as_view(), name="transaction-update" ),
    path('transaction/<int:pk>/delete/',TransactionDeleteView.as_view(), name="transaction-delete" ),

]
