from django.db import models

# Create your models here.

class Genre(models.Model):
    """ Model representing a book genre. """
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction')

    def __str__(self):
        """ String for representing the Model object. """
        return self.name

from django.urls import reverse

class Book(models.Mobile):
    """ Model representing a book (but not a specific book). """

    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """ String for the representing the Model object. """
        return self.title

    def get_absolute_url(self):
        """ Returns the URL to access the detail record of this book. """
        return ('book-detail', args=[str(self.id)])
    
