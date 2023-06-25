# """
# Pick from:
# Rock, loses to Paper and Spock
# Paper, loses to Scissors and Lizard
# Scissors, loses to Rock and Spock
# Lizard, Loses to Rock and Scissors
# Spock, loses to Lizard and Paper
# """



paper = {
    'name' : "Paper",
    'emoji' : "\U0000270B",
    'rock' : "Paper covers Rock",
    'spock' : "Paper disproves Spock",
}
rock = {
    'name' : "Rock",
    'emoji' : "\U0000270A",
    'scissors' : "Rock crushes Scissors",
    'lizard' : "Rock crushes Lizard",
}
scissors = {
    'name' : "Scissors",
    'emoji' : "\U0000270C",
    'paper' : "Scissors cuts Paper",
    'lizard' : "Scissors decapitates Lizard",
}
spock = {
    'name' : "Spock",
    'emoji' : "\U0001F596",
    'rock' : "Spock vaporizes Rock",
    'scissors' : "Spock smashes Scissors",
}
lizard = {
    'name' : "Lizard",
    'emoji' : "\U0001F98E",
    'spock' : "Lizard poisons Spock",
    'paper' : "Lizard eats Paper",
}
list_choices = [paper, rock, scissors, spock, lizard]
