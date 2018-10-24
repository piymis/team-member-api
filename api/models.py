from django.db import models

role_map = (
    (0, "Admin"),
    (1, "Regular"),
)

class TeamMember(models.Model):
    """
    Model representing a team member.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.IntegerField(default=1, choices=role_map)


