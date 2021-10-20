# culture_takehome
Homework for interviewing at Culture Biosciences

## How to install
Develped on Python 3.8 so use an earlier version at your own risk!

```bash
# a virtualenv is preferred instead of polluting the root installation
# if you don't want to deal you can skip the next three lines
$ pip3 install --user virtualenv # Only needs to be done once
$ virtualenv venv
$ source ./venv/bin/activate

# install the requirements
$ pip3 install -r requirements.txt
```

## How to Run
TBD

## Recipe Format
In yaml:
```yaml
# Can be used to kill time between recipe steps
- pause: 
    time: 30 # minutes

# Add a fixed mass of glucose
- bolus:
    target_mass: 30 # grams

# Add an arbitrary mass of glucose at an increasing/decreasing rate until target is hit
- linear:
    target_rate: 30 # steps/min

# Feed in glucose at a given volumetric rate for a given time
- timed:
    rate: 30 # steps/min
    time: 30 # minutes
```
