
from django_opensearch_dsl import Document
from django_opensearch_dsl.registries import registry
from .models import Book, Review


@registry.register_document
class BookDocument(Document):
    class Index:
        # Nombre del índice en Elasticsearch
        name = 'books'
        settings = {  # See Opensearch Indices API reference for available settings
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Book  # El modelo asociado a este documento
        fields = [
            'name',
            'summary',
            'date_of_publication',
        ]

@registry.register_document
class ReviewDocument(Document):
    class Index:
        # Nombre del índice en Elasticsearch
        name = 'reviews'
        settings = {  # See Opensearch Indices API reference for available settings
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Review  # El modelo asociado a este documento
        fields = [
            'review',
            'score',
        ]