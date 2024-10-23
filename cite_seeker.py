from pypdf import PdfReader
from research_paper import ResearchPaper


"""
    opens the PDF and reads the contents specified
"""
def open_read_pdf():
    # creating a pdf reader object
    # change your path after renaming the paper
    reader = PdfReader('research_paper.pdf')

    citation_reader = ResearchPaper(reader=reader)
    citation_reader.parse_research_papers()
    # supply number of papers to check
    citation_reader.highest_reference_paper(5)



def main():
    open_read_pdf()


main()
