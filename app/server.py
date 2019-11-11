import flask
import app.utils.config as config
import app.controller.route as resumen_route
import app.gateways.rabbit_service as rabbitService
import os
from flask_cors import CORS

class MainApp:
	def __init__(self):
		self.flask_app = flask.Flask(__name__)
		CORS(self.flask_app, supports_credentials=True, automatic_options=True)
		self._generate_api_doc()
		self._init_routes()
		self._init_rabbit()
		self.resumenstats()

	def _generate_api_doc(self):
		os.system("apidoc -i ./ -o ./public")	


	def resumenstats(self):
		resumen_route.init(self.flask_app)
	def _init_routes(self):
		# Servidor de archivos estáticos de apidoc
		# Por el momento se genera con ../auth/node_modules/.bin/apidoc -i ./ -o public
		@self.flask_app.route('/<path:path>')
		def api_index(path):
			return flask.send_from_directory('../public', path)


		@self.flask_app.route('/')
		def index():
			return flask.send_from_directory('../public', "index.html")
		
	

	def _init_rabbit(self):
    		rabbitService.init()


	def start(self,debug=True):
    		self.flask_app.run(port=config.get_server_port(),debug=debug)

	def get_flask_app(self):
    		return self.flask_app
	

