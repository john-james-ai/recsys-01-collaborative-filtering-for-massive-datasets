#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems Lab: Towards State-of-the-Art                                   #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.8                                                                              #
# Filename   : /tests/test_workspace/test_operator.py                                              #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/recsys-lab                                         #
# ------------------------------------------------------------------------------------------------ #
# Created    : Sunday March 5th 2023 12:33:42 am                                                   #
# Modified   : Friday March 17th 2023 03:00:23 pm                                                  #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from datetime import datetime

from recsys import Operator


# ------------------------------------------------------------------------------------------------ #
#                                      TEST OPERATOR                                               #
# ------------------------------------------------------------------------------------------------ #
class TestOperator(Operator):
    """Operator does nothing."""

    def __init__(self) -> None:
        super().__init__()

    def execute(self, *args, **kwargs) -> None:
        """Downloads a zipfile."""
        self._logger.debug(datetime.now())