from zope.interface import Interface

from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone.utils import getToolByName
from Acquisition import aq_inner
from DateTime import DateTime
from zope.component import getMultiAdapter

from zope.i18nmessageid import MessageFactory
from Products.CMFPlone import PloneMessageFactory as PMF
_ = MessageFactory('simpleTask')

class IsimpleTaskPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    # TODO: Add any zope.schema fields here to capture portlet configuration
    # information. Alternatively, if there are no settings, leave this as an
    # empty interface - see also notes around the add form and edit form
    # below.

    # some_field = schema.TextLine(title=_(u"Some field"),
    #                              description=_(u"A field to use"),
    #                              required=True)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IsimpleTaskPortlet)

    # TODO: Set default values for the configurable parameters here

    # some_field = u""

    # TODO: Add keyword parameters for configurable parameters here
    # def __init__(self, some_field=u""):
    #    self.some_field = some_field

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return PMF(u"Tasks portlet")

class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('simpletaskportlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.portal_url = portal_state.portal_url()
        self.portal = portal_state.portal()

    def mytasks(self):
        return self._data()
    
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        membership = getToolByName(context, 'portal_membership')
        user = membership.getAuthenticatedMember().getId()

        return catalog(portal_type='simpleTask',
                       getTaskOwner=user,
                       review_state='inprogress',
                       sort_on='getEndby')[:5]

    def isDue(self, taskDate):
        return taskDate < DateTime()

    def test(self, value, trueVal, falseVal):
        """
            helper method, mainly for setting html attributes.
        """
        if value:
            return trueVal
        else:
            return falseVal

    def all_my_tasks_link(self):
            return '%s/lesmevestasques' % self.portal_url

# NOTE: If this portlet does not have any configurable parameters, you can
# inherit from NullAddForm and remove the form_fields variable.

class AddForm(base.NullAddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IsimpleTaskPortlet)

    def create(self):
        return Assignment()

# NOTE: IF this portlet does not have any configurable parameters, you can
# remove this class definition and delete the editview attribute from the
# <plone:portlet /> registration in configure.zcml

#class EditForm(base.EditForm):
#    """Portlet edit form.
#
#    This is registered with configure.zcml. The form_fields variable tells
#    zope.formlib which fields to display.
#    """
#    form_fields = form.Fields(IsimpleTaskPortlet)