import yaml

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access variables
db_name = config['database']['name']
debug_mode = config['settings']['debug_mode']

print(F"{db_name}")