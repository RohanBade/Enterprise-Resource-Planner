from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from home.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.db.models import Sum


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
    paginate_by =5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = len(User.objects.all())
        context['transactions'] = len(Transaction.objects.all())
        if self.request.user.is_authenticated:
            inflow_transactions = self.request.user.transaction_set.filter(transaction_type='income')
            outflow_transactions = self.request.user.transaction_set.filter(transaction_type='expense')
            total_cost_in = inflow_transactions.aggregate(total_cost=Sum('cost'))['total_cost']
            total_cost_out = outflow_transactions.aggregate(total_cost=Sum('cost'))['total_cost']
            context['cash_inflow'] = total_cost_in
            context['cash_outflow'] = total_cost_out
        return context

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

class CustomLogoutView(LogoutView):
    template_name = "users/logout.html"  

    def get_context_data(self, **kwargs):
        # Add your custom context data here
        context = super().get_context_data(**kwargs)
        context['users'] = len(User.objects.all())
        context['transactions'] = len(Transaction.objects.all())
        return context