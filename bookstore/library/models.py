from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country_of_origin = models.CharField(max_length=100)
    short_description = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    date_of_publication = models.DateField()
    number_of_sales = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    number_of_upvotes = models.IntegerField(default=0)


class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sales')
    year = models.IntegerField()
    sale = models.IntegerField()

