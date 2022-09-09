#!/usr/bin/env python
"""
Help4multiqc plugin for MultiQC

For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'multiqc_help4multiqc_plugin',
    version = version,
    author = 'Cervin Guyomar',
    author_email = 'cervin.guyomar@inrae.fr',
    description = "Help4MultiQC plugin",
    long_description = __doc__,
    keywords = 'bioinformatics',
    url = '',
    download_url = '',
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'multiqc'
    ],
    entry_points = {
        'multiqc.cli_options.v1': [
            'disable_plugin = help4multiqc_plugin.cli:disable_plugin',
            'help4multiqc_config = help4multiqc_plugin.cli:config_file'
        ],
        'multiqc.hooks.v1': [
            'execution_start = help4multiqc_plugin.help4MultiQC:help4multiqc_plugin_execution_start',
            'after_modules = help4multiqc_plugin.help4MultiQC:help4multiqc_plugin_after_modules'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
