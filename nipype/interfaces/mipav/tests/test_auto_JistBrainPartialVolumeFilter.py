# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistBrainPartialVolumeFilter


def test_JistBrainPartialVolumeFilter_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inInput=dict(
            argstr='--inInput %s',
            extensions=None,
        ),
        inPV=dict(argstr='--inPV %s', ),
        inoutput=dict(argstr='--inoutput %s', ),
        null=dict(argstr='--null %s', ),
        outPartial=dict(
            argstr='--outPartial %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = JistBrainPartialVolumeFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_JistBrainPartialVolumeFilter_outputs():
    output_map = dict(outPartial=dict(extensions=None, ), )
    outputs = JistBrainPartialVolumeFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
