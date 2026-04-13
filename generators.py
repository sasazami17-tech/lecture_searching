from random import choices


def unordered_sequence(max_len=100):
    """
    Generates a list of random integers in arbitrary order.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: List of randomly selected integers from range -1000 to 999.
    """
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    """
    Generates a sorted list of random integers.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: Sorted list of randomly selected integers
        from range -1000 to 999.
    """
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    """
    Generates a random DNA sequence.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        str: String composed of characters "A", "C", "G", "T".
    """
    return "".join(choices("ACGT", k=max_len))


def main():
    """
    Runs basic tests for sequence generation functions.
    """
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()
hghghghgfdgfg