def checkInclusion(self, s1: str, s2: str) -> bool:
    # Count arrays for frequency of characters in s1 and the current window in s2
    count1 = [0] * 26
    count2 = [0] * 26

    len1, len2 = len(s1), len(s2)

    # Early return if s1 is longer than s2
    if len1 > len2:
        return False

    # Initialize the frequency count for s1 and the first window of s2
    for i in range(len1):
        count1[ord(s1[i]) - ord('a')] += 1
        count2[ord(s2[i]) - ord('a')] += 1

    # Check the initial window
    if count1 == count2:
        return True

    # Sliding window over s2
    for i in range(len1, len2):
        # Include the next character in the window
        count2[ord(s2[i]) - ord('a')] += 1
        # Remove the character that is sliding out of the window
        count2[ord(s2[i - len1]) - ord('a')] -= 1

        # Check if the current window matches s1's frequency count
        if count1 == count2:
            return True

    # If no matching window is found
    return False
