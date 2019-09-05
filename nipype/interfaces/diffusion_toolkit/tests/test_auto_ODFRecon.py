# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..odf import ODFRecon


def test_ODFRecon_inputs():
    input_map = dict(
        DWI=dict(
            argstr='%s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        args=dict(argstr='%s', ),
        dsi=dict(argstr='-dsi', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        filter=dict(argstr='-f', ),
        image_orientation_vectors=dict(argstr='-iop %f', ),
        matrix=dict(
            argstr='-mat %s',
            extensions=None,
            mandatory=True,
        ),
        n_b0=dict(
            argstr='-b0 %s',
            mandatory=True,
        ),
        n_directions=dict(
            argstr='%s',
            mandatory=True,
            position=2,
        ),
        n_output_directions=dict(
            argstr='%s',
            mandatory=True,
            position=3,
        ),
        oblique_correction=dict(argstr='-oc', ),
        out_prefix=dict(
            argstr='%s',
            position=4,
            usedefault=True,
        ),
        output_entropy=dict(argstr='-oe', ),
        output_type=dict(
            argstr='-ot %s',
            usedefault=True,
        ),
        sharpness=dict(argstr='-s %f', ),
        subtract_background=dict(argstr='-bg', ),
    )
    inputs = ODFRecon.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ODFRecon_outputs():
    output_map = dict(
        B0=dict(extensions=None, ),
        DWI=dict(extensions=None, ),
        ODF=dict(extensions=None, ),
        entropy=dict(extensions=None, ),
        max=dict(extensions=None, ),
    )
    outputs = ODFRecon.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
