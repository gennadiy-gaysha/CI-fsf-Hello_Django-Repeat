from django.db import models


# Create your models here.


class Item(models.Model):
    # The null equals false attribute here prevents items from being created without a name
    # programmatically
    # and blank equals false will make the field required on forms.
    # This way we're certain that a todo item can't be created without a name
    # whether it's done in Python code. Or by a user in a web form or even an administrator in the
    # admin panel.
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)

    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=priority_choices,
        default='medium',  # Default value if not specified
    )

    def __str__(self):
        return f'{self.name} - {self.status}'
