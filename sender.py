import time
from receiver import ReceiverProcess, RDTReceiver


class SenderProcess:
    """ Represent the sender process in the application layer """

    __buffer = list()

    @staticmethod
    def set_outgoing_data(buffer):
        """ To set the message the process would send out over the network
        :param buffer: a python list of characters represent the outgoing message
        :return: no return value
        """
        SenderProcess.__buffer = buffer

    @staticmethod
    def get_outgoing_data():
        """ To get the message the process would send out over the network
        :return: a python list of characters represent the outgoing message
        """
        return SenderProcess.__buffer


class RDTSender:
    """ Implement the Reliable Data Transfer Protocol V2.2 Sender Side """

    def __init__(self, net_srv):
        """ This is a class constructor
        It initializes the RDT sender sequence number to '0' and the network layer services
        The network layer service provides the method udt_send(send_pkt)
        """
        self.sequence = '0'
        self.net_srv = net_srv
        

    @staticmethod
    def get_checksum(data):
        return ord(data)

    @staticmethod
    def clone_packet(packet):
        """ Make a copy of the outgoing packet
        :param packet: a python dictionary representing a packet
        :return: return a packet as a python dictionary
        """
        pkt_clone = {
            'sequence_number': packet['sequence_number'],
            'data': packet['data'],
            'checksum': packet['checksum']
        }
        return pkt_clone

    @staticmethod
    def is_corrupted(reply):
        """ Check if the received reply from the receiver is corrupted or not
        :param reply: a python dictionary representing a reply sent by the receiver
        :return: True -> if the reply is corrupted | False -> if the reply is NOT corrupted
        """        
        expected_checksum = RDTSender.get_checksum(reply['ack'])
        return reply['checksum'] != expected_checksum

    @staticmethod
    def is_expected_seq(reply, exp_seq):
        """ Check if the received reply from the receiver has the expected sequence number
        :param reply: a python dictionary representing a reply sent by the receiver
        :param exp_seq: the sender expected sequence number '0' or '1' represented as a character
        :return: True -> if ack in the reply matches the expected sequence number otherwise False
        """
        return reply['ack'] == exp_seq

    @staticmethod
    def make_pkt(seq, data):
        """ Create an outgoing packet as a python dictionary
        :param seq: a character representing the sequence number of the packet, the one expected by the receiver '0' or '1'
        :param data: a single character the sender wants to send to the receiver
        :return: a python dictionary representing the packet to be sent
        """
        checksum = RDTSender.get_checksum(data)
        packet = {
            'sequence_number': seq,
            'data': data,
            'checksum': checksum
        }
        return packet

    def rdt_send(self, process_buffer):
        """ Implement the RDT v2.2 for the sender
        :param process_buffer: a list storing the message the sender process wishes to send to the receiver process
        :return: terminate without returning any value
        """
        count= 0
        # for every character in the buffer
        for data in process_buffer:
            sent = False
            pkt = RDTSender.make_pkt(self.sequence, data)
            print(f"===========================================================================================================")
            if count != 0:
                print("\033[94mSender: will start sending the next packet\033[0m")
        
            while not sent:
                         
                clonepkt = RDTSender.clone_packet(pkt)
                checksum_in_clonepkt = clonepkt['checksum']
                print(f"\033[94mSender: expecting\033[0m {{'sequence_number': '{self.sequence}', and 'checksum': '{ord(self.sequence)}'}}")
                print(f"\033[94mSender: sending\033[0m {pkt}")
                reply = self.net_srv.udt_send(clonepkt)                               
    
                if not RDTSender.is_corrupted(reply) and RDTSender.is_expected_seq(reply, self.sequence):
                    print(f"\033[94mSender: received \033[0m {reply}")
                    self.sequence = '1' if self.sequence == '0' else '0'
                    sent = True
                    count= count+1
                    print(f"\033[94mLetter {data} is sent and received correctly\033[0m")
                else:
                    print(f"\033[94mSender: received \033[0m {reply}")                
                            
        print(f"===========================================================================================================")
        print("Sender Done!")
        print(f"===========================================================================================================")
        return