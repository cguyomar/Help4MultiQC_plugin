#!/usr/bin/env python
""" MultiQC example plugin functions

We can add any custom Python functions here and call them
using the setuptools plugin hooks.
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import report, util_functions, config

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

# Save this plugin's version number (defined in setup.py) to the MultiQC config
config.help4multiqc_plugin_version = get_distribution("multiqc_help4multiqc_plugin").version


# Add default config options for the things that are used in MultiQC_NGI
def help4multiqc_plugin_execution_start():
    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_plugin', True):
        return None

    log.info("Running Help4MultiQC Plugin v{}".format(config.example_plugin_version))

def help4multiqc_plugin_after_modules():
    log.info("Loading the custom help")
    config_file = config.kwargs.get('help4multiqc_config')

    # Loading the custom help
    help_overload_dict = dict()
    with open(config_file) as help_conf:
        for i,line in enumerate(help_conf):
            if i==0:
                continue
            line = line.split("\t")
            if line[0] not in help_overload_dict.keys():
                help_overload_dict[line[0]] = dict()
            help_overload_dict[line[0]][line[1]] = line[2]

    # Changing the help text
    for module in report.modules_output:
        if module.name in help_overload_dict.keys():
            log.info("Found alternative help text for module : " + module.name)
            for section in module.sections:
                if section["name"] in help_overload_dict[module.name].keys():
                    log.info("Section : " + section["name"])
                    section['helptext'] = help_overload_dict[module.name][section["name"]]

