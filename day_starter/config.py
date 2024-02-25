from typing import Optional

from pydantic import BaseModel, root_validator

from day_starter.exceptions import DayStarterValidationException


class _ForgesAPIKeys(BaseModel):
    github: Optional[str] = None
    gitlab: Optional[str] = None
    pagure: Optional[str] = None

    @classmethod
    @root_validator()
    def validate_if_at_least_one_is_not_none(cls, field_values: dict) -> dict:
        if all(item is None for item in field_values.items()):
            raise DayStarterValidationException("At least one API key should be set for forge.")

        return field_values


class _ForgeProject(BaseModel):
    namespace: str
    repos: Optional[list[str]]


class _ForgesProjects(BaseModel):
    github: Optional[list[_ForgeProject]] = None
    gitlab: Optional[list[_ForgeProject]] = None
    pagure: Optional[list[_ForgeProject]] = None

    @classmethod
    @root_validator()
    def validate_if_at_least_one_is_not_none(cls, field_values: dict) -> dict:
        if all(item is None for item in field_values.items()):
            raise DayStarterValidationException("No projects to check for")

        return field_values


class Config(BaseModel):
    tokens: _ForgesAPIKeys
    projects: _ForgesProjects
    show_prs_without_review: bool = False

    @classmethod
    def get_config(cls) -> "Config":
        pass
