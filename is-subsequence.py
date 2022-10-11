# write a function that takes 2 strings as parameters
# the function returns True if the first string is a subsequence within the second string
# returns False otherwise


def is_subseq(str1, str2):
    return (str1 in str2)


print(f"Should return True: {str(is_subseq("hello", "hello world"))}")
print(f"Should return False: {str(is_subseq("sing", "sting"))}")
print(f"Should return True: {str(is_subseq("hello", "hello world"))}")