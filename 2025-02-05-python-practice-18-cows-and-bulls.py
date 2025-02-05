import random

# def generate_4_digits_number():
# return random.rand.int(1000, 9999)

# def check_one_correct_digit(random_num, user_num):

# def check_two_correct_digits(random_num, user_num):
# rand_str= str(random_num)
# user_str = str(user_num)
# count = 0
# for i in range(4):
# if user_str[i] ==rand_str[i]
# count = count+1
# correct_count = (i for i in range(4) user_str[i] ==rand_str[i])

# print("bull")

if __name__ == "__main__":
    results = ["0", "0", "0", "0"]
    cow = 0
    rand_str = str(random.randint(1000, 9999))
    print(rand_str)
    while cow < 4:
        user_str = input("Give me a number: ")

        bull = 0
        cow = 0
        for i in range(4):
            if user_str[i] == rand_str[i]:
                cow = cow + 1
                results[i] = "c"
        for i in range(4):
            for k in range(4):
                if (
                    (user_str[i] == rand_str[k])
                    and (results[k] != "c")
                    and (results[k] != "b")
                ):
                    bull = bull + 1
                    results[k] = "b"
        print(f"cows : {cow}. bulls :{bull}")


# if user_num == random.ran.int:
#  user_num = True
# print("cow")
# if user_num != random.ran.int:
