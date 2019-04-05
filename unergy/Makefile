SHELL := /bin/bash

.DEFAULT_GOAL := help

.PHONY: \
	help \
	test \
	setup

npm-run-dev: build-dev
	docker run -it \
		-p 8080:8080 \
		--rm \
		--name unergy \
		unergy

build-dev: ## Build docker images locally for development use
	docker build \
		-t unergy .

help: ## Display this help message
	@cat $(MAKEFILE_LIST) \
		| grep -e "^[a-zA-Z_\-]*: *.*## *" \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


test:
	echo "Not yet implemented"
