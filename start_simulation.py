import os
from pathlib import Path
import tempfile
import hydra
from nuplan.planning.script.run_simulation import main as main_simulation

experiment_path = os.getenv('NUPLAN_EXP_ROOT') + '/training/train_lanegcn/'

best_model_path = experiment_path + str(sorted(os.listdir(experiment_path))[-1]) + '/best_model/'
best_model = best_model_path + str(os.listdir(best_model_path)[0])

print(best_model)

# MODEL_PATH = str(checkpoint).replace("=", "\=")
MODEL_PATH=str(best_model).replace("=", "\=")

CONFIG_PATH = 'nuplan/planning/script/config/simulation'
CONFIG_NAME = 'default_simulation'
CHALLENGE = 'open_loop_boxes'
PLANNER = 'ml_planner'

hydra.core.global_hydra.GlobalHydra.instance().clear()
hydra.initialize(config_path=CONFIG_PATH)

cfg = hydra.compose(config_name=CONFIG_NAME, overrides=[
    #'job_name=simulation_urban_driver_fulldataset_nmv',
    #'experiment_name=simulation',
    f'+simulation={CHALLENGE}',
    'planner=ml_planner',
    'model=vector_model',
    'planner.ml_planner.model_config=${model}',
    f'planner.ml_planner.checkpoint_path={MODEL_PATH}',
    'scenario_builder=nuplan_mini',
    'scenario_filter=all_scenarios',
    'scenario_filter.scenario_types=[starting_straight_traffic_light_intersection_traversal,changing_lane, starting_left_turn, starting_right_turn, stopping_with_lead, following_lane_with_lead, near_multiple_vehicles, traversing_pickup_dropoff, behind_long_vehicle, waiting_for_pedestrian_to_cross]',
    'scenario_filter.num_scenarios_per_type=100'])

main_simulation(cfg)


