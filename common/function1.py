def area (height,width,radius):
    arearec=height*width
    areacircle=3.14*radius**2
    total_area=arearec+areacircle
    return total_area

ans=area(10,4,3)
# total_area= arearec + areacircle
print(ans)
