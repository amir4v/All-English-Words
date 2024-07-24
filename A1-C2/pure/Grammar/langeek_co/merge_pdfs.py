import PyPDF2

def merge_pdfs(pdf_list, output_path):
    """
    Merges multiple PDF files into a single PDF file.

    Parameters:
    pdf_list (list): List of paths to the PDF files to be merged.
    output_path (str): Path to save the merged PDF file.
    """
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Iterate through the list of PDF files
    for pdf in pdf_list:
        # Append each PDF file to the merger object
        pdf_merger.append(pdf)

    # Write out the merged PDF to the specified output path
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Merged PDF saved to {output_path}')

# Example usage
pdfs_to_merge = [
"1-langeek_co_en_grammar_course_494_nouns.pdf",
"2-langeek_co_en_grammar_course_492_pronouns.pdf",
"3-langeek_co_en_grammar_course_496_verbs.pdf",
"4-langeek_co_en_grammar_course_497_adjectives.pdf",
"5-langeek_co_en_grammar_course_501_adverbs.pdf",
"6-langeek_co_en_grammar_course_622_tenses.pdf",
"7-langeek_co_en_grammar_course_450_modals.pdf",
"8-langeek_co_en_grammar_course_500_determiners.pdf",
"9-langeek_co_en_grammar_course_502_prepositions.pdf",
"10-langeek_co_en_grammar_course_696_sentences.pdf",
"11-langeek_co_en_grammar_course_881_ponctuation.pdf",
"12-langeek_co_en_grammar_course_257_phrases.pdf",
"13-langeek_co_en_grammar_course_548_moods.pdf",
"14-langeek_co_en_grammar_course_1599_morphology.pdf",
]
output_pdf_path = 'merged_output.pdf'
merge_pdfs(pdfs_to_merge, output_pdf_path)
