#! /bin/bash

python nuplan/planning/script/run_training.py \
    job_name=my_train \
    experiment_name=training \
    py_func=train \
    +training=training_raster_model \
    worker=sequential \
    scenario_builder=nuplan_mini \
    scenario_filter=all_scenarios \
    lightning.trainer.params.max_epochs=10 \
    data_loader.params.batch_size=8 \
    data_loader.params.num_workers=8 \
    optimizer.lr=1e-4

