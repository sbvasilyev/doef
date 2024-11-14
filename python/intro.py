x = 30
x = True

y = 0.5
s = "Hello, Мир!"

print(f"type of 1 is {type(1)}")       # => <class 'int'>
print(f"type of True is {type(True)}") # => <class 'bool'>

x = 42
print(f'type of x is: {type(x)}') # => int

y = 42.0
print(f'type of y is: {type(y)}') # => float

1.0 + 1.0 + 1.0 == 3.0 # => False

x = 11
print(x + 31)   # => 42
print(x - 12)   # => -1
print(x * 3)    # => 33
print(x / 2)    # => 5.5
print(x // 2)   # => 5     (целочисленное деление)
print(x ** 2)   # => 121   (возведение в степень)
print(x % 3)    # => 2     (остаток от деления)

print(x + 2.0)  # => 13.0
print(x ** 2.0) # => 121.0

i = 1
while i <= 10:
    print(f'square of {i} is {i ** 2}')
    i += 1

def id_with_print(x):
    print(f"function called with x = {x}")
    return x

some_list = [0, 1, 2, 3, 4, 5]

# with +=
some_list[id_with_print(2)] += 4
# => "function called with x = 2" печатается один раз

# without +=
some_list[id_with_print(2)] = some_list[id_with_print(2)] + 4
# => "function called with x = 2" печатается дважды

t = 42 > -90  # => True
f = 0 != 0    # => False

print(f"True AND False is {t and f}")  # => False
print(f"True OR  False is {t or f}")   # => True
print(f"     NOT False is {not f}")    # => True

x = 0
y = 5
if x != 0 and y / x > 1:
    print(f"y is {y}")

some_string = "Καλημέρα ντουνιά!"
another_string = 'Привет, мир!'

x = 5
interpolated_string = f"x is {x} and x^2 is {x ** 2}"
print(interpolated_string)  # => x is 5 and x^2 is 25

print("I can use double quotes inside \"that way\"")
print('And \'single quotes\' also')

s = "  some strInG  "
print(s.strip())               # => "some strInG"
print(s.strip().upper())       # => "SOME STRING"

s = "ANOTHER STRING"
print(s.lower())               # => "another string"
print(s.replace("ING", "ONG")) # => "ANOTHER STRONG"
print(s.split(" "))            # => ["ANOTHER", "STRING"]

mark = 6.3

if mark < 4:
    print("неудовлетворительно")
elif mark < 6:
    print("удовлетворительно")
elif mark < 8:
    print("хорошо")
else:
    print("отлично")

n_groups = 3
total_amount = 9000

amount_per_group = total_amount / n_groups if n_groups > 0 else total_amount

read_input = "q"

match read_input:
    case "q" | "quit":
        print("quiting...")
    case "r" | "run":
        print("running...")
    case cmd:
        print(f"you entered: {cmd}")
