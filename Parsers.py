from Models import LogEntry

class Parser: 

    def __init__(self, logfile):
        self.logfile = logfile 
        self.log_lines = []
        self.filtered_lines = []
        self.rejected_line = [] 
        self.cheaked_lines  = []
        self.count_line = 0 


    def CombinedFormatParser (self):
        self.log_lines  = self.logfile.split("\n")

        for line in self.log_lines:
            self.count_line += 1 
            if (len (line.split('"'))) == 7:
                self.cheaked_lines.append(line)
            else:
                self.rejected_line.append(f"Line: {self.count_line} contains more or less then 7 postional value ")
      
 

        for line in self.cheaked_lines:
            self.filtered_lines.append(line.split())
            
        return self.filtered_lines
        
    