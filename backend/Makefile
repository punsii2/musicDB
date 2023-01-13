.PHONY: all clean

all: venv

venv: venv/venv_stamp

venv/venv_stamp: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/venv_stamp

# test: venv
    # . venv/bin/activate; nosetests project/test

clean:
	rm -rf venv
	rm -rf __pycache__
	find -iname "*.pyc" -delete