from flask import Flask
from flask_restful import Api, Resource # Resource is used for requests/CRUD handling

# Make new Flask app
app = Flask(__name__)

# Wrap app in api. Initializes RESTful api
api = Api(app)

class HelloWorld(Resource):
    def get(self, name):
        return {"api": "Lore Names"}
    def post(self):
        return {"data": "posted"}

# register the resource (like a route off the base url)
## resource is an endpoint
### <data_type_here:parameter_name> defines information the client can send to this resource
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    # do not run debug = True in prod
    app.run(debug=True)