def list_generator(num_seq):
    return num_seq.split(",")

def tuple_generator(num_seq):
    return tuple(list_generator(num_seq))


num_seq = input("Introduce a number sequence: ")

print(list_generator(num_seq))

print(tuple_generator(num_seq))