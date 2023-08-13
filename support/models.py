from django.db import models


class Ticket(models.Model):
    email = models.CharField(max_length=200)
    content = models.TextField()
    is_fixed = models.BooleanField(default=False)
    department = models.ForeignKey(
        "support.SupportDepartment", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.email


class SupportDepartment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
