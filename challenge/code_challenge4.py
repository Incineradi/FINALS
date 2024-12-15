def cc():
    num1=eval(input("input first number: "))
    num2=eval(input("input second number: "))

    sum=num1 + num2

    diff=num1 - num2

    prod=num1 * num2

    quot=num1 / num2

    exp=num1 ** num2

    rem=num1 % num2

    floor=num1 // num2

    print(
    f"\nthe sum of { num1 } and { num2 } is { sum }",
    f"\nthe difference of { num1 } and { num2 } is { diff }",
    f"\nthe product of { num1 } and { num2 } is { prod }",
    f"\nthe quotient of { num1 } and { num2 } is { quot }",
    f"\n{ num1 } exponent by { num2 } is { exp }",
    f"\nthe remainder of { num1 } and { num2 } is { rem }",
    f"\nthe floor division of { num1 } and { num2 } is { floor }",
    )