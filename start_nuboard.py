import os
import hydra
from nuplan.planning.script.run_nuboard import main as main_nuboard

# Location of path with all nuBoard configs
CONFIG_PATH = 'nuplan/planning/script/config/nuboard'
CONFIG_NAME = 'default_nuboard'

# Initialize configuration management system
hydra.core.global_hydra.GlobalHydra.instance().clear()  # reinitialize hydra if already initialized
hydra.initialize(config_path=CONFIG_PATH)

simulation_path = os.getenv('NUPLAN_EXP_ROOT') + '/simulation/open_loop_boxes'
simulation_file = simulation_path + '/' +  str(sorted(os.listdir(simulation_path))[-1])

print(simulation_file)
# Compose the configuration
cfg = hydra.compose(config_name=CONFIG_NAME, overrides=[
    'scenario_builder=nuplan',  # set the database (same as simulation) used to fetch data for visualization
    f'simulation_path={simulation_file}',  # nuboard file path(s), if left empty the user can open the file inside nuBoard
])

main_nuboard(cfg)

