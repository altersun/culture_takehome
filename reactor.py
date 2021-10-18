import logging
import os
import schema
import yaml


class RecipeError(Exception):
    """A simple purpose-branded exception"""
    pass


def parse_recipe(filename: str) -> list:
    """
    Load recipe from file and confirm it follows format
    """
    recipe_scheme = schema.Schema([
        schema.Or(
            {'bolus': {'target_mass': int}}, 
            {'linear': {'target_rate': int}},
            {'timed': {'rate': int, 'time': int}},
            {'pause': {'time': int}},
        )
    ])

    with recipe_file as open(filename, 'r'):
        recipe_dict = yaml.safe_load(recipe_file)
    recipe_scheme.validate(recipe_dict)
    return recipe_dict


       
        
            
     
