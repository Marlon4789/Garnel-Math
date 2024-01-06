from django import forms
from .models import Post, Subscription, Feedback

# form suscripción
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        
# form feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']