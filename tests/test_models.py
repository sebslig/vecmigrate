import unittest
from vecmigrate.models import VectorRecord

class TestModels(unittest.TestCase):
    def test_vector_record_creation(self):
        record = VectorRecord(id="1", vector=[0.1, 0.2], metadata={"key": "val"})
        self.assertEqual(record.id, "1")
        self.assertEqual(len(record.vector), 2)
        self.assertEqual(record.metadata["key"], "val")

if __name__ == "__main__":
    unittest.main()
