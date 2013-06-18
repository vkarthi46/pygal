# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2013 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Charts styling
"""
from __future__ import division
from pygal.util import cycle_fill
from colorsys import rgb_to_hls, hls_to_rgb


def darken(color, percent):
    assert color[0] == '#', '#rrggbb and #rgb format are supported'
    color = color[1:]
    assert len(color) in (3, 6), '#rrggbb and #rgb format are supported'
    if len(color) == 3:
        color = [a for b in zip(color, color) for a in b]

    return '#%02x%02x%02x' % tuple(
        map(lambda x: 255 * x,
            hls_to_rgb(*(
                lambda h, l, s: (h, max(0, min(1, l - percent / 100)), s))(
                    *rgb_to_hls(*map(
                        lambda x: int(''.join(x), 16) / 255,
                        zip(color[::2], color[1::2])))
                ))))


def lighten(color, percent):
    return darken(color, -percent)


class Style(object):
    """Styling class containing colors for the css generation"""
    def __init__(
            self,
            background='black',
            plot_background='#111',
            foreground='#999',
            foreground_light='#eee',
            foreground_dark='#555',
            opacity='.8',
            opacity_hover='.9',
            transition='250ms',
            colors=(
                '#ff5995', '#b6e354', '#feed6c', '#8cedff', '#9e6ffe',
                '#899ca1', '#f8f8f2', '#bf4646', '#516083', '#f92672',
                '#82b414', '#fd971f', '#56c2d6', '#808384', '#8c54fe',
                '#465457')):
        self.background = background
        self.plot_background = plot_background
        self.foreground = foreground
        self.foreground_light = foreground_light
        self.foreground_dark = foreground_dark
        self.opacity = opacity
        self.opacity_hover = opacity_hover
        self.transition = transition
        self._colors = colors

    @property
    def colors(self):
        """Get the css color list"""

        def color(tupl):
            """Make a color css"""
            return (
                '.color-{0} {{\n'
                '  stroke: {1};\n'
                '  fill: {1};\n'
                '}}\n'.format(*tupl))
        return '\n'.join(map(color, enumerate(cycle_fill(self._colors, 16))))

    def to_dict(self):
        config = {}
        for attr in dir(self):
            if not attr.startswith('__'):
                value = getattr(self, attr)
                if not hasattr(value, '__call__'):
                    config[attr] = value
        return config


DefaultStyle = Style(opacity_hover='.4', opacity='.8')
LightStyle = Style(
    background='white',
    plot_background='rgba(0, 0, 255, 0.1)',
    foreground='rgba(0, 0, 0, 0.7)',
    foreground_light='rgba(0, 0, 0, 0.9)',
    foreground_dark='rgba(0, 0, 0, 0.5)',
    colors=('#242424', '#9f6767', '#92ac68',
            '#d0d293', '#9aacc3', '#bb77a4',
            '#77bbb5', '#777777'))
NeonStyle = Style(
    opacity='.1',
    opacity_hover='.75',
    transition='1s ease-out')
CleanStyle = Style(
    background='transparent',
    plot_background='rgba(240, 240, 240, 0.7)',
    foreground='rgba(0, 0, 0, 0.9)',
    foreground_light='rgba(0, 0, 0, 0.9)',
    foreground_dark='rgba(0, 0, 0, 0.5)',
    colors=(
        'rgb(12,55,149)', 'rgb(117,38,65)', 'rgb(228,127,0)', 'rgb(159,170,0)',
        'rgb(149,12,12)'))

solarized_colors = (
    '#b58900', '#cb4b16', '#dc322f', '#d33682',
    '#6c71c4', '#268bd2', '#2aa198', '#859900')

DarkSolarizedStyle = Style(
    background='#073642',
    plot_background='#002b36',
    foreground='#839496',
    foreground_light='#fdf6e3',
    foreground_dark='#657b83',
    opacity='.66',
    opacity_hover='.9',
    transition='500ms ease-in',
    colors=solarized_colors)

LightSolarizedStyle = Style(
    background='#fdf6e3',
    plot_background='#eee8d5',
    foreground='#657b83',
    foreground_light='#073642',
    foreground_dark='#073642',
    opacity='.6',
    opacity_hover='.9',
    transition='500ms ease-in',
    colors=solarized_colors)

AnaeleStyle = Style(
    background='#c3c4c6',
    plot_background='#e6e7e9',
    foreground='rgba(0, 0, 0, 0.9)',
    foreground_light='rgba(0, 0, 0, 0.9)',
    foreground_dark='rgba(0, 0, 0, 0.5)',
    opacity='.6',
    opacity_hover='.9',
    colors=(
        '#d94e4c', '#e5884f', '#39929a', '#3c6368',
        '#b73a3b', '#b73a3b', '#b73a3b', '#234547'))


DarkColorizedStyle = Style(
    background='#3a2d3f',
    plot_background='#4c3c53',
    foreground='rgba(255, 255, 255, 0.9)',
    foreground_light='rgba(255, 255, 255, 0.9)',
    foreground_dark='rgba(255, 255, 255, 0.5)',
    opacity='.6',
    opacity_hover='.9',
    colors=(
        '#02b8ff', '#d801ff'))

styles = {'default': DefaultStyle,
          'light': LightStyle,
          'neon': NeonStyle,
          'clean': CleanStyle,
          'anaele': AnaeleStyle,
          'dark_solarized': DarkSolarizedStyle,
          'light_solarized': LightSolarizedStyle,
          'dark_colorized': DarkColorizedStyle }
