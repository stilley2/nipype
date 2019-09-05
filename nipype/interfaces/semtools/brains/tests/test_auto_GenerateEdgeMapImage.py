# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utilities import GenerateEdgeMapImage


def test_GenerateEdgeMapImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputMRVolumes=dict(argstr='--inputMRVolumes %s...', ),
        inputMask=dict(
            argstr='--inputMask %s',
            extensions=None,
        ),
        lowerPercentileMatching=dict(argstr='--lowerPercentileMatching %f', ),
        maximumOutputRange=dict(argstr='--maximumOutputRange %d', ),
        minimumOutputRange=dict(argstr='--minimumOutputRange %d', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputEdgeMap=dict(
            argstr='--outputEdgeMap %s',
            hash_files=False,
        ),
        outputMaximumGradientImage=dict(
            argstr='--outputMaximumGradientImage %s',
            hash_files=False,
        ),
        upperPercentileMatching=dict(argstr='--upperPercentileMatching %f', ),
    )
    inputs = GenerateEdgeMapImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GenerateEdgeMapImage_outputs():
    output_map = dict(
        outputEdgeMap=dict(extensions=None, ),
        outputMaximumGradientImage=dict(extensions=None, ),
    )
    outputs = GenerateEdgeMapImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
