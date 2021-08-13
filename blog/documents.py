from elasticsearch_dsl import analyzer

from django_elasticsearch_dsl import Document, Index, fields

from .models import Post

post_index = Index('posts')
post_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@post_index.doc_type
class PostDocument(Document):
    """Post elasticsearch document"""

    id = fields.IntegerField(attr='id')
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    content = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    created_at = fields.DateField()
    updated_at = fields.DateField()

    class Django:
        model = Post
