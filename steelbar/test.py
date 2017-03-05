import steelbar


def SteelBarTest():
    count_p = 7
    count_xp = 40
    count_xxp = 40
    p = steelbar.SteelBar(count_p, 'happy')
    for i in range(count_p):
        xp = steelbar.SteelBar(count_xp, 'less happy')
        for j in range(count_xp):
            xxp = steelbar.SteelBar(count_xxp, 'still happy')
            for k in range(count_xxp):
                xxp.Increment()
            xp.Increment()
        p.Increment()


if __name__ == '__main__':
    SteelBarTest()
