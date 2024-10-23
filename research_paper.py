import re

class ResearchPaper():

    def __init__(self, reader):
        self.page_length = reader.pages
        self.reader = reader
        self.reference_papers = {}

    """
        returns the highest reference paper count
    """
    def highest_reference_paper(self,):
        
        pass

    def parse_research_papers(self):
        for page_num in range(len(self.page_length)):
            # creating a page object
            page = self.reader.pages[page_num]
            reference_regex = r'\d+(?:,\s*\d+)*'
            # extracting text from page
            page_content = page.extract_text()
            matches = re.findall(reference_regex, page_content)
            if len(matches) > 0:


