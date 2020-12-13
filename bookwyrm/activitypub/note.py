''' note serializer and children thereof '''
from dataclasses import dataclass, field
from typing import Dict, List

from .base_activity import ActivityObject, Link
from .image import Image

@dataclass(init=False)
class Tombstone(ActivityObject):
    ''' the placeholder for a deleted status '''
    published: str
    deleted: str
    type: str = 'Tombstone'


@dataclass(init=False)
class Note(ActivityObject):
    ''' Note activity '''
    published: str
    attributedTo: str
    content: str
    to: List[str] = field(default_factory=lambda: [])
    cc: List[str] = field(default_factory=lambda: [])
    replies: Dict = field(default_factory=lambda: {})
    inReplyTo: str = ''
    summary: str = ''
    tag: List[Link] = field(default_factory=lambda: [])
    attachment: List[Image] = field(default_factory=lambda: [])
    sensitive: bool = False
    type: str = 'Note'


@dataclass(init=False)
class Article(Note):
    ''' what's an article except a note with more fields '''
    name: str
    type: str = 'Article'


@dataclass(init=False)
class GeneratedNote(Note):
    ''' just a re-typed note '''
    type: str = 'GeneratedNote'


@dataclass(init=False)
class Comment(Note):
    ''' like a note but with a book '''
    inReplyToBook: str
    type: str = 'Comment'


@dataclass(init=False)
class Review(Comment):
    ''' a full book review '''
    name: str
    rating: int
    type: str = 'Review'


@dataclass(init=False)
class Quotation(Comment):
    ''' a quote and commentary on a book '''
    quote: str
    type: str = 'Quotation'
