##
# Author: Andrew Scott
# Version: SP2017
# Description: Run the slot machine program.
##
from slot_machine import SlotMachine
INITIAL_CREDITS = 5  # Start the game with 10 credits.


def main():
    """Create a slot machine and play it"""
    # Call the constructor of the slot machine.
    slot = SlotMachine(INITIAL_CREDITS)
    slot.play()


# Run the main function if this is called directly by the Python interpreter
if __name__ == "__main__":
    main()
