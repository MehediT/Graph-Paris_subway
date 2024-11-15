# Variables
PYTHON = python3
SRC_DIR = src
RES_DIR = res
MAIN = main.py
REQ_FILE = requirements.txt

# Default target
all: run

# Install dependencies
install:
	$(PYTHON) -m pip install -r $(REQ_FILE)

# Run the main program
run: install
	$(PYTHON) $(SRC_DIR)/$(MAIN)

# Lint the code
lint:
	flake8 $(SRC_DIR)

# Clean up temporary and compiled files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.log

# PHONY targets to prevent conflicts with files
.PHONY: all install run lint test clean docs
