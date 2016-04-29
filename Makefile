.PHONY: test run install

PIP?=pip
FLAKE8?=flake8
PYTEST?=py.test
PYTHON?=python

install:
	$(PIP) install -r requirements.txt

test: lint
	$(PYTEST) --cov count_words --cov-config .coveragerc 001-counting-words/test_count_words.py
	$(PYTEST) --cov list_length --cov-config .coveragerc 002-list-length/test_single_method_list.py
	$(PYTEST) --cov playlist --cov-config .coveragerc 003-chaining-songs/test_playlist.py

# run:
# 	$(PYTHON) 001-counting-words/count_words.py
#
lint:
	$(FLAKE8) --config=.flake8rc 001-counting-words/count_words.py
	$(FLAKE8) --config=.flake8rc 002-list-length/test_single_method_list.py
	$(FLAKE8) --config=.flake8rc 003-chaining-songs/test_playlist.py
