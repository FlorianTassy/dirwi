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
