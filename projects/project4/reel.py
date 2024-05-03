from random import choice


class Reel:
    def __init__(self, symbol_list: list) -> None:
        """
        Initializes reel's internal variables.

        :param symbol_list: symbols on the reel, which are randomly selected
            from when the reel is spun.
        """
        self.reel_values = symbol_list  # List of images in the reel
        self.selected_value = symbol_list[0]

    def __str__(self) -> str:
        """
        Strings of the reel return only the current value of the reel.

        :return: reel's current value.
        """
        return self.selected_value

    def __eq__(self, other) -> bool:
        """
        Checks two reels' `selected_value`, not their possible values.

        :param other: reel being compared.
        :return: bool corresponding to two reels having the same
            `selected_value`.
        """
        return self.selected_value == other.selected_value

    def spin(self) -> None:
        """
        Randomizes the `reel_values` list and sets the `selected_value` to
        the first value in the that list.
        """
        self.selected_value = choice(self.reel_values)

    def set_value(self, symbol) -> None:
        """
        Sets the reel's `selected_value` to `symbol` if `symbol` is in the
        reel's `reel_values`.
        :param symbol: symbol the `selected_value` is being set to.
        :return:
        """
        if symbol in self.reel_values:
            self.selected_value = symbol
        else:
            print('error, selected symbol not in reel')

    def get_value(self) -> str:
        """
        Return's the reel's selected value.
        :return: the reel's `selected_vale`
        """
        return self.selected_value
