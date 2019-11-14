from flask import Blueprint
api_bp = Blueprint('api', __name__)
from app.api.views import api
api.init_app(api_bp)
