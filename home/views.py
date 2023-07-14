from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from home.models import Transaction
from django.contrib.auth.models import User


# Create your views here.

def about( request ):
    context = {
        "title": "About",
    }
    return render( request, "home/about.html",context )

class TransactionListView( ListView ):
    model = Transaction
    template_name = "home/transaction_list.html"
    context_object_name="objects"
    ordering =['-datetime']

class UserTransactionListView(ListView):
    model = Transaction
    template_name = 'home/user_transactions.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Transaction.objects.filter(username=user).order_by('-datetime')


class TransactionDetailView( DetailView ):
    model = Transaction

class TransactionCreateView( LoginRequiredMixin, CreateView ):
    model = Transaction
    fields = ['subject', 'transaction_type', 'datetime', 'cost', 'remarks']

    def form_valid( self, form ):
        form.instance.username = self.request.user
        return super().form_valid( form )

class TransactionUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Transaction
    fields = ['subject', 'transaction_type', 'datetime', 'cost', 'remarks']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.username:
            return True
        return False

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url = '/'

    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.username:
            return True
        return False