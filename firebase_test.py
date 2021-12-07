import firebase_admin
from firebase_admin import credentials,db 

ced = credentials.Certificate("ya.json")

# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.

default_app = firebase_admin.initialize_app(ced, {'databaseURL': 'https://integratedcamera-36d77-default-rtdb.firebaseio.com'})
ref = db.reference('interval')
#snapshot = ref.order_by_child('interval').get()
print(ref.get())


