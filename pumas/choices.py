CATEGORY = (
    ('book', 'book'),
    ('journal', 'journal'),
    ('undergradute-project', 'undergradute-project'),
    ('gradute-project', 'gradute-project'),
    ('articles', 'articles'),
    ('conference-preceeding', 'conference-preceeding'),
    ('book-chapter', 'book-chapter'),
    ('technical-report', 'technical-report'),
    ('dessertation', 'dessertation'),
    ('thesis', 'thesis'),
    ('project-document', 'project-document')
)


DOCUMENT_TYPES = [
    ['----', '-----'],
    ["<a href='{% url 'admin:pumas_document_add' %}'>Upload Document</a>", 'dessertation'],
    ["<a href='{% url 'admin:pumas_article_add' %}'>Upload Document</a>", 'articles']
]
