from django.db import models

TASK_STATUSES = [
            ("1", "To do"),
            ("2", "Doing"),
            ("3", "Done")
        ]

# Create your models here.
class Task(models.Model):
    # owner = primary key de algum usuário, n sei fazer ainda.
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=320, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=TASK_STATUSES,
        default=1
    )

    def __str__(self):
        return self.name