def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    averages = []
    for num in range(1,len(sequence)+1):
        sum = 0
        for item in sequence[:num]:
            sum += item
        averages.append(round(sum/num, 2))
    return averages
        