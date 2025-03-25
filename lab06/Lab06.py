class Person:
    def __init__(self, name, age):
        # Initialize name and age
        self.name = name
        self.age = age
        self.child = None  # Only one child (no list)

    def add_child(self, child):
        # Assign the given child to this person
        self.child = child

    def print_family_line(self):
        # TODO: Print this person's name and age
        print('Name:', self.name, '\nAge:', self.age)
        if self.child is not None:
            self.child.print_family_line()
        # Then, if they have a child, call this same function on the child
        pass

    def count_large_age_gaps(self, gap_limit):
        # TODO: Count how many parent-child pairs have an age gap > gap_limit
        # Hint:
        if self.child is None:
            return 0
        age_gap = self.age - self.child.age
       
        if age_gap > gap_limit:
            gap_count= 1
        else:
            gap_count = 0
       
        child_gap_count = self.child.count_large_age_gaps(gap_limit)
       
        total_gap_count = gap_count+child_gap_count
       
        return total_gap_count
       
        pass


def build_family_line():
    name = str(input('Enter persons name: '))
    age = int(input('Enter persons age: '))
    person = Person(name, age)

    has_child = str(input('Enter yes if you have a child, no if not: ')).strip().lower()
    # TODO: Ask the user if this person has a child (yes or no)
    if has_child == 'yes':
        child = build_family_line()
        person.add_child(child)
       
    return person

    pass


# --- Main Program Starts Here ---
print("Welcome to the Generational Gap Checker!\n")

# TODO: Build the family line from user input
root = build_family_line()

print("\nHere is your family line:\n")
root.print_family_line()
# TODO: Call the function to print the family line

gap_limit = int(input('Enter an age gap limit: '))

large_gaps = root.count_large_age_gaps(gap_limit)
# TODO: Call the function to count large age gaps and print the result
print(f'Number of large age gaps greater than {gap_limit}: {large_gaps}')