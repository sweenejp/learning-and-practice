musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]

# i = 0
# for groups in musical_groups:
#     if len(musical_groups[i]) == 3:
#         members = ", ".join(musical_groups[i])
#         print(members)
#     i += 1

all_mems = []

for group in musical_groups:
  all_mems.append(group)

print(str(all_mems))
print(str(musical_groups))