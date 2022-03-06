import json
xabar = {}
def xabarlar(soni,id):
    global xabar
    # xabar[str(x)]=id
    try:
        #----------------Faylni ochish----------------#
        with open("data\_user_id.txt") as fayl:
            xabar = json.loads(fayl.read())
            # js = json.loads(data)

            # print(ariza_soni)
            xabar[f"{soni}"]=id
        fayl.close()
        # print(ccc)
        # ------------------FAylga yozish -----------------------#
        with open("data\_user_id.txt",'w') as fayl:
            fayl.write(json.dumps(xabar))        #'w'-"write"---Ma'lumotlarni o'chirib yangidan yozadi
        fayl.close()
        #=======================================================#  
            
        
    except:
        xabar[f"{soni}"]=id

        with open("data\_user_id.txt",'w') as fayl:
            fayl.write(json.dumps(xabar))        #'w'-"write"---Ma'lumotlarni o'chirib yangidan yozadi
        fayl.close()


    return xabar
