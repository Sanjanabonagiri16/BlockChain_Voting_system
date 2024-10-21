from blockchain import Blockchain, Block
from utils import print_blockchain
import time

def main():
    # Create a new blockchain
    my_blockchain = Blockchain()

    # Add some blocks
    my_blockchain.add_block(Block(1, time.time(), "Transaction 1", ""))
    my_blockchain.add_block(Block(2, time.time(), "Transaction 2", ""))
    my_blockchain.add_block(Block(3, time.time(), "Transaction 3", ""))

    # Print the blockchain
    print("Blockchain:")
    print_blockchain(my_blockchain)

    # Validate the blockchain
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")

    # Try to tamper with the blockchain
    my_blockchain.chain[1].data = "Tampered Transaction"
    print("\nAfter tampering:")
    print_blockchain(my_blockchain)

    # Validate the blockchain again
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main()