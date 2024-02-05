from pprint import pprint
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")

    def delete_node(self, node):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node in src or node in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")

    def add_link(self, *ports, existing_port = False):
        link1 = (ports[0], ports[1])
        for item in self.topology.items():
            if (ports[0] or ports[1]) in item:
                existing_port = True
        if link1 in self.topology.items():
            print('Такое соединение существует')
        elif existing_port == True:
            print('Соединение с одним из портов существует')
        else:
            self.topology.update({ports[0]: ports[1]})

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

if __name__ == "__main__":
    T = Topology(topology_example)
    pprint(T.topology)
    T.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    T.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    T.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    pprint(T.topology)