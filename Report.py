from Analyzers import Analyzer
from Parsers import Parser

class Reporter:


    def __init__(self, analyzerOBJ :Analyzer, parserOBJ :Parser):
        self.analyzerOBJ = analyzerOBJ 
        self.parserOBJ = parserOBJ
         


    def report_Everything(self): 
        print ("=== logsentry report: sample.log ===")
        print  (f"TOTAL Logs counted : {self.parserOBJ.count_line} Lines     "
                "                           "
                "                          "
                "                          "
                )
 
                                 
                                
        print ("Status codes:")
        self.analyzerOBJ.status_codes()
        self.analyzerOBJ.calculateErrorRate()
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )
        



        print ("Top IPs:")
        self.analyzerOBJ.popular_ip()
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )

        print ("Top paths:")
        self.analyzerOBJ.top_path()  
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )

        print ("Requests per hour:")
        self.analyzerOBJ.request_perHour()
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )


        print ("WARNING:")
        print ("rejected.log:")
        for bad in self.parserOBJ.rejected_line:
            print (bad )