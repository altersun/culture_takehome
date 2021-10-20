import abc
import simple_pid


class ReactorController(abc.ABC):
    
    def __init__(self):
        # TBD


    def update(feed_scale: float, grams_per_step: float) -> (float, int)
        """
        Take in scale reading and rate calculation, return step rate and step target
        """
        raise NotImplementedError



class Cascade(ReactorController):

    def __init(self, recipe, interval):
        # Tunings?? WIP.
        # TODO: Probably load this from a yaml file or argument
        # TODO: Also these should be constants
        outer = simple_pid.PID(1, 0.1, 0.05, sample_time=interval)
        inner = simple_pid.PID(1, 0.1, 0.05, sample_time=interval)
        # TBD
        super().__init__(recipe)

    @property
    def set_feed_scale(grams: float):
        outer.setpoint = grams

    #@property
    #def set_grams_per_step(rate: float):
    #    inner.setpoint = rate

    def update(feed_scale: float, grams_per_step: float) -> (float, int)
        """
        Take in scale reading and rate calculation, return step rate and step target
        """
        step_target = outer(feed_scale)
        step_rate = inner(step_target)
        return (step_rate, step_target)


        



class Fuzzy(ReactorController):

    def __init(self, recipe):
        # TBD
        raise NotImplementedError
        super().__init__()