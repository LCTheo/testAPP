from flask import Flask, render_template, make_response, redirect
from flask_restx import Api, Resource
import logging
app = Flask(__name__)
api = Api(app=app, version='1.0', title='Resources Doc API', validate=True)


@api.route("/index")
class ResourcesList(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


@api.route("/log/base")
class ResourcesList(Resource):

    def post(self):
        logging.info('this is info log')
        return redirect("/index")


@api.route("/log/error")
class ResourcesList(Resource):

    def post(self):
        logging.error('this is error log')
        return redirect("/index")


@api.route("/charge")
class ResourcesList(Resource):

    def get(self):
        i = 1
        stop = 50
        res = 1
        while i < stop:
            res = res*i
            i += 1
        logging.error('exec time: ' + str(res))
        return redirect("/index")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
