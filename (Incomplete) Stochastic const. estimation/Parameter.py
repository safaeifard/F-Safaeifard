#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:31:39 2021

@author: fateme
"""
import sys
import os
import errno
import warnings
import inspect
import re
import collections
import weakref
import copy
import itertools
import sympy
import scipy.sparse
import networkx as nx
from collections.abc import Iterable, Mapping, Sequence, Set

from importlib import reload
from pysb.core import Component
from pysb.core import Symbol

class Parameter(Component, Symbol):

    """
    Model component representing a named constant floating point number.

    Parameters are used as reaction rate constants, compartment volumes and
    initial (boundary) conditions for species.

    Parameters
    ----------
    value : number, optional
        The numerical value of the parameter. Defaults to 0.0 if not specified.
        The provided value is converted to a float before being stored, so any
        value that cannot be coerced to a float will trigger an exception.
    nonnegative : bool, optional
        Sets the assumption whether this parameter is nonnegative (>=0).
        Affects simplifications of expressions that involve this parameter.
        By default, parameters are assumed to be non-negative.
    integer : bool, optional
        Sets the assumption whether this parameter takes integer values,
        which affects simplifications of expressions that involve this
        parameter. By default, parameters are not assumed to take integer values.

    Attributes
    ----------
    value (see Parameters above).

    """

    def __new__(cls, name, value=0.0, nonnegative=True, integer=False,
                _export=True):

        return super(Parameter, cls).__new__(cls, name, real=True,
                                             nonnegative=nonnegative,
                                             integer=integer)

    def __getnewargs__(self):
        return (self.name, self.value, False)

    def __init__(self, name, value=0.0, _export=True, **kwargs):
        self.value = value
        Component.__init__(self, name, _export)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.check_value(new_value)
        self._value = float(new_value)
    
    def get_value(self):
        return self.value

    def check_value(self, value):
        if self.is_integer:
            if not float(value).is_integer():
                raise ValueError('Cannot assign an non-integer value to a '
                                 'parameter assumed to be an integer')
        if self.is_nonnegative:
            if float(value) < 0:
                raise ValueError('Cannot assign a negative value to a '
                                 'parameter assumed to be nonnegative')
    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, repr(self.name), repr(self.value))

    def __str__(self):
        return repr(self)

