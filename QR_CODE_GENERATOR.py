#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries

import qrcode
import matplotlib.pyplot as plt


# In[2]:


# add data which u want to be qr representation
data = "https://www.bing.com/images/search?view=detailV2&ccid=jHzknUYD&id=CA003DA0FD6FA323CAE3943C18EA1E93255BE1A5&thid=OIP.jHzknUYDNbmX10epkMvTtgHaDJ&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.8c7ce49d460335b997d747a990cbd3b6%3frik%3dpeFbJZMe6hg8lA%26riu%3dhttp%253a%252f%252fosstfupdate.ca%252fwp-content%252fuploads%252f2018%252f02%252fwomens-day.jpg%26ehk%3dHEu6DUPTogP%252fK%252f3WCMooVBLqfVW%252bElHTyIEhcNIlHKE%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=1285&expw=3020&q=womens+day&simid=607996249281609672&FORM=IRPRST&ck=E0956C2EA3EF6A76C6894C39A480504A&selectedIndex=12&ajaxhist=0&ajaxserp=0"
# output file name

filename = "my_qr_code.png"
#generating qr code

image = qrcode.make(data)

#save image into a file

image.save(filename)
plt.imshow(image,cmap='gray')


# # when scan that bar it will automatically open happy birthdat bing

# In[ ]:




