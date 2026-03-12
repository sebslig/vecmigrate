from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class VectorRecord:
    """Standardized representation of a vector record."""
    id: str
    vector: List[float]
    metadata: Dict[str, Any] = field(default_factory=dict)
    namespace: Optional[str] = None

@dataclass
class MigrationStats:
    """Stats for a migration run."""
    total_records: int
    success_count: int
    failure_count: int
    duration_seconds: float
