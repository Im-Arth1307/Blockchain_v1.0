# Why run on different ports?
# In blockchain projects, running multiple instances on different ports is useful for testing the interaction between nodes in the blockchain. Each instance running on a separate port acts as a different node in the network, allowing you to simulate peer-to-peer communication.
import hashlib
import json
from time import time

class Blockchain(object):

    def __init__(self):
        self.current_transactions = []      #This is a list that holds the current transactions until they are added to a block. Once the block is created, these transactions will be cleared from this list.
        
        self.chain = []     #This is a list that will store all the blocks in the blockchain. Each block represents a set of transactions and some metadata.
        
        self.new_block(previous_hash = 1, proof = 100)

        
    def new_block(self):
        """
        Create a new Block in the Blockchain
        
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: <str> Hash of previous Block
        :return: <dict> New Block
        """
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        #Reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block
    
    
    def new_transaction(self, sender, recipient, amount):
        """Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]
        
    
    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        
        :param block": <dict> Block
        "return": <str>
        """
        
        #We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
    
    