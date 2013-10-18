from PIL import Image, ImageStat

def calc_variance(data):
    mean = sum(data)/len(data)
    finlist = []
    finlist[:] = [(data[i]-mean)**2 for i in xrange(len(data))]
    varian = sum(finlist)/len(finlist)
    return varian

def show_variance(src):
    im = Image.open(src)
    im_rgb = im.convert("RGB")
    imx, imy = im.size
    iterat = 256
    rdata = []
    gdata = []
    bdata = []
    filebuffer = [""]*(iterat+1)
    pix = im_rgb.load()
    datafile = open("vdata.txt", "w")
    datafile.write("R, G, B\n")
    for z in xrange(1, iterat + 1):
        rdata[:] = [pix[i, j][0] for j in xrange(0,imy) for i in xrange(imx*(z-1)/iterat,imx*z/iterat)]
        gdata[:] = [pix[i, j][1] for j in xrange(0,imy) for i in xrange(imx*(z-1)/iterat,imx*z/iterat)]
        bdata[:] = [pix[i, j][2] for j in xrange(0,imy) for i in xrange(imx*(z-1)/iterat,imx*z/iterat)]
        print str(z)
        filebuffer[z] = str(calc_variance(rdata)) + ", " + str(calc_variance(gdata)) + ", " + str(calc_variance(bdata)) + "\n"
        rdata[:] = []
        gdata[:] = []
        bdata[:] = []
    datafile.write("".join(filebuffer))


print "baseline carpet values: R=305, G=297, B=295"
show_variance("carpet and binder.jpg")

    
