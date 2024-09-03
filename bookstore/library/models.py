from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    date_of_birth = models.DateField()
    country_of_origin = models.CharField(max_length=100)
    short_description = models.TextField()

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='books/', blank=True, null=True)
    summary = models.TextField()
    date_of_publication = models.DateField()
    number_of_sales = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    number_of_upvotes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})


class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sales')
    year = models.IntegerField()
    sale = models.IntegerField()

    def get_absolute_url(self):
        return reverse('sale-detail', kwargs={'pk': self.pk})

