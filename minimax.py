def opt(game, depth, p):
    if depth == 0:
        return 0, None
    direction = p == game.player #True: maximize
    max_r = None
    best_move = None
    for m in game.possibile_moves():
        x,y  = m
        g2 = game.clone()
        assert g2.move(x,y)
        result = g2.result()
        if result is True or result is False:
            if direction:
                return 1, m
            else:
                return -1, m
        elif result == 0:
            max_r = 0
            best_move = m
        else:
            result, _ = opt(g2, depth-1, p)
            result *= 0.9
            if max_r is None:
                max_r = result
                best_move = m
            elif (
                direction and result > max_r
                ) or (
                not direction and result < max_r
            ):
                max_r = result
                best_move = m
    return max_r, best_move


            