import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

import spreading_dye_sampler.dye_blot

import numpy as np
from numpy.random import random
import pytest

@pytest.fixture
def blot():
    num_cells = 100
    grid_width = 100
    grid_height = 100

    blot = None
    while blot is None:
        blot = spreading_dye_sampler.dye_blot.make_blot(
                [grid_width, grid_height], [10, 10], num_cells)
    return blot

def test_make_dye_blot():
    num_cells = 10
    grid_width = 100
    grid_height = 100

    for i in range(100):
        # make a blot
        blot = None
        while blot is None:
            blot = spreading_dye_sampler.dye_blot.make_blot(
                    [grid_width, grid_height], [10, 20], num_cells)

        # check size
        assert blot.num_cells() == num_cells

        # check that the blot is in range
        for x, y in blot._cells:
            assert 0 <= x
            assert x < grid_width
            assert 0 <= y
            assert y < grid_height

def test_for_each_cell(blot):
    def test_forward(x, y):
        assert x, y in blot._cells

    blot.for_each_cell(test_forward)

def test_aspect():
    grid_width = 1000
    grid_height = 10
    num_cells = 500

    blot = None
    while blot is None:
        blot = spreading_dye_sampler.dye_blot.make_blot(
                [grid_width, grid_height], [1, 100], num_cells)

    assert blot.num_cells() == num_cells
    x_min = min([x for x, y in blot._cells])
    x_max = max([x for x, y in blot._cells])
    y_min = min([y for x, y in blot._cells])
    y_max = max([y for x, y in blot._cells])

    x_size = x_max - x_min
    y_size = y_max - y_min
    # This may fail occasionally. Need to figure out.
    assert x_size / y_size > 5

def test_squeeze():
    grid_width = 10
    grid_height = 10
    num_cells = grid_width * grid_height

    blot = spreading_dye_sampler.dye_blot.make_blot(
            [grid_width, grid_height], [10, 10], num_cells, squeeze=True)

    assert blot is not None
    assert blot.num_cells() == num_cells

    for y in range(grid_height):
        for x in range(grid_width):
            assert (x, y) in blot._cells

def test_masking():
    grid_width = 10
    grid_height = 10
    num_cells = 20

    # Make a mask with 45 permitted cells
    mask = np.zeros([grid_width, grid_height], dtype=bool)
    for y in range(grid_height):
        for x in range(grid_width):
            dx = x - grid_width / 2
            dy = y - grid_height / 2
            mask[x, y] = dx**2 + dy**2 < 4*4

    for i in range(100):
        num_cells = int(np.floor(random() * 44) + 1.0)
        blot = None
        while blot is None:
            blot = spreading_dye_sampler.dye_blot.make_blot(
                    [grid_width, grid_height], [10, 10], num_cells, mask, squeeze=True)

        assert blot.num_cells() == num_cells

        def check(x, y):
            assert mask[x, y]

        blot.for_each_cell(check)
