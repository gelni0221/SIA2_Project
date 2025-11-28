import tkinter as tk
import random
import copy
class SnakeGame:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=400, height=400, bg="black")
        self.canvas.pack()

        self.cell = 20
        self.game_over = False
        self.restart_button = None

        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.change_direction)

        self.reset_game()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.spawn_food()
        self.game_over = False

        self.canvas.delete("game_message")
        if self.restart_button:
            self.canvas.delete("restart_btn")
            self.restart_button = None

        self.update()

    def spawn_food(self):
        while True:
            x = random.randrange(0, 20) * self.cell
            y = random.randrange(0, 20) * self.cell
            new_food = (x, y)
            if new_food not in self.snake:
                return new_food

    def change_direction(self, event):
        key = event.keysym
        if not self.game_over:
            if key == "Up" and self.direction != "Down":
                self.direction = "Up"
            elif key == "Down" and self.direction != "Up":
                self.direction = "Down"
            elif key == "Left" and self.direction != "Right":
                self.direction = "Left"
            elif key == "Right" and self.direction != "Left":
                self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up": head_y -= self.cell
        if self.direction == "Down": head_y += self.cell
        if self.direction == "Left": head_x -= self.cell
        if self.direction == "Right": head_x += self.cell

        new_head = (head_x % 400, head_y % 400)

        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        if self.snake:
            head = self.snake[0]
            self.canvas.create_rectangle(head[0], head[1], head[0] + self.cell, head[1] + self.cell, fill="white")
            for x, y in self.snake[1:]:
                self.canvas.create_rectangle(x, y, x + self.cell, y + self.cell, fill="lime")

        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx + self.cell, fy + self.cell, fill="red")

        if self.game_over:
            self.canvas.create_text(200, 160, text="GAME OVER", fill="white", font=("Helvetica", 24),
                                    tags="game_message")

            self.restart_button = self.canvas.create_rectangle(120, 220, 280, 260, fill="gray", outline="white",
                                                               tags="restart_btn")
            self.canvas.create_text(200, 240, text="RESTART", fill="white", font=("Helvetica", 16), tags="restart_btn")

            self.canvas.tag_bind("restart_btn", "<Button-1>", self.handle_restart_click)

    def handle_restart_click(self, event):

        if self.game_over:
            self.reset_game()

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.draw()

            self.canvas.after(120, self.update)
        else:
            self.draw()

class PongGame:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=600, height=400, bg="black")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")
        self.ball_dx = 3
        self.ball_dy = 3
        self.paddle = self.canvas.create_rectangle(560, 150, 580, 250, fill="white")

    def move_paddle(self, dy):
        self.canvas.move(self.paddle, 0, dy)

    def key_press(self, event):
        if event.keysym == "Up":
            self.move_paddle(-20)
        elif event.keysym == "Down":
            self.move_paddle(20)

    def update(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        if by1 <= 0 or by2 >= 400:
            self.ball_dy *= -1
        if bx1 <= 0:
            self.ball_dx *= -1
        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        if bx2 >= px1 and py1 < by2 < py2:
            self.ball_dx *= -1
        if bx2 > 600:
            self.canvas.coords(self.ball, 290, 190, 310, 210)

        self.parent.after(16, self.update)


class Game2048:
    def __init__(self, parent):
        self.parent = parent
        self.grid_size = 4
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.canvas = tk.Canvas(parent, width=400, height=400, bg="#bbada0")
        self.canvas.pack()

        self.game_active = False
        self.restart_button = None

        self.canvas.focus_set()

        self.canvas.bind("<Key>", self.key_press)


        self.reset_game()

    def reset_game(self):

        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.game_active = True

        self.canvas.delete("all")
        self.restart_button = None
        self.canvas.tag_unbind("restart_btn", "<Button-1>")

        self.add_tile()
        self.add_tile()
        self.draw_grid()

    def add_tile(self):

        empty = [(i, j) for i in range(self.grid_size)
                 for j in range(self.grid_size)
                 if self.grid[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def is_move_possible(self):

        if any(0 in row for row in self.grid):
            return True

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                val = self.grid[i][j]

                if j < self.grid_size - 1 and val == self.grid[i][j + 1]:
                    return True
                if i < self.grid_size - 1 and val == self.grid[i + 1][j]:
                    return True
        return False

    def check_game_state(self):

        if not self.is_move_possible():
            self.game_active = False
            self.draw_game_over()

    def move(self, direction):

        moved = False

        def compress_and_merge(row_or_col):

            new_list = [i for i in row_or_col if i != 0]


            for i in range(len(new_list) - 1):
                if new_list[i] == new_list[i + 1]:
                    new_list[i] *= 2
                    new_list[i + 1] = 0

            new_list = [i for i in new_list if i != 0]

            while len(new_list) < self.grid_size:
                new_list.append(0)

            return new_list

        original_grid = copy.deepcopy(self.grid)

        if direction == "Left":
            for i in range(self.grid_size):
                self.grid[i] = compress_and_merge(self.grid[i])

        elif direction == "Right":
            for i in range(self.grid_size):

                row = self.grid[i]
                new_row = compress_and_merge(row[::-1])[::-1]
                self.grid[i] = new_row

        elif direction == "Up":
            for j in range(self.grid_size):

                col = [self.grid[i][j] for i in range(self.grid_size)]
                new_col = compress_and_merge(col)
                for i in range(self.grid_size):
                    self.grid[i][j] = new_col[i]

        elif direction == "Down":
            for j in range(self.grid_size):

                col = [self.grid[i][j] for i in range(self.grid_size)]
                new_col = compress_and_merge(col[::-1])[::-1]
                for i in range(self.grid_size):
                    self.grid[i][j] = new_col[i]

        if self.grid != original_grid:
            moved = True

        return moved

    def key_press(self, event):

        if not self.game_active:
            return

        key = event.keysym
        if key in ("Up", "Down", "Left", "Right"):
            moved = self.move(key)
            if moved:
                self.add_tile()
                self.draw_grid()
                self.check_game_state()

    def get_tile_style(self, value):
        styles = {
            0: ('#cdc1b4', '#776e65', ("Arial", 24)),
            2: ('#eee4da', '#776e65', ("Arial", 32, "bold")),
            4: ('#ede0c8', '#776e65', ("Arial", 32, "bold")),
            8: ('#f2b179', '#f9f6f2', ("Arial", 32, "bold")),
            16: ('#f59563', '#f9f6f2', ("Arial", 32, "bold")),
            32: ('#f67c5f', '#f9f6f2', ("Arial", 32, "bold")),
            64: ('#f65e3b', '#f9f6f2', ("Arial", 32, "bold")),
            128: ('#edcf72', '#f9f6f2', ("Arial", 28, "bold")),
            256: ('#edcc61', '#f9f6f2', ("Arial", 28, "bold")),
            512: ('#edc850', '#f9f6f2', ("Arial", 28, "bold")),
            1024: ('#edc53f', '#f9f6f2', ("Arial", 24, "bold")),
            2048: ('#edc22e', '#f9f6f2', ("Arial", 24, "bold")),
            'default': ('#3c3a32', '#f9f6f2', ("Arial", 20, "bold"))
        }
        return styles.get(value, styles['default'])

    def draw_grid(self):
        self.canvas.delete("tiles")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                val = self.grid[i][j]

                bg_color, text_color, font_style = self.get_tile_style(val)

                x1, y1 = j * 100 + 5, i * 100 + 5
                x2, y2 = j * 100 + 95, i * 100 + 95

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg_color, tags="tiles", outline="#bbada0", width=5)

                if val != 0:
                    self.canvas.create_text(j * 100 + 50, i * 100 + 50, text=str(val),
                                            fill=text_color, font=font_style, tags="tiles")

    def draw_game_over(self):
        self.canvas.create_rectangle(0, 0, 400, 400, fill="#3c3a32", stipple="gray50", tags="overlay")

        self.canvas.create_text(200, 150, text="GAME OVER", font=("Arial", 40, "bold"), fill="white", tags="game_msg")

        self.restart_button = self.canvas.create_rectangle(120, 240, 280, 300, fill="#8f7a66", outline="#f9f6f2",
                                                           width=2, tags="restart_btn")
        self.canvas.create_text(200, 270, text="RESTART", fill="white", font=("Arial", 18, "bold"), tags="restart_btn")

        self.canvas.tag_bind("restart_btn", "<Button-1>", self.handle_restart_click)

    def handle_restart_click(self, event):
        if not self.game_active:
            self.reset_game()

class CarRacing:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=400, height=600, bg="gray")
        self.canvas.pack()

        self.speed = 5
        self.game_over = False
        self.restart_button = None

        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda e: self.key_press(e))
        self.canvas.bind("<Right>", lambda e: self.key_press(e))

        self.reset_game()

    def reset_game(self):
        self.canvas.delete("all")

        self.car = self.canvas.create_rectangle(180, 500, 220, 550, fill="blue")
        self.obstacles = []
        self.speed = 5
        self.game_over = False
        self.canvas.tag_unbind("restart_btn", "<Button-1>")
        self.restart_button = None

        self.update()

    def move_car(self, dx):
        if not self.game_over:
            x1, y1, x2, y2 = self.canvas.coords(self.car)

            if 0 <= x1 + dx and x2 + dx <= 400:
                self.canvas.move(self.car, dx, 0)

    def key_press(self, event):
        if event.keysym == "Left":
            self.move_car(-20)
        elif event.keysym == "Right":
            self.move_car(20)

    def check_collision(self):

        car_coords = self.canvas.coords(self.car)
        if not car_coords: return
        x1, y1, x2, y2 = car_coords

        for obs in self.obstacles:
            if not self.canvas.coords(obs): continue
            a1, b1, a2, b2 = self.canvas.coords(obs)

            if not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2):

                self.game_over = True
                self.display_game_over()
                break

    def display_game_over(self):
        self.canvas.create_text(200, 250, text="GAME OVER", font=("Arial", 30, "bold"), fill="white",
                                tags="game_message")

        self.canvas.create_rectangle(120, 320, 280, 360, fill="darkgreen", outline="white", tags="restart_btn")
        self.canvas.create_text(200, 340, text="RESTART", fill="white", font=("Arial", 16, "bold"), tags="restart_btn")

        self.canvas.tag_bind("restart_btn", "<Button-1>", self.handle_restart_click)

    def handle_restart_click(self, event):
        if self.game_over:
            self.reset_game()

    def update(self):
        if self.game_over:
            return
        for obs in self.obstacles:
            self.canvas.move(obs, 0, self.speed)
        self.check_collision()
        if self.game_over:
            return
        self.obstacles = [o for o in self.obstacles if self.canvas.coords(o)[1] < 600]

        if random.random() < 0.07:
            x = random.randint(0, 360)
            obs = self.canvas.create_rectangle(x, 0, x + 40, 20, fill="red")
            self.obstacles.append(obs)

        self.parent.after(50, self.update)

class BrickBreaker:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=600, height=400, bg="black")
        self.canvas.pack()

        self.game_active = False
        self.restart_button = None

        self.canvas.focus_set()

        self.canvas.bind("<Left>", lambda e: self.move_paddle(-20))
        self.canvas.bind("<Right>", lambda e: self.move_paddle(20))

        self.reset_game()

    def create_bricks(self):

        bricks = []
        rows, cols = 5, 10
        colors = ["red", "orange", "yellow", "green", "cyan"]
        for i in range(rows):
            for j in range(cols):
                x1 = j * 60
                y1 = i * 20
                x2 = x1 + 58
                y2 = y1 + 18
                fill_color = colors[i % len(colors)]
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, tags="brick")
                bricks.append(brick)
        return bricks

    def reset_game(self):

        self.canvas.delete("all")
        self.game_active = True
        self.restart_button = None
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")

        self.ball_dx = random.choice([-4, 4])
        self.ball_dy = -4
        self.paddle = self.canvas.create_rectangle(250, 380, 350, 390, fill="blue")
        self.bricks = self.create_bricks()

        self.update()

    def move_paddle(self, dx):

        if self.game_active:
            x1, y1, x2, y2 = self.canvas.coords(self.paddle)
            if 0 <= x1 + dx <= 600 - 100:
                self.canvas.move(self.paddle, dx, 0)

    def display_message(self, message, fill_color):

        self.game_active = False
        self.canvas.create_text(300, 180, text=message, font=("Arial", 30, "bold"), fill=fill_color, tags="game_msg")
        self.restart_button = self.canvas.create_rectangle(220, 240, 380, 280, fill="darkblue", outline="white",
                                                           tags="restart_btn")
        self.canvas.create_text(300, 260, text="RESTART", fill="white", font=("Arial", 16, "bold"), tags="restart_btn")

        self.canvas.tag_bind("restart_btn", "<Button-1>", self.handle_restart_click)

    def handle_restart_click(self, event):

        if not self.game_active:
            self.reset_game()

    def update(self):
        if not self.game_active:
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        if bx1 <= 0 or bx2 >= 600:
            self.ball_dx *= -1
        if by1 <= 0:
            self.ball_dy *= -1

        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        if bx2 >= px1 and bx1 <= px2 and by2 >= py1 and by1 <= py2:
            # Simple bounce
            self.ball_dy *= -1

            center_ball = (bx1 + bx2) / 2
            center_paddle = (px1 + px2) / 2
            difference = center_ball - center_paddle
            self.ball_dx += difference * 0.2
        overlapping = self.canvas.find_overlapping(bx1, by1, bx2, by2)

        for item_id in overlapping:
            if item_id in self.bricks:
                self.canvas.delete(item_id)
                self.bricks.remove(item_id)

                self.ball_dy *= -1
                break

        if by2 >= 400:

            self.display_message("GAME OVER", "red")
            return
        elif not self.bricks:

            self.display_message("YOU WIN!", "green")
            return


        self.parent.after(20, self.update)

class game_frame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
        self.parent = parent
        self.controller = controller
    
        self.snake_game = None
        self.pong_game = None
        self.number_game = None
        self.car_game = None
    
        self.frame = tk.Frame(self)
        self.frame = tk.Frame(self, bg="black")
        self.frame.pack(expand=True, fill="both")
    
        self.back_button = tk.Button(self, text="Back", command=lambda: self.controller.show_main_menu_frame())
        self.back_button.place( y=30, anchor='nw', x=40)
    
        self.snake_button = tk.Button(self, text="Snake Game", font=('Arial', 18), bg="#1A1A1A", fg="white",
                                          command=self.snakegame)
        self.snake_button.place(relx=1.0, y=300, anchor='ne', x=-40)
    
        self.pong_button = tk.Button(self, text="Pong Game", font=('Arial', 18), bg="#1A1A1A", fg="white",
                                         command=self.ponggame)
        self.pong_button.place(relx=1.0, y=350, anchor='ne', x=-40)
    
        self.number_button = tk.Button(self, text="2048 Game", font=('Arial', 18), bg="#1A1A1A", fg="white",
                                           command=self.numbergame)
        self.number_button.place(relx=1.0, y=400, anchor='ne', x=-40)
    
        self.car_button = tk.Button(self, text="Car Game", font=('Arial', 18), bg="#1A1A1A", fg="white",
                                        command=self.cargame)
        self.car_button.place(relx=1.0, y=450, anchor='ne', x=-40)
        self.brick_button = tk.Button(self, text="Brick Game", font=('Arial', 18), bg="#1A1A1A", fg="white",
                                        command=self.brickgame)
        self.brick_button.place(relx=1.0, y=500, anchor='ne', x=-40)
    
    def snakegame(self):
        self.clear_frame()
        self.snake_game = SnakeGame(self.frame)
        self.snake_game.canvas.focus_set()
    
    def ponggame(self):
        self.clear_frame()
        self.pong_game = PongGame(self.frame)
        self.focus_set()
        self.pong_game.update()
        self.bind("<KeyPress>", lambda e: self.pong_game.key_press(e))
    
    
    def numbergame(self):
        self.clear_frame()
        self.number_game = Game2048(self.frame)
        self.number_game.canvas.focus_set()
        self.number_game.canvas.bind("<KeyPress>", lambda e: self.number_game.key_press(e))
    
    def cargame(self):
        self.clear_frame()
        self.car_game = CarRacing(self.frame)
        self.car_game.canvas.focus_set()
    
    def brickgame(self):
        self.clear_frame()
        self.brick_game = BrickBreaker(self.frame)
        self.brick_game.canvas.focus_set()
    
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
