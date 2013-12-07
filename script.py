import os

if __name__ == "__main__":
    # Save the world!
    
    # but first say hello to it!
    print 'Hello world!'

    for k in xrange(5):
        with open("%d.dat" % k, "w") as fp:
            pass
    try:
        os.makedirs("data")
    except OSError:
        pass
    for k in xrange(5):
        with open(os.path.join("data",
                               "%d.dat.out" % k), "w") as fp:
            pass
