# Problem Set 4A
# Name: <timeshell>
# Collaborators:
# Time Spent: very long time

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
    
    if len(sequence) == 1:
        return [sequence]
    else:
        first_letter = sequence[0]    
        rest_of_equence = sequence[1:] 
        sequence = get_permutations(rest_of_equence)
        result = []
        for i in range (len(sequence)):
            #将第一个字母插入到剩余的字符串中
            for j in range(len(sequence[i])+1):
                permutations_list = list(sequence[i])
                permutations_list.insert(j,first_letter)
                #列表转字符串
                permutations = ''
                for letter in permutations_list:
                    permutations += letter
                result.append(permutations)            
        return result



if __name__ == '__main__':

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'oh'
    print('Input:', example_input)
    print('Expected Output:', ['oh', 'ho'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'bust'
    print('Input:', example_input)
    print('Expected Output:', ['bust', 'ubst', 'usbt', 'ustb', 'ustb', 'ustb', 'ustb', 'bsut', 'sbut', 'subt', 'sutb', 'sutb', 'sutb', 'sutb', 'bstu', 'sbtu', 'stbu', 'stub', 'stub', 'stub', 'stub', 'buts', 'ubts', 'utbs', 'utsb', 'utsb', 'utsb', 'utsb', 'btus', 'tbus', 'tubs', 'tusb', 'tusb', 'tusb', 'tusb', 'btsu', 'tbsu', 'tsbu', 'tsub', 'tsub', 'tsub', 'tsub'])
    print('Actual Output:', get_permutations(example_input))
    print(get_permutations('aeiou'))



