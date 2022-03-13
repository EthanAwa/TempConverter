def to_f(from_c):
    fahrenheit = (from_c * (9/5)) + 32
    return fahrenheit


def to_c(from_f):
    celsius = (from_f - 32) * (5/9)
    return celsius


temperatures = [-17.8, 0, 100]  # 0, 32, 212 for F -> C
converted = []

choice = input("Convert to Fahrenheit or Celsius (F or C): ")
if choice == "F":
    for item in temperatures:
        ans = to_f(item)

        if ans % 1 == 0:
            ans_statement = "{} C is {:.0f} F".format(item, ans)
        else:
            ans_statement = "{} C is {:.1f} F".format(item, ans)
        converted.append(ans_statement)
else:
    for item in temperatures:
        ans = to_c(item)
        if ans % 1 == 0:
            ans_statement = "{} F is {:.0f} C".format(item, ans)
        else:
            ans_statement = "{} F is {:.1f} C".format(item, ans)
        converted.append(ans_statement)

print(converted)
