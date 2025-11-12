import random


class MetricsClient:
    """3rd party metrics transfer client"""

    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError("expected type str for metric_name")
        
        if not isinstance(metric_value, str):
            raise TypeError("expected type str for metric_value")


class WrappedClient:
    def __init__(self):
        self.client = MetricsClient()
    
    def send(self, metric_name, metric_value):
        return self.client.send(str(metric_name), str(metric_value))
    

class Process:
    def __init__(self):
        self.client = MetricsClient()
    
    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send(f"iteration.{i}", result)
    
    def run_process(self):
        return random.randint(1, 100)