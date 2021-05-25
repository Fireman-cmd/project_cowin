from django.db import models

# Create your models here.

class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return self.name
    

class District(models.Model):
    #get all the data that the api returns.
    district_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200,null=True)
    session_data = models.TextField(max_length=1000,null=True) #this will contain wether the vaccine is available or not
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.name



    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200,null=True)
    # telegram = models.CharField(max_length=200,null=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.name

