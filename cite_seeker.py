from pypdf import PdfReader
from research_paper import ResearchPaper


"""
    opens the PDF and reads the contents specified
"""
def open_read_pdf():
    # creating a pdf reader object
    reader = PdfReader('research_paper.pdf')

    citation_reader = ResearchPaper(reader=reader)
    citation_reader.parse_research_papers()




def main():
    open_read_pdf()


main()
