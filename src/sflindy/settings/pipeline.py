# -*- coding: utf-8 -*-
from __future__ import absolute_import

PIPELINE_COMPILERS = (
    'react.utils.pipeline.JSXCompiler',
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_SASS_BINARY = '/usr/bin/env sassc'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'djangobower.finders.BowerFinder',
)

PIPELINE_CSS = {
    'ninetwenty': {
        'source_filenames': (
            'sass/*.sass',
        ),
        'output_filename': 'css/ninetwenty.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'jsx': {
        'source_filenames': (
            'jsx/*.jsx',
        ),
        'output_filename': 'js/app.js',
    }
}
