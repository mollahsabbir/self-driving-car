import pygame

class EventHandler:
    targets = []
    
    @classmethod
    def register(cls, instance):
        cls.targets.append(instance)
    
    @classmethod
    def notify(cls, event):
        for instance in cls.targets: 
            instance.listen(event)

class GameExitEventListener:
    def listen(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
