from reel import Reel

# PRIZES dictionary represents the amount per appearance for each symbol when
# a winning series is spun
PRIZES = {'Cherry': 1, 'Lemon': 2, 'Grape': 3, 'Orange': 4,
          'Melon': 5, 'Bells': 6, 'Lu7cky': 7}

# Each REEL# constant gives the symbols for each reel. These are randomly
# chosen from when the reel is spun.
REEL1 = ['Melon', 'Cherry', 'Orange', 'Grape', 'Bells', 'Lemon', 'Lu7cky',
         'Cherry', 'Orange', 'Grape', 'Lemon']
REEL2 = ['Melon', 'Cherry', 'Orange', 'Grape', 'Bells', 'Lemon', 'Melon',
         'Lu7cky', 'Grape', 'Orange', 'Lemon']
REEL3 = ['Melon', 'Cherry', 'Orange', 'Grape', 'Bells', 'Lemon', 'Melon',
         'Cherry', 'Lu7cky', 'Bells', 'Grape']


class SlotMachine:
    """
    SlotMachine allows creation and usage of virtual 3-reel slot machines.
    """
    def __init__(self, credits: int):
        """
        Initializes machine's internal variables.

        :param credits: The initial amount of credits in the machine
        """
        # Copy reels to avoid mutating constants
        self.reel1 = Reel(REEL1.copy())
        self.reel2 = Reel(REEL2.copy())
        self.reel3 = Reel(REEL3.copy())

        self.credits = credits
        self.bank = 0

    def __str__(self):
        """
        Stringifies the slot machine, returning a stylized string with
        associated information.
        """
        return (f'\t\t  REELS\n'
                f'=========================\n'
                f'[{self.reel1}][{self.reel2}][{self.reel3}]\n'
                f'=========================\n'
                f'Credits: {self.credits}\n'
                f'Bank: {self.bank}')

    def play(self):
        """
        Method starts the game-loop which allows user to spin the machine,
        view the prize table, see their credits/winnings, add credits, and
        end the game.
        """
        while True:
            print('Options:\n'
                  '1: Spin, 2: View Prizes, '
                  '3: Show Bank, 4: Add credits, 0: Exit')
            option = input('Enter a choice (0, 1, 2, 3, or 4): ')
            print('')
            match option:
                case '0':
                    self.bank += self.credits
                    self.credits = 0
                    print(f'Bank: {self.bank}')
                    break
                case '1':
                    self.spin()
                case '2':
                    self.display_win_table()
                case '3':
                    self.display_bank()
                case '4':
                    self.add_credits()
                case _:
                    print('error, enter a valid option')
            print('')

    def spin(self):
        """
        Checks if the machine has enough credits to spin. If it doesn't, an
        error message is printed. Otherwise, one credit is deducted and the
        `get_wins()` function is called.
        """
        if self.credits > 0:
            self.credits -= 1
            self.get_wins()
        else:
            print('no credits, please enter credits')

    def get_wins(self):
        """
        Randomizes each reel in the slot machine and checks if the results
        correspond to wins on the win table. If any do, a prize is added
        based on the `PRIZES` constant.
        """
        # Spin reels
        self.reel1.spin()
        self.reel2.spin()
        self.reel3.spin()

        win = 0
        if self.reel1 == self.reel2:  # First two reels are equal
            win = 2 * PRIZES[self.reel1.get_value()]
        if self.reel1 == self.reel2 == self.reel3:  # All reels are equal
            win = 3 * PRIZES[self.reel1.get_value()]

        print(self)
        print(f'Win: {win}')  # Print win amount before adding to bank
        self.bank += win

    def add_credits(self):
        """
        Adds credits into the slot machine based on validated user input.
        Adding less than 1 credit is disallowed.
        """
        # Validate input
        while True:
            try:
                credits = int(input('How many credits? '))
                if credits < 1:  # Only accept positive credits
                    print('error, please enter a valid amount')
                    continue
                break
            except ValueError as error:
                print(error)

        self.credits += credits  # Increment credits

    def display_bank(self):
        """
        Displays the current credit amount and current bank amount of the
        slot machine.
        """
        print(f'Credits: {self.credits}\n'
              f'Bank: {self.bank}')

    @staticmethod
    def display_win_table():
        """
        Prints the win table based on the `PRIZES` dictionary constant.
        """
        # PRIZES = {'Cherry': 1, 'Lemon': 2, 'Grape': 3, 'Orange': 4,
        #           'Melon': 5, 'Bells': 6, 'Lu7cky': 7}
        print('Doubles:\n'
              '----------')
        for prize_name in PRIZES:  # Print evenly spaced rows for each prize
            print(f'{prize_name}\t:\t'
                  f'{prize_name}\t:\t'
                  f'---\t\t:\t'
                  f'=\t{PRIZES[prize_name] * 2}')  # Amount based on appearance

        print('')  # Newline to separate doubles and triples tables

        print('Triples:\n'
              '----------')
        for prize_name in PRIZES:
            print(f'{prize_name}\t:\t'
                  f'{prize_name}\t:\t'
                  f'{prize_name}\t:\t'
                  f'=\t{PRIZES[prize_name] * 3}')
