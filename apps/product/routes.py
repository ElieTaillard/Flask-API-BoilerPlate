from flask import request

from apps.product import blueprint


@blueprint.route("/products", methods=["GET"])
def products():
    return "Products"
