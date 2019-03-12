from django.db import models
import numpy as np

# Create your models here.
class Company(models.Model):
    """Creates a Company model"""
    name = models.CharField(max_length=200)

    def average_rating(self):
        """Get average rating for a company"""
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name

class Review(models.Model):
    """Creates a Review class"""
    RATING_CHOISES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_published = models.DateField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOISES)
