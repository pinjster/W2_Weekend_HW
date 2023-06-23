# """
# Pick from:
# Rock,
# Paper,
# Scissors,
# Lizard,
# Spock
# """



paper = {
    'name' : "Paper",
    'lose' : ["scissors"],
}
rock = {
    'name' : "Rock",
    'lose' : ["Paper"],
}
scissors = {
    'name' : "Scissors",
    'lose' : ["Rock"],
}

list_choices = [paper, rock, scissors]