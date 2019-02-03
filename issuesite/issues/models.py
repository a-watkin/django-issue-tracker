from datetime import datetime


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StaffUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Issue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=1000)

    submitted_by = models.ForeignKey(
        'auth.User',
        models.SET_NULL,
        blank=True,
        null=True,
    )

    categories = (
        # actual and human readable values
        ('bug', 'bug'),
        ('enhancement', 'enhancement'),
        ('documentation', 'documentation')
    )

    category = models.CharField(
        max_length=100, choices=categories, default='bug')

    statuses = (
        ('open', 'open'),
        ('closed', 'closed')
    )

    status = models.CharField(max_length=100, choices=statuses, default='open')
    solved_by = models.ForeignKey(
        StaffUser, models.SET_NULL, blank=True, null=True)
    solved_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Ensure that if an issue has a solver that it also
        has a status of closed and a solved time.
        """
        if self.solved_by:
            if self.status == 'open':
                self.status = 'closed'
                self.solved_at = datetime.now()

        super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
