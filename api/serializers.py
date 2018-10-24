from rest_framework import serializers
from api.models import TeamMember, role_map

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'role')