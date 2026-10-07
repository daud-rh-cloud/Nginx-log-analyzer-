from Models import LogEntry 
from Parsers import Parser
from Analyzers import Analyzer 
from Report import Reporter 



with open ("/home/daud/smallfile.txt") as f: 
     Logfile = f.read()

parser1 = Parser (Logfile)
analyzer1 = Analyzer (parser1.CombinedFormatParser())
reporter1 = Reporter(analyzer1,parser1)

# analyzer1.calculateErrorRate()
# analyzer1.status_codes()

reporter1.report_Everything()




 
