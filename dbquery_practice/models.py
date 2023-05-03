from django.db import models
from django.core.validators import FileExtensionValidator
import os


def image_content(instance, filename):
    return os.path.join(
        "media", (type(instance).__name__).lower(), str(instance), filename
    )


class Standard(models.Model):
    standard = models.CharField(max_length=256, db_index=True)

    def __str__(self):
        return self.standard

    class Meta:
        db_table = "standard"
        verbose_name = "standard"
        verbose_name_plural = "standards"


class Subject(models.Model):
    standard = models.ForeignKey(
        "Standard", related_name="subject_standard", on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=256, db_index=True)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = "subject"
        verbose_name = "subject"
        verbose_name_plural = "subjects"


class Student(models.Model):
    profile_image = models.ImageField(
        upload_to=image_content,
        verbose_name="student_image",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
    )
    first_name = models.CharField(max_length=256, db_index=True)
    last_name = models.CharField(max_length=256, db_index=True)
    standard = models.ForeignKey(
        "Standard",
        related_name="student_standard",
        on_delete=models.SET_NULL,
        null=True,
    )
    hobby = models.CharField(max_length=256, db_index=True)
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    contect_no = models.CharField(
        max_length=10, unique=True, help_text="enter 10 digit number", db_index=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "student"
        verbose_name = "student"
        verbose_name_plural = "students"
