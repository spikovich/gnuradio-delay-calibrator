import unittest
from examples.sa import sa

class TestExampleFlowgraph(unittest.TestCase):
    def test_flowgraph_runs(self):
        try:
            tb = sa()
            tb.start()
            tb.stop()
            tb.wait()
        except Exception as e:
            self.fail(f"Flowgraph execution failed with error: {e}")

if __name__ == '__main__':
    unittest.main()