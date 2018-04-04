import base64
import logging
import os
from operator import itemgetter
from urlparse import urljoin

import jinja2
from babel.support import Translations

import ckan.lib.jobs as jobs
from ckan.common import c
from ckan.lib.base import BaseController, abort
from ckan.lib.helpers import flash_success, flash_error, get_page_number, full_current_url
from ckan.model import User
from ckan.plugins import toolkit as tk

log = logging.getLogger(__name__)


class FilesController(BaseController):
    paginated_by = 3

    def index(self):
        print 'OK'
        context = {
            'files_list': [1, 2, 3, 4, 5],
            'total_pages': 1
        }
        return tk.render('files_index.html', context)

