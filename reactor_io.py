import enum
import random


# The average that can be used in a pinch
# NOTE: this is mega fudged
AVG_GRAMPS_PER_STEP = random.random()


class FeedEmptyError(Exception):
    """ Exception for alerting when the feed is empty """
    pass


class Sensor(enum.Enum):
    FEED_SCALE_G = "feed_scale"
    FEED_PUMP_STEPS = "feed_pump_steps"


class Actuator(enum.Enum):
    FEED_PUMP_STEP_RATE = "feed_pump_step_rate"
    FEED_PUMP_STEP_TARGET = "feed_pump_step_target"


sensor_values = {
    FEED_SCALE_G: 1000, # TODO: Provide a function to set this
    FEED_PUMP_STEPS: 0
}


def get_sensor_value(sensor: Sensor) -> float:
    # NOTE: Fudging everything
    global sensor_values
    if sensor == Sensor.FEED_SCALE_G:
        ret = sensor_values[FEED_SCALE_G]
        sensor_values[FEED_SCALE_G] -= random.random()
    elif sensor == Sensor.FEED_PUMP_STEPS:
        ret = sensor_values[FEED_PUMP_STEPS
        sensor_values[FEED_PUMP_STEPS] += random.random()
    else:
        raise KeyError(f'{sensor} is not a valid sensor!')
    return ret


def set_actuator_value(actuator: Actuator, value: float) -> None:
    if not isinstance(actuator, Actuator):
        raise KeyError(f'{actuator} is not a valid actuator!')
    pass
    # NOTE: Normally work would happen here but hey this ain't hooked up to a reactor!
