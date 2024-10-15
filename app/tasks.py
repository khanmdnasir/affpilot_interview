from celery import shared_task
from datetime import timedelta, datetime
from app.models import Book


@shared_task
def set_archived_books():
    date_of_before_10_years_from_today = datetime.today() - timedelta(days=10*365)
    books = Book.objects.filter(published_date__gt=date_of_before_10_years_from_today)
    for book in books:
        book.archived = True
        book.save()
