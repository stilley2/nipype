# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dwi import FitDwi


def test_FitDwi_inputs():
    input_map = dict(
        acceptance=dict(argstr='-accpetance %f', ),
        args=dict(argstr='%s', ),
        ball_flag=dict(
            argstr='-ball',
            position=4,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'ballv_flag', 'nod_flag',
                'nodv_flag'
            ],
        ),
        ballv_flag=dict(
            argstr='-ballv',
            position=4,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'ball_flag', 'nod_flag',
                'nodv_flag'
            ],
        ),
        bval_file=dict(
            argstr='-bval %s',
            extensions=None,
            mandatory=True,
            position=2,
        ),
        bvec_file=dict(
            argstr='-bvec %s',
            extensions=None,
            mandatory=True,
            position=3,
        ),
        cov_file=dict(
            argstr='-cov %s',
            extensions=None,
        ),
        csf_t2_val=dict(argstr='-csfT2 %f', ),
        diso_val=dict(argstr='-diso %f', ),
        dpr_val=dict(argstr='-dpr %f', ),
        dti_flag=dict(
            argstr='-dti',
            position=4,
            xor=[
                'mono_flag', 'ivim_flag', 'ball_flag', 'ballv_flag',
                'nod_flag', 'nodv_flag'
            ],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        error_file=dict(
            argstr='-error %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_error.nii.gz',
        ),
        famap_file=dict(
            argstr='-famap %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_famap.nii.gz',
        ),
        gn_flag=dict(
            argstr='-gn',
            xor=['wls_flag'],
        ),
        ivim_flag=dict(
            argstr='-ivim',
            position=4,
            xor=[
                'mono_flag', 'dti_flag', 'ball_flag', 'ballv_flag', 'nod_flag',
                'nodv_flag'
            ],
        ),
        lm_vals=dict(
            argstr='-lm %f %f',
            requires=['gn_flag'],
        ),
        mask_file=dict(
            argstr='-mask %s',
            extensions=None,
        ),
        maxit_val=dict(
            argstr='-maxit %d',
            requires=['gn_flag'],
        ),
        mcmap_file=dict(
            argstr='-mcmap %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_mcmap.nii.gz',
            requires=['nodv_flag'],
        ),
        mcmaxit=dict(argstr='-mcmaxit %d', ),
        mcout=dict(
            argstr='-mcout %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_mcout.txt',
        ),
        mcsamples=dict(argstr='-mcsamples %d', ),
        mdmap_file=dict(
            argstr='-mdmap %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_mdmap.nii.gz',
        ),
        mono_flag=dict(
            argstr='-mono',
            position=4,
            xor=[
                'ivim_flag', 'dti_flag', 'ball_flag', 'ballv_flag', 'nod_flag',
                'nodv_flag'
            ],
        ),
        nod_flag=dict(
            argstr='-nod',
            position=4,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'ball_flag',
                'ballv_flag', 'nodv_flag'
            ],
        ),
        nodiff_file=dict(
            argstr='-nodiff %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_no_diff.nii.gz',
        ),
        nodv_flag=dict(
            argstr='-nodv',
            position=4,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'ball_flag',
                'ballv_flag', 'nod_flag'
            ],
        ),
        perf_thr=dict(argstr='-perfthreshold %f', ),
        prior_file=dict(
            argstr='-prior %s',
            extensions=None,
        ),
        res_file=dict(
            argstr='-res %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_resmap.nii.gz',
        ),
        rgbmap_file=dict(
            argstr='-rgbmap %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_rgbmap.nii.gz',
            requires=['dti_flag'],
        ),
        rot_sform_flag=dict(argstr='-rotsform %d', ),
        slice_no=dict(argstr='-slice %d', ),
        source_file=dict(
            argstr='-source %s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        swls_val=dict(argstr='-swls %f', ),
        syn_file=dict(
            argstr='-syn %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_syn.nii.gz',
        ),
        te_file=dict(
            argstr='-TE %s',
            extensions=None,
            xor=['te_file'],
        ),
        te_value=dict(
            argstr='-TE %s',
            extensions=None,
            xor=['te_file'],
        ),
        ten_type=dict(usedefault=True, ),
        tenmap2_file=dict(
            argstr='-tenmap2 %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_tenmap2.nii.gz',
            requires=['dti_flag'],
        ),
        tenmap_file=dict(
            argstr='-tenmap %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_tenmap.nii.gz',
            requires=['dti_flag'],
        ),
        v1map_file=dict(
            argstr='-v1map %s',
            extensions=None,
            name_source=['source_file'],
            name_template='%s_v1map.nii.gz',
        ),
        vb_flag=dict(argstr='-vb', ),
        voxel=dict(argstr='-voxel %d %d %d', ),
        wls_flag=dict(
            argstr='-wls',
            xor=['gn_flag'],
        ),
        wm_t2_val=dict(argstr='-wmT2 %f', ),
    )
    inputs = FitDwi.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FitDwi_outputs():
    output_map = dict(
        error_file=dict(extensions=None, ),
        famap_file=dict(extensions=None, ),
        mcmap_file=dict(extensions=None, ),
        mcout=dict(extensions=None, ),
        mdmap_file=dict(extensions=None, ),
        nodiff_file=dict(extensions=None, ),
        res_file=dict(extensions=None, ),
        rgbmap_file=dict(extensions=None, ),
        syn_file=dict(extensions=None, ),
        tenmap2_file=dict(extensions=None, ),
        tenmap_file=dict(extensions=None, ),
        v1map_file=dict(extensions=None, ),
    )
    outputs = FitDwi.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
