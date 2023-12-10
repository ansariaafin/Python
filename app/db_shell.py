from app.models import *

# exe command - exec(open(r'D:\python\Framework\Django_Projects\first_project\app\db_shell.py').read())

# emp = Employee.objects.all()
# print(emp)
# try:
#     emp1 = Employee.objects.get(id = 5) # get method give single value only
#     print(emp1)
# except Employee.DoesNotExist as msg:
#     print(msg)


# For multiple values we usse filter

# emp1 = Employee.objects.filter(first_name__startswith = "E") 
# print(emp1)

# emp1 = Employee.objects.filter(first_name__in = ["Emp1","Emp3"]) 
# print(emp1)

# try:
#     emp1 = Employee.objects.filter(first_name__startswith = "E").first() 
#     print(emp1)
# except Employee.DoesNotExist as msg:
#     print(msg)


# Create Methods
# way 1
emp = Employee(first_name = "Emp1", last_name = "e1lstnm", email = "e1@gmail.com", mob_num 
= 987654346, )
emp.save()

# emp = Employee.objects.create(first_name = "Emp6", last_name = "e6lstnm", email = "e6@gmail.com", mob_num = 554894346 )

# Update

# emp = Employee.objects.get(id = 4)
# emp.is_deleted = True
# emp.save()

# delete

# Employee.objects.get(id = 4).delete()


# contact_1 = Contact.objects.create(phone= '2345656', address= 'Pune')
# contact_2 = Contact.objects.create(phone= '3445566', address= 'Mumbai')
# contact_3 = Contact.objects.create(phone= '4555566', address= 'Goa')
# contact_4 = Contact.objects.create(phone= '6777566', address= 'Delhi')

# per1 = Person.objects.create(first_name= 'Sai', last_name= 'Patel', contact= contact_1)
# per2 = Person.objects.create(first_name= 'Mac', last_name= 'Joe', contact= contact_2)
# per3 = Person.objects.create(first_name= 'John', last_name= 'Michal', contact= contact_3)
# per4 = Person.objects.create(first_name= 'Gorge', last_name= 'Kiya', contact= contact_4)

# res = Person.objects.filter(last_name__endswith = 'l')
# print(res)

# per = Person.objects.get(id = '2')
# print(per)

# con =Contact.objects.filter(phone = '2345656')
# print(con)

# c = Contact.objects.get(id = '2')
# print(c)


# 1 to many

# Creating authors
# a1 = Author.objects.create(name="Author 1")
# a2 = Author.objects.create(name="Author 2")

# # Creating books and associating them with authors
# book1 = Book.objects.create(title="Book 1", author=a1)
# book2 = Book.objects.create(title="Book 2", author=a1)
# book3 = Book.objects.create(title="Book 3", author=a2)
# book3 = Book.objects.create(title="Book 4", author=a2)


au = Author.objects.get(name="Author 1")
bau1 = Book.objects.filter(author=au)
print(bau1)


# retrive data from foreign key

# book = Book.objects.get(title="Book 1")
# author_of_book1 = book.author
