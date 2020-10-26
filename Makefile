.PHONY: init app

help:
	@echo ""
	@echo "init: Install packages"
	@echo ""
	@echo "app: Run Flask app"

init:
	pip install -r requirements.txt

app:
	python app/__init__.py