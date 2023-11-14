import pygame

white = (255,255,255)

def display_message(message,display):

	pygame.init()

	message_display(message,display,30,"centre")
	pygame.time.wait(1000)

def message_display(text,display,size,textPosition):
	display_width = 800
	display_height = 600

	#Sets the text font	
	largeText = pygame.font.Font('freesansbold.ttf',size)

	#Creates the text objects
	TextSurf, TextRect = text_objects(text, largeText)

	TextRect.center = ((display_width/2),(display_height/2))

	# Clear the screen
	display.fill((0, 0, 0))

	#This updates the screen, and sleeps for two seconds
	display.blit(TextSurf, TextRect)
	pygame.display.update()

#These creates and displays a text object
def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()