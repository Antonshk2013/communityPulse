from typing import Any

from src.dto import (
    CategoryRequestDTO,
    CategoryResponseDTO
)
from src.models import Category
from src.repositories.base import BaseRepository


class CategoryService:
    category_repo = BaseRepository(Category)

    def create_category(self, data: dict[str, Any]):
        try:
            validated_data = CategoryRequestDTO(**data)
            category = Category(**validated_data.model_dump())
            category, err = self.category_repo.create(category)

            if err:
                return None, err

            response = CategoryResponseDTO.model_validate(category)

            return response.model_dump_json(indent=4), None

        except Exception as e:
            return None, str(e)

    def get_all_categories(self):
        categories, err = self.category_repo.get_all()

        if err:
            return None, err

        response = [
            CategoryResponseDTO.model_validate(
                category).model_dump_json(indent=4)
            for category in categories
        ]
        return response, None

    def get_category(self, category_id: int):
        category, err = self.category_repo.get_by_id(category_id)

        if err:
            return None, err

        if not category:
            return None, f"Not found"

        response = CategoryResponseDTO.model_validate(category)

        return response.model_dump_json(indent=4), None

    def update_category(self, category_id: int, data: dict[str, Any]):
        try:
            validated_data = CategoryRequestDTO(**data)

            updated_data = validated_data.model_dump(
                exclude_unset=True,
                exclude_none=True
            )

            if not updated_data:
                return None, "No data to update"

            category, err = self.category_repo.update(
                obj_id=category_id,
                data=updated_data
            )

            if err:
                return None, err

            response = CategoryResponseDTO.model_validate(category)

            return response.model_dump_json(indent=4), None

        except Exception as e:
            return None, str(e)

    def delete_category(self, category_id: int):
        return self.category_repo.delete(category_id)
