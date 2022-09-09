from dependencies import get_db
from authentication.utils.hash_password import hash_password
from authentication.role_manager import is_admin
import bcrypt
def create_user(db, API_KEY, user):
    logged_user = get_user(db, API_KEY=API_KEY)
    if is_admin(user=logged_user):
        
        # generates complex data to increase security
        user['salt'] = bcrypt.gensalt()
        
        # hash password and insert user in database
        user['password'] = hash_password(user['password'], user['salt'])
        user = db.User.insert_one(user)
        
        # remove critical info from model to send back to client
        user.pop('password')
        user.pop('api_key')
        user.pop('salt')
        
        return user

def get_user(db, API_KEY):
    return db.User.find_one({'api_key': API_KEY})

def get_user_by_name(db, name):

    return db.User.find_one({'name': name})
