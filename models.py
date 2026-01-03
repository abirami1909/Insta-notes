from pydantic import BaseModel
from typing import List, Dict, Optional

class ImportantTerm(BaseModel):
    term: str
    definition: str

class Summary(BaseModel):
    keyPoints: List[str]
    quickRevision: List[str]
    importantTerms: List[ImportantTerm]

class Note(BaseModel):
    id: str
    title: str
    videoUrl: str
    thumbnail: str
    date: str
    subject: str
    summary: Summary

class GenerateNoteRequest(BaseModel):
    videoUrl: str
    language: str
