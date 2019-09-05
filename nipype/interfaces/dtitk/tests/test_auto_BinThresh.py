# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import BinThresh


def test_BinThresh_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=0,
        ),
        inside_value=dict(
            argstr='%g',
            mandatory=True,
            position=4,
            usedefault=True,
        ),
        lower_bound=dict(
            argstr='%g',
            mandatory=True,
            position=2,
            usedefault=True,
        ),
        out_file=dict(
            argstr='%s',
            extensions=None,
            keep_extension=True,
            name_source='in_file',
            name_template='%s_thrbin',
            position=1,
        ),
        outside_value=dict(
            argstr='%g',
            mandatory=True,
            position=5,
            usedefault=True,
        ),
        upper_bound=dict(
            argstr='%g',
            mandatory=True,
            position=3,
            usedefault=True,
        ),
    )
    inputs = BinThresh.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BinThresh_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = BinThresh.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
