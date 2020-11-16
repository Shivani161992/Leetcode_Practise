sx = 1
sy = 1
tx = 3
ty = 5
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        if sx == tx and sy == ty:
            return True
        elif sx > tx or sy > ty:
            return False
        else:
            while tx >= sx and ty >= sy:
                if tx > ty:
                    if ty > sy:
                        tx = tx % ty
                    else:
                        return (tx - sx) % ty == 0
                else:
                    if tx > sx:
                        ty = ty % tx
                    else:
                        return (ty - sy) % tx == 0

                if tx== sx and ty ==sy:
                    return True
            return False



obj=Solution()
print(obj.reachingPoints(sx, sy, tx, ty))