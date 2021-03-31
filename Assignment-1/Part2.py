def test_isStringPermutation():
    assert isStringPermutation('asdf', 'fsda') == True
    assert isStringPermutation('asdf', 'fsa') == False
    assert isStringPermutation('asdf', 'fsax') == False
    assert isStringPermutation('asdf', 'fsap') == False
    assert isStringPermutation('asdf', 'asdg') == False
    assert isStringPermutation('leirbag', 'gabriel') == True
    assert isStringPermutation('', '') == True
    assert isStringPermutation('', 'dasdas') == False


def test_pairsThatEqualSum():
    assert pairsThatEqualSum([1, 2, 3, 4, 5], 5) == [(1, 4), (2, 3)]
    assert pairsThatEqualSum([1, 2, 3, 4, 5], 1) == []
    assert pairsThatEqualSum([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)]
    assert pairsThatEqualSum([], 100) == []
    assert pairsThatEqualSum([-10, -20, -30, 0,-40], -30) == [(-10, -20), (-30, 0)]


def isStringPermutation(s1: str, s2: str) -> bool:
    """ 
    Check if s1 is permutation of s2.

    First it checks if the strings have the same lenght, returns false if they don't.

    If both strings are empty, it returns True.

    Then if they have the same lenght, it counts the amount of letters in each string,
    if any count is different in each dictionary, it returns False. If the count is not 
    different, it returns True.

    This algorithm is O(n).
    """

    # length difference
    if len(s1) != len(s2):
        return False
    # if both strings are empty
    elif (len(s1) == len(s2)) and len(s1) == 0:
        return True
    # if they have the same lenght and are not empty
    else:
        s1_dict = {}
        s2_dict = {}

        # counts the amount of characters in string s1
        for character in s1:
            if s1_dict.get(character) is None:
                s1_dict[character] = 1
            else:
                s1_dict[character] += 1
        # counts the amount of characters in string s2
        for character in s2:
            if s2_dict.get(character) is None:
                s2_dict[character] = 1
            else:
                s2_dict[character] += 1

        # assume both strings are equal
        equal_strings = True
        for key in s1_dict:
            # if the same key returns different results for each string
            # they are not equal
            if s1_dict.get(key) != s2_dict.get(key):
                equal_strings = False
                # stops the for loop as it's not necessary to check other keys
                break

        return equal_strings


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    """
    Function that takes an array of integers and a target integer and returns an array
    of pairs where each pair contains two numbers from the input array and the sum of
    each pair equals the target integer.

    This algorithm is O(n²).
    """
    answer_list = []

    for i in range(0, len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            if inputArray[i] + inputArray[j] == targetSum:
                answer_list.append((inputArray[i], inputArray[j]))

    return answer_list
