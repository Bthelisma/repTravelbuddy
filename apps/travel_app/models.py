# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
import datetime
from django.db import models


class UserManager(models.Manager):
    def register_validate(self, postData):
        errors = []

        name = postData['name']
        username = postData['username']
        password = postData['password']
        cpassword = postData['cpassword']

        if not name or not username or not password or not cpassword:
            errors.append( "All fields are required")

        # check name
        if len(name) < 3 :
            errors.append( "name fields should be at least 3 characters")

        # check username
        if len(username) < 1:
            errors.append( "Username cannot be blank")


        # check password
        if len(password ) < 8:
            errors.append ( "password must be at least 8 characters")
        elif password != cpassword:
            errors.append ( "password must be match")

        if not errors:
            if User.objects.filter(username=username):
                errors.append("username is not unique")
            else:
                hashed = bcrypt.hashpw((password.encode()), bcrypt.gensalt(5))

                return self.create(
                    name=name,
                    username=username,
                    password=hashed
                )

        return errors

    def login_validate(self, postData):
        errors = []
        password = postData['password']
        username = postData['username']
                # check DB for username
        try:
            # check user's password
            user = self.get(username=username)
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user

        except:
            pass

        errors.append('Invalid login info')
        return errors

class TripManager(models.Manager):
    def trip_validate(self, postData, id):
        errors=[]
        destination=postData['destination']
        description=postData['description']
        start_date=postData['start_date']
        end_date=postData['end_date']
        


        if start_date < datetime.datetime.now().strftime('%m-%d-%Y'):
            errors.append('Start Date must be after today')

        elif start_date > end_date:
                errors.append('End Date must be after Start Date')

        if not destination or not destination or not start_date or not end_date:
            errors.append( "All fields are required")

        if len(destination)<1:
            errors.append('please enter a destination')
        if len(description)<1:
            errors.append('please enter a description')

        if not errors:
            user = User.objects.get(id=id)
            trip = self.create(
                destination = destination,
                description = description,
                start_date = start_date,
                end_date= end_date,
                created_by = user
                )
            trip.travellers.add(user)
            return trip

        return errors


class User(models.Model):
      name = models.CharField(max_length=255)
      username = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()




class Trip(models.Model):
      destination = models.CharField(max_length=255)
      description = models.CharField(max_length=255)
      start_date = models.DateTimeField()
      end_date = models.DateTimeField()
      created_by = models.ForeignKey(User, related_name="planner")
      travellers = models.ManyToManyField(User, related_name="joiner")
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects=TripManager()
