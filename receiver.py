class ReceiverProcess:
    __buffer = list()

    @staticmethod
    def deliver_data(data):
        ReceiverProcess.__buffer.append(data)

    @staticmethod
    def get_buffer():
        return ReceiverProcess.__buffer


class RDTReceiver:

    @staticmethod
    def get_checksum(data):
        return ord(data)

    @staticmethod
    def is_corrupted(packet):
        # Check if the received packet is corrupted by comparing the checksum
        expected_checksum = RDTReceiver.get_checksum(packet['data'])
        return packet['checksum'] != expected_checksum

    @staticmethod
    def is_expected_seq(rcv_pkt, exp_seq):
        # Check if the received packet has the expected sequence number
        return rcv_pkt['sequence_number'] == exp_seq

    def __init__(self):
        self.sequence = '0'

    @staticmethod
    def is_corrupted(packet):
        # Enhanced corruption check: Checksum of received data
        expected_checksum = RDTReceiver.get_checksum(packet['data'])
        return packet['checksum'] != expected_checksum

    @staticmethod
    def is_expected_seq(rcv_pkt, exp_seq):
        # Enhanced sequence check: Check sequence number in the received packet
        return rcv_pkt['sequence_number'] == exp_seq

    @staticmethod
    def make_reply_pkt(seq, checksum):
        """ Create a reply (feedback) packet with to acknowledge the received packet
        :param seq: the sequence number '0' or '1' to be acknowledged
        :param checksum: the checksum of the ack the receiver will send to the sender
        :return:  a python dictionary represent a reply (acknowledgement)  packet
        """
        reply_pck = {
            'ack': seq,
            'checksum': checksum
        }
        return reply_pck

    def rdt_rcv(self, rcv_pkt):
        """ Implement the RDT v2.2 for the receiver
        :param rcv_pkt: a python dictionary representing the received packet
        :return: a python dictionary representing the reply packet
        """
         
        print("\033[92mReceiver: expecting\033[0m {'sequence_number': '" + str(self.sequence) + "'}")        
        if not RDTReceiver.is_corrupted(rcv_pkt) and RDTReceiver.is_expected_seq(rcv_pkt, self.sequence):
            print(f"\033[92mReceiver: received \033[0m{rcv_pkt}")
            # If the received packet is not corrupted and has the expected sequence number
            ReceiverProcess.deliver_data(rcv_pkt['data'])
            tempseq = self.sequence
            
            if self.sequence == '0':
                self.sequence = '1'
            else:
                self.sequence = '0'
            replied_packet = RDTReceiver.make_reply_pkt(tempseq, ord(tempseq))
            print(f"\033[92mReceiver: reply with \033[0m{replied_packet}")

            return replied_packet
        
        else:
            # If the received packet is corrupted or has an unexpected sequence number
            if self.sequence == '0':
                diffseq = '1'
            else:
                diffseq = '0'
    
            print(f"\033[92mReceiver: received \033[0m{rcv_pkt}")
            replied_packet = RDTReceiver.make_reply_pkt(diffseq, ord(diffseq))
            print(f"\033[92mReceiver: reply with \033[0m{replied_packet}")
            return replied_packet

            
