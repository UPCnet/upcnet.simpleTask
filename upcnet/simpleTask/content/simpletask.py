# -*- coding: utf-8 -*-
#
# File: simpleTask.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0-beta11
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.ATContentTypes.content.document import ATDocument
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFPlone.utils import getToolByName
from upcnet.simpleTask.config import *

from DateTime import DateTime


schema = Schema((

    DateTimeField(
        name='startby',
        required=True,
        searchable=False,
        accessor='getStartby',
        default_method=DateTime,
        widget=DateTimeField._properties['widget'](
            label='Startby',
            label_msgid='simpleTask_label_startby',
            i18n_domain='upcnet.simpleTask',
        ),
    ),
    DateTimeField(
        name='endby',
        required=True,
        searchable=False,
        accessor='getEndby',
        default_method=DateTime,
        widget=DateTimeField._properties['widget'](
            label='Endby',
            label_msgid='simpleTask_label_endby',
            i18n_domain='upcnet.simpleTask',
        ),
    ),
    StringField(
        name='priority',
        widget=SelectionWidget(
            label='Priority',
            label_msgid='simpleTask_label_priority',
            i18n_domain='upcnet.simpleTask',
        ),
        default="medium",
        vocabulary=["high","medium","low"],
    ),
    IntegerField(
        name='percentCompleted',
        widget=IntegerField._properties['widget'](
            label='Percentcompleted',
            label_msgid='simpleTask_label_percentCompleted',
            i18n_domain='upcnet.simpleTask',
        ),
        default=0,
    ),
    StringField(
        name='taskOwner',
        widget=StringField._properties['widget'](
            label='Taskowner',
            label_msgid='simpleTask_label_taskOwner',
            i18n_domain='upcnet.simpleTask',
        ),
        default_method='getUserAuth',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

simpleTask_schema = getattr(ATDocument, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here

##/code-section after-schema

class simpleTask(ATDocument):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IsimpleTask)

    meta_type = 'simpleTask'
    _at_rename_after_creation = True

    schema = simpleTask_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def getUserAuth(self):
        membership = getToolByName(self, 'portal_membership')
        return membership.getAuthenticatedMember().getId()


registerType(simpleTask, PROJECTNAME)
# end of class simpleTask

##code-section module-footer #fill in your manual code here
##/code-section module-footer



