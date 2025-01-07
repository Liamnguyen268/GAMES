def find(mainstring, letter):
    for i in range(len(mainstring)):
        if(mainstring[i] == letter):
            return i
    return -1


def encrypt(m, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in range(len(m)):
        letter = m[i]
        idx = find(alpha, letter)
        new_letter = k[idx]
        answer = answer + new_letter
    return answer

def main():
    msg = input("Please enter your message:")
    key = "bpzhgocvjdqswkimlutneryaxf"
    cipher = encrypt(msg, key)
    print("The encrypted message is: ", cipher)
main()