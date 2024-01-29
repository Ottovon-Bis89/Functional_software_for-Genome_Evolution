
class Edit_distance:


    def __init__(self) -> None:
    
        pass
    
    def edit_distance(string1, string2):
        """
        This function takes in two strings and calculates the minimum number of operations required
        to convert/transform string1 into string2. This minimum number of operations, usually insertions,
        deletions and substitutions is the Edit Distance or Levenshtein distance
        """
        m = len(string1)
        n = len(string2)

        # Create a matrix to store the edit distances
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and column of the matrix
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill in the matrix with edit distances
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string1[i - 1] == string2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                    dp[i][j - 1],      # Insertion
                                    dp[i - 1][j - 1])  # Substitution

        # Return the edit distance between the two strings
        return dp[m][n]


    # Test the function
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    distance = edit_distance(string1, string2)
    print("The edit distance between the two strings is:", distance)
