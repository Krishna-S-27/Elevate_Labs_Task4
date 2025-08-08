## Flask REST API with Persistent Storage

This project is a simple **Flask-based REST API** that allows you to perform **CRUD operations** on user data.  
The data is **persistently stored in a JSON file** (`users.json`), so it is not lost when the server restarts.  
We have used **Postman** for testing all endpoints.

---

### Features
- **GET**: Retrieve all users or a specific user by ID
- **POST**: Create a new user
- **PUT**: Update existing user details
- **DELETE**: Remove a user from storage
- **Persistent Storage**: Data is stored in `users.json` instead of memory
- **JSON API**: Communicates using JSON for requests and responses

---
##  API Endpoints

1. Get All Users
Request
GET /users
Response
{
    "1": {
        "name": "Krishna Shalwadi",
        "email": "krishnashalawadi27@gmail.com",
        "phone": 8296949050,
        "place": "Bengaluru"
    }
}

3. Get Single User by ID
Request
GET /users/1
Response
{
    "name": "Krishna Shalwadi",
    "email": "krishnashalawadi27@gmail.com",
    "phone": 8296949050,
    "place": "Bengaluru"
}

5. Create New User
Request
POST /users
Content-Type: application/json

Body
{
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "phone": 9876543210,
    "place": "Gadag"
}
Response
{
    "message": "User created"
}


4. Update User
Request
PUT /users/1
Content-Type: application/json
Body
{
    "email": "newemail@example.com"
}
Response
{
    "message": "User updated"
}
6. Delete User
Request
DELETE /users/1
Response
{
    "message": "User deleted"
}
---

## Workflow / How It Works
Loading Data

On application start, the load_users() function reads users.json (if available).

If the file doesn't exist, it starts with an empty dictionary.

Saving Data

Every POST, PUT, or DELETE operation calls save_users() to store updated data in users.json.

Endpoints

GET /users → Returns all users

GET /users/<id> → Returns a single user by ID

POST /users → Creates a new user

PUT /users/<id> → Updates existing user details

DELETE /users/<id> → Removes a user from the list

Testing with Postman

We use Postman to send HTTP requests to the API and view JSON responses.

Supports sending GET, POST, PUT, DELETE requests with JSON body.

---

## Methods Explanation
Method	Purpose	Code Reference
load_users()	Reads JSON file and loads data into memory	app.py lines 6-12
save_users()	Writes current data to users.json	app.py lines 14-16
get_users()	Returns all user data	@app.route('/users', GET)
get_user(user_id)	Fetches a specific user by ID	@app.route('/users/<int:user_id>', GET)
create_user()	Adds a new user	@app.route('/users', POST)
update_user(user_id)	Updates user details	@app.route('/users/<int:user_id>', PUT)
delete_user(user_id)	Deletes a user	@app.route('/users/<int:user_id>', DELETE)

---
