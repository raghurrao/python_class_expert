# Day 9: Mock Telemetry Logger Application

class TelemetryLogger:
    def __init__(self):
        self.events = []
        self.active_session = False

    def start_session(self):
        """Starts a telemetry capture session."""
        self.active_session = True
        self.events.append("session_started")

    def end_session(self):
        """Ends the telemetry capture session."""
        self.active_session = False
        self.events.append("session_ended")

    def log_event(self, event_name):
        """Logs a single event. Raises RuntimeError if active_session is False."""
        if not self.active_session:
            raise RuntimeError("No active telemetry session")
        self.events.append(event_name)
