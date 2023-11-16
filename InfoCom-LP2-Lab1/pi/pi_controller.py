import requests
import time
import random
import click
from sense_hat import SenseHat

sense = SenseHat()


def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    c = click.getchar()
    if c =='a':
        click.echo('Left')
        send_vel = True
        d_long = -1
        d_la = 0
    elif c == 'd':
        click.echo('Right')
        send_vel = True
        d_long = 1
        d_la = 0
    elif c =='w':
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 1
    elif c == 's':
        click.echo('Down')
        send_vel = True
        d_long = 0
        d_la = -1
    else:
        d_long = 0
        d_la = 0
        click.echo('Invalid input :(')
        send_vel = False
    return d_long, d_la, send_vel

def get_Joy():
    d_long = 0
    d_la = 0
    send_vel = False

    
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "right":
                click.echo('Right')
                send_vel = True
                d_long = 10
                d_la = 0
                
            elif event.direction == "down":
                click.echo('Down')
                send_vel = True
                d_long = 0
                d_la = -10
                
            elif event.direction == "left":
                click.echo('Left')
                send_vel = True
                d_long = -10
                d_la = 0
                
                
            elif event.direction == "up":
                
                click.echo('Up')
                send_vel = True
                d_long = 0
                d_la = 10
                
                
    return d_long, d_la, send_vel

if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = get_Joy()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
