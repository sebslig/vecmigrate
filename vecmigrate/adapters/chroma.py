import chromadb
from typing import List
from vecmigrate.adapters.base import BaseAdapter
from vecmigrate.models import VectorRecord

class ChromaAdapter(BaseAdapter):
    def __init__(self, path: str, collection_name: str):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def fetch_batch(self, batch_size: int, offset: int) -> List[VectorRecord]:
        results = self.collection.get(
            limit=batch_size,
            offset=offset,
            include=["embeddings", "metadatas"]
        )
        
        records = []
        for i in range(len(results["ids"])):
            records.append(VectorRecord(
                id=results["ids"][i],
                vector=results["embeddings"][i],
                metadata=results["metadatas"][i]
            ))
        return records

    def upsert_batch(self, records: List[VectorRecord]) -> bool:
        self.collection.upsert(
            ids=[r.id for r in records],
            embeddings=[r.vector for r in records],
            metadatas=[r.metadata for r in records]
        )
        return True

    def get_count(self) -> int:
        return self.collection.count()
