#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems and Deep Learning in Python                                     #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /conftest.py                                                                        #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/recsys-deep-learning                               #
# ------------------------------------------------------------------------------------------------ #
# Created    : Sunday January 29th 2023 08:08:04 am                                                #
# Modified   : Saturday February 25th 2023 02:51:58 am                                             #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import pytest
from types import SimpleNamespace

from recsys.container import Recsys

# ------------------------------------------------------------------------------------------------ #
#                                         FILEPATHS                                                #
# ------------------------------------------------------------------------------------------------ #
#                                         TEST FILE                                                #
ZIPFILE_URL = "https://stats.govt.nz/assets/Uploads/International-trade/International-trade-September-2022-quarter/Download-data/international-trade-september-2022-quarter-csv.zip"
ZIPFILE_DOWNLOAD = "tests/data/download/international-trade-september-2022-quarter-csv.zip"
ZIPFILE_EXTRACT = "tests/data/extract/"
RATINGS_CSV = "tests/data/test_ratings.csv"
RATINGS_PKL = "tests/data/ratings_1_pct.pkl"


# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="session", autouse=True)
def files():
    files = {
        "zipfile_url": ZIPFILE_URL,
        "zipfile_download": ZIPFILE_DOWNLOAD,
        "zipfile_extract": ZIPFILE_EXTRACT,
        "ratings_csv": RATINGS_CSV,
        "ratings_pkl": RATINGS_PKL,
    }
    files = SimpleNamespace(**files)
    return files


# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="session", autouse=True)
def container():
    container = Recsys()
    container.init_resources()
    container.wire(modules=["recsys.container"], packages=["recsys.operator"])

    return container
