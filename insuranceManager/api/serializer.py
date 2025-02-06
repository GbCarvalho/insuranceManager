from rest_framework import serializers
from .models import Policy

class PolicySerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name')
    policy_id = serializers.UUIDField(source='id', read_only=True)
    policy_type = serializers.CharField(source='type')
    expiry_date = serializers.DateTimeField(format='%Y-%m-%d')
    
    class Meta:
        model = Policy
        fields = ['policy_id', 'customer_name', 'policy_type', 'expiry_date']
