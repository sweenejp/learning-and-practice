def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Give me a better idea")
    return product_idea + "inator"

new_idea = suggest("ab")
print(new_idea)
print(len(new_idea))