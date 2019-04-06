# Author:hxj
from flask import Blueprint

app_cart = Blueprint('app_cart',__name__,template_folder='templates')

from .views import get_cart