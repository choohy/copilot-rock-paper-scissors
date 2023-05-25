#import main file
import main

# write unit test cases for main
def test_determine_winner():
    print("Testing determine_winner()...", end="")
    assert main.determine_winner('R', 'R') == 'tie'
    assert main.determine_winner('R', 'P') == 'computer'
    assert main.determine_winner('R', 'S') == 'user'
    assert main.determine_winner('R', 'L') == 'user'
    assert main.determine_winner('R', 'K') == 'computer'
    assert main.determine_winner('P', 'R') == 'user'
    assert main.determine_winner('P', 'P') == 'tie'
    assert main.determine_winner('P', 'S') == 'computer'
    assert main.determine_winner('P', 'L') == 'computer'
    assert main.determine_winner('P', 'K') == 'user'
    assert main.determine_winner('S', 'R') == 'computer'
    assert main.determine_winner('S', 'P') == 'user'
    assert main.determine_winner('S', 'S') == 'tie'
    assert main.determine_winner('S', 'L') == 'user'
    assert main.determine_winner('S', 'K') == 'computer'
    assert main.determine_winner('L', 'R') == 'computer'
    assert main.determine_winner('L', 'P') == 'user'
    assert main.determine_winner('L', 'S') == 'computer'
    assert main.determine_winner('L', 'L') == 'tie'
    assert main.determine_winner('L', 'K') == 'user'
    assert main.determine_winner('K', 'R') == 'user'
    assert main.determine_winner('K', 'P') == 'computer'
    assert main.determine_winner('K', 'S') == 'user'
    assert main.determine_winner('K', 'L') == 'computer'
    assert main.determine_winner('K', 'K') == 'tie'
    print("Passed!")
