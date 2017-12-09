"""
CSSE1001 Assignment 3
Semester 1, 2017

@author David Riddell

The only file written by David is a3.py
"""

import tkinter as tk
from base import *
from tkinter import messagebox
import random
import time
from highscores import *
import game_regular

import model
import view
from game_regular import RegularGame
# # For alternative game modes
# from game_make13 import Make13Game
# from game_lucky7 import Lucky7Game
# from game_unlimited import UnlimitedGame

__author__ = "David Riddell"
__email__ = "d.riddell@uq.net.au"

__version__ = "1.1.2"


class StatusBar(tk.Frame):
    """Makes a frame for the status bar in lolo app that displays the gamemode and the score."""
    def __init__(self, parent):
        """Contructs the labels that go into the frame"""
        super().__init__(parent)

        self._game_mode_name = tk.Label(self, text='Game: ')
        self._game_mode_name.pack(side=tk.LEFT, anchor=tk.W)
        self._set_score = tk.Label(self, text='Score: ')
        self._set_score.pack(side=tk.BOTTOM)

    def set_game(self, game_mode):
        """Sets the game mode in the label"""
        self._game_mode_name.config(text='Game: {}'.format(game_mode))

    def set_score(self, score):
        """Sets the score in the label"""
        self._set_score.config(text='Score: {}'.format(score))

class LoadingScreen:
    """ Main loading screen for the App, gives choices on what the user wants to do, will open everything
as a new top level
"""
    def __init__(self, master):
        """Contructor that starts the app and gives all the options"""
        self._master = master
        self.frame = tk.Frame(self._master)
        self.frame.pack()
        button_frame = tk.Frame(self._master)
        button_frame.pack(side=tk.LEFT)
        self._logo_frame = tk.Frame(self._master)
        self._logo_frame.pack(side=tk.TOP)

        self._player_frame = tk.Frame(self._master)
        self._player_frame.pack(side=tk.TOP)
        self._high_score_label = tk.Label(self._player_frame, text='Your Name:')
        self._high_score_label.pack(side=tk.LEFT)
        self._high_score_name = tk.Entry(self._player_frame)
        self._high_score_name.pack(side=tk.LEFT)
        self._set_player = tk.Button(self._player_frame, text='Set player', command=self.get_player)
        self._set_player.pack(side=tk.LEFT)
        

        menubar = tk.Menu(self._master)
        self._master.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.exit)
        filemenu.add_command(label="New Game", command=self.regular_game)
        filemenu.add_command(label='High Scores', command=self.open_high_score)

        self._master.bind('<Control-n>', self.regular_game)

        self._auto_play = AutoFrame(self._master)
        self._auto_play.pack(side=tk.RIGHT)

        self._logo = LoloLogo(self._logo_frame)
        self._logo.pack(fill=tk.BOTH, expand=True)

        self._button1 = tk.Button(button_frame, text="Play Regular Lolo", bg='blue', command=self.regular_game)
        self._button1.pack(anchor='w', fill=tk.BOTH, expand=True, pady=20, padx=20, ipadx=20)

        self._button2 = tk.Button(button_frame, text='High Scores', bg='pink', command=self.open_high_score)
        self._button2.pack(anchor='w', fill=tk.BOTH, expand=True, pady=20, padx=20, ipadx=20)

        self._button3 = tk.Button(button_frame, text='Exit', bg='orange', command=self.exit)
        self._button3.pack(anchor='w', fill=tk.BOTH, expand=True, pady=20, padx=20, ipadx=20)

    def open_high_score(self):
        """Opens HighScores as a toplevel app"""
        self._new_window = tk.Toplevel(self._master)
        self.app = HighScoreWindow(self._new_window)

    def regular_game(self, event=None):
        """Opens LoloApp as a toplevel app"""
        self._new_window = tk.Toplevel(self._master)
        self.app = LoloApp(self._new_window)

    def exit(self) :
        """Close the application."""
        self._master.destroy()

    def get_player(self):
        """gets the name of the person currently playing"""
        self._player = self._high_score_name.get()

        

class HighScoreWindow(HighScoreManager):
    """Uses High Score Manager to make a new window displaying the highest scores gotten on lolo"""
    def __init__(self, master):
        """Contructor that creates the frames in the window and displays the scores"""
        super().__init__()

        self._master = master

        highest = HighScoreManager().get_sorted_data()[0]
        grid_list = highest['grid']
        game = game_regular.RegularGame.deserialize(grid_list)
        
        highest_score_player_frame = tk.Frame(self._master)
        highest_score_player_frame.pack(anchor='n')
        highest_score_player = tk.Label(highest_score_player_frame,
                                        text= 'Highest Score belongs to {} with a score of {}'
                                        .format(highest['name'],
                                                highest['score']))
        highest_score_player.pack()

        AutomaticGame(master, game, static=True)
        
                
        high_score_grid_frame = tk.Frame(master)
        high_score_grid_frame.pack(anchor='n')

        high_players_frame = tk.Frame(master)
        high_players_frame.pack(side=tk.LEFT)
        high_players1 = tk.Label(high_players_frame, text=highest['name'])
        high_players2 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[1]['name'])
        high_players3 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[2]['name'])
        high_players4 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[3]['name'])
        high_players5 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[4]['name'])
        high_players6 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[5]['name'])
        high_players7 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[6]['name'])
        high_players8 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[7]['name'])
        high_players9 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[8]['name'])
        high_players10 = tk.Label(high_players_frame, text=HighScoreManager().get_sorted_data()[9]['name'])


        high_players1.pack(anchor='w')
        high_players2.pack(anchor='w')
        high_players3.pack(anchor='w')
        high_players4.pack(anchor='w')
        high_players5.pack(anchor='w')
        high_players6.pack(anchor='w')
        high_players7.pack(anchor='w')
        high_players8.pack(anchor='w')
        high_players9.pack(anchor='w')
        high_players10.pack(anchor='w')

        highest_players_score_frame = tk.Frame(self._master)
        highest_players_score_frame.pack(side=tk.RIGHT)
        

        high_players_score1 = tk.Label(highest_players_score_frame, text=highest['score'])
        high_players_score2 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[1]['score'])
        high_players_score3 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[2]['score'])
        high_players_score4 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[3]['score'])
        high_players_score5 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[4]['score'])
        high_players_score6 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[5]['score'])
        high_players_score7 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[6]['score'])
        high_players_score8 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[7]['score'])
        high_players_score9 = tk.Label(highest_players_score_frame,
                                       text=HighScoreManager().get_sorted_data()[8]['score'])
        high_players_score10 = tk.Label(highest_players_score_frame,
                                        text=HighScoreManager().get_sorted_data()[9]['score'])
        high_players_score1.pack()
        high_players_score2.pack()
        high_players_score3.pack()
        high_players_score4.pack()
        high_players_score5.pack()
        high_players_score6.pack()
        high_players_score7.pack()
        high_players_score8.pack()
        high_players_score9.pack()
        high_players_score10.pack()

class AutoFrame(tk.Frame):
    """Makes the frame so it can be added to loading screen for the game to play automatically"""
    def __init__(self, parent):
        """Contructor that executes the Autoplaying Game"""
        super().__init__(parent)

        AutomaticGame(self)
        
class LoloLogo(tk.Canvas):
    """Creates canvas for the lolo game
Parameters: Stores as a tk.Canvas"""
    def __init__(self, parent):
        """Contructor that creates the logo for lolo"""
        super().__init__(parent, bg='orange', height=170, width=400)

        self.create_rectangle(5,5,35,170, fill='black')
        self.create_rectangle(5,170,75, 140, fill='black')

        self.create_oval(100,5,200,170, fill='black')
        self.create_oval(125,50,175,145, fill='orange')

        self.create_rectangle(215,5,235,170, fill='black')
        self.create_rectangle(215,170,275,140, fill='black')

        self.create_oval(300,5,399,170, fill='black')
        self.create_oval(325,50,375,145,fill='orange')

class AutomaticGame(BaseLoloApp):
    """Automatically playing game that inherits from BaseLoloApp"""
    def __init__(self, master, game=None, grid_view=None, static=None):
        """Constructor that makes the game play itself buy checking for resolve to be emitted"""
        super().__init__(master)

        self._move_delay = 2000
        if static==None:
            self.move()


    def bind_events(self):
        """Binds relevant events."""
        self._game.on('resolve', self.resolve)

    def resolve(self, delay=None):
        """Makes a move after a given movement delay."""
        if delay is None:
            delay = self._move_delay

        self._master.after(delay, self.move)

    def reset(self):
        """Resets the game."""
        self._game.reset()
        self._grid_view.draw(self._game.grid, self._game.find_connections())
        self.move()

    def move(self):
        """Finds a connected tile randomly and activates it."""
        connections = list(self._game.find_groups())

        if connections:
            # pick random valid move
            cells = list()

            for connection in connections:
                for cell in connection:
                    cells.append(cell)

            self.activate(random.choice(cells))
        else:
            self.reset()

class LoloApp(BaseLoloApp):
    """base App that runs Lolo
Parameters: Must use BaseLoloApp for the game to run"""
    def __init__(self, master, game=None, grid_view=None, name=None):
        """Contructs the game using code provided from BaseLoloApp"""
        super().__init__(master)

        self._name = name

        self._master = master

        self._modes = StatusBar(self._master)
        self._modes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        menubar = tk.Menu(self._master)
        self._master.config(menu=menubar)

        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.exit)
        filemenu.add_command(label="New Game", command=self.reset)

        self._master.bind('<Control-n>', self.reset)
        self._master.bind('<Control-l>', self.use_lightning)

        self._lightning = 0

        lightning_frame = tk.Frame(self._master)
        lightning_frame.pack(side=tk.BOTTOM)
        self._lbutton = tk.Button(lightning_frame, text='No Lightning',
                                           command=self.use_lightning, bg='grey')
        self._lbutton.pack(side=tk.BOTTOM)

        game_mode = self._game.get_name()
        self._modes.set_game(game_mode)

        #for toogling lightning
        self._preview_on = True
        self._toogle_count = False


    def reset(self, event=None):
        """Resets the game."""
        self._game.reset()
        #redraws grid
        self._grid_view.draw(self._game.grid, self._game.find_connections())
        self._modes.set_score(0)
        self._game.set_score(0)

    def is_preview_on(self) :
        """checks to see if preview is on"""
        if text in self._lbutton == 'Lightning {}'.format(self._lightning):
            True
        else:
            False

    def toogle_lightning(self):
        """ lightning button toogle"""
        self._preview_on = not self._preview_on
        if self._preview_on:
            self._lbutton.config(bg='yellow', text='Lightning {}'.format(self._lightning))
        else:
            self._lbutton.config(bg='grey', text = 'No Lightning')

    def use_lightning(self, event=None):
        """makes lightning active and gives the ability to remove tiles"""
        self._toogle_count = True
        if self._lightning > 0:
            self._lbutton.config(text='Using Lightning', bg='red')
        if self._lightning == 0:
            self._toogle_count = False
            self._lbutton.config(bg='grey', text='No Lightning')
            messagebox.showinfo(title='Lightning Inactive', message='No Lightning to use')
        
    def exit(self) :
        """Close the application."""
        self._master.destroy()  

    def score(self, points):
        """Handles increase in score."""

        score = self._game.get_score()
        self._modes.set_score(score)

    def game_over(self):
        """Finds if game over is emitted and then gives a message showing the game is over, then resets game"""
        if self._game.on('game_over', self.game_over):
            score = self._game.get_score()
            messagebox.showinfo(title="Game Over", message="The game has ended, your score  is: {}".format
                                (score), command=self.reset())      

    def activate(self, position):
        """ checks to see if clicked position is able to be activated and if it is able to, it will activate it
this function also adds the extra lightning points if the score is a multiple of 10. If lightning mode is
activated it will remove a tile at position clicked but won't add to the score."""
        if self._toogle_count == True:
            #checks to see if lightning avaliable and removes a tile if mode toogled on
            if self._lightning > 0:
                self.remove(position)
                self._lightning -= 1
                self._lbutton.config(text='Lightning {}'.format(self._lightning), bg='yellow')
                self._toogle_count = False
                if self._lightning == 0:
                    self._lbutton.config(bg='grey', text='No Lightning')
            else:
                self._lightning = 0
                self._toogle_count = False
                messagebox.showinfo(title='Lightning Inactive', message='No Lightning to use')
        else:
            try:
                super().activate(position)
                if self._game.get_score() % 10 == 0:
                    self._lightning += 1
                    self._lbutton.config(bg='yellow', text='Lightning {}'.format(self._lightning))
                if self._lightning <= 0:
                    self._lbutton.config(bg='grey', text='No Lightning')
            except IndexError:
                messagebox.showerror('Invalid Activation', 'Cannot move tile at: {}'.format(position))     


def main():
    root = tk.Tk()
    app = LoadingScreen(root)
    root.mainloop()




if __name__ == "__main__":
    main()
