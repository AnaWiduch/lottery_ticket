import random

def generate_lottery_ticket():
    ticket = []
    for _ in range(6):
        ticket.append(random.randint(1, 49))
    return sorted(ticket)

def main():
    ticket = generate_lottery_ticket()
    print("Your lottery ticket numbers is:", *ticket)

if __name__ == "__main__":
    main()
