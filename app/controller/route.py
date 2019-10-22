import flask
import app.utils.security as security
import app.utils.errors as errors
import app.utils.json_serializer as json


def init(app):


	@app.route("/v1/stats/sells",methods=["GET"])
	def total_sells():
		try:
			security.validateAdminRole(flask.request.headers.get("Authorization"))
			params = json.body_to_dic(flask.request.data)
			print('params')
			return json.dic_to_json(params)
		except Exception as err:
			return errors.handleError(err)
