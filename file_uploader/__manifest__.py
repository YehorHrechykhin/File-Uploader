# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
{
    'name': 'File Uploader',
    'version': '16.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Yehor Hrechykhin',
    'license': 'LGPL-3',
    'summary': 'File Uploader',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/file_uploader_views.xml',
        'views/file_uploader_menus.xml',
    ],
    'demo': [
        'demo/file_demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
