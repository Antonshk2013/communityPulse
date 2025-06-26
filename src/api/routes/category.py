from flask import Blueprint
from src.api.controllers.category import CategoryController
from src.core.config import settings


category_blueprint = Blueprint(
    'categories',
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/categories"
)

category_controller = CategoryController()

category_blueprint.add_url_rule(
    '',
    view_func=category_controller.create_category,
    methods=['POST']
)

category_blueprint.add_url_rule(
    '',
    view_func=category_controller.get_categories,
    methods=['GET']
)

category_blueprint.add_url_rule(
    "/<int:category_id>",
    view_func=category_controller.get_category_by_id,
    methods=['GET']
)

category_blueprint.add_url_rule(
    "/<int:category_id>",
    view_func=category_controller.update_category,
    methods=['PUT', 'PATCH']
)

category_blueprint.add_url_rule(
    "/<int:category_id>",
    view_func=category_controller.delete_category,
    methods=['DELETE']
)