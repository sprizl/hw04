from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

parser = reqparse.RequestParser()
parser.add_argument('id')

def convertToBinary(n):
   return bin(n)[2:]
class textToBinary(Resource):
        def post(self):
                args = parser.parse_args()
            id = args['id']
                id_d = int(id)
                id_b = convertToBinary(id_d)
                
                return {"id":id_b}

api.add_resource(textToBinary,'/api/text-to-binary')


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)