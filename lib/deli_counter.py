katz_deli = []

def line():
    if len(katz_deli) == 0:
        return "The line is currently empty."
    else:
        line_status = "The line is currently:"
        for i, customer in enumerate(katz_deli, 1):
            line_status += f"\n{i}. {customer}"
        return line_status

def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}! You are number {position} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = line.pop(0)
        print(f"Now serving {serving_customer}.")