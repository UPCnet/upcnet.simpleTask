from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five import BrowserView

class SimpleTaskView(BrowserView):
    
    template = ViewPageTemplateFile('simpleTask_view.pt')

    def __call__(self):    
        
        return self.template()