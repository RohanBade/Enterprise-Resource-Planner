from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Transaction(models.Model):
    """
        TRANSACTION_CHOICES - either income or expense
        datetime            - basically for sorting purpose might be useful in pagination
        username            - whose transaction
        subject             - topic where income or expense took place
        transaction_type    - a choice between Transaction_Choice
        cost                - money involved
        remarks             - if any remarks
    """
    TRANSACTION_CHOICES =  [
                            ( 'income', 'Income' ),
                            ( 'expense', 'Expense' ),
                            ]
    datetime = models.DateTimeField( default = timezone.now )
    username = models.ForeignKey( User, on_delete = models.CASCADE )
    subject = models.CharField( max_length = 50 )
    transaction_type = models.CharField( max_length = 10, choices = TRANSACTION_CHOICES )
    cost = models.DecimalField( max_digits = 10, decimal_places = 2 )
    remarks = models.TextField( blank=True )

    def __str__(self):
        transaction_name= self.username.username + "_" + str(self.pk) + self.datetime.strftime("_%m-%d-%Y")+ " (" + self.subject +") "
        return transaction_name
    
    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})