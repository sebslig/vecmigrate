from abc import ABC, abstractmethod
from typing import List
from vecmigrate.models import VectorRecord

class BaseAdapter(ABC):
    """Abstract base class for all vector database adapters."""
    
    @abstractmethod
    def fetch_batch(self, batch_size: int, offset: int) -> List[VectorRecord]:
        """Fetch a batch of records from the source."""
        pass
        
    @abstractmethod
    def upsert_batch(self, records: List[VectorRecord]) -> bool:
        """Upsert a batch of records into the target."""
        pass

    @abstractmethod
    def get_count(self) -> int:
        """Return total count of vectors in the store."""
        pass
