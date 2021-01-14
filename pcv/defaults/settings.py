FILENAME = 'cv.html'
JSON_FILES = ['template.json']

TEMPLATE_FOLDERS = []  # relative to the "source" folder
PAGES = ['onepage.html', 'technologies.html', 'publications.html']
STYLES = ['style_pages.css', 'style_zero.css']

BACKGROUND_COLOR = '#438496'
FONT_COLOR = 'white'

SECTIONS = dict(technologies=dict(level=2, priority=2, exclude=[]),
                skills=dict(level=3, priority=1, source='technologies'))
