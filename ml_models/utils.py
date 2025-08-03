import logging

logging.basicConfig(level=logging.INFO)


def words_to_number(word_string: str) -> int | None:
    """
    Converts a string containing numbers in words (e.g., "five hundred and twenty-three")
    to their numerical equivalent (e.g., 523) without using an external library like word2number.

    Handles positive integers up to trillions, including "and".
    Does not handle decimals, negative numbers, or complex fractions.

    Args:
        word_string (str): The string containing the number in words.

    Returns:
        int: The numerical equivalent of the word string.
             Returns None if the string cannot be entirely converted.
    """
    if not isinstance(word_string, str):
        raise TypeError("Input must be a string.")

    # Convert to lowercase and split into words
    words = word_string.lower().replace("-", " ").split()

    # Define mappings for number words
    units = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
    }

    tens = {
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    # Major scales, ordered from largest to smallest for efficient processing
    # The value here is the multiplier, not the base value.
    large_scale_multipliers = {
        "thousand": 1000,
        "million": 1_000_000,
        "billion": 1_000_000_000,
        "trillion": 1_000_000_000_000,
    }

    total_sum = 0
    current_hundreds_block = 0  # Accumulates value within the current 0-999 block (e.g., "five hundred twenty two")

    # Process words from left to right
    for word in words:
        if word in units:
            current_hundreds_block += units[word]
        elif word in tens:
            current_hundreds_block += tens[word]
        elif word == "hundred":
            if current_hundreds_block == 0:  # Implies "one hundred"
                current_hundreds_block = 1
            current_hundreds_block *= 100
        elif word in large_scale_multipliers:
            if (
                current_hundreds_block == 0
            ):  # Handles cases like "thousand" (meaning 1 thousand)
                current_hundreds_block = 1

            # Add the current block's value multiplied by its large scale
            total_sum += current_hundreds_block * large_scale_multipliers[word]
            current_hundreds_block = (
                0  # Reset for the next block of hundreds/tens/units
            )
        elif word == "and":
            continue  # Ignore "and"
        elif (
            word == "a"
        ):  # Handle "a hundred" implicitly by allowing next word to be "hundred"
            continue  # 'a' is context-dependent, handled when 'hundred' or another number follows.
        else:
            logging.warning(
                f"Warning: Unknown word '{word}' encountered. Conversion might be incomplete."
            )
            return None  # Or raise an error as appropriate

    # Add any remaining value from the last block (e.g., "five hundred twenty two" if it's the end of the string)
    total_sum += current_hundreds_block

    return total_sum
