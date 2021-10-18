# culture_takehome

```bash
# a virtualenv is preferred instead of polluting the root installation
# if you don't want to deal you can skip the next three lines
$ pip3 install --user virtualenv # Only needs to be done once
$ virtualenv venv
$ source ./venv/bin/activate

# install the requirements
$ pip3 install -r requirements.txt
```

# Recipe Format
```yaml
# Can be used to kill time between recipe steps
- type: pause
  time: 30 # minutes

# Add a fixed mass of glucose
- type: bolus
  target_mass: 30 # grams

# Add an arbitrary mass of glucose at an increasing/decreasing rate until target is hit
- type: linear
  target_rate: 30 # steps/min

# Feed in glucose at a given volumetric rate for a given time
- type: timed
  rate: 30 # steps/min
  time: 30 # minutes
```
