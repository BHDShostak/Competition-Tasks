#Elephants

# A parade is about to take place at the Byteotian Zoo, in which all the elephants in it will participate.
# The zoo employees have already encouraged the animals to line up in one row, because, according to the ordinance of the zoo director,
# this should be the initial figure of the parade.
# Unfortunately, the director himself came to the scene and he did not like the order of the elephants chosen by the employees at all.
# The director suggested the order in which he thought the animals would look best and instructed the staff to rearrange the elephants as suggested.
# In order to avoid excessive chaos just before the parade, workers decided to rearrange the elephants by switching some pairs of elephants one by one.
# Converted animals do not have to be adjacent to each other in a row. The effort required to make an elephant move is directly proportional to its mass,
# so the effort of swapping two elephants of m1 and m2 can be estimated by m1 + m2.

#Write a program that:
#1.Reads the weights of all zoo elephants and the current and target order of the elephants in a row from the standard input.
#2. determine the elephant rearrangement method that leads from the initial to the final order and minimizes the sum of efforts related to all the elephant position swaps.
#3. write the sum of the values of these efforts to the standard output

#Example:
#For the input data:
#6
#2400 2000 1200 2400 1600 4000
#1 4 5 3 6 2
#5 3 2 4 6 1
#the correct answer is:
#11200


with open('slo1.in') as info:  # open file , you can change file name for reading another file
    file_str = []
    while True: # add string information to list
        str_info = info.readline()
        file_str.append(str_info)
        if not str_info:  # close list
            break


def main():

    elephants_quantity = int(file_str[0])  # input elephants quantity
    weight_of_elephants = list(map(int, file_str[1].split(' ')))  # input weight of elephants
    random_sequence = list(map(lambda x: int(x) - 1, file_str[2].split(' ')))  # input random sequence
    director_sequence = list(map(lambda x: int(x) - 1, file_str[3].split(' ')))  # input director sequence
    efficient_sequence = [0 for _ in range(elephants_quantity)]  # process of efficient sequence

    for elephant in range(elephants_quantity):
        efficient_sequence[director_sequence[elephant]] = random_sequence[elephant]  # create efficient sequence

    main_list_1 = []
    checklist = [False for _ in range(elephants_quantity)]  # create checklist

    for elephant in range(elephants_quantity):  # check elephants
        if not checklist[elephant]:
            main_list_2 = [elephant]
            checklist[elephant] = True
            checklist_index = efficient_sequence[elephant]
            while checklist[checklist_index] is not True:
                checklist[checklist_index] = True
                main_list_2.append(checklist_index)
                checklist_index = efficient_sequence[checklist_index]
            main_list_1.append(main_list_2)

    weight_sum_lists = [sum([weight_of_elephants[weight] for weight in main_list_2]) for main_list_2 in main_list_1]
    min_weight_lists = [min([weight_of_elephants[weight] for weight in main_list_2]) for main_list_2 in main_list_1]
    min_weight_all = min(weight_of_elephants)
    result = 0

    for index, main_list_2 in enumerate(main_list_1):
        method_1 = weight_sum_lists[index] + (len(main_list_2) - 2) * min_weight_lists[index]
        method_2 = weight_sum_lists[index] + min_weight_lists[index] + (len(main_list_2) + 1) * min_weight_all
        result += min(method_1, method_2)
    print(result)


if __name__ == '__main__':
    main()
