def ask_number(question):
    while True:
        answer = input(question).replace(" ", "").replace(",", ".")
        try:
            number = float(answer)
        except ValueError:
            print("Please enter a number, e.g. 249.99")
            continue
        if number > 0:
            return number
        print("The number must be positive.")

def format_dollar(amount):
    return f"${amount:,.2f}"

def main():
    price = ask_number("Item price in $ : ")
    target = ask_number("Your BTC target in $ : ")

if __name__ == "__main__":
    main()
