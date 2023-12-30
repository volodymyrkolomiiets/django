#### The ```save()``` method of the ```models.Model``` class creates a row in the Customer table. 

```
>>> from demoapp.models import Customer 
>>> c=Customer(name="Henry") 
>>> c.save()
>>> Customer.objects.create(name="Hameed") 
```
#### Fetch the Customer object with a primary key = 2.
```
>>> from demoapp.models import Customer, Vehicle  
>>> c=Customer.objects.get(pk=2) 
>>> c.name 
'Hameed' 
```

This object is used as the value of the customer attribute in the Vehicle object.:
```
>>> v=Vehicle(name="Honda", customer=c) 
>>> v.save() 
>>> v=Vehicle(name="Toyota", customer=c)   
>>> v.save() 
>>> c=Customer.objects.get(name="Henry") 
>>> Vehicle.objects.create(name="Ford", customer=c) 
<Vehicle: Vehicle object (3)> 
>>> Vehicle.objects.create(name="Nissan", customer=c) 
<Vehicle: Vehicle object (4)> 
```

### the following statement to retrieve all the customers with names starting with 'H':

```
mydata = Customer.objects.filter(name__startswith='H') 
```