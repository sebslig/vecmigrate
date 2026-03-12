import logging
from typing import List, Optional
from vecmigrate.adapters.base import BaseAdapter
from vecmigrate.models import VectorRecord
from vecmigrate.agents.validator import IntegrityAgent

logger = logging.getLogger(__name__)

class MigrationEngine:
    """Core engine responsible for orchestrating the migration process."""
    
    def __init__(self, source: BaseAdapter, target: BaseAdapter, use_agents: bool = True):
        self.source = source
        self.target = target
        self.agent = IntegrityAgent() if use_agents else None

    def migrate(self, batch_size: int = 100, limit: Optional[int] = None):
        """Executes the migration logic."""
        logger.info(f"Starting migration from {type(self.source).__name__} to {type(self.target).__name__}")
        
        offset = 0
        total_migrated = 0
        
        while True:
            records = self.source.fetch_batch(batch_size=batch_size, offset=offset)
            if not records:
                break
                
            self.target.upsert_batch(records)
            
            if self.agent:
                self.agent.verify_batch(records, self.target)
                
            total_migrated += len(records)
            offset += batch_size
            
            logger.info(f"Migrated {total_migrated} records...")
            
            if limit and total_migrated >= limit:
                break
                
        logger.info("Migration completed successfully.")
        return total_migrated
