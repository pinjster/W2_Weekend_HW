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
    'rock' : "Paper covers Rock",
    'spock' : "Paper disproves Spock",
}
rock = {
    'name' : "Rock",
    'scissors' : "Rock crushes Scissors",
    'lizard' : "Rock crushes Lizard",
}
scissors = {
    'name' : "Scissors",
    'paper' : "Scissors cuts Paper",
    'lizard' : "Scissors decapitates Lizard",
}
spock = {
    'name' : "Spock",
    'rock' : "Spock vaporizes Rock",
    'scissors' : "Spock smashes Scissors",
}
lizard = {
    'name' : "Lizard",
    'spock' : "Lizard poisons Spock",
    'paper' : "Lizard eats Paper",
}
list_choices = [paper, rock, scissors, spock, lizard]
