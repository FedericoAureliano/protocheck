class PEvent:
    payload = ""

    def __init__(self, payload):
        self.payload = payload


class Pmachine:
    var = []
    creates = []
    sends = []
    receives = []
    name = ""
    goto_payload = ""

    def __init__(self, name):
        self.name = name

    def try_send_event(self, target, event):
        self.sends.append((target, event))

    def try_receive_event(self, events):
        self.receives.extend(events)

    def try_goto_state(self, payload):
        self.goto_payload = payload

    def add_var(self, var):
        self.var.append(var)


class PModel:
    machines = []
    events = []

    def add_machine(self, machine):
        self.machines.append(machine)

    def get_machine(self, machine_name):
        for m in self.machines:
            if m.name == machine_name:
                return m

    def add_event(self, event):
        self.events.append(event)
