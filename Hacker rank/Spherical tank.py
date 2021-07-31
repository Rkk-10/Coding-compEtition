import math, cmath

class Height(object):
    
    def __init__(me, radius, liquid_volume):
        me.radius=radius
        me.liquid_volume=liquid_volume
        me.total_volume=(4*math.pi*me.radius**3)/3
        me.cap_volume=me.total_volume-me.liquid_volume
        me.cubic_equation=[-1,3*me.radius,0,(-1*(3/math.pi)*me.cap_volume)]

    def single_cubic(me,eq):
        a0, b0, c0, d0=eq
        a, b, c = b0 / a0, c0 / a0, d0 / a0

        third = 1./3.
        a13 = a*third
        a2 = a13*a13
        sqr3 = math.sqrt(3)

        f = third*b - a2
        g = a13 * (2*a2 - b) + c
        h = 0.25*g*g + f*f*f

        def cubic_root(x):
            if x.real >= 0:
                return x**third
            else:
                return -(-x)**third

        if f == g == h == 0:
            r1 = -cubic_root(c)
            return r1, r1, r1

        elif h <= 0:
            j = math.sqrt(-f)
            k = math.acos(-0.5*g / (j*j*j))
            m = math.cos(third*k)
            n = sqr3 * math.sin(third*k)
            r1 = 2*j*m - a13
            r2 = -j * (m + n) - a13
            r3 = -j * (m - n) - a13
            return r1, r2, r3

        else:
            sqrt_h = cmath.sqrt(h)
            s = cubic_root(-0.5*g + sqrt_h)
            u = cubic_root(-0.5*g - sqrt_h)
            s_plus_u = s + u
            s_minus_u = s - u
            r1 = s_plus_u - a13
            r2 = -0.5*s_plus_u - a13 + s_minus_u*sqr3*0.5j
            r3 = -0.5*s_plus_u - a13 - s_minus_u*sqr3*0.5j
            return r1, r2, r3
    def run(me):
        me.hl=me.single_cubic((me.cubic_equation))
        me.result=[]
        for it in me.hl:
            if it>0 and it<2*me.radius:
                me.result.append(2*me.radius-it)
if __name__ == '__main__':
    r,lv=map(float,(input().split()))
    spherical_tank=Height(r,lv)
    spherical_tank.run()
    print(spherical_tank.result[0])
