from Products.Five import BrowserView
from Products.CMFPlone.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner
from DateTime import DateTime

from zope.i18nmessageid import MessageFactory
from Products.CMFPlone import PloneMessageFactory as PMF
_ = MessageFactory('simpleTask')

class myTasksView(BrowserView):
    
    template = ViewPageTemplateFile('mytasks.pt')

    def statesAvaliable(self):
        return ('inprogress','draft','completed')
    
    def tasksByState(self, state):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        membership = getToolByName(context, 'portal_membership')
        user = membership.getAuthenticatedMember().getId()

        return catalog(portal_type='simpleTask',
                       getTaskOwner=user,
                       review_state=state,
                       sort_on='getEndby')

    def getViewFields(self):
        return (_(u'Title'), _(u'Creator'),_(u'getPriority'), _(u'getPercentCompleted'),_(u'getStartby'), _(u'getEndby'), _(u'getTaskOwner'))

    def test(self, value, trueVal, falseVal):
        """
            helper method, mainly for setting html attributes.
        """
        if value:
            return trueVal
        else:
            return falseVal

    def isDue(self, taskDate):
        return taskDate < DateTime()