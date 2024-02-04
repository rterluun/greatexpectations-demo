> .pre-commit-config.yaml
pip install poetry
poetry init
poetry install --no-root --only=dev
poetry run pre-commit run --all-files
poetry run pre-commit install
poetry install --no-root
great_expectations init
cat gx/.gitignore >> .gitignore
python config/demo-datasource.py
great_expectations suite list
great_expectations suite new --no-jupyter
jupyter notebook gx/uncommitted/edit_default_data_asset_name.warning.ipynb
