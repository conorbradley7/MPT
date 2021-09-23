succ = lambda n: lambda f: lambda x: f(n(f(x)))


add =  lambda n: lambda a: lambda f: lambda x: (a(f)(n(f(x))))

subtracion = lambda n: lambda m: m pred n
