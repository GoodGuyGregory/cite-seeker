import re
import pandas as pd

class ResearchPaper():

    def __init__(self, reader):
        self.page_length = reader.pages
        self.reader = reader
        self.reference_papers = {}

    """
        returns the highest reference paper count
    """
    def highest_reference_paper(self, n):
        reference_dict = pd.DataFrame.from_dict(self.reference_papers, orient='index', columns=['reference_count'])
        # set the index as the keys from the dictionary
        reference_dict.reset_index(inplace=True)
        # renames the column of the keys to 'ref_paper' in place
        reference_dict.rename(columns={'index': 'ref_paper'}, inplace=True)
        top_n_paper_citations = reference_dict.sort_values('reference_count', ascending=False)[:n]
        print(f"Top {n} Research Citations")
        print("----------------------------------")
        print(top_n_paper_citations[['ref_paper','reference_count']])



    def parse_research_papers(self):
        for page_num in range(len(self.page_length)):
            # creating a page object
            page = self.reader.pages[page_num]
            reference_regex = r'\d+(?:,\s*\d+)*'
            # extracting text from page
            page_content = page.extract_text()
            matches = re.findall(reference_regex, page_content)
            if len(matches) > 0:
                for match in matches:
                    if len(match) > 2:
                        found_nums = match.split(',')
                        for digit in found_nums:
                            digit = digit.strip()
                            if int(digit) < 100:
                                if int(digit) != 0:
                                    if digit not in self.reference_papers:
                                        self.reference_papers[digit] = 1
                                    else:
                                        # increases occurences
                                        self.reference_papers[digit] += 1
                    else:
                        if int(match) < 1000:
                            if int(match) != 0:
                                if match not in self.reference_papers:
                                    self.reference_papers[match] = 1
                                else:
                                    # increases occurences
                                    self.reference_papers[match] += 1
                

