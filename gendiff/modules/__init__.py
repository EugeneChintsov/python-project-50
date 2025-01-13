# import my_application.module as my_lib
from gendiff.modules.cli import greet
from gendiff.modules.main import generate_diff


__all__ = (
    # "my_lib",
    "greet",
    "generate_diff",
)