from time import sleep

line =   '\n' + 80 * "-" + '\n'



def print_ws(to_print):
    for char in to_print:
        print(char, end="", flush=True)
        sleep(0.05)
    print(line)
