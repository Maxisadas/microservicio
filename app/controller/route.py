import flask
import app.utils.security as security
import app.utils.errors as errors
import app.utils.json_serializer as json
import app.domain.services.total_sells as service


def init(app):


	@app.route("/v1/stats/sells",methods=["GET"])
	def total_sells():
		try:
			security.validateAdminRole(flask.request.headers.get("Authorization"))
			return json.dic_to_json(service.total_sells()),200
		except Exception as err:
			return errors.handleError(err)