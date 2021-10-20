#! /usr/bin/env python3

import argparse
import asyncio
import logging
import os
import schema
import sys
import time
import yaml

import reactor_controller


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

    with open(filename, 'r') as recipe_file:
        recipe_dict = yaml.safe_load(recipe_file)
    recipe_scheme.validate(recipe_dict)
    return recipe_dict


        
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--recipe', type=str, default='./sample_recipe.yaml', help='Path and name of recipe file')
    parser.add_argument('-l', '--loglvl', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], help='Log verbosity')
    parser.add_argument('-c', '--controller', default='cascade', choices=['cascade, fuzzy'], help='Control type')
    parser.add_argument('-i', '--interval', default=1, type=float, help='Seconds between updates')
    args = parser.parse_args()

    log_fmt = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)3s] %(message)s'
    logging.basicConfig(level=args.loglvl, format=log_fmt)

    try:
        recipe = parse_recipe(args.recipe)
    except Exception as e:
        logging.exception('Issue reading recipe file')
        sys.exit(-1)

    logging.info(f'Successfully parsed recipe from {os.path.basename(args.recipe)}')
    logging.debug(f'Recipe: {recipe}')

    if args.controller == 'cascade':
        controller = reactor_controller.Cascade(args.interval)
    else if controller == 'fuzzy':
        controller = reactor_controller.Fuzzy()

    
    loop = asyncio.get_event_loop()
    
    splart = [10,]
    def desplarter():
        next = loop.time() + 1.0
        loop.call_later(1, desplarter)
        print(f'{splart[0]}, {next-1.0}')
        splart[0] -= 1
        if splart[0] == 0:
            loop.stop()
    
    desplarter()
    loop.run_forever()
    print('Done!')