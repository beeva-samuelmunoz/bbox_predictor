#
# Author: Samuel M.H. <samuel.mh@gmail.com>
# Description:
#    Make-based utility to manage the project.
#    Idea taken from:
#     - http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

#
### PRECONFIG
#

PYTHON_VERSION := 3.5
MODEL := CNN01-0175


#
### PATHS
#
LIBRARY = bbox_predictor


#Don't touch
PATH_PROJECT = $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
PATH_VENV = $(PATH_PROJECT)/venv
PATH_LIBRARY = $(PATH_PROJECT)/$(LIBRARY)
PATH_DATA = $(PATH_PROJECT)/data

#
### Autodocumenting thing, don't touch
#
.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'



#
### Install the project
#
install: ## Create a development environment (virtualenv).
	@echo "Create the environment in "$(PATH_PROJECT)
	@virtualenv -p python$(PYTHON_VERSION) $(PATH_VENV)
	@echo "Install requirements"
	$(PATH_VENV)'/bin/pip' install -r $(PATH_PROJECT)'/deploy/requirements.txt'
	@echo "Create symbolic links"
	# Link to project
	@ln -s $(PATH_PROJECT) $(PATH_VENV)'/'
	# Link code to project library so it is in the PYTHONPATH
	@ln -s $(PATH_LIBRARY) $(PATH_VENV)'/lib/python$(PYTHON_VERSION)/site-packages/'
	# Local configuration
	# @touch $(PATH_LIBRARY)/config.py $(PATH_LIBRARY)/config_local.py
	@mkdir -p -- $(PATH_DATA)
	# Data directory
	@echo "Done"



#
### Run things
#

run-webserver: ## Start the HTTP microservice (development).
	$(PATH_VENV)'/bin/python' -m $(LIBRARY).webserver $(PATH_DATA)/$(MODEL)
