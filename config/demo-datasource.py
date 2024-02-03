import great_expectations as gx

# https://docs.greatexpectations.io/docs/0.15.50/guides/connecting_to_your_data/datasource_configuration/how_to_configure_a_pandas_datasource/

data_context: gx.DataContext = gx.get_context()

datasource_config: dict = {
    "name": "demo",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "my_connector": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "./data",
            "default_regex": {
                "pattern": "(.*)\\.csv",
                "group_names": ["data_asset_name"],
            },
        }
    },
    "batch_spec_passthrough": {
        "reader_method": "csv",
        "reader_options": {
            "header": True,
            "infer_schema": True,
            "sep": ",",
        },
    },
}

data_context.add_datasource(**datasource_config)
