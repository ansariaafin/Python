from django.db import models

# Create your models here.
class str_method(models.Model):
    class Meta:
        abstract = True


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mob_num = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.mob_num}"
    #  {self.last_name} ( ID : {self.employee_id})

class e_profile(models.Model):
    designation =models.CharField(max_length=150)
    salary = models.BigIntegerField()
    Employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.designation}. (Salary: {self.salary})"



# sheetal
# class Contact(models.Model):
#     phone = models.CharField(max_length=50, unique=True)
#     address = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.phone}"

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.first_name}, {self.last_name}"



# One to Many models
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Many to Many Relationship Model  
class College(models.model):
    name = models.CharField(max_length = 100)
    departments = models.CharField(max_length = 100)
