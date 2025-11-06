from abc import ABC, abstractmethod
from patterns.modeling.entity.model import Batch


# Port(interface)
class AbstractRepository(ABC):

    @abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError

# Adapter(implementation)
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def add(self, batch):
        self.session.add(batch)
    
    def get(self, reference):
        return self.session.query(Batch).filter_by(reference=reference)

# Adapter(implementation)
class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)
    
    def add(self, batch):
        self._batches.add(batch)
    
    def get(self, reference):
        return next(
            b for b in self._batches
            if b.reference == reference
        )
    
    def list(self):
        return list(self._batches)