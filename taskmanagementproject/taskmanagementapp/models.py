from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class TaskManagementItem(models.Model):
    class TaskStatus(models.TextChoices):
        UNFINISHED = 'Unfinished'
        FINISHED = 'Finished'
        INPROGRESS = 'In Progress'
        ATRIST = 'At Rist'
        PLANNED = 'Planned'
        OVERDUE = 'Overdue'

    content = models.CharField(max_length=128)
    status = models.CharField(
        max_length = 128,
        choices = TaskStatus.choices,
        default = TaskStatus.UNFINISHED,
    )
    created_at = models.DateTimeField(auto_now_add = True)

    def set_content(self, new_content):
        self.content = new_content

    def get_content(self):
        return self.content

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, new_craeted_at):
        self.created_at = new_craeted_at