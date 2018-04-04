import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

if toolkit.check_ckan_version(min_version='2.5'):
    from ckan.lib.plugins import DefaultTranslation


    class FilesPluginBase(plugins.SingletonPlugin, DefaultTranslation):
        plugins.implements(plugins.ITranslation, inherit=True)
else:
    class FilesPluginBase(plugins.SingletonPlugin):
        pass


class FilesPlugin(FilesPluginBase):
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IConfigurer, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'uploader')

    def before_map(self, sub_map):
        from ckan.config.routing import SubMapper
        with SubMapper(sub_map, controller='ckanext.files.controllers:FilesController') as m:
            m.connect('files_index', '/files', action='index')
        return sub_map
