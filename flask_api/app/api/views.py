from flask_restful import Api, Resource, reqparse

api = Api()


@api.resource('/test')
class APITest(Resource):

    def api_test(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()

        if not args['id']:
            return {
                'code': -1,
                'data': {}
            }

        return {
            'code': 0,
            'data': {
                'id': int(args['id'])
            }
        }

    def get(self):
        return self.api_test()

    def post(self):
        return self.api_test()
