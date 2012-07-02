# -*- coding: utf-8 -*-
""" Projy template for a bootstrap project. """

# system
from datetime import date
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector


class BootstrapTemplate(ProjyTemplate):
    """ Projy template for a bootstrap project. """

    def __init__(self):
        self.project_name = None


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ None,
              'bootstrap',
              'BootstrapScriptFileTemplate'
            ],
        ]
        return files_description

