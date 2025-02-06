from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
def validate_past_date(value):
    if value <= timezone.now():
        raise ValidationError('Expiry date cannot be in the past')

class Policy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(null=False, max_length=100)
    type = models.CharField(max_length=20, choices=[('home', 'Home'), ('auto', 'Auto'), ('life', 'Life')])
    expiry_date = models.DateTimeField(null=False, validators=[validate_past_date])
    
    def policy_id(self):
        return self.id
    
    def policy_type(self):
        return self.type
    
    def policy_expiry_date(self):
        return self.expiry_date

    class Meta:
        verbose_name_plural = 'Policies'
