#! /bin/bash

python nuplan/planning/script/run_training.py \
    group=/tmp/urban_driver_model \
    cache.cache_path=/tmp/urban_driver_model/cache \
    job_name=train_default_urban_driver \
    experiment_name=test_urban_driver_experiment \
    py_func=test \
    +training=training_urban_driver_open_loop_model \
    scenario_builder=nuplan_mini \
    lightning.trainer.params.accelerator=ddp_spawn \
    lightning.trainer.params.max_epochs=10 \
    data_loader.params.batch_size=8 \
    data_loader.params.num_workers=8
