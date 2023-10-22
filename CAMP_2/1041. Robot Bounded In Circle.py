class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def move(direction, x, y):
            x += direction == 0
            x -= direction == 180
            y += direction == 90
            y -= direction == 270
            return (x, y)

        direction = 90
        x, y = 0, 0
        for i in range(1000):
            for ins in instructions:
                if ins == 'L':
                    direction = (direction - 90) % 360
                elif ins == 'R':
                    direction = (direction + 90) % 360
                else:
                    x, y = move(direction, x, y)
            if x == 0 and y == 0 and direction == 90: 
                return True 
        return False



