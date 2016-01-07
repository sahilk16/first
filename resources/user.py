from flask_restful import Resource, reqparse, marshal_with, fields

# These fields map to database
user_fields = {'id': fields.Integer,
               'username': fields.String,
               'first_name': fields.String,
               'last_name': fields.String
               }

class User(Resource):
    def get(self):
        pass

    @marshal_with(user_fields)
    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument('username', dest='username', location='form', required=True,
                                 help="The username is required")
        post_parser.add_argument('first_name', dest='first_name', location='form', required=True,
                                 help="First name is required")
        post_parser.add_argument('last_name', dest='last_name', location='form', required=True,
                                 help="Last name is required")
        args = post_parser.parse_args(strict=True)
        user_object = create_user(args.first_name, args.last_name)
        return user_object


    def put(self):
        pass

    def delete(self):
        pass
