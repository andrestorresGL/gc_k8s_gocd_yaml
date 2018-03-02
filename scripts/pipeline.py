#!/usr/bin/env python
from gomatic import *
#for arg in sys.argv:
import sys

args=str(sys.argv[1])
configurator = GoCdConfigurator(HostRestClient(args, ssl=False))
pipeline = configurator\
	.ensure_pipeline_group("group1")\
	.ensure_replacement_of_pipeline("test_pipeline")\
	.set_template_name("base_template")\
	.set_lock_behavior("unlockWhenFinished")\
	.set_git_url("https://github.com/aetorres/c_test.git")
template = configurator.ensure_replacement_of_template("base_template")
stage = template.ensure_stage("defaultStage")
job = stage.ensure_job("defaultJob")
job.add_task(ExecTask(['/bin/bash', '-c', 'gcc -Wall test.c -o test']))

configurator.save_updated_config()
