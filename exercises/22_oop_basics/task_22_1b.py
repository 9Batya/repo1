from pprint import pprint
import logging
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
    def _normalize(self, topology_dict):
        return {
            min(local, remote): max(local, remote)
            for local, remote in topology_dict.items()
        }
    def delete_link(self, *args):
        links = list(args)
        for link in links:
            if link in self.topology.keys():
                if self.topology.get(self.topology.get(link)) == link:
                    self.topology.pop(self.topology.get(link))
                self.topology.pop(link)
            else:
                print('Такого соединения нет')




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
    T.delete_link(('R1', 'Eth0/0'), ('R1', 'Eth0/0'))
    pprint(T.topology)