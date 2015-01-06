from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CollectiveDirectoryImportView(BrowserView):
    template = ViewPageTemplateFile('collective_directory_import_view.pt')

    def __call__(self):
        """"""
        self.hello_name = getattr(self.context, 'hello_name', 'World')
        return self.template()