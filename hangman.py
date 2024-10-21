import pygame
import math
import random

from solver import generate_valid_words, generate_best_letters

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

FPS = 60
clock = pygame.time.Clock()
run = True

# Buttons
radius = 24
space = 20
letters = []  # [399,122,"A",True]
x_start = round((WIDTH - (radius * 2 + space) * 13) / 2)
y_start = 540

A = 65  # Using ASCII value to print letters on the button. A->65, B->66 and so on

for i in range(26):
    x = x_start + space * 2 + ((radius * 2 + space) * (i % 13))
    y = y_start + ((i // 13) * (space + radius * 2))
    letters.append([x, y, chr(A + i), True])

# Footer Buttons for new game and quit
footer_buttons = {
    "new_game": pygame.Rect(WIDTH - 250, HEIGHT - 60, 120, 40),
    "quit": pygame.Rect(WIDTH - 120, HEIGHT - 60, 80, 40),
}

# Fonts
font = pygame.font.SysFont("comicsans", 45)
WORD = pygame.font.SysFont("comicsans", 40)
TITLE = pygame.font.SysFont("comicsans", 70)
FOOTER = pygame.font.SysFont("comicsans", 30)
SOLVER_HINT_FONT = pygame.font.SysFont("comicsans", 30)

# Time to load images so we can draw a hangman
images = []
for i in range(0, 7):
    image = pygame.image.load(f"pictures/Hangman-{i}.png")
    images.append(image)

# Function to read words from dictionary files
def read_words_from_file(length) -> list :
    try:
        with open(f"data/dico_{length}_lettres.txt", "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Dictionary file for length {length} not found.")
        return []

# Game variables
hangman = 0
word_length = random.choice([6, 7, 8, 9, 10])
word_dict : dict[int:list[str]] = {
    length: read_words_from_file(length) for length in range(6, 11)
}
words = random.choice(word_dict[word_length])
guessed = []
correct_guess: list[tuple[str, int]] = []
wrong_guess = []

letter, nb_bits = generate_best_letters(word_dict[word_length], [letter[2] for letter in letters], correct_guess,
                                        wrong_guess)

solver_hint = (
    f"Il y a {len(word_dict[word_length])} possibilités. "
    f"Meilleure lettre: {letter} ({nb_bits:.2f} bits)."
)

# Function to draw the game board
def draw():
    win.fill((255, 255, 255))  # display with white color

    # TITLE for the game
    title = TITLE.render("HangMan", 1, (0, 0, 0, 0))
    win.blit(title, (WIDTH / 1.9 - title.get_width() / 2, 10))  # Title in center and then y axis= 24

    # Draw word on the screen
    disp_word = ""
    for letter in words:
        if letter in guessed:
            disp_word += letter + " "
        else:
            disp_word += "_ "

    text = WORD.render(disp_word, 1, (0, 0, 0, 0))
    win.blit(text, (500, 250))

    # Display Solver's Hint Rectangle
    hint_rect = pygame.Rect(300, 400, 600, 100)
    pygame.draw.rect(win, (200, 200, 200), hint_rect)
    hint_text = SOLVER_HINT_FONT.render(solver_hint, 1, (0, 0, 0))
    win.blit(hint_text, (hint_rect.x + 10, hint_rect.y + 10))

    # Buttons at center
    for btn_pos in letters:
        x, y, ltr, visible = btn_pos  # making button visible and invisible after clicking it

        if visible:
            pygame.draw.circle(win, (0, 0, 0, 0), (x, y), radius, 4)
            txt = font.render(ltr, 1, (0, 0, 0, 0))
            win.blit(txt, (x - txt.get_width() / 2, y - txt.get_height() / 2))

    # Footer buttons
    pygame.draw.rect(win, (200, 200, 200), footer_buttons["new_game"])
    new_game_text = FOOTER.render("New Game", 1, (0, 0, 0))
    win.blit(new_game_text, (footer_buttons["new_game"].x + 10, footer_buttons["new_game"].y + 5))

    pygame.draw.rect(win, (200, 200, 200), footer_buttons["quit"])
    quit_text = FOOTER.render("Quit", 1, (0, 0, 0))
    win.blit(quit_text, (footer_buttons["quit"].x + 10, footer_buttons["quit"].y + 5))

    win.blit(images[hangman], (50, 50))
    pygame.display.update()

# Function to reset game
def reset_game():
    global guessed, hangman, words, word_length, correct_guess, wrong_guess, solver_hint
    guessed = []
    correct_guess, wrong_guess = [], []
    hangman = 0
    word_length = random.choice([6, 7, 8, 9, 10])
    words = random.choice(word_dict[word_length])
    solver_hint = f"Il y a {len(word_dict[word_length])} possibilités."
    for letter in letters:
        letter[3] = True

# Main game loop
while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():  # Triggering the event
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()

            # Check for footer buttons
            if footer_buttons["new_game"].collidepoint(x_mouse, y_mouse):
                reset_game()

            if footer_buttons["quit"].collidepoint(x_mouse, y_mouse):
                run = False

            # Check letter buttons
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)
                    if dist <= radius:
                        letter[3] = False  # to make the clicked button invisible
                        guessed.append(ltr)
                        if ltr not in words:
                            hangman += 1
                            wrong_guess.append(ltr)
                        else:
                            correct_positions = [pos for pos, char in enumerate(words) if char == ltr]
                            # Append the letter and its positions to correct_guess
                            for pos in correct_positions:
                                correct_guess.append((ltr, pos))

                        valid_words = generate_valid_words(all_words=word_dict[word_length], letter_in=correct_guess, letter_out=wrong_guess)
                        possible_letters = [ltr for x, y, ltr, visible in letters if visible]
                        # Get the top letters to play next
                        letter, nb_bits  = generate_best_letters(valid_words, possible_letters, correct_guess,
                                                            wrong_guess)


                        solver_hint = (
                                f"Il y a {len(valid_words)} possibilités. "
                                f"Meilleure lettre: {letter} ({nb_bits:.2f} bits)."
                            )




    won = True
    for letter in words:
        if letter not in guessed:
            won = False
            break

    if won:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0, 0))
        text = WORD.render("C'est gagné!", 1, (129, 255, 0, 255))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(4000)
        reset_game()

    if hangman == 6:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0, 0))
        text = WORD.render("C'est perdu", 1, (255, 0, 5, 255))
        answer = WORD.render("Le mot était " + words, 1, (129, 255, 0, 0))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        win.blit(answer, ((WIDTH / 2 - answer.get_width() / 2), (HEIGHT / 2 - text.get_height() / 2) + 70))

        pygame.display.update()
        pygame.time.delay(4000)
        print("LOST")
        reset_game()

pygame.quit()
