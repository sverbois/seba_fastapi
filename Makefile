.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install environment
install: venv/bin/pip
	venv/bin/pip install -r requirements.txt -c constraints.txt

.PHONY: start  # Start app 1
start1:
	venv/bin/uvicorn app1.main:api --reload

.PHONY: start  # Start app 2
start2:
	venv/bin/uvicorn app2.main:api --reload

.PHONY: start  # Start app 3
start3:
	venv/bin/uvicorn app3.main:api --reload

.PHONY: start  # Start app 4
start4:
	venv/bin/uvicorn app4.backend.main:api --reload

.PHONY: clean  # Clean developement environment
clean:
	rm -rf venv

venv/bin/pip:
	python3.12 -m venv venv
	venv/bin/python3.12 -m pip install --upgrade pip
