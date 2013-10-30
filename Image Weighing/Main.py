from PIL import Image, ImageStat

def calc_variance(data):
    mean = sum(data)/len(data)
    finlist = []
    finlist[:] = [(data[i]-mean)**2 for i in xrange(len(data))]
    varian = sum(finlist)/len(finlist)
    return varian

def show_variance(src):
    #Open image passed to routine and convert to RGB color
    im = Image.open(src)
    im_rgb = im.convert("RGB")
    imx, imy = im.size
    #Define variables and lists
    iteratx = imx
    iteraty = imy
    rdata = []
    gdata = []
    bdata = []
    finlist = []
    filebufferx = [""]*(iteratx+1)
    filebuffery = [""]*(iteraty+1)
    #Load pixel data from image and create data file to store color variance
    pix = im_rgb.load()
    datafile = open("vdata.txt", "w")
    datafile.write("R, G, B\n")
    #Iterate and load variance data first into lists for RGB then calculate variance
    #and load into buffer then load to the file
    #Vertical slices
    for z in xrange(1, iteratx):
        rdata[:] = [pix[i, j][0] for j in xrange(0,imy) for i in xrange(z-1,z)]
        gdata[:] = [pix[i, j][1] for j in xrange(0,imy) for i in xrange(z-1,z)]
        bdata[:] = [pix[i, j][2] for j in xrange(0,imy) for i in xrange(z-1,z)]
        print str(z)
        mean = sum(rdata)/len(rdata)
        finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
        varianr = sum(finlist)/len(finlist)
        mean = sum(gdata)/len(gdata)
        finlist[:] = [(gdata[i]-mean)**2 for i in xrange(len(gdata))]
        variang = sum(finlist)/len(finlist)
        mean = sum(bdata)/len(bdata)
        finlist[:] = [(bdata[i]-mean)**2 for i in xrange(len(bdata))]
        varianb = sum(finlist)/len(finlist)
        filebufferx[z-1] = str(varianr) + ", " + str(variang) + ", " + str(varianb) + "\n"
        rdata[:] = []
        gdata[:] = []
        bdata[:] = []
    datafile.write("".join(filebufferx))
    #Horizontal slices
    datahfile = open("hdata.txt", "w")
    datahfile.write("R, G, B\n")
    for d in xrange(1, iteraty):
        rdata[:] = [pix[i, j][0] for j in xrange(d-1,d) for i in xrange(0,imx)]
        gdata[:] = [pix[i, j][1] for j in xrange(d-1,d) for i in xrange(0,imx)]
        bdata[:] = [pix[i, j][2] for j in xrange(d-1,d) for i in xrange(0,imx)]
        print str(d)
        mean = sum(rdata)/len(rdata)
        finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
        varianr = sum(finlist)/len(finlist)
        mean = sum(gdata)/len(gdata)
        finlist[:] = [(gdata[i]-mean)**2 for i in xrange(len(gdata))]
        variang = sum(finlist)/len(finlist)
        mean = sum(bdata)/len(bdata)
        finlist[:] = [(bdata[i]-mean)**2 for i in xrange(len(bdata))]
        varianb = sum(finlist)/len(finlist)
        filebuffery[d-1] = str(varianr) + ", " + str(variang) + ", " + str(varianb) + "\n"
        rdata[:] = []
        gdata[:] = []
        bdata[:] = []
    datahfile.write("".join(filebuffery))


#Call routine
show_variance("circle card.jpg")

    
