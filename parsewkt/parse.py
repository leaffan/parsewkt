#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CAVEAT UTILITOR
# This file was automatically generated by Grako.
#    https://bitbucket.org/apalala/grako/
# Any changes you make to it will be overwritten the
# next time the file is generated.
#

from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import * # @UnusedWildImport
from grako.exceptions import * # @UnusedWildImport

__version__ = '13.296.16.54.38'

class WktParser(Parser):
    def __init__(self, whitespace=None, nameguard=True, **kwargs):
        super(WktParser, self).__init__(whitespace=whitespace,
            nameguard=nameguard, **kwargs)

    @rule_def
    def _well_known_text_representation_(self):
        with self._choice():
            with self._option():
                self._point_text_representation_()
            with self._option():
                self._curve_text_representation_()
            with self._option():
                self._surface_text_representation_()
            with self._option():
                self._collection_text_representation_()
            self._error('no available options')

    @rule_def
    def _point_text_representation_(self):
        self._token('POINT')
        with self._optional():
            self._z_m_()
        self._point_text_()

    @rule_def
    def _curve_text_representation_(self):
        with self._choice():
            with self._option():
                self._linestring_text_representation_()
            with self._option():
                self._circularstring_text_representation_()
            with self._option():
                self._compoundcurve_text_representation_()
            self._error('no available options')

    @rule_def
    def _linestring_text_representation_(self):
        self._token('LINESTRING')
        with self._optional():
            self._z_m_()
        self._linestring_text_body_()

    @rule_def
    def _circularstring_text_representation_(self):
        self._token('CIRCULARSTRING')
        with self._optional():
            self._z_m_()
        self._circularstring_text_()

    @rule_def
    def _compoundcurve_text_representation_(self):
        self._token('COMPOUNDCURVE')
        with self._optional():
            self._z_m_()
        self._compoundcurve_text_()

    @rule_def
    def _surface_text_representation_(self):
        self._curvepolygon_text_representation_()

    @rule_def
    def _curvepolygon_text_representation_(self):
        with self._choice():
            with self._option():
                self._token('CURVEPOLYGON')
                with self._optional():
                    self._z_m_()
                self._curvepolygon_text_body_()
            with self._option():
                self._polygon_text_representation_()
            with self._option():
                self._triangle_text_representation_()
            self._error('no available options')

    @rule_def
    def _polygon_text_representation_(self):
        self._token('POLYGON')
        with self._optional():
            self._z_m_()
        self._polygon_text_body_()

    @rule_def
    def _triangle_text_representation_(self):
        self._token('TRIANGLE')
        with self._optional():
            self._z_m_()
        self._triangle_text_body_()

    @rule_def
    def _collection_text_representation_(self):
        with self._choice():
            with self._option():
                self._multipoint_text_representation_()
            with self._option():
                self._multicurve_text_representation_()
            with self._option():
                self._multisurface_text_representation_()
            with self._option():
                self._geometrycollection_text_representation_()
            self._error('no available options')

    @rule_def
    def _multipoint_text_representation_(self):
        self._token('MULTIPOINT')
        with self._optional():
            self._z_m_()
        self._multipoint_text_()

    @rule_def
    def _multicurve_text_representation_(self):
        with self._choice():
            with self._option():
                self._token('MULTICURVE')
                with self._optional():
                    self._z_m_()
                self._multicurve_text_()
            with self._option():
                self._multilinestring_text_representation_()
            self._error('no available options')

    @rule_def
    def _multilinestring_text_representation_(self):
        self._token('MULTILINESTRING')
        with self._optional():
            self._z_m_()
        self._multilinestring_text_()

    @rule_def
    def _multisurface_text_representation_(self):
        with self._choice():
            with self._option():
                self._token('MULTISURFACE')
                with self._optional():
                    self._z_m_()
                self._multisurface_text_()
            with self._option():
                self._multipolygon_text_representation_()
            with self._option():
                self._polyhedralsurface_text_representation_()
            with self._option():
                self._tin_text_representation_()
            self._error('no available options')

    @rule_def
    def _multipolygon_text_representation_(self):
        self._token('MULTIPOLYGON')
        with self._optional():
            self._z_m_()
        self._multipolygon_text_()

    @rule_def
    def _polyhedralsurface_text_representation_(self):
        self._token('POLYHEDRALSURFACE')
        with self._optional():
            self._z_m_()
        self._polyhedralsurface_text_()

    @rule_def
    def _tin_text_representation_(self):
        self._token('TIN')
        with self._optional():
            self._z_m_()
        self._tin_text_()

    @rule_def
    def _geometrycollection_text_representation_(self):
        self._token('GEOMETRYCOLLECTION')
        with self._optional():
            self._z_m_()
        self._geometrycollection_text_()

    @rule_def
    def _linestring_text_body_(self):
        self._linestring_text_()

    @rule_def
    def _curvepolygon_text_body_(self):
        self._curvepolygon_text_()

    @rule_def
    def _polygon_text_body_(self):
        self._polygon_text_()

    @rule_def
    def _triangle_text_body_(self):
        self._triangle_text_()

    @rule_def
    def _point_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._point_()
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _point_(self):
        self._x_()
        self._y_()
        with self._optional():
            self._z_()
        with self._optional():
            self._m_()

    @rule_def
    def _x_(self):
        self._number_()

    @rule_def
    def _y_(self):
        self._number_()

    @rule_def
    def _z_(self):
        self._number_()

    @rule_def
    def _m_(self):
        self._number_()

    @rule_def
    def _linestring_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._point_()
                def block0():
                    self._comma_()
                    self._point_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _circularstring_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._point_()
                def block0():
                    self._comma_()
                    self._point_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _compoundcurve_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._single_curve_text_()
                def block0():
                    self._comma_()
                    self._single_curve_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _single_curve_text_(self):
        with self._choice():
            with self._option():
                self._linestring_text_body_()
            with self._option():
                self._circularstring_text_representation_()
            self._error('no available options')

    @rule_def
    def _curve_text_(self):
        with self._choice():
            with self._option():
                self._linestring_text_body_()
            with self._option():
                self._circularstring_text_representation_()
            with self._option():
                self._compoundcurve_text_representation_()
            self._error('no available options')

    @rule_def
    def _ring_text_(self):
        with self._choice():
            with self._option():
                self._linestring_text_body_()
            with self._option():
                self._circularstring_text_representation_()
            with self._option():
                self._compoundcurve_text_representation_()
            self._error('no available options')

    @rule_def
    def _surface_text_(self):
        with self._choice():
            with self._option():
                self._token('CURVEPOLYGON')
                self._curvepolygon_text_body_()
            with self._option():
                self._polygon_text_body_()
            self._error('no available options')

    @rule_def
    def _curvepolygon_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._ring_text_()
                def block0():
                    self._comma_()
                    self._ring_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _polygon_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._linestring_text_()
                def block0():
                    self._comma_()
                    self._linestring_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _triangle_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._linestring_text_()
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _multipoint_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._point_text_()
                def block0():
                    self._comma_()
                    self._point_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _multicurve_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._curve_text_()
                def block0():
                    self._comma_()
                    self._curve_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _multilinestring_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._linestring_text_body_()
                def block0():
                    self._comma_()
                    self._linestring_text_body_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _multisurface_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._surface_text_()
                def block0():
                    self._comma_()
                    self._surface_text_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _multipolygon_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._polygon_text_body_()
                def block0():
                    self._comma_()
                    self._polygon_text_body_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _polyhedralsurface_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._polygon_text_body_()
                def block0():
                    self._comma_()
                    self._polygon_text_body_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _tin_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._triangle_text_body_()
                def block0():
                    self._comma_()
                    self._triangle_text_body_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _geometrycollection_text_(self):
        with self._choice():
            with self._option():
                self._empty_set_()
            with self._option():
                self._left_paren_()
                self._well_known_text_representation_()
                def block0():
                    self._comma_()
                    self._well_known_text_representation_()
                self._closure(block0)
                self._right_paren_()
            self._error('no available options')

    @rule_def
    def _empty_set_(self):
        self._token('EMPTY')

    @rule_def
    def _z_m_(self):
        with self._choice():
            with self._option():
                self._token('ZM')
            with self._option():
                self._token('Z')
            with self._option():
                self._token('M')
            self._error('expecting one of: Z ZM M')

    @rule_def
    def _left_paren_(self):
        self._token('(')

    @rule_def
    def _right_paren_(self):
        self._token(')')

    @rule_def
    def _number_(self):
        self._pattern(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')

    @rule_def
    def _comma_(self):
        self._token(',')



class WktSemanticParser(CheckSemanticsMixin, WktParser):
    pass


class WktSemantics(object):
    def well_known_text_representation(self, ast):
        return ast

    def point_text_representation(self, ast):
        return ast

    def curve_text_representation(self, ast):
        return ast

    def linestring_text_representation(self, ast):
        return ast

    def circularstring_text_representation(self, ast):
        return ast

    def compoundcurve_text_representation(self, ast):
        return ast

    def surface_text_representation(self, ast):
        return ast

    def curvepolygon_text_representation(self, ast):
        return ast

    def polygon_text_representation(self, ast):
        return ast

    def triangle_text_representation(self, ast):
        return ast

    def collection_text_representation(self, ast):
        return ast

    def multipoint_text_representation(self, ast):
        return ast

    def multicurve_text_representation(self, ast):
        return ast

    def multilinestring_text_representation(self, ast):
        return ast

    def multisurface_text_representation(self, ast):
        return ast

    def multipolygon_text_representation(self, ast):
        return ast

    def polyhedralsurface_text_representation(self, ast):
        return ast

    def tin_text_representation(self, ast):
        return ast

    def geometrycollection_text_representation(self, ast):
        return ast

    def linestring_text_body(self, ast):
        return ast

    def curvepolygon_text_body(self, ast):
        return ast

    def polygon_text_body(self, ast):
        return ast

    def triangle_text_body(self, ast):
        return ast

    def point_text(self, ast):
        return ast

    def point(self, ast):
        return ast

    def x(self, ast):
        return ast

    def y(self, ast):
        return ast

    def z(self, ast):
        return ast

    def m(self, ast):
        return ast

    def linestring_text(self, ast):
        return ast

    def circularstring_text(self, ast):
        return ast

    def compoundcurve_text(self, ast):
        return ast

    def single_curve_text(self, ast):
        return ast

    def curve_text(self, ast):
        return ast

    def ring_text(self, ast):
        return ast

    def surface_text(self, ast):
        return ast

    def curvepolygon_text(self, ast):
        return ast

    def polygon_text(self, ast):
        return ast

    def triangle_text(self, ast):
        return ast

    def multipoint_text(self, ast):
        return ast

    def multicurve_text(self, ast):
        return ast

    def multilinestring_text(self, ast):
        return ast

    def multisurface_text(self, ast):
        return ast

    def multipolygon_text(self, ast):
        return ast

    def polyhedralsurface_text(self, ast):
        return ast

    def tin_text(self, ast):
        return ast

    def geometrycollection_text(self, ast):
        return ast

    def empty_set(self, ast):
        return ast

    def z_m(self, ast):
        return ast

    def left_paren(self, ast):
        return ast

    def right_paren(self, ast):
        return ast

    def number(self, ast):
        return ast

    def comma(self, ast):
        return ast

def main(filename, startrule, trace=False):
    import json
    with open(filename) as f:
        text = f.read()
    parser = WktParser(parseinfo=False)
    ast = parser.parse(text, startrule, filename=filename, trace=trace)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import sys
    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in WktParser.rule_list():
                print(r)
            print()
            sys.exit(0)
    parser = argparse.ArgumentParser(description="Simple parser for Wkt.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(args.file, args.startrule, trace=args.trace)
