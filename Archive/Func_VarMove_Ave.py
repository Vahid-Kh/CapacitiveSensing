

def rec_ave(n, xold, x, x10):
    return xold + 1 / n * (x - x10)


def recursive_variance(data):
    if len(data) == 1:
        return 0
    else:
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return variance + recursive_variance(data[:-1])


def mov_ave(a, n=30):
    if n>0:
        list_mov_ave = a[0:n]
        x_old = sum(list_mov_ave) / n
        for i in range(n, len(a)):
            x_new = rec_ave(n, x_old, a[i], a[i - n])
            list_mov_ave.append(x_new)
            x_old = x_new
        return list_mov_ave

    else:
        return a


def mov_var(a, n=30):
    if n > 0:
        list_var = a[0:n]
        var_old = 0
        for i in range(n, len(a)):
            var_new = recursive_variance(a[i - n:i])
            list_var.append(var_new)
            var_old = var_new
        return list_var

    else:
        return a

# print(recursive_variance([0,0,0,0,0,1,2,3,4,5,6]))

print(mov_ave([0,0,0,0,0,1,2,3,4,5,6],2))
