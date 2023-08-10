from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    content = models.TextField()
    department = models.ForeignKey("general.Department", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.email
    


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
