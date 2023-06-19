from django.db import models

# Create your \

class BookStoreModel(models.Model):
    CATEGORY=(('Mystery','Mystery'),
              ('Thriller','Thriller'),
              ('Fun','Fun'),)
    id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author_name=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=CATEGORY)
    first_pub=models.DateTimeField(auto_now_add=True) #First date to entry/publication 
    last_pub=models.DateTimeField(auto_now=True) #Last update
    