from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth 
from firebase_admin import exceptions
import os
import json 
import firebase_admin


#############################
#data to erase
uid = 'FEb79l5aLKfbk7tKhS76YNSaB1Z2'


############################

with open(os.environ['AF_AUTH']) as s:
    os.environ['AF_AUTH']= s.read()


lb = json.loads(os.environ['AF_AUTH'])
cred = credentials.Certificate(lb)
apps = firebase_admin.initialize_app(cred)
 
#  to make an account to be imported to Firebase 

a = auth.ImportUserRecord(uid )
print(a.email)



################################################
#create a user 
user = auth.create_user(
    email='user@example.com',
    email_verified=False,
    phone_number='+15555550100',
    password='secretPassword',
    display_name='John Doe',
    photo_url='https://www.sortforyou.com/assets/media/cropped-IMG-1475-2-102x61.jpg',
    disabled=False)
print('Sucessfully created new user: {0}'.format(user.uid))
uid = user.uid


################################################

# update a user 

user = auth.update_user(
    uid,
    email='user@example.com',
    phone_number='+15555550100',
    email_verified=True,
    password='newPassword',
    display_name='John Doe',
    photo_url='http://www.example.com/12345678/photo.png',
    disabled=True)
print('Sucessfully updated user: {0}'.format(user.uid))





################################################
# to identify a user 


user = auth.get_user(uid)
print( user.email )

user = auth.get_user_by_phone_number('+15555550100')
print(user.email)
#error for some reason

################################################
# list all users 

# Start listing users from the beginning, 1000 at a time.
page = auth.list_users()
while page:
    for user in page.users:
        print('User: ' + user.uid)
    # Get next batch of users.
    page = page.get_next_page()

# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.
for user in auth.list_users().iterate_all():
    print('User: ' + user.uid)



################################################
#delete a user 
auth.delete_user(uid)
print('Successfully deleted user')


#######################################
# import in bulk


users = list((
    auth.ImportUserRecord(
        uid='uid1',
        email='user1@example.com',
        # password_hash=b'password_hash_1',
        # password_salt=b'salt1'
    ),
    auth.ImportUserRecord(
        uid='uid2',
        email='user2@example.com',
        # password_hash=b'password_hash_2',
        # password_salt=b'salt2'
    ))
)

auth.import_users(users)



#######################################
# import users w/ password 
hash_alg = auth.UserImportHash.hmac_sha256(key=b'secret_key')
try:
    result = auth.import_users(users, hash_alg=hash_alg)
    print('Successfully imported {0} users. Failed to import {1} users.'.format(
        result.success_count, result.failure_count))
    for err in result.errors:
        print('Failed to import {0} due to {1}'.format(users[err.index].uid, err.reason))
except exceptions.FirebaseError:
    # Some unrecoverable error occurred that prevented the operation from running.
    pass

#######################################    


#######################################
# import users w/ MD5, SHA or PBKDF

users = list((
    auth.ImportUserRecord(
        uid='uid3',
        email='user3@example.com',
        password_hash=b'password_hash_1',
        password_salt=b'salt1'
    ),
    auth.ImportUserRecord(
        uid='uid4',
        email='user4@example.com',
        password_hash=b'password_hash_2',
        password_salt=b'salt2'
    ))
)


hash_alg = auth.UserImportHash.pbkdf2_sha256(rounds=100000)
try:
    result = auth.import_users(users, hash_alg=hash_alg)
    print('Successfully imported {0} users for hash w/ rounds. Failed to import {1} users.'.format(
        result.success_count, result.failure_count))    
    for err in result.errors:
        print('Failed to import user:', err.reason)
except exceptions.FirebaseError as error:
    print('Error importing users:', error)


##############################################################################

# SCRYPT hashing 

users = [
    auth.ImportUserRecord(
        uid='some-uid',
        email='user5@example.com',
        password_hash=b'password_hash',
        password_salt=b'salt'
    ),
]

hash_alg = auth.UserImportHash.standard_scrypt(
    memory_cost=1024, parallelization=16, block_size=8, derived_key_length=64)
try:
    result = auth.import_users(users, hash_alg=hash_alg)
    for err in result.errors:
        print('Failed to import user:', err.reason)
except exceptions.FirebaseError as error:
    print('Error importing users:', error)

##############################################################################  

#BCRYPT

users = [
    auth.ImportUserRecord(
        uid='some-uid',
        email='user6@example.com',
        password_hash=b'password_hash',
        password_salt=b'salt'
    ),
]

hash_alg = auth.UserImportHash.bcrypt()
try:
    result = auth.import_users(users, hash_alg=hash_alg)
    print('Successfully imported {0} users for BCRYPT. Failed to import {1} users.'.format(
        result.success_count, result.failure_count))      
    for err in result.errors:
        print('Failed to import user:', err.reason)
except exceptions.FirebaseError as error:
    print('Error importing users:', error)

##############################################################################  

users = [
    auth.ImportUserRecord(
        uid='some-uid',
        display_name='John Doe',
        email='johndoe@gmail.com',
        photo_url='http://www.example.com/12345678/photo.png',
        email_verified=True,
        phone_number='+11234567890',
        custom_claims={'admin': True}, # set this user as admin
        provider_data=[ # user with Google provider
            auth.UserProvider(
                uid='google-uid',
                email='johndoe@gmail.com',
                display_name='John Doe',
                photo_url='http://www.example.com/12345678/photo.png',
                provider_id='google.com'
            )
        ],
    ),
]
try:
    result = auth.import_users(users)
    print('Successfully imported {0} users for combo import. Failed to import {1} users.'.format(
        result.success_count, result.failure_count))     
    for err in result.errors:
        print('Failed to import user:', err.reason)
except exceptions.FirebaseError as error:
    print('Error importing users:', error)
    
##############################################################################      