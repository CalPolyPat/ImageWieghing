from PIL import Image, ImageStat

def calc_variance(data):
    mean = sum(data)/len(data)
    finlist = []
    for i in range(len(data)):
        difmean = data[i]-mean
        difmeansq = difmean**2
        finlist.append(difmeansq)
    varian = sum(finlist)/len(finlist)
    return varian

def show_variance(src):
    im = Image.open(src)
    im_rgb = im.convert("RGB")
    imx, imy = im.size
    rdata = []
    gdata = []
    bdata = []
    pix = im_rgb.load()
    for z in range(1, 5):
        for s in range(1, 5):
            for j in range(imy*(z-1)/4,imy*z/4):
                for i in range(imx*(s-1)/4,imx*s/4): 
                    r, g, b = pix[i, j]
                    rdata.append(r)
                    gdata.append(g)
                    bdata.append(b)
            print "Red for sector { " + str(s) + ", " + str(z) + " }"
            print calc_variance(rdata)
            print "Green for sector { " + str(s) + ", " + str(z) + " }"
            print calc_variance(gdata)
            print "Blue for sector { " + str(s) + ", " + str(z) + " }"
            print calc_variance(bdata)
            rdata[:] = []
            gdata[:] = []
            bdata[:] = []


print "baseline carpet values: R=305, G=297, B=295"
show_variance("carpet and binder.jpg")

    
