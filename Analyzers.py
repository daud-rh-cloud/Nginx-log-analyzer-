from Parsers import Parser

class Analyzer: 


    def __init__(self, filtered_list: list[list[str]]):
        self.filtered_list = filtered_list
        self.ip_list = []
        self.path_list = []
        self.statuscodes_list = []
        self.time_list = []
        self.error_rate = 0 
        pass 




    def status_codes (self):
        for line in self.filtered_list: 
            self.statuscodes_list.append(line[8]) 

        
        counts = {}                                  
        for code in self.statuscodes_list: 
            if code in counts: 
                     counts[code] += 1
            else: 
                    counts[code] = 1 


#error rate count for 5xx 
        totalReq = 0  
        total5xx = 0 
        for i in counts.items():
             totalReq += i[1]   ## the counts :value 
             if "5" in i[0]:
                total5xx += i [1]
         
        self.error_rate = total5xx / totalReq * 100   


        
        def demofunc(parameter_touple):
            return parameter_touple [1]
        
        result = sorted (counts.items(), key=demofunc, reverse=True)

        x = 0       
        # print ("Status code / : ")
        for STCODE, N  in result:
         print (f"{STCODE:<18}{N}")
         

    def calculateErrorRate(self): 
        print (f"5xx Error rate: {self.error_rate :.2f}% ")









    def popular_ip(self):
        for line in self.filtered_list: 
            self.ip_list.append(line[0]) 

        counts = {}                                  
        for ip in self.ip_list:
            if ip in counts: 
                counts[ip] += 1
            else: 
                counts[ip] = 1  
                

        # NOTES --- ----- -------------------
        # the count.item makes each key:value to list of touple(key,value), and the sort need to know the sort key/value 
        # the ( key = ) is a parameter thats sort takes and expects a our own castom written funtion thats retuen the value 
        # that we want to sort with... 
        # it later passes the count.item as parametet to out castom funtion 
        # option -1 (wrtting the castom Funtion myself) //   --or Lambda 

        def my_sort(counts):
            return counts[1]
        
        result = sorted (counts.items(), key= my_sort)

        x = 0 
        for ip, N  in result :
         x += 1 
         print (f"{ip:<18}{N}")
         if x == 4:
             break 
        

         
 






    def top_path (self):
        for line in self.filtered_list: 
            self.path_list.append(line[5]+ line[6])

        counts = {}
        for path in self.path_list:
            if path in counts: 
                counts[path] += 1 
            else : 
                counts[path] = 1 

        def demofunc(parameter_touple):
                return parameter_touple [1]

        result = sorted (counts.items(), key=demofunc, reverse=True)


        
        # print ("TOP PATHS / : ")
        x = 0
        for TP, N  in result :
            x += 1 
            print (f"{TP:<18}{N}")
            if x == 4 :
                break 









    def request_perHour(self):
        for line in self.filtered_list :
              self.time_list.append(line[3])

    
        splited_time = []
        for time in self.time_list:
            splited_time.append (time.split((":")))

            
        DateHourMIn : str
        counts = {}
        for i in splited_time: 
            DateHourMIn = i[0] + ":" +i[1] 
            DateHourMIn = DateHourMIn.strip("[")

            
            if DateHourMIn in counts :
                counts[DateHourMIn] += 1 
            else :
                 counts[DateHourMIn] = 1

        
        def demofunc(parameter_touple):
            return parameter_touple [1]
        
        result = sorted (counts.items(), key=demofunc, reverse=True)


        # print ("Requests per hour: ")
        x = 0 
        for RQ, N  in result :
            x += 1 
            print (f"{RQ:<18}{N}")
            if x == 4:
                break 
