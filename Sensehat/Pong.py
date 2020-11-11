# Simple Pong game played on Sensehat

from sense_hat import SenseHat                                                                        
import time                                                                                           
import random                                                                                         
                                                                                                      
sense = SenseHat()                                                                                    
                                                                                                      
class Game:                                                                                           
    def __init__(self):                                                                               
        self.y = 1                                                                                    
        self.ball_position = [int(random.randint(2,6)),int(random.randint(1,6))]                      
        self.ball_vel = [1,1]                                                                         
        self.ball_col = [0,255,255]                                                                   
        self.empty_col = [0,0,0]                                                                      
        sense.stick.direction_up = self.move_up                                                       
        sense.stick.direction_down = self.move_dwn                                                    
                                                                                                      
    def draw_bat(self):                                                                               
        sense.set_pixel(0,self.y,255,0,255)                                                           
        sense.set_pixel(0,self.y+1,255,0,255)                                                         
        sense.set_pixel(0,self.y-1,255,0,255)                                                         
                                                                                                      
    def move_up(self):                                                                                
        if self.y > 1 and event.action=="pressed":                                                    
            self.y -= 1                                                                               
                                                                                                      
    def move_dwn(self):                                                                               
        if self.y < 6 and event.action=="pressed":                                                    
            self.y+=1                                                                                 
                                                                                                      
    def ball(self):                                                                                   
        sense.set_pixel(self.ball_position[0],self.ball_position[1],180,180,180)                      
        self.ball_position[0] += self.ball_vel[0]                                                     
        self.ball_position[1] += self.ball_vel[1]                                                     
                                                                                                      
        if self.ball_position[0] == 7:                                                                
            self.ball_vel[0] = -self.ball_vel[0]                                                      
                                                                                                      
        elif self.ball_position[1] == 0 or self.ball_position[1] == 7:                                
            self.ball_vel[1] = -self.ball_vel[1]                                                      
                                                                                                      
        elif self.ball_position[0] == 0:                                                              
            quit()                                                                                    
                                                                                                      
        elif self.ball_position[0] == 1 and self.y-1 <=  self.ball_position[1] <= self.y+1:           
            self.ball_vel = -self.ball_vel[0]                                                         
                                                                                                      
    def __call__(self):                                                                               
        while 1:                                                                                      
            sense.clear()                                                                             
            self.draw_bat()                                                                            
            self.ball()                                                                                
            time.sleep(0.5)                                                                            
                                                                                                       
if __name__ == "__main__":                                                                             
    game = Game()                                                                                      
    game()      
