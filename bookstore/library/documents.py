from django_opensearch_dsl import Document, fields
from django_opensearch_dsl.registries import registry
from .models import Book


@registry.register_document
class BookDocument(Document):
    author = fields.NestedField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })

    class Index:
        name = 'books'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Book
        fields = [
            'name',
            'summary',
            'date_of_publication',
            'number_of_sales',
        ]