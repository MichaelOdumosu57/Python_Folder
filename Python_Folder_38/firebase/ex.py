from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth 
import os
import json 
import firebase_admin

with open(os.environ['AF_AUTH']) as s:
    os.environ['AF_AUTH']= s.read()


lb = json.loads(os.environ['AF_AUTH'])
cred = credentials.Certificate(lb)
apps = firebase_admin.initialize_app(cred)
 
#  to make an account to be imported to Firebase 

a = auth.ImportUserRecord('8MagmfdeB2QVNVRfzT4vlx7hKto1')
print(a.email)

################################################


#Represents a page of user records exported from a Firebase project.\\

# b =auth.ListUsersPage()
# need 3 args idk where to get them 
# print(b ) 

################################################


#Represents a hash algorithm used to hash user passwords.

# b =auth.ListUsersPage()
# need 3 args idk where to get them 
# print(b ) 

################################################
