from django.db import models
from django.db.models import Max

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    salary = models.IntegerField()

    def __str__(self):
        return str(self.name)


# in shell,
# 1. from django.db.models import Max, Avg, Q

# 2. Employee.objects.aggregate(Max('salary')) # to find max 

# 3. Employee.objects.filter(salary = 20000) # to find perticular

# 4. Employee.objects.order_by('salary') # to find it in order
#    Employee.objects.order_by('-salary')[0] 
#    Employee.objects.order_by('-salary')[1]

# 5. Employee.objects.aggregate(Avg('salary')) # to find an average

# 6. Employee.objects.filter(salary__gt = 15000) # greater than
#    Employee.objects.filter(salary__gte = 15000) # greater than equal to

#    Employee.objects.filter(salary__lt = 15000) # less than
#    Employee.objects.filter(salary__lte = 15000) # less than equal to

# 7. Employee.objects.exclude(salary = 15000) # to find an employees who dont have 15000 salary
#    Employee.objects.filter(~Q(salary = 15000))
#    Employee.objects.exclude(Q(salary = 15000) | Q(salary = 20000)) # to exclude both values

# 8. Employee.objects.filter(Q(salary = 15000) | Q(salary = 20000)) # to get both values

# 9. Employee.objects.filter(Q(salary = 17000) & Q(name__endswith = 'l')) # if both the condition true

# 10. Employee.objects.filter(name='rahul').update(salary=25000) # to update data

# 11. Employee.objects.filter(salary__lt = 10000).exists() # if such record exists than return True else False

# 12. Employee.objects.all().update(salary=25000) # update All