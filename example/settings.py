FILENAME = 'cv.html'
JSON_FILES = ['cv.json', 'technologies.json']

TEMPLATE_FOLDERS = ['templates']  # relative to "source"
PAGES = ['onepage.html', 'technologies.html', 'custom_publications.html']
STYLES = ['style_pages.css', 'style_zero.css']

THEME_COLOR = '#438496'
THEME_FONT_COLOR = 'white'

SECTIONS = dict(education=dict(priority=2),
                languages=dict(level=4),
                technologies=dict(level=1, priority=2),
                skills=dict(level=3, priority=1, source='technologies',
                            exclude=['windows', 'pycharm', 'bitbucket', 'pip']))
