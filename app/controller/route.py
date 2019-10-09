import flask

def init(app):
	@app.route("/")
	def index():
		return '<h1>Probando 1...2...3...</h1>'