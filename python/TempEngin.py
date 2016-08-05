data={"name":"Eva","age":23,"apple_count":12,"Friends":["Billy","Jhon","Emily"]}

if  data["apple_count"] <12  :
    print "Hello %s , what a fine age, %d , to be baking apple pies.You need %d more apples until you have a dozen. " \
          "Come back when you are  ready!" % (data["name"],data["age"],12-data["apple_count"])
elif data["apple_count"]==12 :
    print "Hello %s what a age, %d, to be baking apple pies. It looks like you have got a round dozen. I will just go " \
          "prheat the oven now." % (data["name"],data["age"])
    if len(data)==4 :
        print "After, you can call %s , %s, %s to help us eat."  %(data["Friends"][0],data["Friends"][1],data["Friends"][2])



