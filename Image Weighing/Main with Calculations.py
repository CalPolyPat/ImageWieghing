from PIL import Image, ImageStat

def calc_variance(data):
    mean = sum(data)/len(data)
    finlist = []
    finlist[:] = [(data[i]-mean)**2 for i in xrange(len(data))]
    varian = sum(finlist)/len(finlist)
    return varian

def deriv_var(data):
    deriv = []
    deriv[:] = [data[i]-data[i-1] for i in xrange(1, len(data))]
    return deriv

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
    deriv = []
    xboundup = []*10
    xbounddown = []*10
    filebufferx = [0]*iteratx
    filebuffery = [0]*iteraty
    #Load pixel data from image and create data file to store color variance
    pix = im_rgb.load()
    datafile = open("vdata.txt", "w")
    datafile.write("R, G, B\n")
    #Iterate and load variance data first into lists for RGB then calculate variance
    #and load into buffer then load to the file
    #Vertical slices
    for z in xrange(1, iteratx):
        rdata[:] = [pix[i, j][0] for j in xrange(0,imy) for i in xrange(z-1,z)]
        #gdata[:] = [pix[i, j][1] for j in xrange(0,imy) for i in xrange(z-1,z)]
        #bdata[:] = [pix[i, j][2] for j in xrange(0,imy) for i in xrange(z-1,z)]
        mean = sum(rdata)/len(rdata)
        finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
        varianr = sum(finlist)/len(finlist)
        #mean = sum(gdata)/len(gdata)
        #finlist[:] = [(gdata[i]-mean)**2 for i in xrange(len(gdata))]
        #variang = sum(finlist)/len(finlist)
        #mean = sum(bdata)/len(bdata)
        #finlist[:] = [(bdata[i]-mean)**2 for i in xrange(len(bdata))]
        #varianb = sum(finlist)/len(finlist)
        filebufferx[z-1] = varianr
        rdata[:] = []
        #gdata[:] = []
        #bdata[:] = []
    deriv[:] = [filebufferx[h]-filebufferx[h-1] for h in xrange(1, len(filebufferx))]
    for l in xrange(0, len(deriv)):
        if deriv[l]>200:
            xboundup.append(l)
    print str(xboundup[0]) + ", " + str(filebufferx[xboundup[0]])
    k = 1
    while k<len(xboundup):
        #if xboundup[k]-xboundup[k-1]>300:
        #    print str(xboundup[k]) + ", " + str(filebufferx[xboundup[k]])
        if xboundup[k]-xboundup[k-1]<300:
            xboundup.pop(k)
        k+=1
    for m in xrange(0, len(deriv)):
        if deriv[m]<-170:
            xbounddown.append(m)
    n = 1
    while n<len(xbounddown):
        #if xbounddown[n]-xbounddown[n-1]>300:
        #    print str(xbounddown[n-1]) + ", " + str(filebufferx[xbounddown[n-1]])
        if xbounddown[n]-xbounddown[n-1]<300:
            xbounddown.pop(n-1)
        n+=1
    datafile.write("".join(str(filebufferx)))
    dxcard = xbounddown[1]-xboundup[1]
    dxbowl = xbounddown[0]-xboundup[0]
    print "DX Bowl " + str(dxbowl) + "DX Card " + str(dxcard)
    lengthobj = dxbowl*2.15/dxcard
    print str(lengthobj)
    #Horizontal slices
    #datahfile = open("hdata.txt", "w")
    #datahfile.write("R, G, B\n")
    #for d in xrange(1, iteraty):
    #    rdata[:] = [pix[i, j][0] for j in xrange(d-1,d) for i in xrange(0,imx)]
    #    gdata[:] = [pix[i, j][1] for j in xrange(d-1,d) for i in xrange(0,imx)]
    #    bdata[:] = [pix[i, j][2] for j in xrange(d-1,d) for i in xrange(0,imx)]
    #    print str(d)
    #    mean = sum(rdata)/len(rdata)
    #    finlist[:] = [(rdata[i]-mean)**2 for i in xrange(len(rdata))]
    #    varianr = sum(finlist)/len(finlist)
    #    mean = sum(gdata)/len(gdata)
    #    finlist[:] = [(gdata[i]-mean)**2 for i in xrange(len(gdata))]
    #    variang = sum(finlist)/len(finlist)
    #    mean = sum(bdata)/len(bdata)
    #    finlist[:] = [(bdata[i]-mean)**2 for i in xrange(len(bdata))]
    #    varianb = sum(finlist)/len(finlist)
    #    filebuffery[d-1] = str(varianr) + ", " + str(variang) + ", " + str(varianb) + "\n"
    #    rdata[:] = []
    #    gdata[:] = []
    #    bdata[:] = []
    #datahfile.write("".join(filebuffery))


#Call routine
show_variance("circle card.jpg")

    
