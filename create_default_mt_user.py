#!/usr/bin/python3
"""
Create default user
"""
from models import storage
from models.users import User

# Reload storage to ensure it's ready
storage.reload()

# Create new user
new_user = User(first_name='aimad',
                last_name='kacem',
                email='kacem.aimad@gmail.com',
                password='test1234')
new_user.save()
storage.save(new_user)
print(new_user.id)
print("User added successfully")
