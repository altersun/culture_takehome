#! /usr/bin/env python3

import argparse
import asyncio
import enum
import logging
import os
import schema
import sys
import time
import yaml

import reactor_controller
import reactor_io


class RecipeState(enum.Enum):
    BOLUS = 'bolus'
    LINEAR = 'linear'
    TIMED = 'timed'
    PAUSE = 'pause'



class RecipeError(Exception):
    """A simple purpose-branded exception"""
    pass


def parse_recipe(filename: str) -> list:
    """
    Load recipe from file and confirm it follows format
    """
    recipe_scheme = schema.Schema([
        schema.Or(
            {RecipeState.BOLUS: {'target_mass': int}}, 
            {RecipeState.LINEAR: {'target_rate': int}},
            {RecipeState.TIMED: {'rate': int, 'time': int}},
            {RecipeState.PAUSE: {'time': int}},
        )
    ])

    with open(filename, 'r') as recipe_file:
        recipe_list = yaml.safe_load(recipe_file)
    recipe_scheme.validate(recipe_list)
    return recipe_list


        
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

    previous_values = {
        'feed_scale': reactor_io.get_sensor_value(reactor_io.Sensor.FEED_SCALE_G)
        'steps': reactor_io.get_sensor_value(reactor_io.Sensor.FEED_PUMP_STEPS)
    }



    # TODO: Consider using asyncio event loop for this to avoid clock drift cost of calculations
    for 
        current_values = {
            'feed_scale': reactor_io.get_sensor_value(reactor_io.Sensor.FEED_SCALE_G)
            'steps': reactor_io.get_sensor_value(reactor_io.Sensor.FEED_PUMP_STEPS)
        }
        grams_per_step = (previous_scale['feed_scale']-current_values['feed_scale']) /\
            (current_values['steps']-previous_scale['steps'])
        if grams_per_step == 0:
            grams_per_step = reactor_io.AVG_GRAMPS_PER_STEP
        
        recipe_step = recipe[0]
        recipe_type = list(recipe[0].keys)[0] # Maybe I should rethink the schema...
        if recipe[0].k == RecipeState.BOLUS:
            controller.set_feed_scale = current_values['feed_scale'] - recipe[0]['target_mass']
        elif recipe[0]

    
    #splart = [10,]
    #def desplarter():
    #    next = loop.time() + 1.0
    #    loop.call_later(1, desplarter)
    #    print(f'{splart[0]}, {next-1.0}')
    #    splart[0] -= 1
    #    if splart[0] == 0:
    #        loop.stop()
    



    desplarter()
    loop.run_forever()
    print('Done!')