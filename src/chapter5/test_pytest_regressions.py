def summary_grids():
    return {
        "Main Grid": {
            "id": 0,
            "cell_count": 1000,
            "active_cells": 300,
            "properties": [
                {"name": "Temperature", "min": 75, "max": 85},
                {"name": "Porosity", "min": 0.3, "max": 0.4},
            ],
        },
        "Refin1": {
            "id": 1,
            "cell_count": 48,
            "active_cells": 44,
            "properties": [
                {"name": "Temperature", "min": 78, "max": 81},
                {"name": "Porosity", "min": 0.36, "max": 0.39},
            ],
        },
    }


def test_grids(data_regression):
    data = summary_grids()
    data_regression.check(data)
