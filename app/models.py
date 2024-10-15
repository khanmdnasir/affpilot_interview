from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Book)
def generate_log_signals(sender, instance, created, **kwargs):
    BookLog.objects.create(
        title=instance.title,
        authors=instance.authors,
        action="create" if created else "delete",
    )


action_type_choices = (('create', 'Create'), ('delete', 'Delete'))
class BookLog(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    action = models.CharField(max_length=100, choices=action_type_choices)