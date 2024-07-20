#Faça um programa em python que abra e reporduza o áudio de um arquivo MP3.
import pygame
pygame.init()

pygame.mixer.music.load('Som3ad.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
