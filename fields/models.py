from django.db import models
from django.conf import settings


class NumericField(models.Model):
    big_integer_field = models.BigIntegerField()
    small_integer_field = models.SmallIntegerField()
    decimal_field = models.DecimalField(max_digits=4, decimal_places=2)
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    binary_field = models.BinaryField(max_length=255)


class StringField(models.Model):
    char_field = models.CharField(max_length=255)
    email_field = models.EmailField(max_length=255)
    url_field = models.URLField(max_length=255)
    text_field = models.TextField()


class DateTimeField(models.Model):
    time_field = models.TimeField(auto_now=True)
    date_field = models.DateField(auto_now=True)
    date_time_field = models.DateTimeField(auto_now=True)
    duration_field = models.DurationField()


# Can't have more than one auto-generated field
# class AutoField(models.Model):
    # auto_field = models.AutoField()
    # big_auto_field = models.BigAutoField()
    # small_auto_field = models.SmallAutoField()


class FileField(models.Model):
    file_field = models.FileField(upload_to='files')
    file_path_field = models.FilePathField(path=settings.MEDIA_ROOT.joinpath('files'), null=True, blank=True)
    image_field = models.ImageField(upload_to='images')


class BooleanField(models.Model):
    boolean_field = models.BooleanField()
    null_boolean_field = models.NullBooleanField()


class RelationshipField(models.Model):
    pass


class MiscellaneousField(models.Model):
    generic_ip_address_field = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    json_field = models.JSONField()
    slug_field = models.SlugField()
    uuid_field = models.UUIDField()
