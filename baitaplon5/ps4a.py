# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # pass #delete this line and replace with your code here
    def mix_char_into_string(char,string):
        result_list = []
        for i in range(len(string) + 1):
            result_list.append(string[:i] + char + string[i:])
        return result_list
    def mix(char,L):
        result_list = []
        for ele in L:
            result_list.extend(mix_char_into_string(char,ele))
        return result_list
    if len(sequence) == 1:
        return [sequence]
    return mix(sequence[0], get_permutations(sequence[1:]))

    
if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', sorted(get_permutations(example_input)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here

