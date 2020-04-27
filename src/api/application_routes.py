import services.application_services as application_service

from flask import Blueprint, jsonify

http = Blueprint(name="http_application", import_name=__name__, url_prefix="/application")


@http.route('/health', methods=['GET'])
def get_application_status():
    application_health = application_service.get_application_health()
    return jsonify(application_health.dict())
