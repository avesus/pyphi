#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from pyphi.network import Network


@pytest.fixture()
def network():
    size = 3
    current_state = (0, 1, 0)
    tpm = np.ones([2] * size + [size]).astype(float) / 2
    return Network(tpm, current_state)


def test_network_init_validation(network):
    with pytest.raises(ValueError):
        # Totally wrong shape
        tpm = np.arange(3).astype(float)
        state = (0, 1, 0)
        Network(tpm, state)
    with pytest.raises(ValueError):
        # Non-binary nodes (4 states)
        tpm = np.ones((4, 4, 4, 3)).astype(float)
        state = (0, 1, 0)
        Network(tpm, state)
    with pytest.raises(ValueError):
        # Wrong current state length
        current_state = (0, 1)
        Network(network.tpm, current_state)


def test_repr(standard):
    print(repr(standard))


def test_str(standard):
    print(str(standard))
